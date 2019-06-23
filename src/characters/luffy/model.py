import arcade
from src.characters.model import Player


class LuffyPlayer(Player):
    life = 100
    basic_attack = 5
    special_attack = 15
    speed = 5

    def __init__(self, x, y, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.direction = direction
        self.animation = LuffyAnimation(self.x, self.y, self.direction, 2)

    def move(self, direction):
        self.x += direction*self.speed
        self.animation.move_x(self.x, direction)

    def action_basic_attack(self, direction):
        self.animation.action_basic_attack(self.x, direction)

    def stop(self, direction):
        self.animation.stop_move(direction)

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()


class LuffyAnimation(object):
    sprite_path = "assets/sprites/luffy.png"

    def __init__(self, x, y, direction, scale):
        super().__init__()
        self.scale = scale

        self.sprite_list = arcade.SpriteList()
        move_sprite = arcade.AnimatedTimeSprite(scale=self.scale)
        move_sprite.position = [x, y]
        move_sprite.textures = self.stand_animation(direction)
        self.sprite_list.append(move_sprite)

    def draw(self):
        self.sprite_list.draw()

    def update(self):
        self.sprite_list.update_animation()

    def move_animation(self, direction) -> [arcade.Texture]:
        mirror = (direction == "left")
        t1 = arcade.load_texture(self.sprite_path, 387, 12, 55, 70, mirrored=mirror, scale=self.scale)
        t2 = arcade.load_texture(self.sprite_path, 440, 12, 51, 70, mirrored=mirror, scale=self.scale)
        t3 = arcade.load_texture(self.sprite_path, 490, 12, 58, 70, mirrored=mirror, scale=self.scale)
        t4 = arcade.load_texture(self.sprite_path, 547, 12, 51, 70, mirrored=mirror, scale=self.scale)
        t5 = arcade.load_texture(self.sprite_path, 597, 12, 51, 70, mirrored=mirror, scale=self.scale)
        t6 = arcade.load_texture(self.sprite_path, 646, 12, 52, 70, mirrored=mirror, scale=self.scale)
        t7 = arcade.load_texture(self.sprite_path, 698, 12, 58, 70, mirrored=mirror, scale=self.scale)
        t8 = arcade.load_texture(self.sprite_path, 755, 12, 51, 70, mirrored=mirror, scale=self.scale)
        return [t1, t2, t3, t4, t5, t6, t7, t8]

    def stand_animation(self, direction) -> [arcade.Texture]:
        mirror = (direction == "left")
        t1 = arcade.load_texture(self.sprite_path, 0, 10, 46, 66, mirrored=mirror, scale=self.scale)
        t2 = arcade.load_texture(self.sprite_path, 44, 10, 44, 66, mirrored=mirror, scale=self.scale)
        t3 = arcade.load_texture(self.sprite_path, 88, 7, 44, 69, mirrored=mirror, scale=self.scale)
        t4 = arcade.load_texture(self.sprite_path, 139, 7, 44, 69, mirrored=mirror, scale=self.scale)
        t5 = arcade.load_texture(self.sprite_path, 181, 5, 40, 72, mirrored=mirror, scale=self.scale)
        t6 = arcade.load_texture(self.sprite_path, 139, 7, 44, 69, mirrored=mirror, scale=self.scale)
        t7 = arcade.load_texture(self.sprite_path, 88, 7, 44, 69, mirrored=mirror, scale=self.scale)
        t8 = arcade.load_texture(self.sprite_path, 44, 10, 44, 66, mirrored=mirror, scale=self.scale)
        return [t1, t2, t3, t4, t5, t6, t7, t8]

    def basic_attack_animation(self, direction) -> [arcade.Texture]:
        mirror = (direction == "left")
        t1 = arcade.load_texture(self.sprite_path, 0, 83, 48, 66, mirrored=mirror, scale=self.scale)
        t2 = arcade.load_texture(self.sprite_path, 46, 83, 44, 66, mirrored=mirror, scale=self.scale)
        t3 = arcade.load_texture(self.sprite_path, 88, 83, 65, 66, mirrored=mirror, scale=self.scale)
        t4 = arcade.load_texture(self.sprite_path, 153, 83, 68, 66, mirrored=mirror, scale=self.scale)
        t5 = arcade.load_texture(self.sprite_path, 220, 83, 44, 66, mirrored=mirror, scale=self.scale)
        return [t1, t2, t3, t4, t5]

    def get_sprite(self) -> arcade.AnimatedTimeSprite:
        return self.sprite_list[0]

    def move_x(self, x, direction):
        sprite = self.get_sprite()
        sprite.center_x = x

        if direction > 0:
            sprite.textures = self.move_animation("right")
        else:
            sprite.textures = self.move_animation("left")

    def action_basic_attack(self, x, direction):
        sprite = self.get_sprite()
        sprite.center_x = x

        if direction > 0:
            sprite.textures = self.basic_attack_animation("right")
        else:
            sprite.textures = self.basic_attack_animation("left")

    def stop_move(self, direction):
        sprite = self.get_sprite()
        sprite.textures = self.stand_animation(direction)

