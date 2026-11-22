# Configurações centrais do jogo Bolha.
# Todos os números do jogo ficam aqui, para não haver "números soltos" no resto do código.

# ---------------- Tela e grid ----------------
TAMANHO_CELULA = 20          # tamanho de cada casa do grid, em pixels
COLUNAS = 40                 # quantidade de casas na horizontal
LINHAS = 27                  # quantidade de casas na vertical
ALTURA_PAINEL = 60           # faixa no topo da tela para pontos, vidas e diversidade

LARGURA_TELA = COLUNAS * TAMANHO_CELULA                   # 800 px
ALTURA_TELA = LINHAS * TAMANHO_CELULA + ALTURA_PAINEL     # 600 px
FPS = 60

TITULO_JOGO = "Bolha"

# ---------------- Regras gerais ----------------
VIDAS_INICIAIS = 3
TAMANHO_INICIAL_COBRA = 3
PONTOS_POR_COMIDA = 10
BONUS_PONTOS = 5

# ---------------- Categorias de conteúdo ----------------
CATEGORIAS = ["Esporte", "Música", "Games", "Ciência", "Notícias"]

CORES_CATEGORIAS = {
    "Esporte": (230, 126, 34),    # laranja
    "Música": (155, 89, 182),     # roxo
    "Games": (52, 152, 219),      # azul
    "Ciência": (46, 204, 113),    # verde
    "Notícias": (231, 76, 60),    # vermelho
}

LETRAS_CATEGORIAS = {
    "Esporte": "E",
    "Música": "M",
    "Games": "G",
    "Ciência": "C",
    "Notícias": "N",
}

# ---------------- Algoritmo de recomendação ----------------
PESO_INICIAL = 1                  # todas as categorias começam iguais (algoritmo neutro)
REFORCO_PESO = 3                  # quanto o peso sobe a cada comida
QUANTIDADE_COMIDAS_ALGORITMO = 2  # comidas escolhidas pelos pesos (a 3ª é a "fora da bolha")

# ---------------- Diversidade ----------------
JANELA_DIVERSIDADE = 8            # olha as últimas 8 comidas
COMIDAS_PARA_CONHECER = 5         # até a 5ª comida a diversidade fica em 100
PONTOS_POR_CATEGORIA = 20         # cada categoria diferente vale 20 de diversidade
DIVERSIDADE_MAXIMA = 100
DIVERSIDADE_BAIXA = 40            # a partir daqui (ou abaixo) a barra fica vermelha

# ---------------- Velocidade (modo vício) ----------------
# Cada item: (diversidade mínima, casas por segundo).
# Lido de cima para baixo: o primeiro que a diversidade alcançar é o usado.
VELOCIDADES = [
    (60, 8),
    (40, 11),
    (0, 14),
]
MILISSEGUNDOS_POR_SEGUNDO = 1000
INTERVALO_INICIAL_MS = MILISSEGUNDOS_POR_SEGUNDO // 8   # 125 ms por passo
INTERVALO_MINIMO_MS = 60          # limite para o jogo não ficar injogável

# ---------------- Cores da interface ----------------
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
COR_FUNDO = (24, 24, 32)
COR_GRID = (36, 36, 48)
COR_PAREDE = (90, 90, 110)
COR_COBRA = (120, 200, 80)
COR_CABECA = (200, 255, 120)
COR_PAINEL = (15, 15, 20)
COR_TEXTO = (235, 235, 235)
COR_BARRA_OK = (46, 204, 113)
COR_BARRA_BAIXA = (231, 76, 60)
COR_FORA_DA_BOLHA = (255, 255, 255)

# ---------------- Mapa ----------------
CARACTERE_PAREDE = "#"
CARACTERE_LIVRE = "."
CARACTERE_INICIO = "S"

# ---------------- Arquivos ----------------
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_FASE_1 = "data/fase1.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"
