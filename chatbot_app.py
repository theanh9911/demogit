import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import time
from datetime import datetime
import json
import os

# Cấu hình trang
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
    }
    .bot-message {
        background-color: #f3e5f5;
        border-left: 5px solid #9c27b0;
    }
    .message-time {
        font-size: 0.8rem;
        color: #666;
        margin-top: 0.5rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load model và tokenizer từ Hugging Face"""
    try:
        # Sử dụng model nhỏ hơn để tải nhanh hơn
        model_name = "microsoft/DialoGPT-medium"
        
        st.info(f"Đang tải model {model_name}...")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        
        # Thêm padding token nếu chưa có
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            
        return tokenizer, model
    except Exception as e:
        st.error(f"Lỗi khi tải model: {str(e)}")
        return None, None

def generate_response(tokenizer, model, user_input, conversation_history):
    """Tạo response từ model"""
    try:
        # Kết hợp conversation history với input mới
        full_input = ""
        for msg in conversation_history[-5:]:  # Chỉ lấy 5 tin nhắn gần nhất
            if msg["role"] == "user":
                full_input += f"User: {msg['content']}\n"
            else:
                full_input += f"Assistant: {msg['content']}\n"
        
        full_input += f"User: {user_input}\nAssistant:"
        
        # Tokenize input
        inputs = tokenizer.encode(full_input, return_tensors="pt", truncation=True, max_length=512)
        
        # Generate response
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=150,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Decode response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Trích xuất phần response mới
        response = response.split("Assistant:")[-1].strip()
        
        return response if response else "Xin lỗi, tôi không hiểu. Bạn có thể nói rõ hơn không?"
        
    except Exception as e:
        st.error(f"Lỗi khi tạo response: {str(e)}")
        return "Xin lỗi, có lỗi xảy ra. Vui lòng thử lại."

def save_conversation(conversation_history):
    """Lưu conversation vào file"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.json"
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(conversation_history, f, ensure_ascii=False, indent=2)
        
        return filename
    except Exception as e:
        st.error(f"Lỗi khi lưu conversation: {str(e)}")
        return None

def load_conversation(filename):
    """Load conversation từ file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Lỗi khi load conversation: {str(e)}")
        return []

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Chatbot</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Cài đặt")
        
        # Load model
        tokenizer, model = load_model()
        
        if tokenizer and model:
            st.success("✅ Model đã sẵn sàng!")
        else:
            st.error("❌ Không thể tải model")
            return
        
        st.divider()
        
        # Quản lý conversation
        st.subheader("💾 Quản lý Chat")
        
        if st.button("💾 Lưu Conversation"):
            if "conversation_history" in st.session_state:
                filename = save_conversation(st.session_state.conversation_history)
                if filename:
                    st.success(f"Đã lưu conversation vào {filename}")
        
        if st.button("🗑️ Xóa Conversation"):
            if "conversation_history" in st.session_state:
                st.session_state.conversation_history = []
                st.success("Đã xóa conversation!")
                st.rerun()
        
        st.divider()
        
        # Thông tin
        st.subheader("ℹ️ Thông tin")
        st.write("**Model:** DialoGPT-medium")
        st.write("**Framework:** Hugging Face + Streamlit")
        st.write("**Tính năng:**")
        st.write("- Chat real-time")
        st.write("- Lưu/tải conversation")
        st.write("- Giao diện đẹp")
        
    # Main chat area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Initialize conversation history
        if "conversation_history" not in st.session_state:
            st.session_state.conversation_history = []
        
        # Display conversation history
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.conversation_history:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>👤 Bạn:</strong><br>
                        {message["content"]}
                        <div class="message-time">{message["timestamp"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <strong>🤖 AI:</strong><br>
                        {message["content"]}
                        <div class="message-time">{message["timestamp"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Input area
        st.divider()
        
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_area(
                "💬 Nhập tin nhắn của bạn:",
                height=100,
                placeholder="Hãy nói gì đó với tôi..."
            )
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                submit_button = st.form_submit_button("🚀 Gửi", use_container_width=True)
            
            with col2:
                if st.form_submit_button("🔄 Làm mới", use_container_width=True):
                    st.session_state.conversation_history = []
                    st.rerun()
        
        # Process user input
        if submit_button and user_input.strip():
            # Add user message to history
            user_message = {
                "role": "user",
                "content": user_input.strip(),
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.conversation_history.append(user_message)
            
            # Generate bot response
            with st.spinner("🤖 AI đang suy nghĩ..."):
                bot_response = generate_response(
                    tokenizer, 
                    model, 
                    user_input.strip(), 
                    st.session_state.conversation_history
                )
            
            # Add bot message to history
            bot_message = {
                "role": "assistant",
                "content": bot_response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.conversation_history.append(bot_message)
            
            # Rerun to display new messages
            st.rerun()

if __name__ == "__main__":
    main() 