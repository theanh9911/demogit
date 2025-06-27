# 🚀 Hướng dẫn nhanh - AI Chatbot

## ✅ Môi trường ảo đã được tạo!

### Cách chạy chatbot:

**Cách 1: Sử dụng script tự động (Khuyến nghị)**
```bash
# Double-click vào file này
activate_and_run.bat
```

**Cách 2: Chạy thủ công**
```bash
# 1. Kích hoạt môi trường ảo
chatbot_env\Scripts\activate.bat

# 2. Chạy chatbot đơn giản
streamlit run simple_chatbot.py

# 3. Hoặc chạy chatbot đầy đủ
streamlit run chatbot_app.py
```

### 🌐 Truy cập chatbot:
- **URL**: http://localhost:8501
- **Thời gian tải model**: 30-60 giây (lần đầu)
- **Model**: DialoGPT-small (nhanh) hoặc DialoGPT-medium (chất lượng tốt hơn)

### 📁 Files quan trọng:
- `simple_chatbot.py` - Chatbot đơn giản, tải nhanh
- `chatbot_app.py` - Chatbot đầy đủ tính năng
- `activate_and_run.bat` - Script tự động
- `chatbot_env/` - Môi trường ảo

### 🔧 Troubleshooting:
- **Lỗi model không tải**: Kiểm tra kết nối internet
- **Lỗi memory**: Đóng các ứng dụng khác
- **Lỗi port**: Đóng browser và thử lại

### 💡 Tips:
- Lần đầu chạy sẽ tải model từ internet
- Model sẽ được cache lại cho lần sau
- Có thể thay đổi model trong code

---
**🎉 Chúc bạn chat vui vẻ!** 