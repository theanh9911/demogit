@echo off
echo 🤖 AI Chatbot với Hugging Face và Streamlit
echo ================================================
echo.

REM Kích hoạt môi trường ảo
echo 🔧 Kích hoạt môi trường ảo...
call chatbot_env\Scripts\activate.bat

REM Kiểm tra xem môi trường đã được kích hoạt chưa
if not defined VIRTUAL_ENV (
    echo ❌ Không thể kích hoạt môi trường ảo
    pause
    exit /b 1
)

echo ✅ Môi trường ảo đã được kích hoạt: %VIRTUAL_ENV%
echo.

REM Kiểm tra các package đã cài đặt
echo 📦 Kiểm tra packages...
python -c "import streamlit, torch, transformers; print('✅ Tất cả packages đã sẵn sàng!')" 2>nul
if errorlevel 1 (
    echo ⚠️ Một số packages chưa được cài đặt. Đang cài đặt...
    pip install -r requirements_chatbot.txt
)

echo.
echo 🚀 Khởi động AI Chatbot...
echo 📱 Ứng dụng sẽ mở tại: http://localhost:8501
echo ⏳ Đang tải model (có thể mất 30-60 giây)...
echo.
echo 💡 Nhấn Ctrl+C để dừng chatbot
echo.

REM Chạy chatbot
streamlit run simple_chatbot.py

pause 