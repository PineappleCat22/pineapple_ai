from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

print("Initializing D.A.V.E. AI...")

# bge-base embedding model
print("Starting embedding model: BGE-BASE-EN-v1.5")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
#apparently an embedding model is required. who knew!

# ollama
print("Starting base model: Llama 3")
Settings.llm = Ollama(model="llama3", request_timeout=360.0)

print("Linking data documents...")
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(
    documents, # ALL OF DAVES DIALOG. THIS IS NOT HOW THIS IS SUPPOSED TO WORK. IT WONT WORK
)
# IF I CAN REMOVE THIS I SHOULD

print("Starting the query engine...")
query_engine = index.as_query_engine(streaming=True)
while True:
    response = query_engine.chat(input("Enter a prompt:\n"))
    response.print_response_stream()
#I TRIED CONFIGURING THIS FOR CHAT. NO GUARANTEES, HAHAHAHAHHAHAHA :):):):)
