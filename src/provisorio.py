"""PLANO B: versões provisórias das partes do Lucas e do Yudy.

Servem só para o jogo rodar enquanto as versões oficiais não chegam.
Quando o merge de cada um entrar:
  1. troque o import correspondente no topo de src/jogo.py;
  2. apague daqui a função que foi substituída.
Quando não sobrar nada, apague este arquivo.
"""

import pygame

from src.config import (
    COLUNAS,
    LINHAS,
    TAMANHO_CELULA,
    ALTURA_PAINEL,
    LARGURA_TELA,
    PONTOS_POR_COMIDA,
    BONUS_PONTOS,
    CARACTERE_PAREDE,
    CARACTERE_LIVRE,
    CARACTERE_INICIO,
    CORES_CATEGORIAS,
    LETRAS_CATEGORIAS,
    COR_FUNDO,
    COR_GRID,
    COR_PAREDE,
    COR_COBRA,
    COR_CABECA,
    COR_PAINEL,
    COR_TEXTO,
    COR_BARRA_OK,
    COR_BARRA_BAIXA,
    COR_FORA_DA_BOLHA,
    DIVERSIDADE_BAIXA,
    DIVERSIDADE_MAXIMA,
    PRETO,
)


# =====================================================================
# LUCAS: regras da cobra (src/funcoes.py)
# =====================================================================

def proxima_posicao(cabeca, direcao):
    """Devolve a nova posição da cabeça andando uma casa na direção."""
    return (cabeca[0] + direcao[0], cabeca[1] + direcao[1])


def bateu_na_parede(posicao, mapa):
    """Verdadeiro se a posição for parede (ou estiver fora do mapa)."""
    coluna, linha = posicao
    if linha < 0 or linha >= len(mapa) or coluna < 0 or coluna >= len(mapa[0]):
        return True
    return mapa[linha][coluna] == CARACTERE_PAREDE


def bateu_no_corpo(posicao, cobra):
    """Verdadeiro se a posição estiver em alguma parte da cobra."""
    return posicao in cobra


def mover_cobra(cobra, nova_cabeca, comeu):
    """Devolve a nova cobra. Se comeu, mantém a cauda (cresce)."""
    nova_cobra = [nova_cabeca] + cobra
    if not comeu:
        nova_cobra.pop()
    return nova_cobra


def calcular_pontos_comida(fora_da_bolha):
    """Pontos de uma comida, com bônus se for fora da bolha."""
    if fora_da_bolha:
        return PONTOS_POR_COMIDA + BONUS_PONTOS
    return PONTOS_POR_COMIDA


# =====================================================================
# YUDY: fase e leitura de dados (data/fase1.txt e src/dados.py)
# =====================================================================

def criar_mapa_provisorio():
    """Cria um mapa com borda de paredes e o S no centro (sem arquivo)."""
    mapa = []
    for linha in range(LINHAS):
        nova_linha = []
        for coluna in range(COLUNAS):
            borda = linha == 0 or linha == LINHAS - 1 or coluna == 0 or coluna == COLUNAS - 1
            if borda:
                nova_linha.append(CARACTERE_PAREDE)
            else:
                nova_linha.append(CARACTERE_LIVRE)
        mapa.append(nova_linha)
    mapa[LINHAS // 2][COLUNAS // 2] = CARACTERE_INICIO
    return mapa


def encontrar_inicio(mapa):
    """Devolve a posição (coluna, linha) do S."""
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == CARACTERE_INICIO:
                return (coluna, linha)
    return (1, 1)


def listar_celulas_livres(mapa):
    """Devolve a lista de posições (coluna, linha) que não são parede."""
    livres = []
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] != CARACTERE_PAREDE:
                livres.append((coluna, linha))
    return livres


# =====================================================================
# YUDY: desenho (src/desenho.py)
# =====================================================================

def _retangulo_da_celula(posicao):
    """Converte (coluna, linha) do grid para um retângulo em pixels."""
    coluna, linha = posicao
    x = coluna * TAMANHO_CELULA
    y = linha * TAMANHO_CELULA + ALTURA_PAINEL
    return pygame.Rect(x, y, TAMANHO_CELULA, TAMANHO_CELULA)


def desenhar_mapa(tela, mapa):
    """Desenha o fundo, o grid e as paredes."""
    tela.fill(COR_FUNDO)
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            retangulo = _retangulo_da_celula((coluna, linha))
            if mapa[linha][coluna] == CARACTERE_PAREDE:
                pygame.draw.rect(tela, COR_PAREDE, retangulo)
            else:
                pygame.draw.rect(tela, COR_GRID, retangulo, 1)


def desenhar_cobra(tela, cobra):
    """Desenha a cobra, com a cabeça em outra cor."""
    for indice in range(len(cobra)):
        cor = COR_CABECA if indice == 0 else COR_COBRA
        pygame.draw.rect(tela, cor, _retangulo_da_celula(cobra[indice]).inflate(-2, -2))


def desenhar_comidas(tela, comidas, fonte):
    """Desenha as comidas com cor e letra; a fora da bolha ganha contorno."""
    for comida in comidas:
        retangulo = _retangulo_da_celula(comida["posicao"])
        cor = CORES_CATEGORIAS[comida["categoria"]]
        pygame.draw.rect(tela, cor, retangulo.inflate(-2, -2))
        if comida["fora_da_bolha"]:
            pygame.draw.rect(tela, COR_FORA_DA_BOLHA, retangulo, 2)
        letra = fonte.render(LETRAS_CATEGORIAS[comida["categoria"]], True, PRETO)
        tela.blit(letra, letra.get_rect(center=retangulo.center))


def desenhar_painel(tela, fonte, pontos, vidas, diversidade, favorita, porcentagem):
    """Desenha pontos, vidas, barra de diversidade e a frase do algoritmo."""
    pygame.draw.rect(tela, COR_PAINEL, (0, 0, LARGURA_TELA, ALTURA_PAINEL))

    texto = fonte.render(f"Pontos: {pontos}    Vidas: {vidas}", True, COR_TEXTO)
    tela.blit(texto, (10, 8))

    frase = f"O algoritmo acha que você gosta de: {favorita} ({porcentagem}%)"
    tela.blit(fonte.render(frase, True, COR_TEXTO), (10, 34))

    # Barra de diversidade
    largura_barra = 200
    x_barra = LARGURA_TELA - largura_barra - 10
    tela.blit(fonte.render("Diversidade", True, COR_TEXTO), (x_barra, 8))
    pygame.draw.rect(tela, COR_GRID, (x_barra, 30, largura_barra, 16))
    cor = COR_BARRA_BAIXA if diversidade <= DIVERSIDADE_BAIXA else COR_BARRA_OK
    preenchido = largura_barra * diversidade // DIVERSIDADE_MAXIMA
    pygame.draw.rect(tela, cor, (x_barra, 30, preenchido, 16))
