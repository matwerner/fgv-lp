import pygame

class Player:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.gravity_y = 2 # pixels^2 / frame
        self.speed_y = 0
        self.jump_count = 0
        self.jump_count_max = 2
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.speed_y += self.gravity_y
        self.rect.y += self.speed_y

    def on_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self._jump()
    
    def _jump(self):
        if self.jump_count >= self.jump_count_max:
            return
        self.speed_y = -40
        self.jump_count += 1

    def on_key_pressed(self, key_map):
        if key_map[pygame.K_RIGHT] or key_map[pygame.K_w]:
            self.rect.x += 10
        elif key_map[pygame.K_LEFT]:
            self.rect.x -= 10
    
    def on_collision(self, other):
        # TODO: Comportamento precisa ser diferente dependendo lado da colisão
        if isinstance(other, Ground):
            ground_y = other.rect.top
            self.rect.bottom = ground_y
            self.speed_y = 0
            self.jump_count = 0

class Ground:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        pass

    def on_collision(self, other):
        pass

class GameManager:

    def __init__(self) -> None:
        pygame.init()

        # A tela
        self.width = 800
        self.height = 600
        screen_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill((0, 0, 0))

        # Objetos
        self.player = Player(self.width // 2, self.height // 2, 50, 50)
        self.grounds = [
            Ground(0, self.height - 30, self.width, 60),
            Ground(self.width // 2, self.height - 200, 100, 20),
            Ground(300, self.height - 90, 50, 50)
        ]

        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        while self.is_running:            
            self.event()
            self.update()
            self.draw()
            self.clock.tick(30)
        pygame.quit()

    def event(self):
        # Eventos
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            self.player.on_event(event)

        # Chaves pressionadas no momento
        key_map = pygame.key.get_pressed()
        self.player.on_key_pressed(key_map)

    def update(self):
        self.player.update()
        for ground in self.grounds:
            ground.update()
        self.collision_detection()

    def collision_detection(self):
        # Verificar colisao
        for ground in self.grounds:
            has_collided = self.player.rect.colliderect(ground.rect)
            if has_collided:
                self.player.on_collision(ground)
                ground.on_collision(self.player)

    def draw(self):
        # Renderizaçao
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for ground in self.grounds:
            ground.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    game = GameManager()
    game.run()
