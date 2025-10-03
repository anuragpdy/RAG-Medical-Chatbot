import os
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DB_FAISS_PATH = "vectorstore/db_faiss"
DATA_PATH = "C:/Users/Unnati/Desktop/Courses/GenAI Courses/LLMOps & AIOps/RAG Medical Chatbot/WorkingDirectory/RAG-Medical-Chatbot/data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50