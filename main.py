import pygame
from pygame import Vector2
from pygame.event import Event

from lib.CollisionBox import CollisionBox
from lib.EntityAnimation import EntityAnimation
from lib.Game import Game
from lib.HumanEntity import HumanEntity
from lib.Player import Player


player_animation = EntityAnimation("resources/player/", int(180 / 10))
pos = pygame.Vector2(400, 300)
player = Player(pos, 2 / (180 / 60), animation=player_animation, collision_box=CollisionBox(
    Vector2(0, 0), Vector2(-16, -32), Vector2(16, 32)))
game = Game("My_game", player, (800, 600))


@game.on_event()
def event(e: Event):
    if e.type == pygame.KEYDOWN:
        if e.dict['unicode'] == 'e':
            game.player.slash()
        if e.dict['unicode'] == 'r':
            game.player.cast()
        if e.dict['unicode'] == ' ':
            game.get_entities()[1].slash()


@game.on_update()
def update():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not keys[pygame.K_s]:
        game.player.walk_forward()
    if keys[pygame.K_s] and not keys[pygame.K_w]:
        game.player.walk_back()
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        game.player.walk_left()
    if keys[pygame.K_d] and not keys[pygame.K_a]:
        game.player.walk_right()
    if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        game.get_entities()[1].walk_forward()
    if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        game.get_entities()[1].walk_back()
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        game.get_entities()[1].walk_left()
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        game.get_entities()[1].walk_right()


if __name__ == '__main__':
    player2 = HumanEntity(pos.copy(), 2 / (game.fps / 60),
                          animation=EntityAnimation('resources/player/', int(game.fps / 10)))
    game.add_entity(player2)
    game.run()
