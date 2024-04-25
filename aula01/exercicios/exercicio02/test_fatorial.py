import pytest
from fatorial import calcular_fatorial

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (5, 120),
    (10, 3628800),
    (3, 6),
    (-1, "O número deve ser não negativo"),
    (-5, "O número deve ser não negativo"),
])
def test_fatorial(n, expected):
    # Testes do fatorial
    result = calcular_fatorial(n)
    assert result == expected, f"Falha ao calcular fatorial de {n}. Esperado: {expected}, Recebido: {result}"
