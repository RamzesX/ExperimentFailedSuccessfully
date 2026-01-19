# Stylometric Analysis Report: Essay Quality & Mathematical Signatures
## Overview
This analysis identifies mathematical patterns and statistical signatures in the essay collection.
The metrics help assess essay quality and identify distinctive writing characteristics.

## 1. Corpus Statistics
| Essay | Words | Sentences | Vocabulary | TTR |
|-------|-------|-----------|------------|-----|
| The Chalice of Gethsemane.md... | 1936 | 134 | 714 | 0.369 |
| Quantum Sword.md... | 2505 | 126 | 958 | 0.382 |
| When One Became Two.md... | 3550 | 255 | 1192 | 0.336 |
| The Aleph in the Machine.md... | 2567 | 244 | 931 | 0.363 |
| I am disturbed en.md... | 2320 | 299 | 872 | 0.376 |
| From Override to Activation.md... | 2024 | 123 | 929 | 0.459 |
| Ender Bearing the Cross.md... | 1597 | 123 | 594 | 0.372 |
| What They Never Told Me About Mathematic... | 1507 | 161 | 468 | 0.311 |
| The Ghost of Tsushima Sandomierz mode en... | 2898 | 372 | 971 | 0.335 |
| Deva init en.md... | 2808 | 410 | 884 | 0.315 |

## 2. Zipf's Law Compliance (Word Frequency Distribution)
Natural language follows Zipf's Law with coefficient ≈ 1.0. Higher R² indicates better fit to this universal pattern.

| Essay | Zipf Coefficient | R² | Interpretation |
|-------|-----------------|-----|----------------|
| The Chalice of Gethsemane.md... | 0.764 | 0.938 | ~ Slight deviation from typical |
| Quantum Sword.md... | 0.747 | 0.934 | ~ Slight deviation from typical |
| When One Became Two.md... | 0.819 | 0.963 | ~ Slight deviation from typical |
| The Aleph in the Machine.md... | 0.758 | 0.937 | ~ Slight deviation from typical |
| I am disturbed en.md... | 0.748 | 0.945 | ~ Slight deviation from typical |
| From Override to Activation.md... | 0.657 | 0.929 | ~ Slight deviation from typical |
| Ender Bearing the Cross.md... | 0.760 | 0.940 | ~ Slight deviation from typical |
| What They Never Told Me About Mathe... | 0.872 | 0.945 | ~ Slight deviation from typical |
| The Ghost of Tsushima Sandomierz mo... | 0.802 | 0.945 | ~ Slight deviation from typical |
| Deva init en.md... | 0.832 | 0.956 | ~ Slight deviation from typical |

## 3. Heaps' Law (Vocabulary Growth Rate)
Heaps' Law (V = K × N^β) models vocabulary growth. Typical β ≈ 0.4-0.6; higher β indicates richer vocabulary growth.

| Essay | K | β (Beta) | R² | Vocabulary Richness |
|-------|---|----------|-----|--------------------|
| The Chalice of Gethsemane.md... | 1.92 | 0.792 | 0.996 | High - diverse vocabulary |
| Quantum Sword.md... | 1.98 | 0.801 | 0.995 | High - diverse vocabulary |
| When One Became Two.md... | 2.82 | 0.748 | 0.995 | High - diverse vocabulary |
| The Aleph in the Machine.md... | 2.44 | 0.763 | 0.999 | High - diverse vocabulary |
| I am disturbed en.md... | 2.65 | 0.754 | 0.998 | High - diverse vocabulary |
| From Override to Activation.md... | 1.78 | 0.831 | 0.998 | High - diverse vocabulary |
| Ender Bearing the Cross.md... | 2.32 | 0.758 | 0.998 | High - diverse vocabulary |
| What They Never Told Me About Mathe... | 2.82 | 0.701 | 0.998 | High - diverse vocabulary |
| The Ghost of Tsushima Sandomierz mo... | 2.71 | 0.748 | 0.994 | High - diverse vocabulary |
| Deva init en.md... | 3.69 | 0.697 | 0.994 | High - diverse vocabulary |

## 4. Readability Metrics
| Essay | Flesch Score | Grade Level | ARI | Complexity |
|-------|--------------|-------------|-----|------------|
| The Chalice of Gethsemane.md... | 58.5 | 8.7 | 8.3 | Academic |
| Quantum Sword.md... | 42.8 | 12.2 | 14.2 | Academic |
| When One Became Two.md... | 46.9 | 10.2 | 10.5 | Academic |
| The Aleph in the Machine.md... | 51.0 | 8.8 | 8.1 | Academic |
| I am disturbed en.md... | 64.0 | 6.3 | 5.6 | Accessible |
| From Override to Activation.md... | 26.1 | 13.7 | 14.5 | Complex |
| Ender Bearing the Cross.md... | 58.0 | 8.4 | 8.2 | Academic |
| What They Never Told Me About Mathe... | 69.6 | 5.9 | 5.0 | Accessible |
| The Ghost of Tsushima Sandomierz mo... | 70.6 | 5.4 | 4.6 | Accessible |
| Deva init en.md... | 71.1 | 5.0 | 4.9 | Accessible |

## 5. N-gram Entropy (Predictability Patterns)
Higher entropy indicates more diverse, less predictable word combinations.

| Essay | Bigram Entropy | Trigram Entropy | Pattern Type |
|-------|---------------|-----------------|---------------|
| The Chalice of Gethsemane.md... | 10.54 | 10.84 | Highly varied |
| Quantum Sword.md... | 11.06 | 11.26 | Highly varied |
| When One Became Two.md... | 11.40 | 11.71 | Highly varied |
| The Aleph in the Machine.md... | 10.90 | 11.25 | Highly varied |
| I am disturbed en.md... | 10.85 | 11.11 | Highly varied |
| From Override to Activation.md... | 10.82 | 10.95 | Highly varied |
| Ender Bearing the Cross.md... | 10.27 | 10.59 | Highly varied |
| What They Never Told Me About Mathe... | 10.04 | 10.41 | Highly varied |
| The Ghost of Tsushima Sandomierz mo... | 11.01 | 11.39 | Highly varied |
| Deva init en.md... | 10.92 | 11.30 | Highly varied |

## 6. Hapax Legomena (Unique Word Usage)
Hapax legomena are words appearing only once. Higher ratios often indicate specialized vocabulary.

| Essay | Hapax Count | Hapax Ratio | Interpretation |
|-------|-------------|-------------|----------------|
| The Chalice of Gethsemane.md... | 457 | 0.640 | Very rich vocabulary |
| Quantum Sword.md... | 623 | 0.650 | Very rich vocabulary |
| When One Became Two.md... | 694 | 0.582 | Very rich vocabulary |
| The Aleph in the Machine.md... | 598 | 0.642 | Very rich vocabulary |
| I am disturbed en.md... | 537 | 0.616 | Very rich vocabulary |
| From Override to Activation.md... | 606 | 0.652 | Very rich vocabulary |
| Ender Bearing the Cross.md... | 375 | 0.631 | Very rich vocabulary |
| What They Never Told Me About Mathe... | 279 | 0.596 | Very rich vocabulary |
| The Ghost of Tsushima Sandomierz mo... | 604 | 0.622 | Very rich vocabulary |
| Deva init en.md... | 505 | 0.571 | Very rich vocabulary |

## 7. Function Word Signature (Stylometric Markers)
Function words are often unconscious choices and serve as authorship indicators.

| Essay | Articles | Pronouns | Conjunctions | Function Total |
|-------|----------|----------|--------------|----------------|
| The Chalice of Gethsemane.md... | 0.074 | 0.124 | 0.062 | 0.417 |
| Quantum Sword.md... | 0.074 | 0.091 | 0.048 | 0.347 |
| When One Became Two.md... | 0.073 | 0.089 | 0.059 | 0.369 |
| The Aleph in the Machine.md... | 0.103 | 0.088 | 0.039 | 0.389 |
| I am disturbed en.md... | 0.080 | 0.115 | 0.046 | 0.372 |
| From Override to Activation.md... | 0.058 | 0.059 | 0.038 | 0.257 |
| Ender Bearing the Cross.md... | 0.117 | 0.101 | 0.044 | 0.413 |
| What They Never Told Me About Mathe... | 0.081 | 0.146 | 0.048 | 0.434 |
| The Ghost of Tsushima Sandomierz mo... | 0.094 | 0.092 | 0.058 | 0.379 |
| Deva init en.md... | 0.084 | 0.083 | 0.050 | 0.339 |

## 8. Mathematical Signature Summary
Each essay has a unique mathematical 'fingerprint' combining all metrics:

### The Chalice of Gethsemane.md
```
Zipf: α=0.764 (R²=0.938)
Heaps: K=1.92, β=0.792
Entropy: bi=10.54, tri=10.84
Lexical: TTR=0.369, MSTTR=0.742, Yule's K=90.0
```

### Quantum Sword.md
```
Zipf: α=0.747 (R²=0.934)
Heaps: K=1.98, β=0.801
Entropy: bi=11.06, tri=11.26
Lexical: TTR=0.382, MSTTR=0.776, Yule's K=67.2
```

### When One Became Two.md
```
Zipf: α=0.819 (R²=0.963)
Heaps: K=2.82, β=0.748
Entropy: bi=11.40, tri=11.71
Lexical: TTR=0.336, MSTTR=0.739, Yule's K=78.9
```

### The Aleph in the Machine.md
```
Zipf: α=0.758 (R²=0.937)
Heaps: K=2.44, β=0.763
Entropy: bi=10.90, tri=11.25
Lexical: TTR=0.363, MSTTR=0.727, Yule's K=101.0
```

### I am disturbed en.md
```
Zipf: α=0.748 (R²=0.945)
Heaps: K=2.65, β=0.754
Entropy: bi=10.85, tri=11.11
Lexical: TTR=0.376, MSTTR=0.766, Yule's K=68.8
```

### From Override to Activation.md
```
Zipf: α=0.657 (R²=0.929)
Heaps: K=1.78, β=0.831
Entropy: bi=10.82, tri=10.95
Lexical: TTR=0.459, MSTTR=0.808, Yule's K=47.7
```

### Ender Bearing the Cross.md
```
Zipf: α=0.760 (R²=0.940)
Heaps: K=2.32, β=0.758
Entropy: bi=10.27, tri=10.59
Lexical: TTR=0.372, MSTTR=0.719, Yule's K=118.0
```

### What They Never Told Me About Mathematics.md
```
Zipf: α=0.872 (R²=0.945)
Heaps: K=2.82, β=0.701
Entropy: bi=10.04, tri=10.41
Lexical: TTR=0.311, MSTTR=0.670, Yule's K=91.3
```

### The Ghost of Tsushima Sandomierz mode en.md
```
Zipf: α=0.802 (R²=0.945)
Heaps: K=2.71, β=0.748
Entropy: bi=11.01, tri=11.39
Lexical: TTR=0.335, MSTTR=0.736, Yule's K=85.3
```

### Deva init en.md
```
Zipf: α=0.832 (R²=0.956)
Heaps: K=3.69, β=0.697
Entropy: bi=10.92, tri=11.30
Lexical: TTR=0.315, MSTTR=0.744, Yule's K=76.3
```


## 9. Quality Assessment Summary

| Rank | Essay | Quality Score |
|------|-------|---------------|
| 1 | What They Never Told Me About Mathematic... | 8/9 ★★★★★ |
| 2 | The Chalice of Gethsemane.md... | 7/9 ★★★★★ |
| 3 | Quantum Sword.md... | 7/9 ★★★★★ |
| 4 | When One Became Two.md... | 7/9 ★★★★★ |
| 5 | The Aleph in the Machine.md... | 7/9 ★★★★★ |
| 6 | I am disturbed en.md... | 7/9 ★★★★★ |
| 7 | Ender Bearing the Cross.md... | 7/9 ★★★★★ |
| 8 | From Override to Activation.md... | 5/9 ★★★★★ |
| 9 | The Ghost of Tsushima Sandomierz mode en... | 5/9 ★★★★★ |
| 10 | Deva init en.md... | 5/9 ★★★★★ |

## 10. Key Findings

### Statistical Patterns Identified:

1. **Zipf's Law Compliance**: Average coefficient = 0.776 (slight variation from typical)

2. **Vocabulary Growth**: Average Heaps' β = 0.759 (rich vocabulary)

3. **Lexical Diversity**: Average MSTTR = 0.743 (high diversity)

### Authorship Signature Observations:

The function word ratios and punctuation patterns reveal consistent stylistic choices across the essays. Key signature elements include:

- Pronoun usage: 0.099 (indicates narrative style)
- Conjunction usage: 0.049 (indicates argument structure)

### Conclusion

The essays demonstrate sophisticated language use with strong compliance to natural language statistical patterns (Zipf's and Heaps' laws). The high lexical diversity and entropy values indicate creative, non-formulaic writing. The consistent function word signatures suggest a coherent authorial voice even across collaborative human-AI writing.
