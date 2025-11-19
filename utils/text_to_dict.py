from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def format_text_to_dict(prompt: str) -> str:
    print("Working...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            system_instruction="""
            Your task is to format the text of dialogs in to a JSON or Python 
            dictionary-like format. Example:

            Input:
            Man: What do you want to eat tonight?
            Woman: Nothing special. How about curry and rice?
            Man: I had that for lunch. What about pizza?

            Output:
            [
                {
                    "speaker": "Man",
                    "text": "What do you want to eat tonight?"
                },
                {
                    "speaker": "Woman",
                    "text": "Nothing special. How about curry and rice?"
                },
                {
                    "speaker": "Man",
                    "text": "I had that for lunch. What about pizza?"
                }
            ]

            Return this data without any additional comments or questions. 
            Don't add code fences or annotate the output with `json`, etc.
            """
        ),
    )
    return response.text


test_dialog = """
    Boy: Did you do your homework?
    Girl: Yes. Why?
    Boy: I forgot to do mine! Can you help me?
"""

result = format_text_to_dict(test_dialog)
print(result)