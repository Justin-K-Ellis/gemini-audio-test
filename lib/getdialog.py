from google import genai
from google.genai import types

from .wavefile import wave_file
from utils.Dialog import Dialog

def get_dialog(dialog: Dialog, index: int = 0):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a dialog."""
    client = genai.Client()
    speaker1_voice = "Kore" if dialog.speaker1_gen == "female" else "Puck"
    speaker2_voice = "Kore" if dialog.speaker2_gen == "female" else "Puck"

    prompt = f"""
    TTS the following conversation between {dialog.speaker1} and {dialog.speaker2}:

    {dialog.text}
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
                        speaker=dialog.speaker1,
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=speaker1_voice,
                            )
                        )
                    ),
                    types.SpeakerVoiceConfig(
                        speaker=dialog.speaker2,
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=speaker2_voice,
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
