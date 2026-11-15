# Proposta Inicial do Jogo

Este documento apresenta a proposta inicial do jogo, desenvolvido com **Python e Pygame** para o projeto final de Introdução a Algoritmos (Engenharia de Software, PUC Minas, Coração Eucarístico, noite, 2026/2).

Eixo temático do enunciado: **Inteligência Artificial no Cotidiano: Aplicações e Uso Responsável**.

## 1. Nome provisório do jogo

**Nome:**

> **Bolha**

## 2. Integrantes do grupo

- Nome 1: José Venâncio de Carvalho Freitas
- Nome 2: _(a preencher)_
- Nome 3: _(a preencher)_
- Nome 4: _(a preencher)_

## 3. Tema escolhido

**Tema:**

> **Sistemas de recomendação e bolha de filtro.** Plataformas como TikTok, YouTube e Instagram usam algoritmos que observam o que a pessoa consome e mostram cada vez mais do mesmo. Com o tempo, o feed se fecha em poucos assuntos.

**Como esse tema se relaciona com o jogo?**

> No jogo, o "algoritmo" observa as comidas que a cobra come e passa a gerar mais comida da mesma categoria. Se o jogador só come games, a tela logo vira games. Uma barra de diversidade cai quando o jogador se fecha em uma categoria. Com diversidade baixa, a cobra fica mais rápida, no "modo vício", e a porta para a próxima fase não abre. O tema muda as regras de geração de comida, de velocidade e de avanço de fase.

**Aspecto de uso responsável trabalhado:**

> **Análise crítica e transparência.** O jogo mostra que a personalização não é neutra: ela reforça escolhas passadas e pode prender a pessoa em uma bolha. A tela mostra o tempo todo o que o algoritmo "acha" que o jogador gosta. No final, um gráfico mostra quanto do feed ficou preso na bolha. Isso convida o jogador a buscar conteúdo variado de propósito.

## 4. Tipo de jogo

**Tipo escolhido:**

> Snake, com fases e portas.

## 5. Descrição geral do jogo

**Descrição:**

> A tela é um grid em que o jogador controla uma cobra que anda sem parar. Na tela há sempre **3 comidas**, cada uma de uma categoria de conteúdo, com cor e letra próprias: Esporte, Música, Games, Ciência e Notícias.
>
> Cada comida que a cobra come a faz crescer e ensina o "algoritmo". Duas das três comidas na tela são escolhidas pelo algoritmo, que prefere as categorias mais comidas. A terceira é sempre de uma categoria diferente da favorita, a **comida "fora da bolha"**. Assim o jogador sempre tem uma saída, mas precisa escolher ir atrás dela.
>
> No topo, um painel mostra os pontos, as vidas, a fase, a **barra de diversidade** e a frase "O algoritmo acha que você gosta de: Games (62%)". Depois de algumas comidas, aparece uma **porta** no mapa. Ela só abre com diversidade alta. Passar por ela leva à próxima fase, que tem mais paredes. As fases são lidas de arquivos de texto.

## 6. Objetivo do jogador

**Objetivo:**

> Passar pela porta das **3 fases** sem perder todas as vidas. Para isso, o jogador precisa manter o feed variado, porque é a diversidade que abre as portas e mantém a cobra controlável.

## 7. Regras principais

- Regra 1: o jogador começa com **3 vidas**. Bater na parede, no próprio corpo ou em uma porta fechada tira **1 vida** e a cobra recomeça a fase com tamanho 3. Os pontos são mantidos.
- Regra 2: cada comida vale **+10 pontos**. Uma comida de categoria diferente da anterior vale **+5 pontos extras**, o bônus de explorar.
- Regra 3: o algoritmo começa com **peso 1** para cada categoria. Cada comida que a cobra come soma **+3** ao peso da sua categoria. A chance de uma nova comida ser de uma categoria é o peso dela dividido pela soma dos pesos.
- Regra 4: a **diversidade** é o número de categorias diferentes entre as **últimas 8 comidas**, vezes 20, de 20 a 100. Até a 5ª comida, ela fica em 100, porque "o algoritmo ainda não te conhece".
- Regra 5: com diversidade **60 ou mais**, a cobra anda a 8 casas por segundo e a porta fica aberta. Com **40**, anda a 11. Com **20**, entra no **modo vício** e anda a 14. Abaixo de 60, a porta fica fechada e funciona como parede.

## 8. Condição de vitória

**Condição de vitória:**

> O jogador vence ao passar pela porta aberta da **fase 3**.

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:**

> O jogador perde quando as vidas chegam a **zero**. ESC encerra o jogo a qualquer momento.
>
> Em vitória ou derrota, a tela final mostra o **gráfico do feed**: uma barra para cada categoria, com quantas comidas de cada uma foram comidas. Ela mostra também a porcentagem da categoria mais comida, a diversidade média da partida e uma mensagem como "Você passou 70% do tempo na bolha de Games". A pontuação é comparada com o recorde salvo em arquivo.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** a cobra, guardada como uma lista de posições no grid.
- **Obstáculos ou desafios:** as paredes de cada fase, o próprio corpo da cobra, a porta fechada e o aumento de velocidade do modo vício.
- **Itens ou objetos de interação:** as comidas de cinco categorias, a comida "fora da bolha" e a porta de cada fase.
- **Pontuação, vidas, tempo ou progresso:** pontos, vidas, fase atual, barra de diversidade e a frase do algoritmo aparecem no painel. O recorde é salvo em arquivo.

## 11. Controles previstos

**Controles:**

> Setas ou W, A, S, D mudam a direção da cobra. P pausa. ENTER inicia ou reinicia a partida. ESC sai do jogo.

## 12. Principais dificuldades esperadas

- Dificuldade 1: a movimentação em grid com velocidade variável. A cobra precisa andar por "passos" em um intervalo de tempo, e não a cada quadro.
- Dificuldade 2: testar o sorteio do algoritmo. A solução prevista é uma função pura que recebe o número aleatório como parâmetro, para o teste não depender da sorte.
- Dificuldade 3: desenhar o gráfico do feed na tela final com `pygame.draw.rect`, com as barras proporcionais à quantidade de cada categoria.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:**

> Uma cobra controlável no grid, com crescimento e colisões. As comidas têm as cinco categorias e são geradas pelo algoritmo de pesos, com a comida "fora da bolha" garantida. O escopo inclui a barra de diversidade, a velocidade do modo vício, a porta que só abre com diversidade, pelo menos **2 fases** lidas de arquivo, vidas, pontuação, a tela final com o gráfico do feed, o recorde salvo em arquivo e testes das funções de regra.

## 14. Possíveis melhorias, caso haja tempo

- Melhoria 1: a terceira fase e um ranking com os 5 melhores, salvo em `data/ranking.txt`.
- Melhoria 2: efeito visual de "bolha" que fecha as bordas da tela conforme a diversidade cai.
- Melhoria 3: sons de comida e de porta e uma tela inicial com instruções.

## 15. Organização inicial do código

O projeto mantém a estrutura do template oficial e separa as responsabilidades em módulos pequenos:

| Arquivo | Responsabilidade prevista |
|---|---|
| `main.py` | Ponto de entrada: chama `executar_jogo()`. |
| `src/config.py` | Constantes: tamanho do grid, cores das categorias, velocidades, pontos e limites de diversidade. |
| `src/jogo.py` | Loop principal, eventos de teclado e troca de estados (início, jogando, pausa e fim). |
| `src/funcoes.py` | Funções puras de regra: pontos, vidas, próxima posição da cobra, colisões e vitória ou derrota. |
| `src/recomendacao.py` | O "algoritmo": pesos, sorteio da categoria, reforço da preferência, diversidade, velocidade e porta. |
| `src/desenho.py` | Desenho do grid, da cobra, das comidas, do painel e do gráfico do feed. |
| `src/dados.py` | Leitura das fases e das categorias e leitura e gravação do recorde. |
| `src/sprites.py` | Recorte de imagens da spritesheet, mantido do template. |
| `data/categorias.csv` | Nome, cor e letra de cada categoria. |
| `data/fase1.txt`, `data/fase2.txt`, `data/fase3.txt` | Mapa de cada fase como matriz de caracteres: `#` parede, `.` livre, `P` porta e `S` início da cobra. |
| `data/recorde.txt` | Melhor pontuação. |
| `tests/` | Testes `pytest` das regras e do algoritmo de recomendação. |

Estruturas de dados previstas:

```python
pesos = {"Esporte": 1, "Música": 1, "Games": 1, "Ciência": 1, "Notícias": 1}   # dicionário
cobra = [(10, 7), (9, 7), (8, 7)]                     # lista de tuplas (coluna, linha)
comidas = [{"categoria": "Games", "posicao": (15, 4), "fora_da_bolha": False}]   # lista de dicionários
historico = ["Games", "Games", "Música"]              # lista das categorias comidas
mapa = [["#", "#", "#"], ["#", ".", "#"]]             # matriz lida do arquivo da fase
```

O sorteio do algoritmo fica em uma função pura, por exemplo `escolher_categoria(pesos, sorteio)`. Ela recebe um número entre 0 e 1 e devolve a categoria, para que o teste não dependa da sorte.

Conceitos da disciplina previstos: variáveis, entrada pelo teclado, saída na tela, condicionais, laços, listas, dicionários, tuplas, matrizes, funções, modularização, leitura e escrita de arquivos, docstrings e testes.

## 16. Recursos previstos

- Python 3 e Pygame 2, listados em `requirements.txt`.
- `pytest` para os testes.
- Fonte padrão do Pygame, sem arquivo externo.
- Cobra, comidas, portas e gráfico desenhados com `pygame.draw`, sem imagens externas no escopo mínimo.
- Os mapas das fases e a lista de categorias serão escritos pelo grupo.
- Qualquer imagem, som, fonte, código ou tutorial externo usado será listado no `README.md`, com origem e licença.

## 17. Declaração de originalidade

Declaramos que a proposta do jogo **Bolha** é original e foi elaborada para esta disciplina no semestre 2026/2. O estilo Snake é clássico, mas as mecânicas de recomendação, diversidade, modo vício e portas foram criadas pelo grupo para o tema. O jogo não reutiliza jogos de semestres anteriores e não é cópia de tutoriais ou repositórios prontos. O ponto de partida é o template oficial da disciplina. Ferramentas de IA podem ser usadas como apoio no desenvolvimento. Todo recurso externo será identificado no `README.md`, e cada integrante é capaz de explicar as partes que desenvolveu.

- José Venâncio de Carvalho Freitas
- _(demais integrantes)_
