from google import genai
from google.genai import types
from dotenv import load_dotenv

from lib.createdialogprompt import create_dialog_prompt
from lib.getmonolog import get_monolog
from lib.getdialog import get_dialog

load_dotenv()

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


def main():
    # get_monolog("hi there")
    # get_dialog(dialog_prompt)
    # dialog_prompt = create_dialog_prompt(dialog_text)
    # print(dialog_prompt)
    # get_dialog(dialog_prompt)


if __name__ == "__main__":
    main()
