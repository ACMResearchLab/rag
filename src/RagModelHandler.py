# import logging
from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration
import os

class RAGModelHandler:
    def __init__(self):
        """
        Initialize the RAGModelHandler, loadomg the model and related components either from the local cache directory or by downloading them if necessary.

        Raises:
            FileNotFoundError: If the model files are not found in the cache directory or unable to download them.

        Notes:
            The model_name and cache_dir are hardcoded within the method for simplicity. 
            Adjustments may be needed based on specific requirements and configurations.
        """
        print("Loading model... This might take a while.")
        model_name = "facebook/rag-token-nq"
        print("-" * 10 + "cache_dir" + "-" * 10, end="\n")
        cache_dir = os.path.expanduser("~/.cache/huggingface/transformers")
        # if not self.is_model_downloaded(cache_dir, model_name):
        #     print("Do you want to install 40G of data?")
        #     if(not (input() == 'y' or 'Y')):
        #         return 0
                
        print("-" * 10 + "RagTokenizer" + "-" * 10, end="\n")
        # logger.info("Step 1 - Create the dataset")
        self.tokenizer = RagTokenizer.from_pretrained(model_name)
        print("-" * 10 + "RagRetriever" + "-" * 10, end="\n")
        self.retriever = RagRetriever.from_pretrained(model_name, index_name="exact", use_dummy_dataset=True)
        print("-" * 10 + "RagTokenForGeneration" + "-" * 10, end="\n")
        self.model = RagTokenForGeneration.from_pretrained(model_name, retriever=self.retriever)

        # if not self.is_model_downloaded(cache_dir, model_name):
        #     print(f"Downloading model {model_name}...")
        #     print("-" * 10 + "RagTokenizer" + "-" * 10)
        #     self.tokenizer = RagTokenizer.from_pretrained(model_name)
        #     print("-" * 10 + "RagRetriever" + "-" * 10)
        #     self.retriever = RagRetriever.from_pretrained(model_name, index_name="exact", use_dummy_dataset=True)
        #     print("-" * 10 + "RagTokenForGeneration" + "-" * 10)
        #     self.model = RagTokenForGeneration.from_pretrained(model_name, retriever=self.retriever)
        #     print("Model downloaded and loaded successfully.")
        # else:
        #     print(f"Model {model_name} already downloaded. Loading from cache...")
        #     self.tokenizer = RagTokenizer.from_pretrained(model_name, local_files_only=True)
        #     self.retriever = RagRetriever.from_pretrained(model_name, index_name="exact", local_files_only=True)
        #     self.model = RagTokenForGeneration.from_pretrained(model_name, retriever=self.retriever, local_files_only=True)
        #     print("Model loaded successfully from cache.")

    def generate_response(self, query: str, max_length: int = 30):
        print(f"Generating response for query: {query}")
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        output = self.model.generate(input_ids, max_length=max_length)
        print(f"Generated response: {output[0]}")
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def is_model_downloaded(self, cache_dir, model_name):
        return os.path.exists(cache_dir) and len(os.listdir(cache_dir)) > 0
    
    def size_of_download():
        cache_dir = os.path.expanduser("~/.cache/huggingface")
        total_size = 0
        
        for root, dirs, files in os.walk(cache_dir):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
        
        # Convert bytes to human-readable format
        def sizeof_fmt(num, suffix='B'):
            for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
                if abs(num) < 1024.0:
                    return "%3.1f %s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f %s%s" % (num, 'Y', suffix)
        
        return sizeof_fmt(total_size)