from google import genai
from google.genai import types
from .wavefile import wave_file

from utils.Monolog import Monolog

def get_monolog(monolog: Monolog):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a monolog."""
    client = genai.Client()

    speaker = "Kore" if monolog.speaker_gender == "female" else "Orus"

    print(f"Creating item {monolog.no} (monolog)...")
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

        file_name=f'no_{monolog.no}_{format_lesson_name(monolog.lesson_number)}_type_{monolog.type}_monolog.wav'
        wave_file(f"./output/monologs/{file_name}", data)
        print(f"Item {monolog.no} (monolog) created and saved!")
    except Exception as error:
        print(f"Something went wrong when creating item {monolog.no}.\n")
        print(monolog.text + "\n")
        print(error)

# helper
def format_lesson_name(lesson_name: str) -> str:
    return lesson_name.lower().replace(" ", "_")
    