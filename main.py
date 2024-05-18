from pygame.event import Event

from pygame import Surface

from lib.HumanEntity import HumanEntity
from lib.Player import Player

import pygame

from lib.EntityAnimation import EntityAnimation

screen: Surface
running = False
clock = pygame.time.Clock()
entities = []
fps: int = 180


def init(title: str = None):
    global screen, running, clock, fps
    pygame.init()
    screen = pygame.display.set_mode((800, 600), flags=pygame.RESIZABLE)
    pygame.display.set_caption(title)
    pygame.display.set_icon(pygame.image.load('resources/logo.png'))
    player_animation = EntityAnimation("resources/player/", int(fps / 10))
    pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    entities.append(Player(pos, 2 / (fps / 60), screen=screen, animation=player_animation))
    entities.append(HumanEntity(pos.copy(), 2 / (fps / 60), screen=screen,
                                animation=EntityAnimation('resources/player/', int(fps / 10))))
    running = True


def update():
    global entities
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not keys[pygame.K_s]:
        entities[0].walk_forward()
    if keys[pygame.K_s] and not keys[pygame.K_w]:
        entities[0].walk_back()
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        entities[0].walk_left()
    if keys[pygame.K_d] and not keys[pygame.K_a]:
        entities[0].walk_right()
    if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        entities[1].walk_forward()
    if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        entities[1].walk_back()
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        entities[1].walk_left()
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        entities[1].walk_right()


def event_processor(e: Event):
    global entities
    if e.type == pygame.KEYDOWN:
        if e.dict['unicode'] == 'e':
            entities[0].slash()
        if e.dict['unicode'] == 'r':
            entities[0].cast()
        if e.dict['unicode'] == ' ':
            entities[1].slash()


def screen_update():
    global screen, entities
    screen.fill("purple")
    for entity in sorted(entities, key=lambda e: e.get_pos().y):
        entity.draw()


if __name__ == '__main__':
    init('My_Game')
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            event_processor(event)
        update()
        screen_update()
        pygame.display.update()
        clock.tick(fps)
