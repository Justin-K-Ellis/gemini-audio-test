def create_dialog_prompt(dialog_list: list[dict[str, str]]):
    result = f"TTS the following conversation between {dialog_list[0]["speaker"]} and {dialog_list[1]["speaker"]}:"
    for part in dialog_list:
        turn = f"\n{part["speaker"]}: {part["text"]}"
        result += turn
    return result