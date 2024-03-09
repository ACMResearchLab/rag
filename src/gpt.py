import tiktoken
import os
import dotenv
from openai import OpenAI
import logging

dotenv.load_dotenv()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class GPT:
    def __init__(self, model='gpt-3.5-turbo') -> None:
        self.encoding = tiktoken.encoding_for_model(model) # gpt-3.5, gpt-3.5-turbo
        self.api_key = os.environ.get('OPEN_AI_API_KEY')

    def translate_code(self, code_segment: str):
        return self._generate_text(code_segment)

    def _generate_text(self, text):
        prompt_message_system = "Translate the following code into English"
        prompt_message_user = f"{text}"
        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": prompt_message_system},
                {"role": "user", "content": prompt_message_user}
            ]
        )
        return completion.choices[0].message.content

    def tokenize_translated_text(self, code):
        english = self._generate_text(code)
        tokens = self.encoding.encode(english)
        return tokens
