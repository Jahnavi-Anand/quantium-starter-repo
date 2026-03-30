@echo off

echo Activating virtual environment...
call venv\Scripts\activate

echo Running tests...
pytest

IF %ERRORLEVEL% NEQ 0 (
    echo Tests failed ❌
    exit /b 1
)

echo All tests passed ✅
exit /b 0