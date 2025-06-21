📦 AI Prompt-to-Video Generator (KlingAI-style)

Streamlit + Runway Gen-2 Based Backend

import streamlit as st import requests import time

st.set_page_config(page_title="AI Talking & Moving Video App", layout="centered") st.title("🎬 Prompt-to-Video AI Generator") st.write("Kling AI जैसा AI वीडियो जनरेट करो — Prompt डालो और Body Motion Video पाओ!")

📥 User Prompt

prompt = st.text_input("📝 Enter your prompt (e.g. A boy is running and waving):")

📤 Runway API (Use your own key here)

RUNWAY_API_KEY = "Unseencraft" VIDEO_GENERATION_URL = "https://api.runwayml.com/v1/generate"

🔁 Function to send prompt to Runway Gen-2 API (mock for now)

def generate_video(prompt): headers = { "Authorization": f"Bearer {RUNWAY_API_KEY}", "Content-Type": "application/json" } data = { "prompt": prompt, "num_frames": 75, "width": 512, "height": 512, "seed": 42 } # 🔁 Uncomment below to use real Runway API (requires access) # response = requests.post(VIDEO_GENERATION_URL, headers=headers, json=data) # video_url = response.json().get("video_url")

# ⚠️ Mock output for demo
st.info("⚠️ Real API access needed. Showing sample video.")
video_url = "https://media.githubusercontent.com/media/runwayml/stable-diffusion/main/example-output.mp4"
return video_url

🚀 Trigger

if st.button("🎥 Generate Video"): if prompt: with st.spinner("⏳ Generating your KlingAI-style video..."): time.sleep(2) video = generate_video(prompt) if video: st.video(video) else: st.error("❌ Video generation failed. Check API Key or quota.") else: st.warning("🚨 Please enter a prompt first!")

st.markdown("""

👨‍💻 Built by UnseenCraft | Inspired by KlingAI """)

