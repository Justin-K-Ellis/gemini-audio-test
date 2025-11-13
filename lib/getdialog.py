from google import genai
from google.genai import types

from .wavefile import wave_file

def get_dialog(prompt: str):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a dialog."""
    client = genai.Client()

    print("Creating audio file...")
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                    types.SpeakerVoiceConfig(
                        speaker='Joe',
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name='Kore',
                            )
                        )
                    ),
                    types.SpeakerVoiceConfig(
                        speaker='Jane',
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name='Puck',
                            )
                        )
                    ),
                    ]
                )
            )
        )
        )

        data = response.candidates[0].content.parts[0].inline_data.data
        file_name='dialog_test.wav'
        wave_file(file_name, data) # Saves the file to current directory
        print("Dialog audio created and saved!")

    except Exception as error:
        print("Something went wrong when creating the dialog.")
        print(error)
