import arcade
from src.characters.luffy.model import LuffyPlayer

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE = 2
PLAYER_1_DEFAULT_POSITION = "right"
PLAYER_2_DEFAULT_POSITION = "left"

DIRECTION_LEFT = -1
DIRECTION_RIGHT = 1


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "One Fight")
        self.background = None
        self.move_speed = 0
        self.player_1 = LuffyPlayer(280, 100, PLAYER_1_DEFAULT_POSITION)
        self.player_2 = LuffyPlayer(1000, 100, PLAYER_2_DEFAULT_POSITION)

    def setup(self):
        self.background = arcade.load_texture("assets/backgrounds/arena.png")

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background
        )

        self.player_1.draw()
        self.player_2.draw()

    def update(self, delta_time):
        self.player_1.update()
        self.player_2.update()

        hit_list = arcade.check_for_collision(self.player_1.animation.get_sprite(), self.player_2.animation.get_sprite())

        if self.move_speed != 0:  # If player is moving
            self.player_1.move(self.move_speed)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.move_speed = DIRECTION_LEFT
        if symbol == arcade.key.RIGHT:
            self.move_speed = DIRECTION_RIGHT
        if symbol == arcade.key.K:
            self.player_1.action_basic_attack(-1)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player_1.stop("left")
            self.move_speed = 0

        elif symbol == arcade.key.RIGHT:
            self.player_1.stop("right")
            self.move_speed = 0


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
