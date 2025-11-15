@echo off
setlocal enabledelayedexpansion

echo ===============================================
echo   Konwersja esejow do eleganckiego PDF
echo ===============================================
echo.

REM Konwertuj Ender niosacy krzyz
echo Konwertuje: Ender niosacy krzyz...
pandoc "src\Ender niosący krzyż.md" ^
    -o "output\Ender_niosacy_krzyz.pdf" ^
    --metadata-file=ender-config.yaml ^
    --pdf-engine=xelatex ^
    --verbose

if !errorlevel! neq 0 (
    echo BLAD: Nie udalo sie skonwertowac Ender niosacy krzyz
) else (
    echo SUKCES: Ender_niosacy_krzyz.pdf utworzony
)

echo.

REM Konwertuj Kielich Getsemani
echo Konwertuje: Kielich Getsemani...
pandoc "src\Kielich Getsemani.md" ^
    -o "output\Kielich_Getsemani.pdf" ^
    --metadata-file=kielich-config.yaml ^
    --pdf-engine=xelatex ^
    --verbose

if !errorlevel! neq 0 (
    echo BLAD: Nie udalo sie skonwertowac Kielich Getsemani
) else (
    echo SUKCES: Kielich_Getsemani.pdf utworzony
)

echo.
echo ===============================================
echo   Konwersja zakonczona!
echo   Pliki PDF znajduja sie w katalogu: output\
echo ===============================================
pause