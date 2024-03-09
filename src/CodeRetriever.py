import os
import ast
import dotenv
import numpy as np
from openai import OpenAI
from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

dotenv.load_dotenv()

class CodeRetriever:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.environ.get('OPEN_AI_API_KEY'))

    def parse_functions(self, code_str: str) -> list:
        tree = ast.parse(code_str)
        return [ast.unparse(node) for node in tree.body if isinstance(node, ast.FunctionDef)]

    def translate_to_english(self, function_list: list) -> list:
        prompt_system = "Summarize the functions into English within 20 tokens."
        return [self._generate_translation(func, prompt_system) for func in function_list]

    def _generate_translation(self, text, prompt_system):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": text},
            ],
            temperature=0,
            max_tokens=25
        )
        return response.choices[0].message.content

    def normalize_l2(self, np_arr: np.ndarray) -> np.ndarray:
        return normalize(np_arr.reshape(1, -1))

    def generate_embeddings(self, text: str, model_type: str) -> np.ndarray:
        if model_type == 'openai':
            response = self.client.embeddings.create(
                input=text,
                model="text-embedding-3-small",
            )
            embedding = np.array(response.data[0].embedding)
        else:
            model = SentenceTransformer(model_type)
            embedding = model.encode(text)[0]
        return embedding

    def rank_functions(self, query: str, translated_functions: list, model_type: str) -> dict:
        query_embedding = self.generate_embeddings(query, model_type)
        function_embeddings = [self.generate_embeddings(func, model_type) for func in translated_functions]
        ranks = {i: cosine(query_embedding, func_embedding) for i, func_embedding in enumerate(function_embeddings)}
        return dict(sorted(ranks.items(), key=lambda item: item[1]))

    def process_file(self, file_path: str, query: str, model_type: str) -> None:
        with open(file_path) as file:
            code_content = file.read()

        functions = self.parse_functions(code_content)
        english_functions = self.translate_to_english(functions)
        ranked_functions = self.rank_functions(query, english_functions, model_type)

        print("Ranked functions:")
        for i, (index, similarity) in enumerate(ranked_functions.items(), 1):
            function_name = functions[index]
            print(f"Rank {i}: Similarity: {similarity}, Function: {function_name}")