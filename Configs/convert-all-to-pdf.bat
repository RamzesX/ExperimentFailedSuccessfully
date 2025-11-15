@echo off
setlocal enabledelayedexpansion

echo ===============================================================
echo   Converting All Essays (Polish + English) to Elegant PDFs
echo ===============================================================
echo.

echo === POLISH VERSIONS ===
echo.

REM Convert Polish Ender
echo Converting: Ender niosacy krzyz (PL)...
pandoc "src\Ender niosący krzyż.md" ^
    -o "output\Ender_niosacy_krzyz.pdf" ^
    --metadata-file=ender-config.yaml ^
    --pdf-engine=xelatex

if !errorlevel! neq 0 (
    echo [X] ERROR: Failed to convert Ender (PL)
) else (
    echo [✓] SUCCESS: Ender_niosacy_krzyz.pdf
)

REM Convert Polish Chalice
echo Converting: Kielich Getsemani (PL)...
pandoc "src\Kielich Getsemani.md" ^
    -o "output\Kielich_Getsemani.pdf" ^
    --metadata-file=kielich-config.yaml ^
    --pdf-engine=xelatex

if !errorlevel! neq 0 (
    echo [X] ERROR: Failed to convert Kielich (PL)
) else (
    echo [✓] SUCCESS: Kielich_Getsemani.pdf
)

echo.
echo === ENGLISH VERSIONS ===
echo.

REM Convert English Ender
echo Converting: Ender Bearing the Cross (EN)...
pandoc "src\Ender Bearing the Cross.md" ^
    -o "output\Ender_Bearing_the_Cross.pdf" ^
    --metadata-file=ender-english-config.yaml ^
    --pdf-engine=xelatex

if !errorlevel! neq 0 (
    echo [X] ERROR: Failed to convert Ender (EN)
) else (
    echo [✓] SUCCESS: Ender_Bearing_the_Cross.pdf
)

REM Convert English Chalice
echo Converting: The Chalice of Gethsemane (EN)...
pandoc "src\The Chalice of Gethsemane.md" ^
    -o "output\The_Chalice_of_Gethsemane.pdf" ^
    --metadata-file=chalice-english-config.yaml ^
    --pdf-engine=xelatex

if !errorlevel! neq 0 (
    echo [X] ERROR: Failed to convert Chalice (EN)
) else (
    echo [✓] SUCCESS: The_Chalice_of_Gethsemane.pdf
)

echo.
echo ===============================================================
echo   All conversions completed!
echo   PDF files are located in: output\
echo ===============================================================
echo.
echo Generated files:
echo   Polish:
echo     - Ender_niosacy_krzyz.pdf
echo     - Kielich_Getsemani.pdf
echo   English:
echo     - Ender_Bearing_the_Cross.pdf
echo     - The_Chalice_of_Gethsemane.pdf
echo ===============================================================
pause