#!/usr/bin/env python3
"""
Script để cài đặt và chạy AI Chatbot
"""

import subprocess
import sys
import os

def install_requirements():
    """Cài đặt các dependencies cần thiết"""
    print("🔧 Đang cài đặt dependencies...")
    
    try:
        # Cài đặt từ requirements file
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements_chatbot.txt"
        ])
        print("✅ Cài đặt dependencies thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi cài đặt dependencies: {e}")
        return False

def run_chatbot():
    """Chạy chatbot"""
    print("🚀 Khởi động AI Chatbot...")
    print("📱 Ứng dụng sẽ mở tại: http://localhost:8501")
    print("⏳ Đang tải model (có thể mất 30-60 giây)...")
    
    try:
        # Chạy streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "simple_chatbot.py"
        ])
    except KeyboardInterrupt:
        print("\n👋 Tạm biệt!")
    except Exception as e:
        print(f"❌ Lỗi chạy chatbot: {e}")

def main():
    print("🤖 AI Chatbot với Hugging Face và Streamlit")
    print("=" * 50)
    
    # Kiểm tra file requirements
    if not os.path.exists("requirements_chatbot.txt"):
        print("❌ Không tìm thấy file requirements_chatbot.txt")
        return
    
    # Cài đặt dependencies
    if not install_requirements():
        return
    
    print("\n" + "=" * 50)
    
    # Chạy chatbot
    run_chatbot()

if __name__ == "__main__":
    main() 