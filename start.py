from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

print("Initializing Pineapple AI...")

# bge-base embedding model
print("Starting embedding model: BGE-BASE-EN-v1.5")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
#I CANT FIGURE OUT HOW TO GET THIS OUT OF HERE

# ollama
print("Starting base model: Llama 3")
Settings.llm = Ollama(model="llama3", request_timeout=360.0, base_url="http://localhost:11434")

print("Linking data documents...")
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(
    documents,
)
# IF I CAN REMOVE THIS I SHOULD

print("Starting the query engine...")
chat_engine = index.as_chat_engine()
chat_engine.chat_repl()
#streaming_response = chat_engine.stream_chat(input("Prompt: \n"))
#for token in streaming_response.response_gen:
#    print(token, end="")
#I TRIED CONFIGURING THIS FOR CHAT. NO GUARANTEES, HAHAHAHAHHAHAHA ;)

# TODO: Query engine while loop doesnt seem to remember itself.
# TODO: The way the data is implemented does NOT work for fine-tuning, that configuration is for answers to questions.
# TODO: I DONT KNOW HOW TO FINE TUNE THE THING