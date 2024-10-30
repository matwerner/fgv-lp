# Pygame: Movimentação e Colisão

## 1. Eventos e Controle de Teclado

* No pygame, eventos são ações detectadas pelo sistema, como pressionar teclas ou mexer o mouse:
    - `pygame.event.get()` captura eventos discretos como um clique ou pressionamento de uma tecla. (**Obs**: Esse método armazena apenas os eventos ocorridos desde a sua última chamada)
    - Em contraste, `pygame.key.get_pressed()` é útil para verificar o estado contínuo de teclas, permitindo uma movimentação suave.

### Exemplo

#### Usando `pygame.event.get()`

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player.jump()  # Pulo ativado
```

#### Usando `pygame.key.get_pressed()`

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.rect.x -= 5
if keys[pygame.K_RIGHT]:
    player.rect.x += 5
```

## 2. Movimentação Avançada

### 2.1 Movimentação em Jogos Top-Down e 2D

* Em um jogo com visão 2D, temos dois tipos comuns de movimentação:
    1. Movimentação em um plano bidimensional sem gravidade (comumente usada em jogos top-down).
    2. Movimentação com gravidade, como em jogos de plataforma, onde o personagem pode pular e é atraído para o chão.

* Hoje, vamos focar na segunda opção, abordando o conceito de pulo com gravidade. Em uma movimentação desse tipo, o personagem deve:
    - Cair quando não está no chão.
    - Pular ao comando do jogador, mas sem poder pular novamente enquanto está no ar.

### 2.2 Implementando o Pulo com Controle de Estado

* Para garantir que o personagem só possa pular quando está tocando o chão, precisamos de uma variável de estado que sinalize se ele está no chão ou no ar. Dessa forma:
    - Se ele está no chão, o pulo pode ser ativado.
    - Se ele está no ar, o pulo está desativado até ele tocar o chão novamente.
* Além disso, precisaremos de dois atributos para controlar a velocidade no eixo y do personagem e a gravidade
    - Assim que detectamos a ação de pulo, atribuimos uma valor negativo (cima) para velocidade
    - Depois, com o tempo, essa velocidade  deve ir diminuindo devido a força da gravidade.
    - Eventualmente, esse valor se tornará positivo, o que fará o objeto descer.
    - Ao tocar um dos limites da tela, devemos zerar a velocidade como se a borda fosse o chão

#### Estrutura Modularizada com Classes

* Para essa implementação inicial, criaremos uma classe especifica para organizar o código relacionado ao jogador
* O `Player` vai controlar a posição, o movimento e o pulo do personagem.

#### Player

* Organização em Métodos: Vamos modularizar o código do personagem criando métodos para cada aspecto:
    - `update()` e `draw()` para atualizar e desenhar o personagem,
    - `on_event()` para lidar com eventos de salto
    - e `__on_out_of_bounds()` para tratar colisões com as bordas da tela.

```python
class Player:
    def __init__(self, x: int, y: int, width: int = 50, height: int = 50):
        self.rect = pygame.Rect(x, y, width, height)  # Define o retângulo do jogador
        self.vel_y = 0  # Velocidade vertical
        self.gravity = 0.5  # Força da gravidade
        self.is_jumping = False  # Estado de pulo

    def __jump(self):
        if not self.is_jumping:
            self.vel_y = -10  # Força do pulo
            self.is_jumping = True

    def __apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y  # Atualiza a posição do personagem

    def __on_out_of_bounds(self):
        if self.rect.right > SCREEN_WIDTH:  # Limite da borda direita
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:   # Limite da borda esquerda
            self.rect.left = 0
        if self.rect.top < 0:   # Limite da borda superior
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:   # Limite da borda inferior
            self.rect.bottom = SCREEN_HEIGHT
            self.is_jumping = False

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.__jump()

    def update(self):
        self.__apply_gravity()
        self.__on_out_of_bounds()
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Desenha o jogador
```

#### Game

```python
import pygame

# Inicialização do Pygame
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Instância dos objetos
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.on_event(event)

    # Atualização do estado do jogo
    player.update()

    # Renderização
    screen.fill((0, 0, 0))  # Limpa a tela
    player.draw(screen)
    pygame.display.flip()  # Atualiza a tela
    clock.tick(30)  # Controla a taxa de quadros por segundo

pygame.quit()
```

#### Explicação da Lógica

* Neste código, usamos métodos privados (`__jump` e `__apply_gravity`) para modularizar a lógica de movimento e manter o controle do estado de pulo e gravidade.
* `__on_out_of_bounds` limita a posição do personagem às bordas da tela.

### 2.3 Exercício Prático 

* Experimente ajustar a velocidade vertical (vel_y) e limite de borda, observando os efeitos.
* Altere o código de forma a permitir o jogador se mover lateralmente.


## 3. Colisão

### 3.1 O que é Colisão?

* A colisão é a interação entre objetos que se sobrepõem no jogo.
* Detectar essa sobreposição é essencial para criar interações, como pular sobre uma plataforma ou impedir que o personagem atravesse paredes.
* Para isso, utilizamos **bounding boxes** (caixas delimitadoras) ao redor dos objetos, que simplificam a detecção de colisão.

### 3.2 Usando Rect para Detecção de Colisões

* O Pygame oferece o tipo `Rect`, uma estrutura retangular que já possui métodos embutidos para detectar colisão. Por exemplo, `colliderect` é um método disponível para verificar se dois retângulos (Rect) se sobrepõem.
* Exemplo: Quando um jogador se aproxima de um obstáculo representado por um `Rect`, podemos usar `colliderect` para verificar se houve uma colisão e reagir de acordo, como reposicionar o jogador ou bloquear seu movimento.

#### Implementando a Detecção de Colisão

* Vamos adicionar um obstáculo ao nosso jogo e implementar a colisão entre o jogador e um obstáculo retangular.

#### Obstacle

```python
class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  # Define a posição e o tamanho do obstáculo

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Desenha o obstáculo
```

#### Atualizar Player

```python
class Player
    ...

    def on_collision(self, other):
        if not self.rect.colliderect(other.rect):
            return

        if isinstance(other, Obstacle):
            if self.vel_y > 0:
                self.rect.bottom = other.rect.top  # Ajusta o personagem para ficar sobre o chão
                self.is_jumping = False  # Permite pular novamente ao tocar o chão
                self.vel_y = 0  # Zera a velocidade vertical
```

#### Atualizar Game

```python
# Inicialização do Pygame
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Instância dos objetos
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
obstacle = Obstacle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.on_event(event)

    # Atualização do estado do jogo
    player.update()
    obstacle.update()

    # Colisão
    if player.rect.colliderect(obstacle.rect):
        player.on_collision(obstacle)

    # Renderização
    screen.fill((0, 0, 0))  # Limpa a tela
    player.draw(screen)
    obstacle.draw(screen)
    pygame.display.flip()  # Atualiza a tela
    clock.tick(30)  # Controla a taxa de quadros por segundo

pygame.quit()
```

### 3.3 Tratando Outros Tipos de Objetos (Introdução)

* Em alguns jogos, nem todos os objetos são facilmente representados por retângulos. Objetos circulares, por exemplo, exigem outra abordagem.
* Para detectar colisões com objetos circulares, o Pygame oferece o método collide_circle, que utiliza as coordenadas e os raios de dois círculos para determinar a colisão.

#### Observação

* Embora retângulos sejam rápidos e eficientes, tipos de colisão mais complexos entre diferentes formas (como retângulos e círculos) podem exigir abordagens personalizadas.
* Por exemplo, para colisões entre um retângulo e um círculo, é necessário comparar a posição e as dimensões relativas de ambos os objetos.

## 4. Exercícios Práticos

1. Colisões Laterais e Superiores
    * Objetivo: Expanda a função de colisão para incluir:
        - **Colisão Lateral**: O jogador não deve atravessar o obstáculo pelas laterais (direita e esquerda).
        - **Colisão Superior**: Se o jogador colidir com a parte inferior de um obstáculo, ele deve ser reposicionado abaixo do obstáculo e parar o movimento vertical.
    * Dicas:
        - Compare a posição do jogador com a do obstáculo nos eixos X e Y para identificar a direção da colisão.
        - Nas colisões laterais, reposicione o jogador à direita ou à esquerda do obstáculo.
        - Para a colisão superior, posicione o jogador abaixo do obstáculo e anule o movimento vertical.

2. Novo Tipo de Obstáculo: ObstacleBounce
    * Objetivo: Crie um novo tipo de obstáculo chamado ObstacleBounce.
        - Ao colidir com a parte superior desse obstáculo, o jogador deve receber um impulso vertical (como um salto).
        - Defina um valor de impulso para aumentar a altura do salto ao colidir com esse obstáculo.
    * Dicas:
        - Verifique se o jogador está colidindo pela parte inferior do ObstacleBounce e aplique um valor de impulso no eixo Y.
        - Diferencie o comportamento entre esse obstáculo e os demais para tornar o salto exclusivo do ObstacleBounce.