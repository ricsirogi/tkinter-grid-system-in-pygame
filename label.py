import pygame
import json
from grid import Grid

# TODO Make width and height change according to the text


class Label():
    def __init__(self, parent: Grid, text: str, font_size: int, font_color: tuple[int, int, int], background_color: tuple[int, int, int], surface: pygame.Surface) -> None:
        self.config = json.load(open('config.json', 'r'))
        self.font_family: str = self.config['basic_button']['font_family']

        self.parent = parent
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.surface = surface
        self.background_color = background_color

        self.x: int = 0
        self.y: int = 0
        self.row: int = 0
        self.column: int = 0

        # Will calculate this later
        self.width: int = 0
        self.height: int = 0

        self.background_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.font: pygame.font.Font = pygame.font.SysFont(self.font_family, self.font_size)

        self.width, self.height = self.font.size(self.text)

        self.text_surface = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))

        self.background_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def grid(self, row, column):
        self.row = row
        self.column = column

        new_pos = self.parent.add(self, row, column)

        self.x = new_pos[0]
        self.y = new_pos[1]

        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.background_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.parent.update_members_positions()

    def draw(self):
        pygame.draw.rect(self.surface, self.background_color, self.background_rect)

        self.surface.blit(self.text_surface, self.text_rect)
