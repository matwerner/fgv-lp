import pygame
pygame.init()
import json

from game_objects import Ball, Paddle, Brick, Wall

from typing import List, Dict, Tuple

class GameManager:

    def __init__(self, config):
        self.config = config

        # UI
        screen_config = config["screen"]
        self.load_screen(screen_config)

        # GAME OBJECTS
        difficulty_config = config["difficulty"]["hard"]
        game_objects_config = config["objects"]

        paddle_config = game_objects_config["paddle"]
        self.load_paddle(paddle_config, difficulty_config)

        ball_config = game_objects_config["ball"]
        self.load_ball(ball_config, difficulty_config)

        brick_types = {
            "brick_blue": self.load_brick(game_objects_config["brick_blue"]),
            "brick_green": self.load_brick(game_objects_config["brick_green"]),
            "brick_purple": self.load_brick(game_objects_config["brick_purple"])
        }
        level_configs = config["levels"]
        self.load_level(level_configs[0], brick_types)
        self.load_walls()

        self.running = False
        self.clock = None

    def load_screen(self, config: dict):
        self.screen_width = config["width"]
        self.screen_height = config["height"]
        self.fps = config["fps"]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Breakout")

    def load_paddle(self, sprite_config: dict, difficulty_config: dict):
        width = sprite_config["width"]
        height = sprite_config["height"]
        x = self.screen_width // 2 - width // 2
        y = self.screen_height - 50
        sprite_paths = sprite_config["images"]
        frames_per_image = sprite_config["frames_per_image"]
        vel_x = difficulty_config["paddle_vel_x"]
        self.paddle = Paddle(x, y, width, height, sprite_paths, frames_per_image, vel_x)
    
    def load_ball(self, sprite_config: dict, difficulty_config: dict):
        radius = sprite_config["radius"]
        sprite_path = sprite_config["image"]
        x = self.screen_width // 2
        y = self.screen_height // 2
        vel_x = difficulty_config["ball_vel_x"]
        vel_y = difficulty_config["ball_vel_y"]
        self.ball = Ball(x, y, radius, sprite_path, vel_x, vel_y)
    
    def load_brick(self, config: dict):
        width = config["width"]
        height = config["height"]
        normal_sprite_path = config["image_map"]["normal"]
        cracked_sprite_path = config["image_map"]["cracked"]
        return Brick(0, 0, width, height, normal_sprite_path, cracked_sprite_path)
    
    def load_level(self, config: dict, brick_types: Dict[str, Brick]):
        self.bricks = pygame.sprite.Group()
        for brick_config in config["layout"]:
            brick_type = brick_config["type"]
            x = brick_config["x"]
            y = brick_config["y"]

            brick = brick_types[brick_type].copy()
            brick.rect.x = x
            brick.rect.y = y
            self.bricks.add(brick)
    
    def load_walls(self):
        self.walls = pygame.sprite.Group()
        self.walls.add(Wall(-10, 0, 10, self.screen_height))               # wall_left
        self.walls.add(Wall(self.screen_width, 0, 10, self.screen_height)) # wall_right
        self.walls.add(Wall(0, -10, self.screen_width, 10))                # wall_top

        # This wall has a different behavior then the others
        # It will reset the ball when it collides with it
        self.wall_bottom = Wall(0, self.screen_height, self.screen_width, 10) # wall_bottom

    def run(self):
        self.running = True
        self.clock = pygame.time.Clock()
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()
    
    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        
        key_map = pygame.key.get_pressed()
        self.paddle.on_key_pressed(key_map)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.bricks.draw(self.screen)
        pygame.display.flip()

    def update(self):
        self.ball.update()
        self.paddle.update()
        self.check_collisions()
    
    def check_collisions(self):
        # BALL - BRICK
        # BALL - WALL
        # BALL - BOTTOM WALL
        # PADDLE - WALL
        # PADDLE - BALL
        pass

if __name__ == "__main__":
    config_path = "../config/config.json"
    config = json.load(open(config_path, "r")) 
    gm = GameManager(config)
    gm.run()
