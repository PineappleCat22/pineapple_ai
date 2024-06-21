from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama2-uncensored", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
)

# hey so idk how to access cloned models so this just uses ollama.
# i need to figure out how to use modelfiles which point to the model location, i guess.
# to do, find out where ollama stores model files.
# some notes:
# using base llama 2 uncen, it doesnt seem to acknowledge itself sometimes. i told it that i was its creator and it was just... fine with that.
# not really what im shooting for. if i can create some kind of handler rule so that it can handle stuff like that, would be schweet
# want to try using the ai with and without the bge embedding model.

# as of now im still waiting on the discord data to comb through, format for ai use, and uhhh yknow install it
# that will pose its own problems, but for now humanizing the ai and preparing it to interface with things like discord and shit is a good first step.
# i am a little concerned about how some of this poses ai models as a data retrieval question (ie asking a question and having an answer in a dataset)
# this does pose a problem: how does me-ai handle questions? and questions without answers? planning on including a basic file of facts for the ai to pull from in that case
# but for questions without answers, i will need to tune the ai's ability to get creative.

# also hey im using a python venv for this so heres where the road gets bumpy.
# for some reason the environment is externally managed
# i was helped along by this thread: https://askubuntu.com/questions/1465218/pip-error-on-ubuntu-externally-managed-environment-%C3%97-this-environment-is-extern
# ill keep a comprehensive list here of packages installed in the virtual environment.
# llama-index-llms-ollama
# llama-index-embeddings-huggingface

# uhhhh i dont know if you need to like... source to the venv every time?
# heres the command you run to point to the venv:
# source .venv/bin/activate
# i hope it works how i think it does so i can automate it

# addendum to the first three lines of notes:
# I FIGURED IT OOOOOOOOOOOOOOOOOOUT
# its pointless but for the sake of portability i will create the modelfiles for both bge and ll2-u, and leave them in.
