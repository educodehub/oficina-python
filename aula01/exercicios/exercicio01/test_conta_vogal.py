import pytest
from contar_vogais import contar_vogais

@pytest.mark.parametrize("texto, expected", [
    ("hello", 2),             
    ("Python", 1),           
    ("ALGORITHM", 3),         
    ("Oi eu me chamo Joao", 10),         
    ("", 0),                 
    ("12345", 0),                         
])
def test_contar_vogais(texto, expected):
    result = contar_vogais(texto)
    assert result == expected, f"Falha na contagem de vogais para a entrada '{texto}'. Esperado: {expected}, Recebido: {result}"
