import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image_paths):
        # image_animation_right: List[str]
        # image_animation_left: List[str]
        # image_animation_up: List[str]
        # image_animation_down: List[str]
        # image_animation_idle: List[str]
        super().__init__()

        #
        self.idle_animation = []
        for image_path in image_paths:
            sprite = pygame.image.load(image_path)
            # sprite = pygame.transform.scale(sprite, (width, height))
            self.idle_animation.append(sprite)
        self.current_frame_index = 0
        self.image = self.idle_animation[self.current_frame_index]

        self.frames_per_sprite = 5
        self.frame_index = 0

        self.rect = self.image.get_rect()        
        self.rect.x = x
        self.rect.y = y

        self.color = (255, 0, 0)
        self.gravity_y = 2 # pixels^2 / frame
        self.speed_y = 0
        self.jump_count = 0
        self.jump_count_max = 2
    
    def draw(self, screen):
        self.frame_index += 1
        if self.frame_index >= self.frames_per_sprite:
            self.frame_index = 0
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.idle_animation):
                self.current_frame_index = 0
        self.image = self.idle_animation[self.current_frame_index]
        screen.blit(self.image, self.rect)

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

class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = (0, 255, 0)

    # def draw(self, screen):
    #     pygame.draw.rect(screen, self.color, self.rect)
    
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
        sprite_paths = [
            "./sprites/link/down_idle/link_down_idle_0.png",
            "./sprites/link/down_idle/link_down_idle_1.png",
            "./sprites/link/down_idle/link_down_idle_2.png"
        ]

        self.player = Player(self.width // 2, self.height // 2, 50, 75, sprite_paths)

        sprite_path = "./sprites/powerup.png"
        self.ground_group = pygame.sprite.Group()
        self.ground_group.add(Ground(0, self.height - 30, self.width, 60, sprite_path))
        self.ground_group.add(Ground(self.width // 2, self.height - 200, 100, 20, sprite_path))
        self.ground_group.add(Ground(300, self.height - 90, 50, 50, sprite_path))

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
        self.ground_group.update()
        self.collision_detection()

    def collision_detection(self):
        # Verificar colisao
        for ground in self.ground_group:
            has_collided = self.player.rect.colliderect(ground.rect)
            if has_collided:
                self.player.on_collision(ground)
                ground.on_collision(self.player)

    def draw(self):
        # Renderizaçao
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        self.ground_group.update()
        self.ground_group.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    game = GameManager()
    game.run()