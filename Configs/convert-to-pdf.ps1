# Skrypt PowerShell do konwersji esejów do PDF
# Użycie: .\convert-to-pdf.ps1

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "   Konwersja esejów do eleganckiego PDF" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Funkcja konwersji
function Convert-Essay {
    param(
        [string]$SourceFile,
        [string]$OutputFile,
        [string]$ConfigFile,
        [string]$Template = "templates\simple-elegant.tex"
    )

    Write-Host "Konwertuję: $SourceFile..." -ForegroundColor Yellow

    $params = @(
        $SourceFile,
        "-o", $OutputFile,
        "--metadata-file=$ConfigFile",
        "--pdf-engine=xelatex",
        "--template=$Template"
    )

    # Opcjonalnie: użyj filtra Lua (zakomentuj jeśli powoduje problemy)
    # $params += "--lua-filter=templates\biblical-quotes.lua"

    & pandoc $params

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ SUKCES: $OutputFile utworzony" -ForegroundColor Green
    } else {
        Write-Host "✗ BŁĄD: Nie udało się skonwertować $SourceFile" -ForegroundColor Red
    }
    Write-Host ""
}

# Konwertuj oba eseje
Convert-Essay `
    -SourceFile "src\Ender niosący krzyż.md" `
    -OutputFile "output\Ender_niosacy_krzyz.pdf" `
    -ConfigFile "ender-config.yaml"

Convert-Essay `
    -SourceFile "src\Kielich Getsemani.md" `
    -OutputFile "output\Kielich_Getsemani.pdf" `
    -ConfigFile "kielich-config.yaml"

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "   Konwersja zakończona!" -ForegroundColor Cyan
Write-Host "   Pliki PDF znajdują się w katalogu: output\" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan

Write-Host "Naciśnij dowolny klawisz aby zakończyć..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")