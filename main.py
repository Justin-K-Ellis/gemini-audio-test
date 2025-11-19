from dotenv import load_dotenv

from lib.createdialogprompt import create_dialog_prompt
from lib.getmonolog import get_monolog
from lib.getdialog import get_dialog
from utils.Dialog import Dialog
from utils.Monolog import Monolog

load_dotenv()

# == Dialogs ==
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
    Dialog(dialog_text1, speaker1="Man", speaker1_gen="male", speaker2="Woman", speaker2_gen="female"),
    Dialog(dialog_text2, speaker1="Tom", speaker1_gen="male", speaker2="Lisa", speaker2_gen="female")
]

# == Monologs ==
mono1 = """
Welcome to Green Market. You can find fresh apples near the entrance. Today, we have 
fresh eggs. They are on sale. Don't miss our special bread in asile four.
"""

mono2 = """
There is a beautiful mountain in my town. There is a waterfall near the bottom of the 
mountain and a small shrine at the top of the mountain.
"""

monolog_texts: list[Monolog] = [
    Monolog(text=mono1, speaker_gender="female"),
    Monolog(text=mono2, speaker_gender="male")
]

def main():
    # for index, dialog in enumerate(dialog_texts):
    #     get_dialog(dialog, index=index)
    for index, monolog in enumerate(monolog_texts):
        get_monolog(monolog=monolog, index=index)


if __name__ == "__main__":
    main()
