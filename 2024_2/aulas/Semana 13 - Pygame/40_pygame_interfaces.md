# Pygame: Interface básica

* A ídeia dessa aula é explorar os recursos básicos para construir interfaces no Pygame, como exibir texto, criar botões e desenvolver um menu inicial.
* Esses elementos serão úteis para tornar o jogo interativo e visualmente agradável para os jogadores.

## 1. Exibindo Texto na Tela

* Antes de adicionar botões e menus, precisamos entender como mostrar texto na tela.
* Isso envolve carregar uma fonte, renderizar o texto e exibi-lo na posição desejada.

### Passos para exibir texto

1. **Importando e iniciando fontes**:
    ```python
    import pygame
    pygame.init()
    ```

2. **Carregando a fonte**: Escolha uma fonte e um tamanho. Pygame tem fontes padrão, mas também é possível carregar fontes personalizadas.
    ```python
    font = pygame.font.Font(None, 36)  # None usa a fonte padrão, 36 é o tamanho
    ```

3. **Renderizando o texto**: Renderize o texto criando uma superfície, onde você define a cor do texto e a cor de fundo.
    ```python
    text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))  # Branco
    ```

4. **Posicionando e desenhando o texto na tela**: Escolha uma posição e use blit para desenhar o texto.
    ```python
    screen = pygame.display.set_mode((800, 600))
    screen.blit(text_surface, (100, 100))
    ```

5. **Atualizando a tela**: Não esqueça de chamar `pygame.display.flip()` ou `pygame.display.update()` para que o texto apareça.

## 2. Criando Botões

* Agora que sabemos como exibir texto, vamos criar botões interativos.
* Um botão no Pygame é basicamente uma área retangular onde detectamos cliques e respondemos a eles.

### Passos para criar um botão

1. **Desenhando o retângulo do botão**: Crie um retângulo e desenhe-o na tela. A cor e a posição podem ser personalizadas.
    ```python
    button_color = (0, 128, 255)
    button_rect = pygame.Rect(300, 250, 200, 50)  # Posição e tamanho do botão
    pygame.draw.rect(screen, button_color, button_rect)
    ```

2. **Adicionando texto ao botão**: Use a mesma técnica para exibir texto no retângulo.
    ```python
    button_text = font.render("Start", True, (255, 255, 255))  # Texto branco
    screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))
    ```

3. **Detecção de clique no botão**: Para saber se o botão foi clicado, use o evento pygame.MOUSEBUTTONDOWN.
    ```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Verifica clique dentro do botão
                print("Botão Start clicado!")
    ```
4. **Convertendo para uma classe**:
    ```python
    class Button:
        def __init__(self, x, y, width, height, text, color, text_color=(255, 255, 255)):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.color = color
            self.text_color = text_color
            self.font = pygame.font.Font(None, 36)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            button_text = self.font.render(self.text, True, self.text_color)
            button_text_rect = button_text.get_rect(center=self.rect.center) # Centrizar o texto dentro do botão
            screen.blit(button_text, button_text_rect)

        def update(self):
            pass

        def on_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):  # Verifica clique dentro do botão
                    print(f"Botão '{self.text}' clicado!")
    ```

## 3. Criando um Menu com "Start" e "Exit"

* Vamos construir um menu inicial que aparece ao abrir o jogo. Ele terá apenas dois botões: `"Start"` e `"Exit"`.

1. **Organização básica do menu**: Começaremos criando duas classes: `MainMenu` para exibir o menu e `GameManager` para iniciar o jogo quando o botão Start for pressionado.

2. **Função de menu**: Na classe `MainMenu`, desenhe o plano de fundo, os botões de `Start` e `Exit` e aguarde o clique do usuário para determinar o que fazer.
    ```python
    class MainMenu():
        def __init__(self):
            self.start_button = Button(300, 250, 200, 50, "Start", (0, 128, 0))
            self.exit_button = Button(300, 350, 200, 50, "Exit", (255, 0, 0))
        
        def draw(self, screen):
            screen.fill((0, 0, 0))  # Fundo preto
            self.start_button.draw(screen)
            self.exit_button.draw(screen)
            pygame.display.flip()
        
        def update(self):
            self.start_button.update()
            self.exit_button.update()

        def on_event(self, event):
            self.start_button.on_event(event)
            self.exit_button.on_event(event)
    ```
    

3. **Classe principal do jogo** (GameManager): Esta classe contém a lógica do jogo. Após o jogador clicar em `"Start"` no menu, o jogo inicia.
    ```python
    class GameManager:
        def __init__(self):
            self.screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Jogo com Menu e Nível")

            self.main_menu = MainMenu()

            self.is_running = False
            self.clock = None

        def run(self):
            self.is_running = True
            self.clock = pygame.time.Clock()
            while self.is_running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.is_running = False
                    self.main_menu.on_event(event)
                
                self.main_menu.update()

                self.main_menu.draw(self.screen)
                self.clock.tick(30)
            pygame.quit()
    ```

## 4. Adicionando Callbacks aos Botões e Menu

* Para tornar o menu interativo, precisamos associar ações específicas aos botões, como iniciar o jogo ou fechar a aplicação.
* Para isso, utilizaremos uma técnica chamada `callback` — uma função que será chamada em resposta a um evento.

### 4.1 O que é um Callback?

* Um callback é uma função que você passa como argumento para outra função ou classe.
* Essa função é `"chamada de volta"` quando ocorre um evento específico.
* No caso dos nossos botões, queremos que cada botão tenha um comportamento diferente ao ser pressionado.
* Em vez de codificar diretamente no botão o que ele deve fazer, passamos uma função que será executada quando ele for clicado.
* Isso torna o botão mais flexível e independente de uma lógica específica.
* No caso do menu, o botão `"Start"` inicia o jogo, enquanto o botão `"Exit"` fecha o programa. Podemos passar essas funções como callbacks para cada botão.

#### Implementando Callbacks nos Botões

* Primeiro, vamos modificar a classe Button para aceitar um callback no momento da criação:
    ```python
    class Button:
        def __init__(self, x, y, width, height, text, callback, color, text_color=(255, 255, 255)):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.color = color
            self.text_color = text_color
            self.font = pygame.font.Font(None, 36)
            self.callback = callback

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            button_text = self.font.render(self.text, True, self.text_color)
            button_text_rect = button_text.get_rect(center=self.rect.center) # Centrizar o texto dentro do botão
            screen.blit(button_text, button_text_rect)

        def update(self):
            pass

        def on_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):  # Verifica clique dentro do botão
                    self.callback()  # Chama a função passada como callback
    ```
* Com isso, podemos passar qualquer função para `Button`, e ela será executada ao clicar no botão.

### 4.2 Introduzindo o State Pattern

* Agora que nossos botões podem executar callbacks, podemos organizar melhor o fluxo do jogo usando o `State Pattern`.
* Esse padrão nos ajuda a separar os estados do jogo em classes distintas (como `MainMenu`, `GameLevel`, etc.), permitindo que o jogo mude de comportamento ao trocar entre essas classes.

#### Criando a Estrutura do State Pattern

* Vamos criar uma estrutura que facilita a troca entre estados como `MainMenu` e `GameLevel`. Usaremos o `GameManager` para gerenciar esses estados.
    * `GameState`: uma interface de base que define métodos para todos os estados do jogo.
    * `MainMenu` e `GameLevel`: classes que representam o menu inicial e o nível do jogo, respectivamente.

##### Classe `GameState`

* A classe `GameState` será a base para todos os estados. Cada estado específico (como `MainMenu` e `GameLevel`) será responsável por implementar esses métodos.
    ```python
    class GameState:
        def __init__(self, manager):
            self.manager = manager

        def on_event(self, event):
            pass

        def update(self):
            pass

        def draw(self, screen):
            pass
    ```

##### Classe `GameLevel`

* A `GameLevel` representa um estado simples do jogo. Quando o jogo começa, ele apenas pinta a tela para indicar que mudou de estado.

    ```python
    class GameLevel(GameState):
        def __init__(self, manager):
            super().__init__(manager)

        def draw(self, screen):
            screen.fill((0, 0, 128))  # Fundo azul para representar o jogo
            pygame.display.flip()
    ```

##### Classe `MainMenu`

* A classe `MainMenu` representa o estado do menu inicial do jogo, onde o jogador escolhe entre "Start" e "Exit".

    ```python
    class MainMenu(GameState):
        def __init__(self, manager):
            super().__init__(manager)
            self.start_button = Button(300, 250, 200, 50, "Start", self.start_game, (0, 128, 0))
            self.exit_button = Button(300, 350, 200, 50, "Exit", self.exit_game, (255, 0, 0))

        def start_game(self):
            self.manager.change_state("game_level")

        def exit_game(self):
            self.manager.is_running = False

        def draw(self, screen):
            screen.fill((0, 0, 0))  # Fundo preto
            self.start_button.draw(screen)
            self.exit_button.draw(screen)
            pygame.display.flip()
        
        def update(self):
            self.start_button.update()
            self.exit_button.update()

        def on_event(self, event):
            self.start_button.on_event(event)
            self.exit_button.on_event(event)
    ```

* Aqui, `start_game` e `exit_game` são as callbacks que definem o comportamento dos botões.
* Com o `State Pattern`, a `MainMenu` só precisa notificar o `GameManager` para que ele altere o estado do jogo.

##### Controlando o Estado com `GameManager`

* A classe `GameManager` coordena os estados do jogo.
* Ela mantém uma referência ao estado atual (current_state) e fornece um método `change_state` para mudar o estado quando necessário.

    ```python
    class GameManager:
        def __init__(self):
            self.screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Jogo com Menu e Nível")

            self.screen_map = {
                "main_menu": MainMenu(self),
                "game_level": GameLevel(self)
            }
            self.current_screen = self.screen_map["main_menu"]

            self.is_running = False
            self.clock = None

        def change_state(self, screen_name):
            self.current_screen = self.screen_map[screen_name]

        def run(self):
            self.is_running = True
            self.clock = pygame.time.Clock()
            while self.is_running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.is_running = False
                    self.current_screen.on_event(event)
                
                self.current_screen.update()

                self.current_screen.draw(self.screen)
                self.clock.tick(30)
            pygame.quit()
    ```

* Agora, `GameManager` controla o estado do jogo sem precisar conhecer detalhes de cada estado específico.
* Quando o botão `"Start"` é clicado, `MainMenu` simplesmente chama `self.manager.change_state("game_level")`, e o `GameManager` troca para o estado de jogo.