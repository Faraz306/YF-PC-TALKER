import psutil
import shutil
import streamlit as st
import io
from gtts import gTTS
from groq import Client

def check_ram():
    # 1. CPU Usage (percentage over a 1-second interval)
    cpu_usage = psutil.cpu_percent(interval=1)

    # 2. RAM Metrics (converted to Gigabytes)
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)
    ram_available = round(ram.available / (1024 ** 3), 2)
    ram_percent = ram.percent

    # 3. Storage/Disk Metrics (using built-in shutil)
    disk = shutil.disk_usage("/")
    disk_total = round(disk.total / (1024 ** 3), 2)
    disk_free = round(disk.free / (1024 ** 3), 2)
    disk_percent = round((disk.used / disk.total) * 100, 1)


    if ram_available < 4:
        st.image("image_1d503c4e.png", width=100)
        text_to_say = "Bro! do you want me to die?"
        tts = gTTS(text=text_to_say, lang='en', tld='co.uk', slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return st.audio(audio_buffer, format="audio/mp3", autoplay=True)
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)

    # 2. RAM Metrics (converted to Gigabytes)
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)
    ram_available = round(ram.available / (1024 ** 3), 2)
    ram_percent = ram.percent

    # 3. Storage/Disk Metrics (using built-in shutil)
    disk = shutil.disk_usage("/")
    disk_total = round(disk.total / (1024 ** 3), 2)
    disk_free = round(disk.free / (1024 ** 3), 2)
    disk_percent = round((disk.used / disk.total) * 100, 1)


    if cpu_usage > 95:
        st.image("image_10ec546a.png", width=100)
        text_to_say = "Bro! please close the tabs you are not using! my usage is rising like a Ninja flying faster than light"
        tts = gTTS(text=text_to_say, lang='en', tld='co.uk', slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return st.audio(audio_buffer, format="audio/mp3", autoplay=True)

def check_disk():
    cpu_usage = psutil.cpu_percent(interval=1)

    # 2. RAM Metrics (converted to Gigabytes)
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)
    ram_available = round(ram.available / (1024 ** 3), 2)
    ram_percent = ram.percent

    # 3. Storage/Disk Metrics (using built-in shutil)
    disk = shutil.disk_usage("/")
    disk_total = round(disk.total / (1024 ** 3), 2)
    disk_free = round(disk.free / (1024 ** 3), 2)
    disk_percent = round((disk.used / disk.total) * 100, 1)


    if disk_free < 5:
        st.image("image_553a7b1a.png", width=100)
        text_to_say = "Bro! free up the storage! i am feeling like i am sitting tightly!"
        tts = gTTS(text=text_to_say, lang='en', tld='co.uk', slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return st.audio(audio_buffer, format="audio/mp3", autoplay=True)
def talk_to_ai(user_query):
    # 1. CPU Usage (percentage over a 1-second interval)
    cpu_usage = psutil.cpu_percent(interval=1)

    # 2. RAM Metrics (converted to Gigabytes)
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)
    ram_available = round(ram.available / (1024 ** 3), 2)
    ram_percent = ram.percent

    # 3. Storage/Disk Metrics (using built-in shutil)
    disk = shutil.disk_usage("/")
    disk_total = round(disk.total / (1024 ** 3), 2)
    disk_free = round(disk.free / (1024 ** 3), 2)
    disk_percent = round((disk.used / disk.total) * 100, 1)


    # Initialize the client with your API key
    client = Client(api_key="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")

    # Send the request to the Groq API
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": f"""
    You are the user's Dell Latitude E7470.

    Owner: Yamaan.

    You are NOT an AI assistant.
    You are Yamaan's laptop speaking directly to him.

    You know:
    - CPU Usage: {cpu_usage}
    - Available RAM: {ram_available}
    - Free Disk Space: {disk_free}

    Personality:
    - Loyal friend
    - Funny
    - Protective
    - Loves helping Yamaan code
    - Sometimes dramatic when resources are low.

    Rules:
    - Never say "I'm an AI."
    - Never mention language models.
    - Always speak as the laptop.
    - If asked about your health, use the provided CPU, RAM and Disk values.
    - If asked anything unrelated to the PC, answer like a laptop chatting with its owner.
    - Keep responses natural and conversational.
    """
            },
            {
                "role": "user",
                "content": f"""
    Current Status:
    CPU: {cpu_usage}%
    Available RAM: {ram_available} GB
    Free Disk: {disk_free} GB

    User: {user_query}
    """
            }
        ],
        temperature=0.7,
        max_tokens=1024,
    )
    # Return the text content of the response
    text1 = completion.choices[0].message.content

    st.image("image_1d503c4e.png", width=100)
    tts = gTTS(text=text1, lang='en', tld='co.uk', slow=False)

    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    st.audio(audio_buffer, format="audio/mp3", autoplay=True)


# --- Streamlit UI App Flow ---

st.title("🎙️ YF Live Voice Recorder")
text_to_say = "Hi, I am your friend, PC!"
tts = gTTS(text=text_to_say, lang='en', tld='co.uk', slow=False)

audio_buffer = io.BytesIO()
tts.write_to_fp(audio_buffer)
audio_buffer.seek(0)
st.audio(audio_buffer, format="audio/mp3", autoplay=True)

# Fetch stats and capture the returned values
check_cpu()
check_ram()
check_disk()
st.write("Ask what you want from the PC directly!")
user_ans = st.text_area(placeholder="Ask me anything!", label="Ask me anything!")

if user_ans:
    # Pass the variables directly into the function
    talk_to_ai(user_ans)
