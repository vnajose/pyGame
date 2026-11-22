"""O "algoritmo de recomendação" do jogo Bolha.

Todas as funções são puras: recebem dados, devolvem um resultado e não usam Pygame.
Assim elas podem ser testadas com pytest sem abrir a janela do jogo.
"""

import random

from src.config import (
    PESO_INICIAL,
    REFORCO_PESO,
    QUANTIDADE_COMIDAS_ALGORITMO,
    JANELA_DIVERSIDADE,
    COMIDAS_PARA_CONHECER,
    PONTOS_POR_CATEGORIA,
    DIVERSIDADE_MAXIMA,
    VELOCIDADES,
    MILISSEGUNDOS_POR_SEGUNDO,
    INTERVALO_MINIMO_MS,
)


def criar_pesos_iniciais(categorias):
    """Cria o dicionário de pesos com todas as categorias iguais (algoritmo neutro)."""
    pesos = {}
    for categoria in categorias:
        pesos[categoria] = PESO_INICIAL
    return pesos


def reforcar_categoria(pesos, historico, categoria):
    """Soma o reforço ao peso da categoria comida e a coloca no histórico.

    Não altera os originais: devolve uma cópia nova de pesos e de histórico.
    """
    novos_pesos = dict(pesos)
    novos_pesos[categoria] = novos_pesos[categoria] + REFORCO_PESO

    novo_historico = list(historico)
    novo_historico.append(categoria)

    return novos_pesos, novo_historico


def escolher_categoria(pesos, sorteio):
    """Escolhe uma categoria com chance proporcional ao peso.

    `sorteio` é um número entre 0 e 1 (ex.: random.random()).
    Cada categoria ocupa uma "faixa" do tamanho do seu peso; a faixa onde
    o sorteio cair é a categoria escolhida.
    """
    total = sum(pesos.values())
    alvo = sorteio * total

    acumulado = 0
    for categoria, peso in pesos.items():
        acumulado = acumulado + peso
        if alvo < acumulado:
            return categoria

    # Se o sorteio for exatamente 1, cai aqui: devolve a última categoria.
    return list(pesos.keys())[-1]


def categoria_menor_peso(pesos):
    """Devolve a categoria com o menor peso (a "fora da bolha")."""
    menor = None
    for categoria, peso in pesos.items():
        if menor is None or peso < pesos[menor]:
            menor = categoria
    return menor


def categoria_favorita(pesos):
    """Devolve a categoria com o maior peso (o que o algoritmo "acha" que você gosta)."""
    maior = None
    for categoria, peso in pesos.items():
        if maior is None or peso > pesos[maior]:
            maior = categoria
    return maior


def porcentagem_categoria(pesos, categoria):
    """Devolve a chance, de 0 a 100, de a próxima comida ser dessa categoria."""
    total = sum(pesos.values())
    return round(pesos[categoria] * 100 / total)


def calcular_diversidade(historico):
    """Calcula a diversidade do feed, de 20 a 100.

    Conta as categorias diferentes entre as últimas comidas e multiplica por 20.
    No começo da partida fica em 100, porque o algoritmo ainda não conhece o jogador.
    """
    if len(historico) <= COMIDAS_PARA_CONHECER:
        return DIVERSIDADE_MAXIMA

    ultimas = historico[-JANELA_DIVERSIDADE:]
    diferentes = len(set(ultimas))
    diversidade = diferentes * PONTOS_POR_CATEGORIA

    return min(diversidade, DIVERSIDADE_MAXIMA)


def intervalo_por_diversidade(diversidade):
    """Devolve o tempo entre os passos da cobra, em milissegundos.

    Quanto menor a diversidade, menor o intervalo, ou seja, a cobra fica mais
    rápida ("modo vício"). Nunca fica abaixo de INTERVALO_MINIMO_MS.
    """
    casas_por_segundo = VELOCIDADES[-1][1]
    for diversidade_minima, velocidade in VELOCIDADES:
        if diversidade >= diversidade_minima:
            casas_por_segundo = velocidade
            break

    intervalo = MILISSEGUNDOS_POR_SEGUNDO // casas_por_segundo
    return max(intervalo, INTERVALO_MINIMO_MS)


def sortear_posicoes(celulas_livres, cobra, quantidade, gerador):
    """Sorteia posições livres, fora da cobra e sem repetir."""
    disponiveis = []
    for celula in celulas_livres:
        if celula not in cobra:
            disponiveis.append(celula)

    quantidade = min(quantidade, len(disponiveis))
    return gerador.sample(disponiveis, quantidade)


def gerar_comidas(pesos, celulas_livres, cobra, gerador=random):
    """Gera as 3 comidas da tela.

    - 2 comidas escolhidas pelos pesos (tendem a repetir o gosto do jogador);
    - 1 comida "fora da bolha", da categoria de menor peso.

    `gerador` é quem sorteia os números. No jogo é o módulo random; nos testes
    usamos random.Random(semente) para o resultado ser sempre o mesmo.
    """
    categorias = []
    for _ in range(QUANTIDADE_COMIDAS_ALGORITMO):
        categorias.append(escolher_categoria(pesos, gerador.random()))
    categorias.append(categoria_menor_peso(pesos))

    posicoes = sortear_posicoes(celulas_livres, cobra, len(categorias), gerador)

    comidas = []
    for indice in range(len(posicoes)):
        comida = {
            "categoria": categorias[indice],
            "posicao": posicoes[indice],
            "fora_da_bolha": indice == len(categorias) - 1,
        }
        comidas.append(comida)

    return comidas
