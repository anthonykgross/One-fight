import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE = 2
PLAYER_SPEED = 5
PLAYER_1_DEFAULT_POSITION = "right"


class Player(object):
    def __init__(self):
        self.sprite_list = arcade.SpriteList()


class PlayerLuffy(Player):
    sprite_path = "assets/sprites/luffy.png"

    def __init__(self):
        super().__init__()
        self.pos_x = 100
        self.pos_y = 100

    def setup_sprites(self, direction):
        move_sprite = arcade.AnimatedTimeSprite(scale=SCALE)
        move_sprite.position = [self.pos_x, self.pos_y]
        move_sprite.textures = self.stand_animation(direction)
        self.sprite_list.append(move_sprite)

    def move_animation(self, direction) -> [arcade.Texture]:
        mirror = (direction == "left")
        t1 = arcade.load_texture(self.sprite_path, 387, 12, 55, 70, mirrored=mirror, scale=SCALE)
        t2 = arcade.load_texture(self.sprite_path, 440, 12, 51, 70, mirrored=mirror, scale=SCALE)
        t3 = arcade.load_texture(self.sprite_path, 490, 12, 58, 70, mirrored=mirror, scale=SCALE)
        t4 = arcade.load_texture(self.sprite_path, 547, 12, 51, 70, mirrored=mirror, scale=SCALE)
        t5 = arcade.load_texture(self.sprite_path, 597, 12, 51, 70, mirrored=mirror, scale=SCALE)
        t6 = arcade.load_texture(self.sprite_path, 646, 12, 52, 70, mirrored=mirror, scale=SCALE)
        t7 = arcade.load_texture(self.sprite_path, 698, 12, 58, 70, mirrored=mirror, scale=SCALE)
        t8 = arcade.load_texture(self.sprite_path, 755, 12, 51, 70, mirrored=mirror, scale=SCALE)
        return [t1, t2, t3, t4, t5, t6, t7, t8]

    def stand_animation(self, direction) -> [arcade.Texture]:
        mirror = False
        if direction == "left":
            mirror = True
        t1 = arcade.load_texture(self.sprite_path, 0, 10, 46, 66, mirrored=mirror, scale=SCALE)
        t2 = arcade.load_texture(self.sprite_path, 44, 10, 44, 66, mirrored=mirror, scale=SCALE)
        t3 = arcade.load_texture(self.sprite_path, 88, 7, 44, 69, mirrored=mirror, scale=SCALE)
        t4 = arcade.load_texture(self.sprite_path, 139, 7, 44, 69, mirrored=mirror, scale=SCALE)
        t5 = arcade.load_texture(self.sprite_path, 181, 5, 40, 72, mirrored=mirror, scale=SCALE)
        t6 = arcade.load_texture(self.sprite_path, 139, 7, 44, 69, mirrored=mirror, scale=SCALE)
        t7 = arcade.load_texture(self.sprite_path, 88, 7, 44, 69, mirrored=mirror, scale=SCALE)
        t8 = arcade.load_texture(self.sprite_path, 44, 10, 44, 66, mirrored=mirror, scale=SCALE)
        return [t1, t2, t3, t4, t5, t6, t7, t8]

    def get_sprite(self) -> arcade.AnimatedTimeSprite:
        return self.sprite_list[0]

    def move_x(self, speed):
        self.pos_x += speed
        for val in self.sprite_list:
            val.center_x = self.pos_x
            if speed > 0:
                val.textures = self.move_animation("right")
            else:
                val.textures = self.move_animation("left")

    def stop_move(self, direction):
        for val in self.sprite_list:
            val.textures = self.stand_animation(direction)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "One Fight")
        self.background = None
        self.move_speed = 0
        self.player_1 = PlayerLuffy()

    def setup(self):
        self.background = arcade.load_texture("assets/backgrounds/arena.png")
        self.player_1.setup_sprites(PLAYER_1_DEFAULT_POSITION)

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
        self.player_1.sprite_list.update_animation()
        if self.move_speed != 0:  # If player is moving
            self.player_1.move_x(self.move_speed)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.move_speed = -PLAYER_SPEED
        elif symbol == arcade.key.RIGHT:
            self.move_speed = PLAYER_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player_1.stop_move("left")
            self.move_speed = 0

        elif symbol == arcade.key.RIGHT:
            self.player_1.stop_move("right")
            self.move_speed = 0


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
