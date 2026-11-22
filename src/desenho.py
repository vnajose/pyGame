
import pygame

from src.config import (
    TAMANHO_CELULA,
    ALTURA_PAINEL,
    LARGURA_TELA,
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
    CATEGORIAS,
    CORES_CATEGORIAS,
    LETRAS_CATEGORIAS,
    CARACTERE_PAREDE
)


def _retangulo_da_celula(posicao):
    """Converte uma posição da matriz em um retângulo da tela."""
    coluna, linha = posicao

    return pygame.Rect(
        coluna * TAMANHO_CELULA,
        linha * TAMANHO_CELULA + ALTURA_PAINEL,
        TAMANHO_CELULA,
        TAMANHO_CELULA
    )


def desenhar_mapa(tela, mapa):
    """Desenha o fundo, as paredes e a grade do mapa."""
    tela.fill(COR_FUNDO)

    for numero_linha, linha in enumerate(mapa):
        for numero_coluna, caractere in enumerate(linha):
            posicao = (numero_coluna, numero_linha)
            retangulo = _retangulo_da_celula(posicao)

            if caractere == CARACTERE_PAREDE:
                pygame.draw.rect(tela, COR_PAREDE, retangulo)
            else:
                pygame.draw.rect(
                    tela,
                    COR_GRID,
                    retangulo,
                    1
                )


def desenhar_cobra(tela, cobra):
    """Desenha o corpo e a cabeça da cobra."""
    for indice, posicao in enumerate(cobra):
        retangulo = _retangulo_da_celula(posicao)

        if indice == 0:
            pygame.draw.rect(
                tela,
                COR_CABECA,
                retangulo,
                border_radius=4
            )
        else:
            pygame.draw.rect(
                tela,
                COR_COBRA,
                retangulo,
                border_radius=4
            )


def desenhar_comidas(tela, comidas, fonte):
    """Desenha as comidas com as cores e letras das categorias."""
    for comida in comidas:
        categoria = comida["categoria"]
        posicao = comida["posicao"]
        fora_da_bolha = comida["fora_da_bolha"]

        cor = CORES_CATEGORIAS.get(categoria, COR_TEXTO)
        letra = LETRAS_CATEGORIAS.get(categoria, "?")

        retangulo = _retangulo_da_celula(posicao)

        pygame.draw.rect(
            tela,
            cor,
            retangulo.inflate(-4, -4),
            border_radius=5
        )

        if fora_da_bolha:
            pygame.draw.rect(
                tela,
                COR_FORA_DA_BOLHA,
                retangulo.inflate(-2, -2),
                2,
                border_radius=5
            )

        texto = fonte.render(letra, True, COR_TEXTO)
        texto_retangulo = texto.get_rect(center=retangulo.center)

        tela.blit(texto, texto_retangulo)


def desenhar_painel(
    tela,
    fonte,
    pontos,
    vidas,
    diversidade,
    favorita,
    porcentagem
):
    """Desenha o painel superior com as informações da partida."""
    pygame.draw.rect(
        tela,
        COR_PAINEL,
        pygame.Rect(0, 0, LARGURA_TELA, ALTURA_PAINEL)
    )

    texto_pontos = fonte.render(
        f"Pontos: {pontos}",
        True,
        COR_TEXTO
    )

    texto_vidas = fonte.render(
        f"Vidas: {vidas}",
        True,
        COR_TEXTO
    )

    tela.blit(texto_pontos, (10, 18))
    tela.blit(texto_vidas, (125, 18))

    if favorita is None:
        favorita = "Nenhuma"

    texto_favorita = fonte.render(
        f"Favorita: {favorita}",
        True,
        COR_TEXTO
    )

    tela.blit(texto_favorita, (235, 18))

    texto_diversidade = fonte.render(
        f"Diversidade: {diversidade}%",
        True,
        COR_TEXTO
    )

    tela.blit(texto_diversidade, (430, 18))

    # Limita a diversidade ao intervalo de 0 a 100.
    valor_barra = max(0, min(100, diversidade))

    largura_barra = 140
    altura_barra = 12
    posicao_x = 640
    posicao_y = 24

    fundo_barra = pygame.Rect(
        posicao_x,
        posicao_y,
        largura_barra,
        altura_barra
    )

    pygame.draw.rect(tela, COR_GRID, fundo_barra)

    cor_barra = (
        COR_BARRA_OK
        if valor_barra >= 40
        else COR_BARRA_BAIXA
    )

    preenchimento = pygame.Rect(
        posicao_x,
        posicao_y,
        int(largura_barra * valor_barra / 100),
        altura_barra
    )

    pygame.draw.rect(tela, cor_barra, preenchimento)

    pygame.draw.rect(
        tela,
        COR_TEXTO,
        fundo_barra,
        1
    )