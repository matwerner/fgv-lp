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

class Ball:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0, 0, 255)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


player = Player(WIDTH // 2, HEIGHT // 2, 50, 50)
ground = Ground(0, HEIGHT - 30, WIDTH, 60)
ball = Ball(WIDTH // 2, HEIGHT // 2, 20)


def collision_between_rects(rect1, rect2):
    return rect1.colliderect(rect2)

def collision_between_circles(circle1, circle2):
    distance_x = circle1.rect.x - circle2.rect.x
    distance_y = circle1.rect.y - circle2.rect.y
    distance_squared = (distance_x ** 2) + (distance_y ** 2)
    return distance_squared < ((circle1.rect.width + circle2.rect.width) ** 2)

def collision_between_circle_and_rect(circle, rect):
    # Find the closest point to the circle within the rectangle
    closest_x = max(rect.left, min(circle.rect.x, rect.right))
    closest_y = max(rect.top, min(circle.rect.y, rect.bottom))

    # Calculate the distance between the circle's center and this closest point
    distance_x = circle.rect.x - closest_x
    distance_y = circle.rect.y - closest_y

    # If the distance is less than the circle's radius, an intersection occurs
    distance_squared = (distance_x ** 2) + (distance_y ** 2)
    return distance_squared < (circle.rect.width ** 2)

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
    ball.draw(screen)
    pygame.display.flip()

    clock.tick(30)
    
pygame.quit()
