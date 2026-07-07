import anthropic
import json

def crear_agente(api_key):
    return anthropic.Anthropic(api_key=api_key)

tools = [
    {
        "name": "calcular",
        "description": "Realiza operaciones matemáticas",
        "input_schema": {
            "type": "object",
            "properties": {
                "operacion": {
                    "type": "string",
                    "description": "La operación matemática a evaluar, ejemplo: 299 * 12"
                }
            },
            "required": ["operacion"]
        }
    },
    {
        "name": "obtener_contacto",
        "description": "Obtiene información de contacto de la empresa según el tipo: ventas o soporte",
        "input_schema": {
            "type": "object",
            "properties": {
                "tipo": {
                    "type": "string",
                    "description": "Tipo de contacto: ventas o soporte"
                }
            },
            "required": ["tipo"]
        }
    }
]

def calcular(operacion):
    try:
        return str(eval(operacion))
    except:
        return "Error en la operación"

def obtener_contacto(tipo):
    contactos = {
        "ventas": "ventas@techcorp.com",
        "soporte": "soporte@techcorp.com"
    }
    return contactos.get(tipo, "Contacto no encontrado")

def ejecutar_herramienta(tool_name, tool_input):
    if tool_name == "calcular":
        return calcular(tool_input["operacion"])
    elif tool_name == "obtener_contacto":
        return obtener_contacto(tool_input["tipo"])
    return "Herramienta no encontrada"