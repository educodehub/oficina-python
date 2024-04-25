# test_calculo_notas.py
import pytest
from media import calcular_media, verificar_aprovacao

@pytest.mark.parametrize("entrada, esperado", [
    ((8.0, 7.0, 7.0, 6.0), 7.0),
    ((9.0, 5.0, 7.0, 6.0), 6.75),
    ((9.0, 9.0, 10.0, 8.0), 9.0),
])
def test_calcular_media(entrada, esperado):
    try:
        resultado = calcular_media(*entrada)
        assert resultado == esperado, f"Falha ao calcular a média para as notas {entrada}. Esperado: {esperado}, Recebido: {resultado}"
    except ValueError as error:
        assert str(error) == esperado, f"Falha ao calcular a média para as notas {entrada}. Mensagem de erro inesperada: {str(error)}"


@pytest.mark.parametrize("entrada, esperado", [
    (7.0, "Aprovado"),
    (6.75, "Reprovado"),
    (9.0, "Aprovado")
])
def test_verificar_aprovacao(entrada, esperado):
    try:
        resultado = verificar_aprovacao(entrada)
        assert resultado == esperado, f"Falha ao verificar aprovação para a média {entrada}. Esperado: {esperado}, Recebido: {resultado}"
    except ValueError as error:
        assert str(error) == esperado, f"Falha ao verificar a aprovação para a média {entrada}. Mensagem de erro inesperada: {str(error)}"

