@echo off
echo ========================================
echo Tamluk Courts Intelligence Platform
echo Docket Analytics System
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask server...
echo.
echo The application will be available at:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
