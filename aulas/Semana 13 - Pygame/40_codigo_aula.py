import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ScoreManager:

    def __init__(self, x, y, initil_score=0):
        self.x = x
        self.y = y
        self.score = initil_score

        self.font = pygame.font.Font(None, 36)
        self.score_msg = "Pontuação: {:,}"
    
    def draw(self, screen):
        msg = self.score_msg.format(self.score)
        text_box = self.font.render(msg, True, "grey")
        screen.blit(text_box, (self.x, self.y))
    
    def increment(self, points=1):
        self.score += points

class Button:

    def __init__(self, x, y, width, height, text, callback, fontsize=36):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, fontsize)
        self.callback = callback

        self.color_default = "white"
        self.color_hover = "red"
        self.color_current = self.color_default
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color_current, self.rect)
        text_box = self.font.render(self.text, True, "black")
        text_box_rect = text_box.get_rect(center=self.rect.center) 
        screen.blit(text_box, text_box_rect)
    
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            has_collided = self.rect.collidepoint(event.pos)
            if has_collided and event.button == 1:
                self.callback()

        if event.type == pygame.MOUSEMOTION:
            has_collided = self.rect.collidepoint(event.pos)
            if has_collided:
                self.color_current = self.color_hover
            else:
                self.color_current = self.color_default

class MainMenu:

    def __init__(self, manager):
        self.manager = manager
        self.start_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 50, "Start", self.start_callback)
        self.exit_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 200, 50, "exit", self.exit_callback)
    
    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.start_button.draw(screen)
        self.exit_button.draw(screen)
        pygame.display.flip()
    
    def on_event(self, event):
        self.start_button.on_event(event)
        self.exit_button.on_event(event)

    def start_callback(self):
        self.manager.change_state("game_level")
    
    def exit_callback(self):
        self.manager.is_running = False

class GameLevel:

    def __init__(self, manager):
        pass

    def draw(self, screen):
        screen.fill((255, 0, 0))
        pygame.display.update()
    
    def on_event(self, event):
        pass

class GameManager:

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.states = {
            "main_menu": MainMenu(self),
            "game_level": GameLevel(self)
        }
        self.current_state = self.states["main_menu"]
        self.is_running = False

    def change_state(self, state_name):
        self.current_state = self.states[state_name]

    def run(self):        
        self.is_running = True
        while self.is_running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                self.current_state.on_event(event)

            self.current_state.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = GameManager()
    game.run()
