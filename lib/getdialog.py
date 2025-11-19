from google import genai
from google.genai import types

from .wavefile import wave_file

def get_dialog(text: str, index: int = 0, speaker1 = "Joe", speaker2 = "Jane"):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a dialog."""
    client = genai.Client()

    prompt = f"""
    TTS the following conversation between {speaker1} and {speaker2}:

    {text}
    """

    print(f"Creating audio file {index}...")
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
                        speaker=speaker1,
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name='Kore',
                            )
                        )
                    ),
                    types.SpeakerVoiceConfig(
                        speaker=speaker2,
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
        file_name=f'dialog_{index}.wav'
        wave_file(f"./output/{file_name}", data)
        print(f"Dialog {index} audio created and saved!")

    except Exception as error:
        print(f"Something went wrong when creating dialog {index}.")
        print(error)
