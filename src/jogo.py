"""Loop principal do jogo Bolha: janela, estados, controles e integração."""

import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    VIDAS_INICIAIS,
    TAMANHO_INICIAL_COBRA,
    CATEGORIAS,
    CAMINHO_RECORDE,
    COR_FUNDO,
    COR_TEXTO,
)
from src.dados import carregar_recorde, salvar_recorde
from src.recomendacao import (
    criar_pesos_iniciais,
    reforcar_categoria,
    gerar_comidas,
    calcular_diversidade,
    intervalo_por_diversidade,
    categoria_favorita,
    porcentagem_categoria,
)

# PLANO B: funções provisórias do Lucas e do Yudy.
# Quando o merge de cada um entrar, troque estas linhas pelos imports oficiais
# (ex.: from src.funcoes import proxima_posicao, ...).
from src.provisorio import (
    proxima_posicao,
    bateu_na_parede,
    bateu_no_corpo,
    mover_cobra,
    calcular_pontos_comida,
    criar_mapa_provisorio,
    encontrar_inicio,
    listar_celulas_livres,
    desenhar_mapa,
    desenhar_cobra,
    desenhar_comidas,
    desenhar_painel,
)

# Estados do jogo
INICIO = "inicio"
JOGANDO = "jogando"
PAUSA = "pausa"
FIM = "fim"

# Direções: (deslocamento na coluna, deslocamento na linha)
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)

TECLAS_DIRECAO = {
    pygame.K_UP: CIMA,
    pygame.K_w: CIMA,
    pygame.K_DOWN: BAIXO,
    pygame.K_s: BAIXO,
    pygame.K_LEFT: ESQUERDA,
    pygame.K_a: ESQUERDA,
    pygame.K_RIGHT: DIREITA,
    pygame.K_d: DIREITA,
}


def criar_cobra_inicial(inicio):
    """Cria a cobra no S, deitada para a esquerda, andando para a direita."""
    coluna, linha = inicio
    cobra = []
    for indice in range(TAMANHO_INICIAL_COBRA):
        cobra.append((coluna - indice, linha))
    return cobra


def eh_direcao_oposta(direcao_1, direcao_2):
    """Verdadeiro se as duas direções forem opostas (ex.: direita e esquerda)."""
    return direcao_1[0] == -direcao_2[0] and direcao_1[1] == -direcao_2[1]


def nova_partida(mapa):
    """Cria o dicionário com todo o estado de uma partida nova."""
    inicio = encontrar_inicio(mapa)
    cobra = criar_cobra_inicial(inicio)
    pesos = criar_pesos_iniciais(CATEGORIAS)
    livres = listar_celulas_livres(mapa)

    return {
        "cobra": cobra,
        "direcao": DIREITA,
        "proxima_direcao": DIREITA,
        "pesos": pesos,
        "historico": [],
        "comidas": gerar_comidas(pesos, livres, cobra),
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "tempo_acumulado": 0,
    }


def perder_vida(partida, mapa):
    """Tira uma vida e recomeça a cobra no S com tamanho inicial (pontos mantidos)."""
    partida["vidas"] = partida["vidas"] - 1
    partida["cobra"] = criar_cobra_inicial(encontrar_inicio(mapa))
    partida["direcao"] = DIREITA
    partida["proxima_direcao"] = DIREITA
    partida["comidas"] = gerar_comidas(
        partida["pesos"], listar_celulas_livres(mapa), partida["cobra"]
    )


def dar_um_passo(partida, mapa):
    """Anda a cobra uma casa e aplica colisões e comida. Devolve o novo estado do jogo."""
    partida["direcao"] = partida["proxima_direcao"]
    cobra = partida["cobra"]
    nova_cabeca = proxima_posicao(cobra[0], partida["direcao"])

    # A cauda vai sair do lugar neste passo, então não conta como colisão.
    corpo_sem_cauda = cobra[:-1]
    if bateu_na_parede(nova_cabeca, mapa) or bateu_no_corpo(nova_cabeca, corpo_sem_cauda):
        perder_vida(partida, mapa)
        if partida["vidas"] <= 0:
            return FIM
        return JOGANDO

    comida_comida = None
    for comida in partida["comidas"]:
        if comida["posicao"] == nova_cabeca:
            comida_comida = comida

    comeu = comida_comida is not None
    partida["cobra"] = mover_cobra(cobra, nova_cabeca, comeu)

    if comeu:
        partida["pontos"] = partida["pontos"] + calcular_pontos_comida(comida_comida["fora_da_bolha"])
        partida["pesos"], partida["historico"] = reforcar_categoria(
            partida["pesos"], partida["historico"], comida_comida["categoria"]
        )
        partida["comidas"] = gerar_comidas(
            partida["pesos"], listar_celulas_livres(mapa), partida["cobra"]
        )

    return JOGANDO


def desenhar_texto_centralizado(tela, fonte, texto, y):
    """Escreve um texto centralizado na horizontal."""
    superficie = fonte.render(texto, True, COR_TEXTO)
    tela.blit(superficie, superficie.get_rect(center=(LARGURA_TELA // 2, y)))

# Regras mostradas na tela inicial
REGRAS = [
    "Coma as comidas para crescer e ganhar pontos.",
    "Cada cor/letra é uma categoria de conteúdo.",
    "O sistema de recomendação aprende o que você come",
    "e passa a mostrar mais da mesma categoria.",
    "Comidas com contorno branco estão fora da bolha e valem mais.",
    "Pouca diversidade deixa a cobra mais rápida.",
    "Bater na parede ou no próprio corpo tira uma vida.",
]

def desenhar_tela_inicio(tela, fonte_grande, fonte):
    """Tela inicial: título, regras do jogo e controles."""
    tela.fill(COR_FUNDO)

    desenhar_texto_centralizado(tela, fonte_grande, TITULO_JOGO, 70)
    desenhar_texto_centralizado(tela, fonte, "Como jogar", 130)

    y = 170
    espaco_entre_linhas = 28
    for regra in REGRAS:
        desenhar_texto_centralizado(tela, fonte, regra, y)
        y = y + espaco_entre_linhas

    desenhar_texto_centralizado(tela, fonte, "Setas/WASD movem  |  P pausa  |  ESC sai", y + 30)
    desenhar_texto_centralizado(tela, fonte, "Enter para começar", y + 70)


def desenhar_tela_fim(tela, fonte_grande, fonte, partida, recorde):
    tela.fill(COR_FUNDO)
    desenhar_texto_centralizado(tela, fonte_grande, "Fim de jogo", 80)
    desenhar_texto_centralizado(tela, fonte, f"Pontuação: {partida['pontos']}    Recorde: {recorde}", 140)
    desenhar_texto_centralizado(tela, fonte, "Seu feed:", 190)

    y = 230
    for categoria in CATEGORIAS:
        quantidade = partida["historico"].count(categoria)
        desenhar_texto_centralizado(tela, fonte, f"{categoria}: {quantidade}", y)
        y = y + 30

    desenhar_texto_centralizado(tela, fonte, "Enter para jogar de novo", y + 30)


def desenhar_jogo(tela, fonte, partida, mapa):
    diversidade = calcular_diversidade(partida["historico"])
    favorita = categoria_favorita(partida["pesos"])
    desenhar_mapa(tela, mapa)
    desenhar_comidas(tela, partida["comidas"], fonte)
    desenhar_cobra(tela, partida["cobra"])
    desenhar_painel(
        tela, fonte, partida["pontos"], partida["vidas"], diversidade,
        favorita, porcentagem_categoria(partida["pesos"], favorita),
    )


def executar_jogo():
    """Executa o loop principal: eventos, atualização por passos e desenho."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 26)
    fonte_grande = pygame.font.SysFont(None, 72)

    mapa = criar_mapa_provisorio()   # PLANO B: trocar pela leitura de data/fase1.txt do Yudy
    partida = nova_partida(mapa)
    recorde = carregar_recorde(CAMINHO_RECORDE)
    estado = INICIO
    rodando = True

    while rodando:
        tempo_do_frame = relogio.tick(FPS)

        # ---------- Eventos ----------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                elif evento.key == pygame.K_RETURN and estado in (INICIO, FIM):
                    partida = nova_partida(mapa)
                    estado = JOGANDO

                elif evento.key == pygame.K_p and estado == JOGANDO:
                    estado = PAUSA
                elif evento.key == pygame.K_p and estado == PAUSA:
                    estado = JOGANDO

                elif evento.key in TECLAS_DIRECAO and estado == JOGANDO:
                    nova_direcao = TECLAS_DIRECAO[evento.key]
                    if not eh_direcao_oposta(nova_direcao, partida["direcao"]):
                        partida["proxima_direcao"] = nova_direcao

        # ---------- Atualização por passos ----------
        if estado == JOGANDO:
            partida["tempo_acumulado"] = partida["tempo_acumulado"] + tempo_do_frame
            diversidade = calcular_diversidade(partida["historico"])
            intervalo = intervalo_por_diversidade(diversidade)

            if partida["tempo_acumulado"] >= intervalo:
                partida["tempo_acumulado"] = 0
                estado = dar_um_passo(partida, mapa)

                if estado == FIM and partida["pontos"] > recorde:
                    recorde = partida["pontos"]
                    salvar_recorde(CAMINHO_RECORDE, recorde)

        # ---------- Desenho ----------
        if estado == INICIO:
            desenhar_tela_inicio(tela, fonte_grande, fonte)
        elif estado == FIM:
            desenhar_tela_fim(tela, fonte_grande, fonte, partida, recorde)
        else:
            desenhar_jogo(tela, fonte, partida, mapa)
            if estado == PAUSA:
                desenhar_texto_centralizado(tela, fonte_grande, "PAUSA", ALTURA_TELA // 2)

        pygame.display.flip()

    pygame.quit()
