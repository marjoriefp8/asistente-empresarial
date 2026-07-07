from sentence_transformers import SentenceTransformer
import numpy as np

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def cargar_chunks(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return [linea.strip() for linea in lineas if linea.strip()]

def buscar_relevantes(pregunta, chunks, top=3):
    embedding_pregunta = modelo.encode([pregunta])
    embeddings_chunks = modelo.encode(chunks)
    similitudes = np.dot(embeddings_chunks, embedding_pregunta.T).flatten()
    indices = np.argsort(similitudes)[::-1][:top]
    return [chunks[i] for i in indices]