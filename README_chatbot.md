# 🤖 AI Chatbot với Hugging Face và Streamlit

Một chatbot thông minh được xây dựng bằng Hugging Face Transformers và Streamlit, có giao diện web đẹp và dễ sử dụng.

## ✨ Tính năng

- **Chat real-time** với AI model từ Hugging Face
- **Giao diện web đẹp** với Streamlit
- **Lưu/tải conversation** để theo dõi lịch sử chat
- **Responsive design** hoạt động tốt trên mọi thiết bị
- **Model DialoGPT-medium** cho chất lượng chat tốt

## 🚀 Cài đặt

### 1. Cài đặt dependencies

```bash
pip install -r requirements_chatbot.txt
```

### 2. Chạy ứng dụng

```bash
streamlit run chatbot_app.py
```

Ứng dụng sẽ mở tại: `http://localhost:8501`

## 📁 Cấu trúc Project

```
pythonProject1/
├── chatbot_app.py          # File chính của ứng dụng
├── requirements_chatbot.txt # Dependencies
├── README_chatbot.md       # Hướng dẫn này
└── conversation_*.json     # Files lưu conversation (tự động tạo)
```

## 🎯 Cách sử dụng

1. **Khởi động ứng dụng**: Chạy lệnh `streamlit run chatbot_app.py`
2. **Chờ model load**: Model sẽ được tải tự động khi khởi động
3. **Bắt đầu chat**: Nhập tin nhắn vào ô text và nhấn "Gửi"
4. **Quản lý conversation**: 
   - Lưu conversation: Nhấn "Lưu Conversation" trong sidebar
   - Xóa conversation: Nhấn "Xóa Conversation" trong sidebar
   - Làm mới: Nhấn "Làm mới" bên cạnh nút gửi

## 🔧 Tùy chỉnh

### Thay đổi Model

Để sử dụng model khác, thay đổi dòng này trong `chatbot_app.py`:

```python
model_name = "microsoft/DialoGPT-medium"
```

Một số model khác bạn có thể thử:
- `microsoft/DialoGPT-small` (nhỏ hơn, tải nhanh hơn)
- `microsoft/DialoGPT-large` (lớn hơn, chất lượng tốt hơn)
- `EleutherAI/gpt-neo-125M` (model khác)

### Tùy chỉnh giao diện

Bạn có thể thay đổi CSS trong phần `st.markdown` để tùy chỉnh giao diện.

## 🐛 Xử lý lỗi

### Lỗi tải model
- Kiểm tra kết nối internet
- Đảm bảo đã cài đặt đầy đủ dependencies
- Thử model nhỏ hơn nếu RAM không đủ

### Lỗi memory
- Sử dụng model nhỏ hơn
- Giảm `max_length` trong hàm `generate_response`
- Đóng các ứng dụng khác để giải phóng RAM

## 📊 Hiệu suất

- **Model size**: ~774MB (DialoGPT-medium)
- **RAM cần thiết**: ~2GB
- **Thời gian tải model**: ~30-60 giây (tùy thuộc vào internet)
- **Thời gian response**: ~1-3 giây

## 🤝 Đóng góp

Nếu bạn muốn cải thiện project này, hãy:
1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## 📄 License

Project này được phát hành dưới MIT License.

## 🙏 Cảm ơn

- [Hugging Face](https://huggingface.co/) cho các model AI
- [Streamlit](https://streamlit.io/) cho framework web
- [Microsoft](https://www.microsoft.com/) cho DialoGPT model 