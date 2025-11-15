# System formatowania esejów filozoficzno-religijnych

## 📚 Przegląd

System ten umożliwia elegancką konwersję esejów z formatu Markdown do profesjonalnie wyglądających dokumentów PDF, zachowując klasyczny styl akademicki odpowiedni dla tekstów filozoficzno-religijnych.

## 🚀 Szybki start

### Podstawowa konwersja
Uruchom skrypt batch:
```batch
convert-to-pdf.bat
```

Lub użyj PowerShell:
```powershell
.\convert-to-pdf.ps1
```

### Ręczna konwersja pojedynczego pliku
```bash
pandoc "src/Twój_esej.md" -o "output/Twój_esej.pdf" --metadata-file=twoj-config.yaml --pdf-engine=xelatex
```

## 📁 Struktura plików

```
Eseje/
├── src/                        # Pliki źródłowe Markdown
│   ├── Ender niosący krzyż.md
│   └── Kielich Getsemani.md
├── output/                     # Wygenerowane PDF-y
├── templates/                  # Szablony LaTeX
│   ├── polish-elegant.tex     # Główny szablon (polskie znaki)
│   ├── simple-elegant.tex     # Prostsza wersja
│   └── biblical-quotes.lua    # Filtr Lua (opcjonalny)
├── ender-config.yaml          # Konfiguracja dla "Ender"
├── kielich-config.yaml        # Konfiguracja dla "Kielich"
└── convert-to-pdf.bat         # Skrypt konwersji
```

## ⚙️ Pliki konfiguracyjne YAML

Każdy esej ma swój plik `.yaml` z metadanymi:

```yaml
---
title: "Tytuł eseju"
subtitle: "Podtytuł (opcjonalny)"
author: "Imię autora"
date: \today           # lub konkretna data
lang: pl-PL

# Opcje pandoc
pdf-engine: xelatex
template: templates/polish-elegant.tex
toc: false            # spis treści
number-sections: false

# Formatowanie
fontsize: 12pt
documentclass: article
classoption:
  - 12pt
  - a4paper
---
```

## 🎨 Dostępne szablony

### 1. `polish-elegant.tex`
- **Zalety**: Pełne wsparcie polskich znaków, elegancka typografia
- **Czcionka**: TeX Gyre Termes (Times-podobna)
- **Użycie**: Domyślny szablon dla polskich tekstów

### 2. `simple-elegant.tex`
- **Zalety**: Minimalistyczny, uniwersalny
- **Czcionka**: Latin Modern
- **Użycie**: Gdy potrzebujesz prostszego układu

### 3. `elegant-essay.tex`
- **Zalety**: Ozdobne inicjały, dekoracje
- **Czcionka**: Linux Libertine
- **Użycie**: Na specjalne okazje (wymaga dodatkowych pakietów)

## 📝 Formatowanie w Markdown

### Cytaty biblijne
Cytaty w kursywie są automatycznie rozpoznawane:
```markdown
*"Ojcze, przebacz im, bo nie wiedzą, co czynią"* (Łk 23,34)
```

### Sekcje
```markdown
## I. Tytuł głównej sekcji
### Podsekcja
```

### Wyróżnienia
```markdown
**pogrubienie** dla ważnych pojęć
*kursywa* dla cytatów i wyróżnień
```

## 🔧 Rozwiązywanie problemów

### Problem: Brakujące znaki polskie
**Rozwiązanie**: Użyj szablonu `polish-elegant.tex` z XeLaTeX

### Problem: Błędy kompilacji
**Rozwiązanie**: Sprawdź czy masz zainstalowane:
- MiKTeX lub TeX Live (pełna instalacja)
- Pandoc 3.0+
- XeLaTeX

### Problem: Brak czcionek
**Rozwiązanie**: Zainstaluj pakiet `tex-gyre` w MiKTeX:
```
miktex packages install tex-gyre
```

## 🎯 Wskazówki

1. **Długie eseje**: Rozważ dodanie spisu treści (`toc: true`)
2. **Przypisy**: Używaj standardowej składni Markdown: `[^1]`
3. **Bibliografia**: Możesz dodać plik `.bib` i użyć cytowań
4. **Własne style**: Modyfikuj szablony `.tex` według potrzeb

## 📚 Zaawansowane opcje

### Dodanie filtra Lua
W pliku konfiguracyjnym YAML:
```yaml
filters:
  - templates/biblical-quotes.lua
```

### Zmiana rozmiaru strony
```yaml
classoption:
  - 11pt
  - a5paper
```

### Numeracja sekcji rzymskimi
```yaml
number-sections: true
```

## 🌟 Przykłady użycia

### Konwersja z własnym szablonem
```bash
pandoc esej.md -o esej.pdf \
  --template=moj_szablon.tex \
  --pdf-engine=xelatex \
  --metadata title="Mój Esej"
```

### Konwersja wielu plików
```powershell
Get-ChildItem src/*.md | ForEach-Object {
    pandoc $_.FullName -o "output/$($_.BaseName).pdf" `
      --template=templates/polish-elegant.tex `
      --pdf-engine=xelatex
}
```

## 📖 Dokumentacja

- [Pandoc Manual](https://pandoc.org/MANUAL.html)
- [LaTeX WikiBooks](https://en.wikibooks.org/wiki/LaTeX)
- [XeLaTeX Guide](https://www.overleaf.com/learn/latex/XeLaTeX)

---

*System stworzony dla esejów filozoficzno-religijnych z pełnym wsparciem języka polskiego.*