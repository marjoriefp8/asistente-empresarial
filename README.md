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

## Despliegue

Este proyecto está pensado para ejecutarse localmente. `sentence-transformers` depende de PyTorch, que por sí solo supera los 512MB de RAM disponibles en los tiers gratuitos de hosting típicos (Render, Railway), por lo que no está desplegado en vivo.

Ver [`analizador-pdf`](https://github.com/marjoriefp8/analizador-pdf) y [`agenteWeb`](https://github.com/marjoriefp8/agenteWeb) para demos en vivo de proyectos con requisitos de memoria más livianos.

## Instalación
1. Clona el repositorio
2. Instala dependencias: `pip install -r requirements.txt`
3. Crea un archivo `.env` con tu API key: `ANTHROPIC_API_KEY=tu_key`
4. Ejecuta: `python app.py`
5. Abre: http://127.0.0.1:5000