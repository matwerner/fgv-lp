# Pygame: Introdução

## 1. Introdução ao Pygame

### 1.1 Jogos como Aplicações Práticas de Orientação a Objetos
- **Contextualização**: Nesta disciplina, optamos por utilizar jogos como um meio de aplicar e solidificar os conceitos de Programação Orientada a Objetos (POO), que já discutimos anteriormente, incluindo herança, polimorfismo e composição.
- **Objetivo**: Através do desenvolvimento de jogos, os alunos terão a oportunidade de ver como esses conceitos se manifestam na prática, promovendo um aprendizado mais dinâmico e interativo.

### 1.2 O que é Pygame?
- **Definição**: Pygame é uma biblioteca de desenvolvimento de jogos para Python, projetada para facilitar a criação de jogos 2D de forma acessível e divertida. É uma ferramenta popular entre educadores e iniciantes que desejam aprender sobre programação de jogos.
  
### 1.3 Exemplos de Jogos Feitos com Pygame
- Para ilustrar o potencial do Pygame, aqui estão alguns exemplos de jogos criados com essa biblioteca:
  - **Super Potato Bruh**: Um jogo de plataforma divertido disponível [aqui](https://dafluffypotato.itch.io/super-potato-bruh).
  - **Flappy Bird**: Uma versão do clássico jogo, que pode ser encontrada [neste link](https://www.pygame.org/project/4846).
  - **Outros Jogos**: Para explorar mais projetos feitos com Pygame, você pode visitar [esta página](https://www.pygame.org/tags/all).

### 1.4 Por que usar Pygame?
- **Aprendizado Prático**: Pygame oferece uma maneira intuitiva de implementar jogos, permitindo que os alunos experimentem com conceitos de programação em um ambiente divertido.
- **Limitações**: É importante notar que, enquanto Pygame é uma excelente ferramenta para educação, existem frameworks mais robustos, como Unity (C#), Unreal Engine (C++) e Godot (C#), que são usados em desenvolvimento profissional de jogos. Contudo, para o aprendizado dos fundamentos da POO, Pygame é uma escolha ideal.

## 2. Estrutura Básica de um Jogo (30 min)

### 2.1 Explicação do Loop do Jogo

* **Conceitos Fundamentais**: Um jogo pode ser dividido em três componentes principais:
    - **Processamento de eventos**: Captura de ações do usuário (teclado, mouse).
    - **Atualização do Jogo**: Modificações nos estados dos objetos, incluindo a física do jogo (ex.: gravidade, movimentação).
    - **Renderização**: Desenho dos objetos na tela.

* **Exemplo Prático**: Pense no jogo da cobra:
    1. O usuário aperta uma tecla do teclado.
    2. O jogo captura a tecla apertada.
    3. Verifica se essa tecla está mapeada a algum comportamento.
    4. Se for um movimento válido (por exemplo, direcional com WASD ou setas), o jogo atualiza a direção da cobra.
    5. O estado do jogo é atualizado, verificando colisões com alimentos ou paredes.
    6. A tela do jogo é atualizada, e o processo recomeça.

### 2.2 Demonstração do Loop Simples

#### Estrutura Básica do Loop do Jogo

```python
import pygame

# Inicializa o Pygame
pygame.init()

# Define a tela do jogo
screen = pygame.display.set_mode((640, 480))  # Cria uma janela de 640x480 pixels
pygame.display.set_caption('Exemplo de Loop do Jogo')  # Define o título da janela

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():  # Captura eventos
        if event.type == pygame.QUIT:  # Verifica se o evento é de fechamento
            running = False  # Encerra o loop

# Encerra o Pygame
pygame.quit()
```

* O que cada linha faz:
  - `pygame.init()`: Inicializa todos os módulos do Pygame.
  - `pygame.display.set_mode((640, 480))`: Cria a janela do jogo.
  - `pygame.display.set_caption('Exemplo de Loop do Jogo')`: Define o título da janela.
  - `pygame.event.get()`: Captura os eventos que ocorrem.
  - `pygame.QUIT`: Evento que indica que a janela foi fechada.
  - `pygame.quit()`: Encerra todos os módulos do Pygame.


#### + Exibindo um Retângulo

```python
import pygame

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Exibir Retângulo')

# Define a cor do retângulo (vermelho)
rect_color = (255, 0, 0)
rect = pygame.Rect(100, 100, 50, 50)  # (x, y, largura, altura)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Preenche a tela com branco
    screen.fill((255, 255, 255))
    # Desenha o retângulo na tela
    pygame.draw.rect(screen, rect_color, rect)
    
    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
```

* O que cada linha faz:

- `rect_x, rect_y, rect_width, rect_height`: Define as coordenadas e o tamanho do retângulo -> (0,0) fica posicionado no canto esquerdo superior.
- `pygame.draw.rect()`: Desenha o retângulo na tela.
- `pygame.display.flip()`: Atualiza a tela para exibir o novo conteúdo.


### 3. Eventos, Teclado e Movimentação

#### O que são Eventos?

* Eventos são ações ou ocorrências que acontecem durante a execução de um programa, e podem ser gerados por:
  - Interações do usuário (como pressionar uma tecla ou mover o mouse); ou,
  - Por ações do sistema (como o fechamento de uma janela).
* No contexto de jogos, os eventos são essenciais para tornar o jogo interativo, permitindo que o jogador controle os objetos na tela.
* No Pygame, os eventos são processados em uma fila, que pode ser acessada e manipulada em um loop de jogo.

```python
import pygame

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Movimentação do Retângulo')

# Define a cor do retângulo (vermelho)
rect_color = (255, 0, 0)
rect = pygame.Rect(100, 100, 50, 50)  # (x, y, largura, altura)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= 5  # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        rect.x += 5  # Move para a direita
    if keys[pygame.K_UP]:
        rect.y -= 5  # Move para cima
    if keys[pygame.K_DOWN]:
        rect.y += 5  # Move para baixo

    # Preenche a tela com branco
    screen.fill((255, 255, 255))
    # Desenha o retângulo na tela
    pygame.draw.rect(screen, rect_color, rect)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
```

* O que cada linha faz:

  - `pygame.event.get()`: Captura os eventos que ocorrem.
  - `pygame.key.get_pressed()`: Captura o estado das teclas.

Nesta seção, abordaremos a detecção de colisões entre dois objetos. A implementação se baseará no exemplo da V3.
O que é Colisão?

## 4. Colisão de Objetos

### 4.1 O que são colisões?

* Colisão refere-se ao momento em que dois ou mais objetos se encontram ou se sobrepõem em um espaço definido, como uma tela de jogo.
* No desenvolvimento de jogos, a detecção de colisão é crucial para a interação entre objetos, permitindo que ações específicas ocorram, como a destruição de um objeto, a pontuação, ou a alteração do estado do jogo.
* No Pygame, a colisão pode ser verificada utilizando métodos como `colliderect()`, que determina se dois retângulos se sobrepõem.


```python
import pygame

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Colisão de Objetos')

# Define as cores dos retângulos
rect_color_1 = (255, 0, 0)   # Vermelho
rect_color_2 = (0, 0, 255)   # Azul

# Cria dois retângulos
rect1 = pygame.Rect(100, 100, 50, 50)  # (x, y, largura, altura)
rect2 = pygame.Rect(300, 300, 50, 50)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= 5  # Move o retângulo vermelho para a esquerda
    if keys[pygame.K_RIGHT]:
        rect1.x += 5  # Move o retângulo vermelho para a direita
    if keys[pygame.K_UP]:
        rect1.y -= 5  # Move o retângulo vermelho para cima
    if keys[pygame.K_DOWN]:
        rect1.y += 5  # Move o retângulo vermelho para baixo

    # Preenche a tela com branco
    screen.fill((255, 255, 255))
    
    # Desenha os retângulos na tela
    pygame.draw.rect(screen, rect_color_1, rect1)
    pygame.draw.rect(screen, rect_color_2, rect2)

    # Verifica a colisão
    if rect1.colliderect(rect2):
        # Se houver colisão, transporta o rect1 para uma nova posição
        rect1.x = 100
        rect1.y = 100

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
```

* O que cada linha faz:
  - `pygame.Rect()`: Cria retângulos que serão usados para verificar colisões.
  - `rect1.colliderect(rect2)`: Verifica se os retângulos colidiram e imprime uma mensagem se a colisão for detectada.


## 5. Erros Comuns e Como Evitá-los

1. **Loop do Jogo Não Terminando**: Um erro comum é esquecer de verificar o evento `pygame.QUIT`, o que pode causar a falta de resposta da janela. Sempre inclua essa verificação para garantir que o jogo possa ser fechado corretamente.

2. **Retângulo Não Movendo**: Se o retângulo não se move, verifique se as teclas estão sendo corretamente capturadas. Utilize `pygame.key.get_pressed()` para garantir que você está verificando o estado atual das teclas.

3. **Colisões Não Detectadas**: Se as colisões não estão sendo detectadas, assegure-se de que as posições dos retângulos estão sendo atualizadas antes da verificação de colisão. Além disso, garanta que o método `colliderect()` esteja sendo utilizado corretamente.

4. **Problemas de Renderização**: Se os objetos não aparecem, verifique se a tela está sendo preenchida antes de desenhar os objetos. Não se esqueça de chamar `pygame.display.flip()` após fazer as atualizações para visualizar as mudanças.

5. **Desempenho do Jogo**: Se o jogo estiver lento ou travando, considere adicionar um controle de FPS (frames por segundo) usando `pygame.time.Clock()`, o que ajuda a limitar a taxa de quadros.

## 6. Exercícios Práticos

1. Lidar com o Fim da Tela:
    * Objetivo: Crie uma parede que impeça o retângulo de sair da tela. Quando o retângulo atinge a borda, deve ser transportado para o lado oposto da tela.
    * Dicas: Use as coordenadas do retângulo e compare com as dimensões da tela. Se rect.x < 0, mova rect.x para screen_width - rect.width.

2. Colisão e Transporte:
    * Objetivo: Quando houver uma colisão entre o retângulo e um segundo objeto, o retângulo deve ser transportado para uma nova posição, por exemplo, (50, 50).
    * Dicas: Utilize a mesma lógica de detecção de colisão usada na seção anterior, mas em vez de reposicionar apenas o primeiro retângulo, defina uma nova posição fixa.