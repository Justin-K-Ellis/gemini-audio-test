from dotenv import load_dotenv

from lib.getmonolog import get_monolog
from lib.getdialog import get_dialog
from lib.read_monolog_csv import read_in_monolog_csv
from utils.Dialog import Dialog
from utils.Monolog import Monolog


load_dotenv()

# == Dialogs ==
# dialog_text1 = """
# Man: What do you want to have for dinner today? Pasta?
# Woman: How about curry? 
# Man: I had that for lunch. 
# """

# dialog_text2 = """
# Tom: Look! It's snowing a lot today!
# Lisa: Yeah! Let's make a snowman outside.
# Tom: Good idea. After that, we can drink hot chocolate inside.
# """

# dialog_texts: list[Dialog] = [
#     Dialog(dialog_text1, speaker1="Man", speaker1_gen="male", speaker2="Woman", speaker2_gen="female"),
#     Dialog(dialog_text2, speaker1="Tom", speaker1_gen="male", speaker2="Lisa", speaker2_gen="female")
# ]

def main():
    monologs_path = "./input/monologs.csv"
    monologs = read_in_monolog_csv(filepath=monologs_path)
    for index, monolog in enumerate(monologs):
        get_monolog(monolog=monolog, index=index)


if __name__ == "__main__":
    main()
