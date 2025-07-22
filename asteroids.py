import arcade
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroid Avoider"
PLAYER_SCALE = 0.5
ASTEROID_SCALE = 0.5
PLAYER_MOVEMENT_SPEED = 5
ASTEROID_SPEED = 3


class Player(arcade.Sprite):
    def update(self, delta_time: float = 1/60):
        self.center_x += self.change_x
        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

class Asteroid(arcade.Sprite):
    def update(self, delta_time: float = 1/60):
        self.center_y -= ASTEROID_SPEED
        if self.bottom < 0:
            self.top = SCREEN_HEIGHT
            self.center_x = random.randint(0, SCREEN_WIDTH)

class AsteroidAvoider(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.player = None
        self.asteroid_list = None
        self.score = 0

    def setup(self):
        self.player = Player(':resources:/images/space_shooter/playerShip1_orange.png', PLAYER_SCALE)
        self.player.center_x = SCREEN_WIDTH // 2 # integer division, truncating decimal, centering
        self.player.bottom = 10
        self.asteroid_list = arcade.SpriteList()

        for _ in range(10):
            asteroid = Asteroid(':resources:/images/space_shooter/meteorGrey_med1.png', ASTEROID_SCALE)
            asteroid.center_x = random.randint(0, SCREEN_WIDTH)
            asteroid.center_y = random.uniform(0, SCREEN_HEIGHT)
            self.asteroid_list.append(asteroid)
        self.score = 0

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.asteroid_list.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        self.player.update()
        self.asteroid_list.update()
        if arcade.check_for_collision_with_list(self.player, self.asteroid_list):
            self.setup()
        else:
            self.score+=1
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

def main():
    game = AsteroidAvoider()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()