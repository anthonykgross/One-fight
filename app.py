import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE = 2


class Player(object):
    def __init__(self):
        self.sprite_list = arcade.SpriteList()


class PlayerLuffy(Player):
    sprite_path = "assets/sprites/luffy.png"

    def __init__(self):
        super().__init__()

    def setup_sprites(self):
        move_sprite = arcade.AnimatedTimeSprite(scale=SCALE)
        move_sprite.position = [100, 100]
        move_sprite.textures = self.get_left_to_right_animation()
        self.sprite_list.append(move_sprite)

    def get_left_to_right_animation(self) -> [arcade.Texture]:
        t1 = arcade.load_texture(self.sprite_path, 387, 12, 55, 70, scale=SCALE)
        t2 = arcade.load_texture(self.sprite_path, 440, 12, 51, 70, scale=SCALE)
        t3 = arcade.load_texture(self.sprite_path, 490, 12, 58, 70, scale=SCALE)
        t4 = arcade.load_texture(self.sprite_path, 547, 12, 51, 70, scale=SCALE)
        t5 = arcade.load_texture(self.sprite_path, 597, 12, 51, 70, scale=SCALE)
        t6 = arcade.load_texture(self.sprite_path, 646, 12, 52, 70, scale=SCALE)
        t7 = arcade.load_texture(self.sprite_path, 698, 12, 58, 70, scale=SCALE)
        t8 = arcade.load_texture(self.sprite_path, 755, 12, 51, 70, scale=SCALE)
        return [t1, t2, t3, t4, t5, t6, t7, t8]

    def get_left_to_right_sprite(self) -> arcade.AnimatedTimeSprite:
        return self.sprite_list[0]


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "One Fight")
        self.background = None

    def setup(self):
        self.background = arcade.load_texture("assets/backgrounds/arena.png")

        self.player_1 = PlayerLuffy()
        self.player_1.setup_sprites()

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background
        )

        self.player_1.sprite_list.draw()

    def update(self, delta_time):
        animation_1 = self.player_1.get_left_to_right_sprite()
        animation_1.center_x += 6

        self.player_1.sprite_list.update_animation()


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
