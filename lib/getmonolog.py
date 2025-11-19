from google import genai
from google.genai import types
from .wavefile import wave_file

from utils.Monolog import Monolog

def get_monolog(monolog: Monolog, index: int):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a monolog."""
    client = genai.Client()

    speaker = "Kore" if monolog.speaker_gender == "female" else "Orus"

    print(f"Creating monolog {index}...")
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=monolog.text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=speaker,
                    )
                )
            ),
        )
        )

        data = response.candidates[0].content.parts[0].inline_data.data

        file_name=f'monolog_{index}.wav'
        wave_file(f"./output/{file_name}", data)
        print(f"Monolog {index} created and saved!")
    except Exception as error:
        print(f"Something went wrong when creating monolog {index}.\n")
        print(monolog.text + "\n")
        print(error)