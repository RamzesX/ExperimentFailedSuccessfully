@echo off
setlocal enabledelayedexpansion

echo ===============================================
echo   Converting English Essays to Elegant PDFs
echo ===============================================
echo.

REM Convert Ender Bearing the Cross
echo Converting: Ender Bearing the Cross...
pandoc "src\Ender Bearing the Cross.md" ^
    -o "output\Ender_Bearing_the_Cross.pdf" ^
    --metadata-file=ender-english-config.yaml ^
    --pdf-engine=xelatex ^
    --verbose

if !errorlevel! neq 0 (
    echo ERROR: Failed to convert Ender Bearing the Cross
) else (
    echo SUCCESS: Ender_Bearing_the_Cross.pdf created
)

echo.

REM Convert The Chalice of Gethsemane
echo Converting: The Chalice of Gethsemane...
pandoc "src\The Chalice of Gethsemane.md" ^
    -o "output\The_Chalice_of_Gethsemane.pdf" ^
    --metadata-file=chalice-english-config.yaml ^
    --pdf-engine=xelatex ^
    --verbose

if !errorlevel! neq 0 (
    echo ERROR: Failed to convert The Chalice of Gethsemane
) else (
    echo SUCCESS: The_Chalice_of_Gethsemane.pdf created
)

echo.
echo ===============================================
echo   Conversion completed!
echo   PDF files are located in: output\
echo ===============================================
pause