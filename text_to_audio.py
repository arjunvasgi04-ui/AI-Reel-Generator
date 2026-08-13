
import os
from typing import IO
from io import BytesIO
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVEN_LABS_API_KEY


elevenlabs = ElevenLabs(
    api_key=ELEVEN_LABS_API_KEY,
)


def text_to_speech_file(text: str, folder:str) -> IO[bytes]:
    # Perform the text-to-speech conversion
    response = elevenlabs.text_to_speech.stream(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

     # uncomment the line below to play the audio back
    # play(response)
    # Generating a unique file name for the output MP3 file
    save_file_path = os.path.join(f"user_uploads/{folder}","audio.mp3")
    # Writing the audio to a file

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    print(f"{save_file_path}: A new audio file was saved successfully!")
    # Return the path of the saved audio file
    return save_file_path


#text_to_speech_file("HEY MY name is Arjun and i ama  good boy","7cb4d9b9-94dd-11f1-b398-e86ade7109ed")
