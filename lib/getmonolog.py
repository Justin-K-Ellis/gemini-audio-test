from google import genai
from google.genai import types

from .wavefile import wave_file

def get_monolog(prompt: str):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a monolog."""
    client = genai.Client()

    print("Creating the monolog...")
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name='Kore',
                    )
                )
            ),
        )
        )

        data = response.candidates[0].content.parts[0].inline_data.data

        file_name='monolog_test2.wav'
        wave_file(file_name, data) # Saves the file to current directory
        print("Monolog created and saved!")
    except Exception as error:
        print("Something went wrong when creating the monolog.")
        print(error)