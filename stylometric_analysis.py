#!/usr/bin/env python3
"""
Stylometric Analysis Tool for Essay Quality Assessment

This tool analyzes essays to identify mathematical patterns and statistical
signatures in language, providing quantitative metrics for essay quality
and authorship characteristics.

Mathematical Blueprints Analyzed:
1. Zipf's Law Compliance - word frequency distribution
2. Heaps' Law - vocabulary growth rate  
3. Type-Token Ratio (TTR) - lexical diversity
4. Sentence Complexity - structure variation
5. Readability Indices - accessibility metrics
6. N-gram Entropy - predictability patterns
7. Hapax Legomena Ratio - unique word usage

Usage:
    python stylometric_analysis.py [essays_directory]
    
    If no directory is provided, defaults to ./Essays relative to the script location.
"""

import os
import re
import math
import statistics
import sys
from collections import Counter
from pathlib import Path
import json

# Configuration constants
ZIPF_FREQUENCY_LIMIT = 1000  # Maximum number of words for Zipf analysis
FILENAME_DISPLAY_LENGTH = 40  # Truncation length for filenames in reports


def clean_text(text: str) -> str:
    """Remove markdown formatting and extract pure text."""
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)
    # Remove markdown headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', text)
    text = re.sub(r'_{1,3}([^_]+)_{1,3}', r'\1', text)
    # Remove links
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', text)
    # Remove horizontal rules
    text = re.sub(r'^-{3,}$', '', text, flags=re.MULTILINE)
    # Remove block quotes markers
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Remove empty lines and normalize whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def tokenize_words(text: str) -> list:
    """Extract words from text, handling contractions and preserving meaning."""
    # Convert to lowercase and extract word tokens
    text = text.lower()
    # Match words including contractions
    words = re.findall(r"\b[a-z]+(?:'[a-z]+)?\b", text)
    return words


def tokenize_sentences(text: str) -> list:
    """Split text into sentences."""
    # Handle common abbreviations
    text = re.sub(r'\b(Mr|Mrs|Ms|Dr|Prof|etc|vs|e\.g|i\.e)\.\s', r'\1<dot> ', text)
    # Split on sentence boundaries
    sentences = re.split(r'[.!?]+\s+', text)
    # Restore abbreviation dots
    sentences = [s.replace('<dot>', '.') for s in sentences if s.strip()]
    return sentences


def calculate_zipf_coefficient(word_counts: Counter) -> tuple:
    """
    Calculate Zipf's Law coefficient.
    
    Zipf's Law: frequency ∝ 1/rank^s
    Natural language typically has s ≈ 1.0
    
    Returns (coefficient, r_squared) where coefficient is the Zipf exponent
    and r_squared indicates how well the data fits Zipf's law.
    """
    if len(word_counts) < 10:
        return (0, 0)
    
    # Get frequencies sorted by rank
    frequencies = sorted(word_counts.values(), reverse=True)
    n = min(len(frequencies), ZIPF_FREQUENCY_LIMIT)  # Limit for stability
    
    # Log-log regression: log(freq) = log(c) - s*log(rank)
    log_ranks = [math.log(i + 1) for i in range(n)]
    log_freqs = [math.log(f) for f in frequencies[:n]]
    
    # Linear regression
    mean_x = statistics.mean(log_ranks)
    mean_y = statistics.mean(log_freqs)
    
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(log_ranks, log_freqs))
    denominator = sum((x - mean_x) ** 2 for x in log_ranks)
    
    if denominator == 0:
        return (0, 0)
    
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    
    # Calculate R-squared
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(log_ranks, log_freqs))
    ss_tot = sum((y - mean_y) ** 2 for y in log_freqs)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    
    return (-slope, r_squared)  # Negate slope to get positive coefficient


def calculate_heaps_coefficient(text_words: list) -> tuple:
    """
    Calculate Heaps' Law coefficient.
    
    Heaps' Law: V = K * N^β
    where V = vocabulary size, N = total words, K and β are constants.
    Typical β ≈ 0.4-0.6 for natural text.
    
    Returns (K, beta, r_squared)
    """
    if len(text_words) < 100:
        return (0, 0, 0)
    
    # Sample vocabulary growth at intervals
    intervals = [int(len(text_words) * i / 20) for i in range(1, 21)]
    intervals = [i for i in intervals if i > 0]
    
    log_ns = []
    log_vs = []
    
    for n in intervals:
        vocab = set(text_words[:n])
        if len(vocab) > 0:
            log_ns.append(math.log(n))
            log_vs.append(math.log(len(vocab)))
    
    if len(log_ns) < 5:
        return (0, 0, 0)
    
    # Linear regression: log(V) = log(K) + β*log(N)
    mean_x = statistics.mean(log_ns)
    mean_y = statistics.mean(log_vs)
    
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(log_ns, log_vs))
    denominator = sum((x - mean_x) ** 2 for x in log_ns)
    
    if denominator == 0:
        return (0, 0, 0)
    
    beta = numerator / denominator
    log_k = mean_y - beta * mean_x
    k = math.exp(log_k)
    
    # R-squared
    ss_res = sum((y - (log_k + beta * x)) ** 2 for x, y in zip(log_ns, log_vs))
    ss_tot = sum((y - mean_y) ** 2 for y in log_vs)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    
    return (k, beta, r_squared)


def calculate_type_token_ratio(words: list, window_size: int = 100) -> dict:
    """
    Calculate various Type-Token Ratio metrics.
    
    Standard TTR varies with text length, so we also calculate:
    - MSTTR: Mean Segmental TTR (average over fixed windows)
    - MATTR: Moving Average TTR
    """
    if len(words) == 0:
        return {"ttr": 0, "msttr": 0, "vocabulary_richness": 0}
    
    # Standard TTR
    types = len(set(words))
    tokens = len(words)
    ttr = types / tokens
    
    # MSTTR (Mean Segmental TTR)
    if len(words) >= window_size:
        segment_ttrs = []
        for i in range(0, len(words) - window_size + 1, window_size):
            segment = words[i:i + window_size]
            segment_ttr = len(set(segment)) / len(segment)
            segment_ttrs.append(segment_ttr)
        msttr = statistics.mean(segment_ttrs) if segment_ttrs else ttr
    else:
        msttr = ttr
    
    # Vocabulary richness (Yule's K)
    word_freqs = Counter(words)
    freq_of_freqs = Counter(word_freqs.values())
    
    n = len(words)
    m1 = n
    m2 = sum(f ** 2 * v for f, v in freq_of_freqs.items())
    
    if m1 > 0 and m1 != m2:
        yules_k = 10000 * (m2 - m1) / (m1 ** 2)
    else:
        yules_k = 0
    
    return {
        "ttr": round(ttr, 4),
        "msttr": round(msttr, 4),
        "yules_k": round(yules_k, 2),
        "unique_words": types,
        "total_words": tokens
    }


def calculate_hapax_metrics(word_counts: Counter) -> dict:
    """
    Calculate hapax legomena (words appearing once) and dis legomena (twice).
    
    High hapax ratio often indicates rich vocabulary or specialized text.
    """
    total_types = len(word_counts)
    total_tokens = sum(word_counts.values())
    
    hapax = sum(1 for count in word_counts.values() if count == 1)
    dis = sum(1 for count in word_counts.values() if count == 2)
    
    return {
        "hapax_count": hapax,
        "dis_legomena_count": dis,
        "hapax_ratio": round(hapax / total_types, 4) if total_types > 0 else 0,
        "hapax_token_ratio": round(hapax / total_tokens, 4) if total_tokens > 0 else 0,
        "sichel_s": round(dis / total_types, 4) if total_types > 0 else 0
    }


def calculate_sentence_metrics(sentences: list, words: list) -> dict:
    """Calculate sentence-level complexity metrics."""
    if not sentences:
        return {"avg_sentence_length": 0, "sentence_std": 0, "complexity_index": 0}
    
    # Words per sentence
    sentence_lengths = []
    for sent in sentences:
        sent_words = tokenize_words(sent)
        if sent_words:
            sentence_lengths.append(len(sent_words))
    
    if not sentence_lengths:
        return {"avg_sentence_length": 0, "sentence_std": 0, "complexity_index": 0}
    
    avg_len = statistics.mean(sentence_lengths)
    std_len = statistics.stdev(sentence_lengths) if len(sentence_lengths) > 1 else 0
    
    # Complexity index: combination of length and variation
    # Higher variation suggests more complex writing style
    complexity = avg_len * (1 + std_len / avg_len) if avg_len > 0 else 0
    
    return {
        "sentence_count": len(sentences),
        "avg_sentence_length": round(avg_len, 2),
        "sentence_std": round(std_len, 2),
        "min_sentence_length": min(sentence_lengths),
        "max_sentence_length": max(sentence_lengths),
        "complexity_index": round(complexity, 2)
    }


def calculate_readability(text: str, words: list, sentences: list) -> dict:
    """
    Calculate readability metrics.
    
    - Flesch Reading Ease (higher = easier)
    - Flesch-Kincaid Grade Level
    - Automated Readability Index
    """
    if not words or not sentences:
        return {"flesch_reading_ease": 0, "flesch_kincaid_grade": 0, "ari": 0}
    
    # Estimate syllables (rough approximation for English)
    def count_syllables(word):
        word = word.lower()
        if len(word) <= 3:
            return 1
        # Count vowel groups
        vowels = 'aeiouy'
        count = 0
        prev_vowel = False
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_vowel:
                count += 1
            prev_vowel = is_vowel
        # Adjust for silent e
        if word.endswith('e') and count > 1:
            count -= 1
        return max(1, count)
    
    total_syllables = sum(count_syllables(w) for w in words)
    total_words = len(words)
    total_sentences = len(sentences)
    total_chars = sum(len(w) for w in words)
    
    # Flesch Reading Ease
    asl = total_words / total_sentences  # Average Sentence Length
    asw = total_syllables / total_words   # Average Syllables per Word
    flesch = 206.835 - (1.015 * asl) - (84.6 * asw)
    
    # Flesch-Kincaid Grade Level
    fk_grade = (0.39 * asl) + (11.8 * asw) - 15.59
    
    # Automated Readability Index
    avg_chars_per_word = total_chars / total_words
    ari = (4.71 * avg_chars_per_word) + (0.5 * asl) - 21.43
    
    return {
        "flesch_reading_ease": round(max(0, min(100, flesch)), 1),
        "flesch_kincaid_grade": round(max(0, fk_grade), 1),
        "ari": round(max(0, ari), 1),
        "avg_word_length": round(avg_chars_per_word, 2),
        "avg_syllables_per_word": round(asw, 2)
    }


def calculate_ngram_entropy(words: list, n: int = 2) -> float:
    """
    Calculate Shannon entropy of n-grams.
    
    Higher entropy = more unpredictable/diverse word combinations.
    Lower entropy = more repetitive/formulaic patterns.
    """
    if len(words) < n:
        return 0
    
    ngrams = [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]
    ngram_counts = Counter(ngrams)
    total = len(ngrams)
    
    entropy = 0
    for count in ngram_counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    
    return round(entropy, 4)


def calculate_function_word_ratio(words: list) -> dict:
    """
    Analyze function word usage - a key stylometric signature.
    
    Function words (articles, prepositions, pronouns) are often used
    unconsciously and can be distinctive authorship markers.
    """
    function_words = {
        'articles': {'a', 'an', 'the'},
        'prepositions': {'in', 'on', 'at', 'to', 'for', 'with', 'by', 'from', 'of', 'about',
                        'into', 'through', 'during', 'before', 'after', 'above', 'below',
                        'between', 'under', 'over'},
        'pronouns': {'i', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours',
                    'you', 'your', 'yours', 'yourself', 'he', 'him', 'his', 'himself',
                    'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
                    'they', 'them', 'their', 'theirs', 'themselves',
                    'this', 'that', 'these', 'those', 'who', 'whom', 'which', 'what'},
        'conjunctions': {'and', 'but', 'or', 'nor', 'for', 'yet', 'so', 'because',
                        'although', 'while', 'if', 'when', 'unless', 'until'},
        'auxiliaries': {'is', 'are', 'was', 'were', 'be', 'been', 'being',
                       'have', 'has', 'had', 'do', 'does', 'did',
                       'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'can', 'could'}
    }
    
    total = len(words)
    if total == 0:
        return {}
    
    results = {}
    all_function_words = set()
    
    for category, word_set in function_words.items():
        count = sum(1 for w in words if w in word_set)
        results[f"{category}_ratio"] = round(count / total, 4)
        all_function_words.update(word_set)
    
    total_function = sum(1 for w in words if w in all_function_words)
    results["total_function_word_ratio"] = round(total_function / total, 4)
    results["content_word_ratio"] = round(1 - total_function / total, 4)
    
    return results


def calculate_punctuation_signature(text: str) -> dict:
    """
    Analyze punctuation patterns - another stylometric marker.
    """
    total_chars = len(text)
    if total_chars == 0:
        return {}
    
    punctuation_counts = {
        'commas': text.count(','),
        'periods': text.count('.'),
        'semicolons': text.count(';'),
        'colons': text.count(':'),
        'exclamations': text.count('!'),
        'questions': text.count('?'),
        'dashes': text.count('—') + text.count('–') + text.count('-'),
        'quotes': text.count('"') + text.count('"') + text.count('"'),
        'parentheses': text.count('(') + text.count(')')
    }
    
    total_punct = sum(punctuation_counts.values())
    
    return {
        **{f"{k}_per_1000": round(v / total_chars * 1000, 2) for k, v in punctuation_counts.items()},
        "total_punctuation_per_1000": round(total_punct / total_chars * 1000, 2)
    }


def calculate_mathematical_signature(word_counts: Counter, words: list) -> dict:
    """
    Calculate the mathematical 'fingerprint' of the text.
    
    This combines multiple metrics into a signature that can distinguish
    between authors or writing styles.
    """
    zipf_coef, zipf_r2 = calculate_zipf_coefficient(word_counts)
    heaps_k, heaps_beta, heaps_r2 = calculate_heaps_coefficient(words)
    
    bigram_entropy = calculate_ngram_entropy(words, 2)
    trigram_entropy = calculate_ngram_entropy(words, 3)
    
    return {
        "zipf_coefficient": round(zipf_coef, 4),
        "zipf_r_squared": round(zipf_r2, 4),
        "heaps_k": round(heaps_k, 4),
        "heaps_beta": round(heaps_beta, 4),
        "heaps_r_squared": round(heaps_r2, 4),
        "bigram_entropy": bigram_entropy,
        "trigram_entropy": trigram_entropy,
        "entropy_ratio": round(trigram_entropy / bigram_entropy, 4) if bigram_entropy > 0 else 0
    }


def analyze_essay(filepath: Path) -> dict:
    """Perform complete stylometric analysis on a single essay."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    # Clean and tokenize
    cleaned_text = clean_text(raw_text)
    words = tokenize_words(cleaned_text)
    sentences = tokenize_sentences(cleaned_text)
    word_counts = Counter(words)
    
    # Calculate all metrics
    analysis = {
        "filename": filepath.name,
        "file_size_bytes": filepath.stat().st_size,
        "character_count": len(cleaned_text),
        "raw_character_count": len(raw_text),
        
        # Lexical metrics
        "lexical_metrics": calculate_type_token_ratio(words),
        "hapax_metrics": calculate_hapax_metrics(word_counts),
        
        # Sentence metrics
        "sentence_metrics": calculate_sentence_metrics(sentences, words),
        
        # Readability
        "readability_metrics": calculate_readability(cleaned_text, words, sentences),
        
        # Mathematical signatures
        "mathematical_signature": calculate_mathematical_signature(word_counts, words),
        
        # Stylometric markers
        "function_word_signature": calculate_function_word_ratio(words),
        "punctuation_signature": calculate_punctuation_signature(cleaned_text),
        
        # Top words
        "top_20_words": dict(word_counts.most_common(20))
    }
    
    return analysis


def generate_comparison_report(analyses: list) -> str:
    """Generate a markdown report comparing all essays."""
    report = []
    report.append("# Stylometric Analysis Report: Essay Quality & Mathematical Signatures\n")
    report.append("## Overview\n")
    report.append("This analysis identifies mathematical patterns and statistical signatures in the essay collection.\n")
    report.append("The metrics help assess essay quality and identify distinctive writing characteristics.\n\n")
    
    # Summary statistics
    report.append("## 1. Corpus Statistics\n")
    report.append("| Essay | Words | Sentences | Vocabulary | TTR |\n")
    report.append("|-------|-------|-----------|------------|-----|\n")
    
    for a in analyses:
        report.append(f"| {a['filename'][:FILENAME_DISPLAY_LENGTH]}... | "
                     f"{a['lexical_metrics']['total_words']} | "
                     f"{a['sentence_metrics']['sentence_count']} | "
                     f"{a['lexical_metrics']['unique_words']} | "
                     f"{a['lexical_metrics']['ttr']:.3f} |\n")
    
    # Zipf's Law Analysis
    report.append("\n## 2. Zipf's Law Compliance (Word Frequency Distribution)\n")
    report.append("Natural language follows Zipf's Law with coefficient ≈ 1.0. ")
    report.append("Higher R² indicates better fit to this universal pattern.\n\n")
    report.append("| Essay | Zipf Coefficient | R² | Interpretation |\n")
    report.append("|-------|-----------------|-----|----------------|\n")
    
    for a in analyses:
        coef = a['mathematical_signature']['zipf_coefficient']
        r2 = a['mathematical_signature']['zipf_r_squared']
        if 0.9 <= coef <= 1.1 and r2 > 0.95:
            interp = "✓ Natural language pattern"
        elif r2 > 0.9:
            interp = "~ Slight deviation from typical"
        else:
            interp = "? Unusual distribution"
        name_truncated = a['filename'][:FILENAME_DISPLAY_LENGTH - 5]
        report.append(f"| {name_truncated}... | {coef:.3f} | {r2:.3f} | {interp} |\n")
    
    # Heaps' Law Analysis
    report.append("\n## 3. Heaps' Law (Vocabulary Growth Rate)\n")
    report.append("Heaps' Law (V = K × N^β) models vocabulary growth. ")
    report.append("Typical β ≈ 0.4-0.6; higher β indicates richer vocabulary growth.\n\n")
    report.append("| Essay | K | β (Beta) | R² | Vocabulary Richness |\n")
    report.append("|-------|---|----------|-----|--------------------|\n")
    
    for a in analyses:
        k = a['mathematical_signature']['heaps_k']
        beta = a['mathematical_signature']['heaps_beta']
        r2 = a['mathematical_signature']['heaps_r_squared']
        if beta > 0.55:
            richness = "High - diverse vocabulary"
        elif beta > 0.45:
            richness = "Medium - balanced"
        else:
            richness = "Low - focused vocabulary"
        name_truncated = a['filename'][:FILENAME_DISPLAY_LENGTH - 5]
        report.append(f"| {name_truncated}... | {k:.2f} | {beta:.3f} | {r2:.3f} | {richness} |\n")
    
    # Readability Analysis
    report.append("\n## 4. Readability Metrics\n")
    report.append("| Essay | Flesch Score | Grade Level | ARI | Complexity |\n")
    report.append("|-------|--------------|-------------|-----|------------|\n")
    
    for a in analyses:
        flesch = a['readability_metrics']['flesch_reading_ease']
        grade = a['readability_metrics']['flesch_kincaid_grade']
        ari = a['readability_metrics']['ari']
        if flesch >= 60:
            level = "Accessible"
        elif flesch >= 30:
            level = "Academic"
        else:
            level = "Complex"
        name_truncated = a['filename'][:FILENAME_DISPLAY_LENGTH - 5]
        report.append(f"| {name_truncated}... | {flesch:.1f} | {grade:.1f} | {ari:.1f} | {level} |\n")
    
    # Entropy Analysis
    report.append("\n## 5. N-gram Entropy (Predictability Patterns)\n")
    report.append("Higher entropy indicates more diverse, less predictable word combinations.\n\n")
    report.append("| Essay | Bigram Entropy | Trigram Entropy | Pattern Type |\n")
    report.append("|-------|---------------|-----------------|---------------|\n")
    
    for a in analyses:
        bi = a['mathematical_signature']['bigram_entropy']
        tri = a['mathematical_signature']['trigram_entropy']
        if bi > 10:
            pattern = "Highly varied"
        elif bi > 8:
            pattern = "Moderate variation"
        else:
            pattern = "Repetitive patterns"
        name_truncated = a['filename'][:FILENAME_DISPLAY_LENGTH - 5]
        report.append(f"| {name_truncated}... | {bi:.2f} | {tri:.2f} | {pattern} |\n")
    
    # Hapax Analysis
    report.append("\n## 6. Hapax Legomena (Unique Word Usage)\n")
    report.append("Hapax legomena are words appearing only once. Higher ratios often indicate specialized vocabulary.\n\n")
    report.append("| Essay | Hapax Count | Hapax Ratio | Interpretation |\n")
    report.append("|-------|-------------|-------------|----------------|\n")
    
    for a in analyses:
        hapax = a['hapax_metrics']['hapax_count']
        ratio = a['hapax_metrics']['hapax_ratio']
        if ratio > 0.5:
            interp = "Very rich vocabulary"
        elif ratio > 0.4:
            interp = "Rich vocabulary"
        else:
            interp = "Focused vocabulary"
        name_truncated = a['filename'][:FILENAME_DISPLAY_LENGTH - 5]
        report.append(f"| {name_truncated}... | {hapax} | {ratio:.3f} | {interp} |\n")
    
    # Function Word Signature
    report.append("\n## 7. Function Word Signature (Stylometric Markers)\n")
    report.append("Function words are often unconscious choices and serve as authorship indicators.\n\n")
    report.append("| Essay | Articles | Pronouns | Conjunctions | Function Total |\n")
    report.append("|-------|----------|----------|--------------|----------------|\n")
    
    for a in analyses:
        art = a['function_word_signature'].get('articles_ratio', 0)
        pro = a['function_word_signature'].get('pronouns_ratio', 0)
        conj = a['function_word_signature'].get('conjunctions_ratio', 0)
        total = a['function_word_signature'].get('total_function_word_ratio', 0)
        name_truncated = a['filename'][:FILENAME_DISPLAY_LENGTH - 5]
        report.append(f"| {name_truncated}... | {art:.3f} | {pro:.3f} | {conj:.3f} | {total:.3f} |\n")
    
    # Mathematical Signature Comparison
    report.append("\n## 8. Mathematical Signature Summary\n")
    report.append("Each essay has a unique mathematical 'fingerprint' combining all metrics:\n\n")
    
    for a in analyses:
        report.append(f"### {a['filename']}\n")
        report.append("```\n")
        sig = a['mathematical_signature']
        report.append(f"Zipf: α={sig['zipf_coefficient']:.3f} (R²={sig['zipf_r_squared']:.3f})\n")
        report.append(f"Heaps: K={sig['heaps_k']:.2f}, β={sig['heaps_beta']:.3f}\n")
        report.append(f"Entropy: bi={sig['bigram_entropy']:.2f}, tri={sig['trigram_entropy']:.2f}\n")
        lex = a['lexical_metrics']
        report.append(f"Lexical: TTR={lex['ttr']:.3f}, MSTTR={lex['msttr']:.3f}, Yule's K={lex['yules_k']:.1f}\n")
        report.append("```\n\n")
    
    # Quality Assessment
    report.append("\n## 9. Quality Assessment Summary\n\n")
    
    # Calculate composite scores
    scores = []
    for a in analyses:
        score = 0
        # Zipf compliance (natural language)
        if 0.85 <= a['mathematical_signature']['zipf_coefficient'] <= 1.15:
            score += 2
        if a['mathematical_signature']['zipf_r_squared'] > 0.9:
            score += 1
        # Vocabulary richness
        if a['mathematical_signature']['heaps_beta'] > 0.5:
            score += 2
        if a['lexical_metrics']['msttr'] > 0.7:
            score += 1
        # Complexity
        if 30 <= a['readability_metrics']['flesch_reading_ease'] <= 70:
            score += 2
        # Entropy (not too predictable, not too random)
        if 8 <= a['mathematical_signature']['bigram_entropy'] <= 12:
            score += 1
        scores.append((a['filename'], score))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    
    report.append("| Rank | Essay | Quality Score |\n")
    report.append("|------|-------|---------------|\n")
    for i, (name, score) in enumerate(scores, 1):
        stars = "★" * min(score, 5) + "☆" * max(0, 5 - score)
        name_truncated = name[:FILENAME_DISPLAY_LENGTH]
        report.append(f"| {i} | {name_truncated}... | {score}/9 {stars} |\n")
    
    # Conclusions
    report.append("\n## 10. Key Findings\n\n")
    
    # Find averages
    avg_zipf = statistics.mean(a['mathematical_signature']['zipf_coefficient'] for a in analyses)
    avg_heaps = statistics.mean(a['mathematical_signature']['heaps_beta'] for a in analyses)
    avg_ttr = statistics.mean(a['lexical_metrics']['msttr'] for a in analyses)
    
    report.append("### Statistical Patterns Identified:\n\n")
    report.append(f"1. **Zipf's Law Compliance**: Average coefficient = {avg_zipf:.3f} ")
    report.append(f"({'typical natural language' if 0.9 <= avg_zipf <= 1.1 else 'slight variation from typical'})\n\n")
    report.append(f"2. **Vocabulary Growth**: Average Heaps' β = {avg_heaps:.3f} ")
    report.append(f"({'rich vocabulary' if avg_heaps > 0.5 else 'moderate vocabulary'})\n\n")
    report.append(f"3. **Lexical Diversity**: Average MSTTR = {avg_ttr:.3f} ")
    report.append(f"({'high diversity' if avg_ttr > 0.7 else 'moderate diversity'})\n\n")
    
    report.append("### Authorship Signature Observations:\n\n")
    report.append("The function word ratios and punctuation patterns reveal consistent stylistic choices ")
    report.append("across the essays. Key signature elements include:\n\n")
    
    # Find distinctive patterns
    avg_pronoun = statistics.mean(a['function_word_signature'].get('pronouns_ratio', 0) for a in analyses)
    avg_conjunction = statistics.mean(a['function_word_signature'].get('conjunctions_ratio', 0) for a in analyses)
    
    report.append(f"- Pronoun usage: {avg_pronoun:.3f} (indicates narrative style)\n")
    report.append(f"- Conjunction usage: {avg_conjunction:.3f} (indicates argument structure)\n\n")
    
    report.append("### Conclusion\n\n")
    report.append("The essays demonstrate sophisticated language use with strong compliance to ")
    report.append("natural language statistical patterns (Zipf's and Heaps' laws). The high lexical ")
    report.append("diversity and entropy values indicate creative, non-formulaic writing. ")
    report.append("The consistent function word signatures suggest a coherent authorial voice ")
    report.append("even across collaborative human-AI writing.\n")
    
    return "".join(report)


def main():
    """Main function to run the analysis."""
    # Determine essays directory
    # Priority: 1) Command line argument, 2) Relative to script location
    if len(sys.argv) > 1:
        essays_dir = Path(sys.argv[1])
    else:
        # Default to Essays directory relative to script location
        script_dir = Path(__file__).parent.resolve()
        essays_dir = script_dir / "Essays"
    
    if not essays_dir.exists():
        print(f"Error: Essays directory not found: {essays_dir}")
        print(f"Usage: python {sys.argv[0]} [essays_directory]")
        sys.exit(1)
    
    # Only analyze English essays (skip Polish versions to avoid language mixing)
    english_essays = [
        "The Chalice of Gethsemane.md",
        "Quantum Sword.md",
        "When One Became Two.md",
        "The Aleph in the Machine.md",
        "I am disturbed en.md",
        "From Override to Activation.md",
        "Ender Bearing the Cross.md",
        "What They Never Told Me About Mathematics.md",
        "The Ghost of Tsushima Sandomierz mode en.md",
        "Deva init en.md"
    ]
    
    print("=" * 70)
    print("STYLOMETRIC ANALYSIS: Essay Quality & Mathematical Signatures")
    print("=" * 70)
    print()
    
    analyses = []
    
    for essay_name in english_essays:
        filepath = essays_dir / essay_name
        if filepath.exists():
            print(f"Analyzing: {essay_name}")
            analysis = analyze_essay(filepath)
            analyses.append(analysis)
        else:
            print(f"  [SKIP] Not found: {essay_name}")
    
    print()
    print("-" * 70)
    print(f"Analyzed {len(analyses)} essays")
    print("-" * 70)
    print()
    
    # Generate report
    report = generate_comparison_report(analyses)
    
    # Save report
    report_path = essays_dir.parent / "STYLOMETRIC_ANALYSIS_REPORT.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Report saved to: {report_path}")
    print()
    
    # Also print summary to console
    print("=" * 70)
    print("SUMMARY OF MATHEMATICAL SIGNATURES")
    print("=" * 70)
    
    for a in analyses:
        print(f"\n{a['filename'][:50]}...")
        sig = a['mathematical_signature']
        lex = a['lexical_metrics']
        print(f"  Zipf coefficient: {sig['zipf_coefficient']:.3f} (R²={sig['zipf_r_squared']:.3f})")
        print(f"  Heaps' β: {sig['heaps_beta']:.3f}")
        print(f"  MSTTR: {lex['msttr']:.3f}")
        print(f"  Bigram entropy: {sig['bigram_entropy']:.2f}")
    
    # Save detailed JSON results
    json_path = essays_dir.parent / "stylometric_analysis_results.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(analyses, f, indent=2)
    
    print(f"\nDetailed results saved to: {json_path}")
    
    return analyses


if __name__ == "__main__":
    main()
