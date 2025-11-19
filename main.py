from dotenv import load_dotenv

from lib.createdialogprompt import create_dialog_prompt
from lib.getmonolog import get_monolog
from lib.getdialog import get_dialog

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

dialog_texts: list[str] = [dialog_text1, dialog_text2]


def main():
    for index, dialog in enumerate(dialog_texts):
        get_dialog(dialog, index=index)


if __name__ == "__main__":
    main()
