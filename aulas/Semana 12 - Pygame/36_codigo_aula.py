import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)
screen.fill((0, 0, 0))

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

        # TODO: Usar colisao entre objetos
        if self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
            self.speed_y = 0
            self.jump_count = 0

    def on_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump()
    
    def jump(self):
        if self.jump_count >= self.jump_count_max:
            return
        self.speed_y = -40
        self.jump_count += 1

    def on_key_pressed(self, key_map):
        if key_map[pygame.K_RIGHT] or key_map[pygame.K_w]:
            self.rect.x += 10
        if key_map[pygame.K_LEFT]:
            self.rect.x -= 10

class Ground:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        pass

player = Player(WIDTH // 2, HEIGHT // 2, 50, 50)
ground = Ground(0, HEIGHT - 30, WIDTH, 60)

clock = pygame.time.Clock()

is_running = True
while is_running:
    # Eventos
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

        player.on_event(event)

    key_map = pygame.key.get_pressed()
    player.on_key_pressed(key_map)

    # Logica
    player.update()
    ground.update()

    has_collided = player.rect.colliderect(ground.rect)
    print(has_collided)

    # Renderizaçao
    screen.fill((0, 0, 0))
    player.draw(screen)
    ground.draw(screen)
    pygame.display.flip()

    clock.tick(30)
    
pygame.quit()
