# Relatório de Desenvolvimento

Este documento registra cada tarefa feita no projeto **Bolha**: o que foi feito, como o código ficou e como a arquitetura evoluiu. Ele é atualizado ao final de toda tarefa, para que o grupo possa revisar e entender cada mudança antes de cada entrega.

- Integrantes: José Venâncio de Carvalho Freitas e demais integrantes a preencher
- Repositório: https://github.com/vnajose/pyGame
- Disciplina: Introdução a Algoritmos, Engenharia de Software, PUC Minas, Coração Eucarístico, noite, 2026/2

## Cronograma

| Etapa | Prazo | Situação |
|---|---|---|
| Entrega 1: proposta em `docs/proposta.MD` | 15/11/2026 | Proposta aprovada e publicada no GitHub. Faltam os nomes dos integrantes e o envio do zip no Canvas |
| Atividade individual: docstrings e testes | 14 ou 15/11/2026 | Fora deste repositório. Cada integrante faz a sua |
| Entrega 2: versão parcial executável | 22/11/2026 | Não iniciada |
| Entrega 3: jogo completo, documentação e testes | 29/11/2026 | Não iniciada |
| Apresentação | Semana de 30/11/2026 | Não iniciada |

As entregas são feitas no Canvas, enviando o repositório em arquivo zip.

## Estado atual da arquitetura

O código ainda é o do template oficial. Nenhum arquivo de `src/` foi alterado.

```text
main.py              -> chama executar_jogo()
src/jogo.py          -> loop principal (exemplo do template: jogador, gema e morcego)
src/config.py        -> constantes de tela, cores e caminhos
src/funcoes.py       -> funções puras: pontos, dano, derrota, limite e colisão
src/sprites.py       -> recorte da spritesheet
src/dados.py         -> leitura e gravação do recorde
tests/test_logica.py -> 6 testes das funções puras
```

A arquitetura planejada para o jogo está na seção 15 da proposta.

---

## Registro de tarefas

### Tarefa 1: repositório na conta pessoal e recomeço (11/11 a 13/11/2026)

**O que foi feito**

- O repositório foi recriado em **vnajose/pyGame**, a conta pessoal, a partir do template oficial `ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template`. O repositório antigo, criado por engano na conta da empresa, foi apagado.
- Uma primeira proposta, chamada "Confere Aí!", chegou a ser publicada. Quando o grupo se formou e escolheu outro tema, a branch `main` voltou ao commit inicial do template. Essa proposta antiga está guardada fora do repositório, no arquivo `pyGame-backup-confere-ai.bundle`, para consulta.

**Como ficou o código:** nenhuma mudança. O template roda sem erros e os 6 testes passam.

### Tarefa 2: Entrega 1, proposta do Bolha (13/11/2026)

**O que foi feito**

- A ideia do grupo, um Snake com sistemas de recomendação, foi transformada em `docs/proposta.MD`. O arquivo cobre as 14 seções do template e acrescenta três que o enunciado exige e o template não tinha: organização inicial do código, recursos e declaração de originalidade.
- As ideias do grupo viraram regras com números concretos, para que possam ser testadas. A tabela abaixo mostra cada uma.
- O `README.md` recebeu o nome do jogo, a descrição, as regras e os controles planejados.
- Foi criado um `.gitignore` para não versionar o ambiente virtual e os arquivos de cache.

**Como as ideias do grupo viraram regras**

| Ideia do grupo | Regra proposta |
|---|---|
| O algoritmo gera mais comida do que você come | Cada categoria começa com peso 1 e ganha +3 a cada comida. A chance de uma categoria é o peso dela dividido pela soma dos pesos. |
| A tela inteira vira games | Com 5 comidas de Games, o peso é 16 contra 1 de cada outra, ou seja, 80% de chance de Games. |
| Barra de diversidade | Categorias diferentes entre as últimas 8 comidas, vezes 20. Fica em 100 até a 5ª comida. |
| Portas que só abrem com diversidade alta | A porta abre com diversidade 60 ou mais, ou seja, 3 categorias nas últimas 8. Fechada, ela é parede. |
| Modo vício | 8 casas por segundo com diversidade 60 ou mais, 11 com 40 e 14 com 20. |
| Gráfico do feed | Barras por categoria na tela final, a porcentagem da categoria mais comida e a diversidade média. |

**Decisões tomadas pelo agente, que o grupo deve confirmar**

- **Comida "fora da bolha":** das 3 comidas na tela, uma é sempre de uma categoria diferente da favorita. Sem isso, a bolha poderia ficar impossível de quebrar e o jogo travaria o jogador.
- **Bônus de explorar:** +5 pontos ao trocar de categoria. Isso faz a diversidade valer a pena também na pontuação.
- **Transparência:** o painel mostra o que o algoritmo "acha" que o jogador gosta. Isso liga o jogo ao aspecto de uso responsável.
- **Vidas em vez de morte imediata:** o Snake clássico acaba na primeira batida. Com 3 vidas, o jogador consegue chegar às fases seguintes.
- **Escopo mínimo de 2 fases:** a fase 3 fica como melhoria, caso falte tempo.

**Como ficou o código:** nenhuma mudança em `src/`. A Entrega 1 é só planejamento.

**Decisões técnicas registradas para a Entrega 2**

- O algoritmo de recomendação vai ficar em um módulo próprio, `src/recomendacao.py`, só com funções puras. Isso facilita os testes e permite dividir o trabalho entre os integrantes.
- O sorteio vai usar `escolher_categoria(pesos, sorteio)`, com o número aleatório recebido como parâmetro.
- A cobra vai andar por passos com intervalo de tempo, e não a cada quadro. Assim a velocidade pode mudar com a diversidade.
- As fases ficam em arquivos de texto lidos como matriz, o que cobre os requisitos de arquivos e de estruturas de dados.

**Sugestão de divisão para a Entrega 2**

| Parte | Arquivos |
|---|---|
| Movimento da cobra, colisões e vidas | `src/funcoes.py`, `src/jogo.py` |
| Algoritmo de recomendação e diversidade | `src/recomendacao.py` e testes |
| Fases e arquivos | `src/dados.py`, `data/fase*.txt`, `data/categorias.csv` |
| Desenho, painel e gráfico do feed | `src/desenho.py` |

**Como revisar:** leia `docs/proposta.MD` inteira, principalmente as regras da seção 7 e as decisões acima. Os números de pontos, pesos, velocidades e limites podem ser ajustados agora sem nenhum custo.

---

### Tarefa 3: aprovação e publicação da proposta (15/11/2026)

**O que foi feito**

- O grupo aprovou a proposta do Bolha, incluindo as decisões tomadas pelo agente, sem mudanças.
- As mudanças da Entrega 1 foram registradas em um commit e enviadas para **vnajose/pyGame**.
- Foi gerado o arquivo `pyGame-entrega1.zip`, com o conteúdo do repositório, para envio no Canvas. Ele fica fora do repositório, na pasta `Documents/PessoalJose/Projects`.
- Os nomes dos demais integrantes ainda não foram informados e continuam como "a preencher". Quando chegarem, os três documentos serão atualizados e o zip será gerado de novo.

**Como ficou o código:** nenhuma mudança em `src/`.

**Próximo passo:** a Entrega 2, até 22/11/2026, pede a janela do Pygame, o loop principal, os controles básicos, pelo menos uma interação funcional e um elemento da mecânica temática. O plano é começar pelo algoritmo de recomendação em `src/recomendacao.py`, com testes, e pela cobra andando no grid.

---

## Pendências

- [ ] Preencher os nomes dos integrantes na proposta, no README e neste relatório, e gerar o zip de novo.
- [x] Revisar a proposta com o grupo e confirmar as decisões do agente.
- [x] Publicar no GitHub e gerar o zip para o Canvas.
- [ ] Enviar o zip no Canvas hoje, 15/11/2026, que é o prazo final.
- [ ] Cada integrante confere se entregou a atividade individual de docstrings e testes. O enunciado cita 14/11 e 15/11 como prazo.
