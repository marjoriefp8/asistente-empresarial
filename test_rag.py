from rag import cargar_chunks


def test_cargar_chunks_lee_lineas_no_vacias(tmp_path):
    archivo = tmp_path / "test_doc.txt"
    archivo.write_text(
        "Primera linea\n\nSegunda linea\n   \nTercera linea\n",
        encoding="utf-8"
    )

    chunks = cargar_chunks(str(archivo))

    assert len(chunks) == 3
    assert chunks[0] == "Primera linea"
    assert chunks[1] == "Segunda linea"
    assert chunks[2] == "Tercera linea"


def test_cargar_chunks_elimina_espacios(tmp_path):
    archivo = tmp_path / "test_doc2.txt"
    archivo.write_text("  Texto con espacios  \n", encoding="utf-8")

    chunks = cargar_chunks(str(archivo))

    assert chunks[0] == "Texto con espacios"