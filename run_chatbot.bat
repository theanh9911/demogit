@echo off
echo 🤖 AI Chatbot với Hugging Face và Streamlit
echo ================================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python không được cài đặt hoặc không có trong PATH
    echo Vui lòng cài đặt Python từ https://python.org
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt
echo.

REM Cài đặt dependencies
echo 🔧 Đang cài đặt dependencies...
pip install -r requirements_chatbot.txt
if errorlevel 1 (
    echo ❌ Lỗi cài đặt dependencies
    pause
    exit /b 1
)

echo ✅ Cài đặt dependencies thành công!
echo.

REM Chạy chatbot
echo 🚀 Khởi động AI Chatbot...
echo 📱 Ứng dụng sẽ mở tại: http://localhost:8501
echo ⏳ Đang tải model (có thể mất 30-60 giây)...
echo.

streamlit run simple_chatbot.py

pause 