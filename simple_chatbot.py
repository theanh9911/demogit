import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime

# Cấu hình trang
st.set_page_config(
    page_title="Simple AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# CSS đơn giản
st.markdown("""
<style>
    .chat-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .user-msg {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        border-left: 4px solid #2196f3;
    }
    .bot-msg {
        background-color: #f3e5f5;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        border-left: 4px solid #9c27b0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load model từ Hugging Face"""
    try:
        # Sử dụng model nhỏ để tải nhanh
        model_name = "microsoft/DialoGPT-small"
        
        with st.spinner(f"Đang tải model {model_name}..."):
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(model_name)
            
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token
                
        return tokenizer, model
    except Exception as e:
        st.error(f"Lỗi tải model: {e}")
        return None, None

def generate_response(tokenizer, model, user_input):
    """Tạo response từ model"""
    try:
        # Tạo input cho model
        input_text = f"User: {user_input}\nAssistant:"
        inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=256)
        
        # Generate response
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=100,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Decode response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.split("Assistant:")[-1].strip()
        
        return response if response else "Xin lỗi, tôi không hiểu."
        
    except Exception as e:
        return f"Lỗi: {str(e)}"

def main():
    st.title("🤖 Simple AI Chatbot")
    st.markdown("---")
    
    # Load model
    tokenizer, model = load_model()
    
    if not tokenizer or not model:
        st.error("Không thể tải model. Vui lòng kiểm tra kết nối internet.")
        return
    
    st.success("✅ Model đã sẵn sàng!")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="user-msg">
                <strong>👤 Bạn:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bot-msg">
                <strong>🤖 AI:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input
    st.markdown("---")
    
    # Input form
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("💬 Nhập tin nhắn:", placeholder="Hãy nói gì đó...")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            submit = st.form_submit_button("🚀 Gửi", use_container_width=True)
        
        with col2:
            if st.form_submit_button("🔄 Làm mới", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
    
    # Process input
    if submit and user_input.strip():
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input.strip(),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        # Generate bot response
        with st.spinner("🤖 AI đang suy nghĩ..."):
            bot_response = generate_response(tokenizer, model, user_input.strip())
        
        # Add bot message
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_response,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        st.rerun()
    
    # Sidebar info
    with st.sidebar:
        st.header("ℹ️ Thông tin")
        st.write("**Model:** DialoGPT-small")
        st.write("**Framework:** Streamlit + Hugging Face")
        st.write(f"**Tin nhắn:** {len(st.session_state.messages)}")
        
        if st.button("🗑️ Xóa chat"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main() 