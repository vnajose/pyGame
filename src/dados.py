
from src.config import (
    CAMINHO_FASE_1,
    COLUNAS,
    LINHAS,
    CARACTERE_PAREDE,
    CARACTERE_LIVRE,
    CARACTERE_INICIO
)


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0


def carregar_mapa(caminho_arquivo=CAMINHO_FASE_1):
    """Carrega e valida o mapa da fase a partir de um arquivo texto."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            mapa = [list(linha.rstrip("\n")) for linha in arquivo]

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Arquivo da fase não encontrado: {caminho_arquivo}"
        )

    if len(mapa) != LINHAS:
        raise ValueError(
            f"O mapa deve possuir {LINHAS} linhas."
        )

    for linha in mapa:
        if len(linha) != COLUNAS:
            raise ValueError(
                f"Cada linha do mapa deve possuir {COLUNAS} colunas."
            )

    caracteres_validos = {
        CARACTERE_PAREDE,
        CARACTERE_LIVRE,
        CARACTERE_INICIO
    }

    for linha in mapa:
        for caractere in linha:
            if caractere not in caracteres_validos:
                raise ValueError(
                    f"Caractere inválido encontrado: {caractere}"
                )

    quantidade_inicio = sum(
        linha.count(CARACTERE_INICIO) for linha in mapa
    )

    if quantidade_inicio != 1:
        raise ValueError(
            "O mapa deve possuir exatamente um ponto de início (S)."
        )

    if any(
        caractere != CARACTERE_PAREDE for caractere in mapa[0]
    ) or any(
        caractere != CARACTERE_PAREDE for caractere in mapa[-1]
    ):
        raise ValueError("O mapa deve possuir paredes nas bordas.")

    for linha in mapa:
        if (
            linha[0] != CARACTERE_PAREDE
            or linha[-1] != CARACTERE_PAREDE
        ):
            raise ValueError("O mapa deve possuir paredes nas laterais.")

    return mapa


def encontrar_inicio(mapa):
    """Encontra e retorna a posição inicial no formato (coluna, linha)."""
    for numero_linha, linha in enumerate(mapa):
        for numero_coluna, caractere in enumerate(linha):
            if caractere == CARACTERE_INICIO:
                return numero_coluna, numero_linha

    raise ValueError("O ponto de início (S) não foi encontrado.")


def listar_celulas_livres(mapa):
    """Retorna as posições livres no formato (coluna, linha)."""
    celulas_livres = []

    for numero_linha, linha in enumerate(mapa):
        for numero_coluna, caractere in enumerate(linha):
            if caractere == CARACTERE_LIVRE:
                celulas_livres.append((numero_coluna, numero_linha))

    return celulas_livres
