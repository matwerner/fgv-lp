import pygame
import utils

class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, radius, image_path, vel_x, vel_y):
        super().__init__()
        self.rect = pygame.Rect(x, y, radius, radius)
        self.image = utils.load_image(image_path, (radius, radius))
        self.vel_x = vel_x
        self.vel_y = vel_y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def on_collision(self, other):
        pass

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))

    def on_collision(self, other):
        pass

class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, normal_image_path, cracked_image_path):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.normal_image = utils.load_image(normal_image_path, (width, height))
        self.cracked_image = utils.load_image(cracked_image_path, (width, height))
        self.image = self.normal_image

        self.points = 10
        self.is_cracked = False
        self.__normal_image_path = normal_image_path
        self.__cracked_image_path = cracked_image_path

    def copy(self):
        return Brick(self.rect.x,
                     self.rect.y,
                     self.rect.width,
                     self.rect.height,
                     self.__normal_image_path,
                     self.__cracked_image_path)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def on_collision(self, other):
        pass

class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image_paths, frames_per_image, vel_x):
        self.rect = pygame.Rect(x, y, width, height)
        self.animation = [utils.load_image(image_path, (width, height))
                          for image_path in image_paths]
        self.image = self.animation[0]
        self.frame = 0
        self.frames_per_image = frames_per_image
        self.vel_x = vel_x
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.frame = (self.frame + 1) % (len(self.animation) * self.frames_per_image)
        self.image = self.animation[self.frame // self.frames_per_image]

    def on_event(self, event):
        pass

    def on_key_pressed(self, key_map):
        if key_map[pygame.K_LEFT]:
            self.rect.x -= self.vel_x
        elif key_map[pygame.K_RIGHT]:
            self.rect.x += self.vel_x
    
    def on_collision(self, other):
        pass
