import pygame
import json
from grid import Grid
from typing import Callable


class Button():
    def __init__(self, parent: Grid, width: int, height: int, text: str, font_size: int, font_color: tuple[int, int, int], default_color: tuple[int, int, int], hovering_color: tuple[int, int, int], clicked_color: tuple[int, int, int], func: Callable, surface: pygame.Surface) -> None:
        pygame.font.init()

        self.config = json.load(open('config.json', 'r'))
        self.font_family: str = self.config['basic_button']['font_family']

        self.parent = parent
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.default_color = default_color
        self.hovering_color = hovering_color
        self.clicked_color = clicked_color
        self.function = func
        self.surface = surface

        self.x: int = 0
        self.y: int = 0
        self.row: int = 0
        self.column: int = 0

        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font: pygame.font.Font = pygame.font.SysFont(self.font_family, self.font_size)

    def grid(self, row, column):
        self.row = row
        self.column = column

        new_pos = self.parent.add(self, row, column)

        self.x = new_pos[0]
        self.y = new_pos[1]

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        color = self.default_color
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                color = self.clicked_color
                self.function()
            else:
                color = self.hovering_color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, color, self.rect)

        text = self.font.render(self.text, True, self.font_color)
        text_rect = text.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.surface.blit(text, text_rect)
