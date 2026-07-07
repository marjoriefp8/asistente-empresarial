# Asistente Empresarial con IA

Chatbot empresarial construido con Claude AI que combina RAG, agentes y memoria persistente.

## Características
- RAG: responde preguntas basándose en documentos propios
- Agentes: ejecuta herramientas como cálculos y consultas de contacto
- Memoria: recuerda la conversación completa
- Interfaz web con Flask

## Tecnologías
- Python
- Anthropic Claude API
- Sentence Transformers
- Flask

## Instalación
1. Clona el repositorio
2. Instala dependencias: `pip install -r requirements.txt`
3. Crea un archivo `.env` con tu API key: `ANTHROPIC_API_KEY=tu_key`
4. Ejecuta: `python app.py`
5. Abre: http://127.0.0.1:5000