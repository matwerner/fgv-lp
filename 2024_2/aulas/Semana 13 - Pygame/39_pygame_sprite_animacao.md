# Pygame: Sprites e Animações

## 1. O que é um Sprite?

* Um sprite é uma imagem 2D que representa qualquer elemento visual do jogo.
* Em Pygame, usamos a classe `pygame.sprite.Sprite` para criar objetos que se movem, colidem e interagem entre si.
* A vantagem de usar sprites com orientação a objetos é que podemos encapsular comportamentos como movimentos, animações e colisões dentro de uma classe, mantendo o código organizado e reutilizável.


## 2. Criando um Sprite com Orientação a Objetos

* Para criar um sprite básico, precisamos criar uma classe que herda de `pygame.sprite.Sprite`.Nesta classe, precisamos definir dois atributos principais:
    - **Imagem** (`self.image`): a imagem do sprite.
    - **Retângulo de colisão** (`self.rect`): define a área retangular do sprite, usada para controlar sua posição e detectar colisões.

### Atributos e Métodos a Ficar de Olho

* Ao criar sprites, existem alguns atributos e métodos que devemos ter em mente:
    * Atributos:
        - `self.image`: A imagem do sprite. Você pode precisar redimensioná-la usando `pygame.transform.scale()` para garantir que ela tenha o tamanho desejado no jogo.
        - `self.rect`: Um retângulo que representa a posição e o tamanho do sprite na tela. O retângulo é usado para calcular colisões e para desenhar o sprite na tela.

    * Métodos:
        - `update()`: Método que você deve sobrescrever para definir a lógica de atualização do sprite, como movimento e animações. Esse método é chamado a cada frame do jogo, o que permite atualizar a posição ou a aparência do sprite.
        - `draw(surface)`: Enquanto o método de desenho é feito pelo grupo de sprites, você também pode chamar `self.image` para desenhar o sprite individualmente em uma superfície.

### Redimensionando Imagens

* Em muitos casos, as imagens que usamos podem ser maiores do que o desejado para o sprite.
* Para garantir que os sprites se encaixem corretamente no jogo e tenham o tamanho desejado, podemos redimensionar a imagem usando `pygame.transform.scale()`.
* Por exemplo, se quisermos que o sprite tenha `32x32` pixels, podemos fazer isso ao carregar a imagem:

### Questão da Transparência

* Um aspecto importante ao trabalhar com imagens de sprites é a transparência.
* Imagens no formato PNG suportam canais de transparência, permitindo que partes da imagem sejam transparentes e o fundo do jogo fique visível através delas.
* Para garantir que a transparência funcione corretamente em Pygame, é importante que as imagens sejam salvas em formato PNG e que o Pygame as carregue corretamente.
* Quando você carrega uma imagem PNG, a transparência é automaticamente reconhecida, e o Pygame usará essa informação ao renderizar a imagem na tela.
* Isso é especialmente útil para sprites que possuem formas irregulares, como personagens ou objetos.

### Exemplo

```python
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        # Carrega a imagem do jogador e redimensiona para 32x32 pixels
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (32, 32))
        
        # Define o retângulo de colisão e posição inicial do sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Controle de movimentação simples usando teclas direcionais
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def draw(self, screen):
        # Desenha o sprite na tela
        screen.blit(self.image, self.rect)
```

* Explicação
    - ` __init__`: O método inicializa o sprite, carrega a imagem e redimensiona-a para um tamanho específico (32x32 pixels). Também define o self.rect, que é o retângulo de colisão usado para posicionamento e detecção de colisões.
    - `update()`: Esse método é chamado para atualizar o estado do sprite em cada frame. Aqui, ele verifica as teclas pressionadas e ajusta a posição (self.rect.x e self.rect.y) de acordo.
    - `draw(screen)`: Este método exibe o sprite na tela. Usamos o blit() de Pygame, que desenha self.image na posição definida por self.rect.


## 3. Utilizando Grupos de Sprites

* À medida que o número de sprites aumenta, fica difícil gerenciar cada sprite individualmente.
* Em vez disso, Pygame permite agrupar sprites usando `pygame.sprite.Group`.
* Esse grupo facilita a atualização e renderização dos sprites ao mesmo tempo.

### Por que Grupos de Sprites são Úteis?

* Embora herdar de `pygame.sprite.Sprite` forneça a base para criar sprites, o verdadeiro valor surge quando utilizamos esses sprites em conjunto com `pygame.sprite.Group`.
* O grupo permite que Pygame utilize os atributos `image` e `rect` de cada sprite para gerenciar suas exibições e detecções de colisões automaticamente:
    - `image` é usado pelo Group para desenhar a imagem do sprite na tela.
    - `rect` é usado para controlar a posição e a detecção de colisões entre sprites.
    - `update()` é chamado automaticamente para atualizar o estado dos sprites sem precisar de chamadas individuais.

    **Nota**: Usar o método `draw()` diretamente em sprites individuais se torna desnecessário, pois `pygame.sprite.Group.draw()` desenha todos os sprites no grupo de uma só vez.

### Criando e Utilizando um Grupo de Sprites

```python
all_sprites = pygame.sprite.Group()
player = Player("player_image.png", 100, 100)
all_sprites.add(player)
```

* Explicação:
    - Criar o grupo `pygame.sprite.Group()`: cria um grupo que pode conter múltiplos sprites, permitindo o gerenciamento centralizado.
    - Adicionar ao Grupo: Usamos `add()` para inserir o sprite player no grupo `all_sprites`.

### Atualizando e Desenhando Sprites com `Group`

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza todos os sprites do grupo
    all_sprites.update()

    # Limpa a tela, desenha todos os sprites e atualiza a tela
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
```

* Explicação:
    - **Atualização com `update()`**: `all_sprites.update()` chama automaticamente o método `update()` de cada sprite no grupo. Isso permite que cada sprite ajuste sua posição ou estado, como movimentação, animação, etc.
    - **Desenho com `draw()`**: `all_sprites.draw(screen)` exibe todos os sprites no grupo de uma vez, utilizando a posição definida pelo rect de cada sprite. Isso elimina a necessidade de chamarmos o `draw()` individualmente para cada sprite.

## 4. Detectando Colisões entre Sprites

* Em jogos, é comum que sprites interajam ao se sobrepor, como quando um personagem coleta um item ou colide com um obstáculo.
* Pygame facilita a detecção de colisões entre sprites por meio de funções integradas que usam o retângulo de colisão (`rect`) dos sprites.

### Principais Funções para Detecção de Colisões

* Pygame oferece algumas funções úteis para verificar colisões entre sprites, usando o rect para detectar sobreposições automaticamente:

    1. `pygame.sprite.spritecollide()`: Verifica colisões entre um único sprite e todos os sprites de um grupo.
        - Sintaxe: pygame.sprite.spritecollide(sprite, group, dokill)
        - Uso Comum: Ideal para detectar se um personagem toca em objetos colecionáveis, como moedas. Se dokill=True, os sprites do grupo que colidirem serão removidos automaticamente.

    2. `pygame.sprite.groupcollide()`: Verifica colisões entre dois grupos de sprites, retornando um dicionário das colisões.
        - Sintaxe: pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
        - Uso Comum: Útil para detectar colisões entre o jogador e inimigos, ou entre projéteis e alvos. dokill1 e dokill2 removem automaticamente sprites dos grupos se houver colisão.

    3. `pygame.sprite.collide_rect()`: Verifica colisão entre dois sprites usando seus rect.
        - Uso Comum: Para verificar colisões entre dois sprites específicos, sem grupos.


### Exemplo

```python
import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Grupos de sprites
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Criando o jogador e algumas moedas
player = Player("player_image.png", 100, 100)
all_sprites.add(player)

for i in range(5):  # Criamos 5 moedas em posições aleatórias
    coin = Coin("coin_image.png", i * 80 + 100, 200)
    all_sprites.add(coin)
    coins.add(coin)

# No loop principal do jogo
while running:
    # Atualiza todos os sprites
    all_sprites.update()

    # Detecta colisões entre o jogador e moedas
    coins_collected = pygame.sprite.spritecollide(player, coins, dokill=True)
    if coins_collected:
        print(f"Moedas coletadas: {len(coins_collected)}")

    # Limpa e desenha os sprites na tela
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
```

* Explicação
    - **Criação de Sprites**: O jogador e as moedas são criados como sprites individuais e adicionados aos grupos `all_sprites` e coins.
    - **Detecção de Colisão**: Usamos `pygame.sprite.spritecollide(player, coins, dokill=True)` para verificar se o jogador colide com qualquer moeda no grupo coins. Se `dokill=True`, as moedas que colidirem com o jogador serão removidas automaticamente do grupo.
    - **Feedback**: Quando o jogador coleta uma moeda, o programa imprime o número de moedas coletadas.

## 5. Criando uma Animação Simples de Sprite

* A animação em jogos consiste em um conjunto de imagens que, mostradas em sequência rápida, criam a ilusão de movimento, como em um personagem andando ou atacando.
* Em Pygame, podemos configurar uma sequência de imagens para alternar rapidamente, criando essa sensação de fluidez visual.

### Frequência de Atualização da Animação

* Para manter o jogo fluido, precisamos controlar a frequência com que as imagens da animação são trocadas.
* Essa taxa pode ser independente da taxa de atualização do jogo, para que os movimentos do personagem e a animação se mantenham naturais, mesmo em situações com muitos sprites ou efeitos na tela.
* **FPS vs. Frequência de Animação**: A taxa de quadros do jogo (FPS) define quantas vezes o jogo é atualizado por segundo, enquanto a frequência da animação controla a velocidade com que as imagens mudam. Por exemplo, para animar um personagem, você pode definir que ele alterne imagens a cada dois quadros do jogo.

### Exemplo

```python
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super().__init__()
        self.frames = [pygame.image.load(img) for img in images]  # Carrega cada imagem da lista
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.animation_speed = 15  # Altera a cada 5 quadros do jogo
        self.frame_count = 0

    def update(self):
        # Controla a frequência da animação
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

# No loop principal
all_sprites = pygame.sprite.Group()
player_images = [
    "./sprites/link/down_idle/link_down_idle_0.png",
    "./sprites/link/down_idle/link_down_idle_1.png",
    "./sprites/link/down_idle/link_down_idle_2.png",
]
player = Player(player_images, 100, 100)
all_sprites.add(player)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)
```

* Explicação
    - **Lista de Imagens**: A animação é composta por várias imagens (`player_walk1.png`, `player_walk2.png`, etc.), carregadas individualmente. Cada uma corresponde a um quadro específico da animação.
    - **Controle da Animação**: `animation_speed` define a frequência com que o quadro muda. Neste exemplo, a cada cinco quadros do jogo, `update()` alterna para a próxima imagem na lista.
    - **Alternância de Frames**: `self.current_frame` avança na lista de imagens e é redefinido para zero ao chegar ao final, criando um loop contínuo de animação.

### Spritesheets

* Para otimizar o uso de imagens no jogo, é comum usar um spritesheet, que é uma imagem única que contém vários quadros de animação organizados em uma grade. Por exemplo, um spritesheet para um personagem pode conter:
    - **Frames de Movimento**: Cada posição de um movimento, como andar, correr ou pular, está em uma área específica do spritesheet.
    - **Outros Elementos**: Em alguns casos, o mesmo spritesheet contém outros objetos do jogo, como efeitos ou itens, facilitando o carregamento de vários recursos ao mesmo tempo.
* Usar spritesheets ajuda a reduzir o número de arquivos carregados e é mais eficiente em termos de memória e desempenho. Com um spritesheet, podemos “recortar” partes específicas para cada quadro da animação.


## 6. Execícios

1. Animação Básica com Lista de Imagens: Implemente uma animação para o personagem enquanto ele se movimenta, usando uma lista de imagens que representam diferentes quadros da animação.
    - Tarefa: Crie uma lista de imagens e alterne entre elas no método update para dar a ilusão de movimento enquanto o personagem anda.
    - Dica: Ajuste a velocidade de troca de frames para uma animação mais suave.

2. Animação Direcional Baseada no Movimento: Crie animações específicas para cada direção do movimento do personagem (para cima, baixo, esquerda e direita).
    - Tarefa: Configure uma lista de imagens para cada direção e alterne entre elas conforme o personagem se movimenta para diferentes direções.
    - Dica: Use pygame.key.get_pressed() para verificar a direção e selecione a animação correspondente.

3. Colisão com Obstáculo: Implemente um sprite de obstáculo e faça com que o personagem pare ao colidir com ele.
    - Tarefa: Crie um grupo de sprites contendo o personagem e o obstáculo. Use pygame.sprite.spritecollide() para detectar a colisão e impedir o personagem de atravessar o obstáculo.
    - Dica: Modifique a posição do personagem para evitar que ele ultrapasse o limite do obstáculo ao colidir.