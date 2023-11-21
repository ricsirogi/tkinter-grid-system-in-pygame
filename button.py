import pygame
import json
from grid import Grid
from typing import Callable, Optional

# TODO make the width and height of the button change depending on the text


class Button():
    def __init__(self, parent: Grid, width: int, height: int, text: str, font_size: int, font_color: tuple[int, int, int], default_color: tuple[int, int, int], hovering_color: tuple[int, int, int], clicked_color: tuple[int, int, int], func: Callable, surface: pygame.Surface) -> None:
        pygame.font.init()

        self.config = json.load(open('config.json', 'r'))
        self.font_family: str = self.config['basic_button']['font_family']

        self.font: pygame.font.Font = pygame.font.SysFont(self.font_family, font_size)
        self.min_width_height = self.font.size(text)

        self.parent = parent
        self.width = width if width > self.min_width_height[0] else self.min_width_height[0]
        self.height = height if height > self.min_width_height[1] else self.min_width_height[1]
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

        self.clicked = False
        self.was_hovering = False
        self.color = self.default_color

    def grid(self, row, column):
        self.row = row
        self.column = column

        new_pos = self.parent.add(self, row, column)

        self.x = new_pos[0]
        self.y = new_pos[1]

        self.parent.update_members_positions()

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and self.was_hovering:
                self.color = self.clicked_color
                if not self.clicked:
                    self.function()
                self.clicked = True
            else:
                self.clicked = False
                self.color = self.hovering_color
                if not pygame.mouse.get_pressed()[0]:
                    self.was_hovering = True
        else:
            self.clicked = False
            self.was_hovering = False
            self.color = self.default_color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect)

        text = self.font.render(self.text, True, self.font_color)
        text_rect = text.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.surface.blit(text, text_rect)

    def config(self, new_parent: Optional[Grid] = None, new_width: Optional[int] = None, new_height: Optional[int] = None, new_text: Optional[str] = None, new_font_size: Optional[int] = None, new_font_color: Optional[tuple[int, int, int]] = None, new_default_color: Optional[tuple[int, int, int]] = None, new_hovering_color: Optional[tuple[int, int, int]] = None, new_clicked_color: Optional[tuple[int, int, int]] = None, new_func: Optional[Callable] = None, new_surface: Optional[pygame.Surface] = None) -> None:
        if new_parent != None:
            self.parent = new_parent
            self.parent.update_members_positions()
        if new_width != None:
            self.width = new_width
        if new_height != None:
            self.height = new_height
        if new_text != None:
            self.text = new_text
        if new_font_size != None:
            self.font_size = new_font_size
        if new_font_color != None:
            self.font_color = new_font_color
        if new_default_color != None:
            self.default_color = new_default_color
        if new_hovering_color != None:
            self.hovering_color = new_hovering_color
        if new_clicked_color != None:
            self.clicked_color = new_clicked_color
        if new_func != None:
            self.function = new_func
        if new_surface != None:
            self.surface = new_surface
