import os
# import wave

from google import genai
from google.genai import types
from dotenv import load_dotenv

from lib.createdialogprompt import create_dialog_prompt
from lib.wavefile import wave_file

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "not found")

dialog_text: list[dict[str, str]] = [
    {
        "speaker": "Joe",
        "text": "How are you today?"
    },
    {
        "speaker": "Jane",
        "text": "I'm fine thank you, and you?"
    },
    {
        "speaker": "Joe",
        "text": "That's great. How's the weather today?"
    },
    {
        "speaker": "Jane",
        "text": "It's cloudy."
    }
]

# # Set up the wave file to save the output:
# def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
#     with wave.open(filename, "wb") as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(sample_width)
#         wf.setframerate(rate)
#         wf.writeframes(pcm)


def get_monolog(prompt: str):
    """Send prompt to Gemini api and save audio to current directory.
    Creates a monolog."""
    client = genai.Client()

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
        print("Audio file created!")

    except Exception as error:
        print("Something went wrong when creating the dialog.")
        print(error)



def main():
    get_monolog("hi there")
    # dialog_prompt = """TTS the following conversation between Joe and Jane:
    #      Joe: How's it going today Jane?
    #      Jane: Not too bad, how about you?"""
    # get_dialog(dialog_prompt)
    # dialog_prompt = create_dialog_prompt(dialog_text)
    # print(dialog_prompt)
    # get_dialog(dialog_prompt)

if __name__ == "__main__":
    main()
