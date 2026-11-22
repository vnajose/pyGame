import random

from src.config import CATEGORIAS
from src.recomendacao import (
    criar_pesos_iniciais,
    reforcar_categoria,
    escolher_categoria,
    categoria_menor_peso,
    categoria_favorita,
    porcentagem_categoria,
    calcular_diversidade,
    intervalo_por_diversidade,
    gerar_comidas,
)


def test_pesos_iniciais_todos_iguais():
    """Todas as categorias devem começar com o mesmo peso."""
    pesos = criar_pesos_iniciais(CATEGORIAS)
    assert len(pesos) == len(CATEGORIAS)
    assert len(set(pesos.values())) == 1


def test_reforco_soma_tres_e_entra_no_historico():
    """Comer uma categoria soma 3 ao peso dela e a coloca no histórico."""
    pesos = {"Games": 1, "Música": 1}
    novos_pesos, historico = reforcar_categoria(pesos, [], "Games")
    assert novos_pesos["Games"] == 4
    assert novos_pesos["Música"] == 1
    assert historico == ["Games"]


def test_reforco_nao_altera_o_original():
    """A função não deve modificar o dicionário recebido."""
    pesos = {"Games": 1}
    reforcar_categoria(pesos, [], "Games")
    assert pesos["Games"] == 1


def test_escolher_categoria_com_sorteio_fixo():
    """Com pesos Games=1 e Música=3, sorteio 0.1 cai em Games e 0.5 em Música."""
    pesos = {"Games": 1, "Música": 3}
    assert escolher_categoria(pesos, 0.1) == "Games"
    assert escolher_categoria(pesos, 0.5) == "Música"


def test_escolher_categoria_sorteio_um():
    """O caso de borda sorteio = 1 deve devolver a última categoria."""
    pesos = {"Games": 1, "Música": 3}
    assert escolher_categoria(pesos, 1) == "Música"


def test_categoria_menor_e_maior_peso():
    pesos = {"Games": 10, "Música": 1, "Esporte": 4}
    assert categoria_menor_peso(pesos) == "Música"
    assert categoria_favorita(pesos) == "Games"


def test_porcentagem_categoria():
    pesos = {"Games": 3, "Música": 1}
    assert porcentagem_categoria(pesos, "Games") == 75


def test_diversidade_no_comeco_e_100():
    """Até a 5ª comida o algoritmo ainda não conhece o jogador."""
    assert calcular_diversidade(["Games"] * 5) == 100


def test_diversidade_baixa_com_uma_categoria():
    assert calcular_diversidade(["Games"] * 8) == 20


def test_diversidade_sempre_entre_0_e_100():
    historico = CATEGORIAS * 4
    diversidade = calcular_diversidade(historico)
    assert 0 <= diversidade <= 100


def test_velocidade_aumenta_com_diversidade_baixa():
    """Diversidade baixa deve dar intervalo menor (cobra mais rápida)."""
    assert intervalo_por_diversidade(20) < intervalo_por_diversidade(100)


def test_velocidade_respeita_limite_minimo():
    assert intervalo_por_diversidade(0) >= 60


def test_sempre_existe_uma_comida_fora_da_bolha():
    pesos = {"Games": 50, "Música": 1, "Esporte": 1}
    livres = [(x, y) for x in range(1, 10) for y in range(1, 10)]
    comidas = gerar_comidas(pesos, livres, [], random.Random(42))
    fora = [comida for comida in comidas if comida["fora_da_bolha"]]
    assert len(comidas) == 3
    assert len(fora) == 1
    assert fora[0]["categoria"] != "Games"


def test_comidas_em_celulas_livres_sem_repetir_e_fora_da_cobra():
    pesos = criar_pesos_iniciais(CATEGORIAS)
    livres = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
    cobra = [(1, 1), (2, 1)]
    comidas = gerar_comidas(pesos, livres, cobra, random.Random(7))
    posicoes = [comida["posicao"] for comida in comidas]
    assert len(set(posicoes)) == len(posicoes)
    for posicao in posicoes:
        assert posicao in livres
        assert posicao not in cobra
