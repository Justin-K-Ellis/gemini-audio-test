from dotenv import load_dotenv

from lib.createdialogprompt import create_dialog_prompt
from lib.getmonolog import get_monolog
from lib.getdialog import get_dialog
from utils.Dialog import Dialog

load_dotenv()

dialog_text1 = """
Man: What do you want to have for dinner today? Pasta?
Woman: How about curry? 
Man: I had that for lunch. 
"""

dialog_text2 = """
Tom: Look! It's snowing a lot today!
Lisa: Yeah! Let's make a snowman outside.
Tom: Good idea. After that, we can drink hot chocolate inside.
"""

dialog_texts: list[Dialog] = [
    Dialog(dialog_text1, speaker1="Man", speaker1_gen="male", speaker2="Woman", speaker2_gen="female")
]


def main():
    for index, dialog in enumerate(dialog_texts):
        get_dialog(dialog, index=index)


if __name__ == "__main__":
    main()
