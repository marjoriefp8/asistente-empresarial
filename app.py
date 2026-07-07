import anthropic
import json
import os
from flask import Flask, render_template, request, jsonify
from rag import cargar_chunks, buscar_relevantes
from agente import crear_agente, tools, ejecutar_herramienta
from dotenv import load_dotenv
import os

app = Flask(__name__)



load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
cliente = crear_agente(API_KEY)
chunks = cargar_chunks("conocimiento.txt")
historial = []

def responder(pregunta):
    contexto = buscar_relevantes(pregunta, chunks)
    contexto_texto = "\n".join(contexto)

    system_prompt = f"""Eres un asistente empresarial de TechCorp.
Responde siempre en español y de forma concisa.
Usa este contexto para responder:

{contexto_texto}

Si no tienes la información, dilo claramente."""

    historial.append({"role": "user", "content": pregunta})

    respuesta = cliente.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        tools=tools,
        messages=historial
    )

    if respuesta.stop_reason == "tool_use":
        tool_use = next(b for b in respuesta.content if b.type == "tool_use")
        resultado = ejecutar_herramienta(tool_use.name, tool_use.input)

        historial.append({"role": "assistant", "content": respuesta.content})
        historial.append({
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": tool_use.id,
                "content": resultado
            }]
        })

        respuesta_final = cliente.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system_prompt,
            tools=tools,
            messages=historial
        )
        texto = respuesta_final.content[0].text
    else:
        texto = respuesta.content[0].text

    historial.append({"role": "assistant", "content": texto})
    return texto

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    pregunta = data.get("mensaje", "")
    respuesta = responder(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)