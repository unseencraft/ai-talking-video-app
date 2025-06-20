import streamlit as st
import requests
import openai

# API keys (अपना key डालना मत भूलना!)
openai.api_key = "YOUR_OPENAI_API_KEY"
DID_API_KEY = "YOUR_D-ID_API_KEY"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def create_talking_video(text):
    url = "https://api.d-id.com/talks"
    headers = {
        "Authorization": f"Bearer {DID_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "script": {
            "type": "text",
            "input": text,
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            }
        },
        "source_url": "https://create-images.d-id.com/ExampleFace.png"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("result_url", "")

# Streamlit UI
st.title("🎬 AI Talking Video Generator")

user_input = st.text_input("👤 Enter your prompt (e.g. A girl is walking and talking):")
if st.button("🎥 Generate Talking Video"):
    with st.spinner("Generating..."):
        reply = generate_response(user_input)
        video_url = create_talking_video(reply)
        if video_url:
            st.video(video_url)
        else:
            st.error("❌ Failed to generate video. Try again.")
