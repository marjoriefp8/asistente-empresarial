from agente import calcular, obtener_contacto, ejecutar_herramienta


def test_calcular_suma():
    resultado = calcular("2 + 2")
    assert resultado == "4"


def test_calcular_multiplicacion():
    resultado = calcular("299 * 12")
    assert resultado == "3588"


def test_calcular_operacion_invalida():
    resultado = calcular("esto no es matematica")
    assert resultado == "Error en la operación"


def test_obtener_contacto_ventas():
    resultado = obtener_contacto("ventas")
    assert resultado == "ventas@techcorp.com"


def test_obtener_contacto_soporte():
    resultado = obtener_contacto("soporte")
    assert resultado == "soporte@techcorp.com"


def test_obtener_contacto_invalido():
    resultado = obtener_contacto("marketing")
    assert resultado == "Contacto no encontrado"


def test_ejecutar_herramienta_calcular():
    resultado = ejecutar_herramienta("calcular", {"operacion": "10 * 5"})
    assert resultado == "50"


def test_ejecutar_herramienta_contacto():
    resultado = ejecutar_herramienta("obtener_contacto", {"tipo": "ventas"})
    assert resultado == "ventas@techcorp.com"


def test_ejecutar_herramienta_desconocida():
    resultado = ejecutar_herramienta("herramienta_inexistente", {})
    assert resultado == "Herramienta no encontrada"