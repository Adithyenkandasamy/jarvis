import requests
import os
import tempfile

def say(text):
    url = "http://localhost:8880/v1/audio/speech"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "input": text,
        "voice": "af_sky"  # Use the voice that your server actually loaded
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(response.content)
            temp_audio_path = f.name
        os.system(f"mpg123 {temp_audio_path}")  # Optional: replace with ffplay for better support
        os.remove(temp_audio_path)
    else:
        print("TTS request failed:", response.status_code, response.text)

say("I know things feel heavy right now, but you’re not alone. I care about you deeply. Together, we’ll get through this. One moment, one breath, one step at a time.")
