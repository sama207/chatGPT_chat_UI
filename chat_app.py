import streamlit as st
import time

st.set_page_config(page_title="Chat App", page_icon="💬")

# Mock responses dictionary
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What would you like to ask?",
    "how are you": "I'm just a mock assistant, but I'm working perfectly!",
    "what is streamlit": "Streamlit is a Python library used to build interactive web apps easily.",
    "help": "You can ask me simple questions like: hello, what is streamlit, or how are you.",
    "bye": "Goodbye! Have a great day!"
}

# Local mock response function
def get_mock_response(user_prompt):
    prompt = user_prompt.lower().strip()

    if prompt in responses:
        return responses[prompt]
    else:
        return "Sorry, I don't have a response for that yet. Try asking something else!"
    
# streaming effect
def stream_response(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
        
st.title("Chat App")
st.write("-----------------------------")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm a mock ChatGPT-style assistant. Ask me something!"
        }
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    

# React to user input
if prompt := st.chat_input("ask me something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
  
    # Generate local mock response
    response = get_mock_response(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        streamed_response = st.write_stream(stream_response(response))

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": streamed_response}
    )