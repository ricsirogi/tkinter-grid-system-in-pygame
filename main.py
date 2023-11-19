import pygame
from button import Button
from grid import Grid
import os


class App():
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Grid System in Pygame')

        self.clock = pygame.time.Clock()

        self.frame = Grid(100, 100)

        self.button1 = Button(self.frame, 100, 50, 'Button1', 20, (0, 0, 0), (150, 150, 150), (200, 200, 200), (255, 255, 255), self.click,
                              self.screen)
        self.button2 = Button(self.frame, 100, 50, 'Button2', 20, (0, 0, 0), (150, 150, 150), (200, 200, 200), (255, 255, 255), self.click,
                              self.screen)
        self.button3 = Button(self.frame, 100, 50, 'Button3', 20, (0, 0, 0), (150, 150, 150), (200, 200, 200), (255, 255, 255), self.click,
                              self.screen)
        self.button4 = Button(self.frame, 100, 50, 'Button4', 20, (0, 0, 0), (150, 150, 150), (200, 200, 200), (255, 255, 255), self.click,
                              self.screen)
        self.button5 = Button(self.frame, 100, 50, 'Button5', 20, (0, 0, 0), (150, 150, 150), (200, 200, 200), (255, 255, 255), self.click,
                              self.screen)
        self.button6 = Button(self.frame, 100, 50, 'Button6', 20, (0, 0, 0), (150, 150, 150), (200, 200, 200), (255, 255, 255), self.click,
                              self.screen)

        self.button1.grid(0, 0)
        self.button2.grid(2, 1)
        self.button3.grid(0, 2)
        self.button4.grid(1, 0)
        self.button5.grid(1, 2)
        self.button6.grid(2, 0)

        self.mainloop()

    def mainloop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill((0, 255, 0))

            self.frame.draw_members()

            pygame.display.flip()
            self.clock.tick(60)

    def click(self) -> None:
        print("clicked from a button")


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = App()
