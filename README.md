# Bolha

Projeto final da disciplina de Introdução a Algoritmos (Engenharia de Software, PUC Minas, Coração Eucarístico, noite, 2026/2), desenvolvido com Python e Pygame a partir do template oficial da disciplina.

Tema: **IA no cotidiano e uso responsável**, com foco em **sistemas de recomendação e bolha de filtro**.

> Situação: **Entrega 1, proposta.** O código ainda é o do template. As regras abaixo descrevem o jogo planejado. Veja `docs/proposta.MD` e o histórico em `docs/relatorio.md`.

## Integrantes do grupo

- José Venâncio de Carvalho Freitas
- _(a preencher)_
- _(a preencher)_
- _(a preencher)_

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, algoritmo de recomendação e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde e, futuramente, fases e categorias).
- `tests/`: testes unitários com `pytest`.
- `docs/`: proposta inicial (`proposta.MD`) e relatório de desenvolvimento (`relatorio.md`).

## Descrição do jogo

Um Snake em que as comidas são conteúdos de cinco categorias: Esporte, Música, Games, Ciência e Notícias. Um "algoritmo de recomendação" observa o que a cobra come e passa a gerar mais comida da mesma categoria, como o feed de uma rede social. Se o jogador se fecha em uma categoria, a barra de diversidade cai, a cobra acelera no "modo vício" e as portas para as próximas fases não abrem. No final, um gráfico mostra quanto o feed ficou preso na bolha.

## Objetivo do jogador

Passar pelas portas das 3 fases mantendo o feed variado, sem perder todas as vidas.

## Regras do jogo

- O jogador começa com 3 vidas. Bater na parede, no corpo ou em uma porta fechada tira 1 vida.
- Cada comida vale 10 pontos. Trocar de categoria em relação à comida anterior vale 5 pontos extras.
- O algoritmo reforça as categorias comidas, e a tela vai se enchendo delas. Sempre há uma comida "fora da bolha".
- A diversidade conta as categorias diferentes entre as últimas 8 comidas.
- Com diversidade baixa, a cobra fica mais rápida e a porta da fase fica fechada.
- Vitória ao passar pela porta da fase 3. Derrota ao perder todas as vidas.

## Controles

- Setas ou W, A, S, D: mudar a direção da cobra
- P: pausar
- Enter: iniciar ou reiniciar a partida
- ESC: sair do jogo

## Como executar o projeto

```bash
git clone https://github.com/vnajose/pyGame.git
cd pyGame
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Recursos externos

- Template oficial da disciplina: https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template, incluindo a spritesheet de exemplo.
- Pygame (LGPL) e pytest (MIT).

## Decisões técnicas

As decisões são registradas a cada tarefa em `docs/relatorio.md`.
