import pygame as py
import sys
import math
from scipy.ndimage import gaussian_filter

class Main:
    def __init__(self):
        py.init()
        self.check = 0
        self.won1 = False
        self.won2 = False
        self.gameBoard = [[0 for _ in range(3)] for _ in range(3)]
        self.image = py.image.load("space1.jpg")
        self.scaled = py.transform.scale(self.image, (1000,800))
        self.screen = py.display.set_mode((1000,800))
        self.display_screen()

    def display_screen(self):
        self.screen.blit(self.scaled, (0,0))
        text = py.font.Font(None,50).render("Tic Tac", True, (255,255,255))
        self.screen.blit(text, text.get_rect(top = self.screen.get_rect().top))
        py.draw.rect(self.screen, (255, 0, 0), (300,100,300,300), 6)
        py.draw.rect(self.screen, (255, 0, 0), (400,100,100,300), 6)
        py.draw.rect(self.screen, (255, 0, 0), (300,200,300,100), 6)
        py.display.flip()

    def update(self, x, y):
        if x in range(300,599) and y in range(100,399) and self.won1 == False and self.won2 == False:
            x1 = math.floor(x/100)
            y1 = math.floor(y/100)
            if self.gameBoard[x1-3][y1-1] == 0:
                if self.check % 2 == 0:
                    py.draw.line(self.screen, (255,255,0), ((x1*100)+25,(y1*100)+75), ((x1*100)+75,(y1*100)+25), 4)
                    py.draw.line(self.screen, (255,255,0), ((x1*100)+75,(y1*100)+75), ((x1*100)+25,(y1*100)+25), 4)
                    self.gameBoard[x1-3][y1-1] = 1
                else:
                    py.draw.circle(self.screen, (255,255,0), ((x1*100)+50, (y1*100)+50), 25, 4)
                    self.gameBoard[x1-3][y1-1] = 2
            self.check += 1
            self.result()
        elif self.won1 == True:
            text = py.font.Font(None,50).render("Player 1 Won", True, (255,255,255))
            self.screen.blit(self.blur(), (0, 0))
            self.screen.blit(text, text.get_rect(center = self.screen.get_rect().center))
            text_surface = py.font.Font(None,28).render("Play Again", True, (255, 255, 255))
            a = py.draw.rect(self.screen, (255, 0, 0), (450,500,103,30))
            self.screen.blit(text_surface, a.topleft)
            if x in range(450,550) and y in range(500,540):
                self.__init__()
        elif self.won2 == True:
            text = py.font.Font(None,50).render("Player 2 Won", True, (255,255,255))
            self.screen.blit(self.blur(), (0, 0))
            self.screen.blit(text, text.get_rect(center = self.screen.get_rect().center))
            text_surface = py.font.Font(None,28).render("Play Again", True, (255, 255, 255))
            b = py.draw.rect(self.screen, (255, 0, 0), (450,500,103,30))
            self.screen.blit(text_surface, b.topleft)
            if x in range(450,550) and y in range(500,540):
                self.__init__()
        py.display.flip()
            
    def result(self):
        if all(cell == 1 for cell in self.gameBoard[0]):
            self.won1 = True
            return
        elif all(cell == 2 for cell in self.gameBoard[0]):
            self.won2 = True
            return
        elif all(cell == 1 for cell in self.gameBoard[1]):
            self.won1 = True
            return
        elif all(cell == 2 for cell in self.gameBoard[1]):
            self.won2 = True
            return
        elif all(cell == 1 for cell in self.gameBoard[2]):
            self.won1 = True
            return
        elif all(cell == 2 for cell in self.gameBoard[2]):
            self.won2 = True
            return

        elif self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1:
            self.won1 = True
            return
        elif self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2:
            self.won2 = True
            return
        elif self.gameBoard[0][2] == 1 and self.gameBoard[1][1] == 1 and self.gameBoard[2][0] == 1:
            self.won1 = True
            return
        elif self.gameBoard[0][2] == 2 and self.gameBoard[1][1] == 2 and self.gameBoard[2][0] == 2:
            self.won2 = True
            return

        elif self.gameBoard[0][0] == 1 and self.gameBoard[1][0] == 1 and self.gameBoard[2][0] == 1:
            self.won1 = True
            return
        elif self.gameBoard[0][0] == 2 and self.gameBoard[1][0] == 2 and self.gameBoard[2][0] == 2:
            self.won2 = True
            return
        elif self.gameBoard[0][1] == 1 and self.gameBoard[1][1] == 1 and self.gameBoard[2][1] == 1:
            self.won1 = True
            return
        elif self.gameBoard[0][1] == 2 and self.gameBoard[1][1] == 2 and self.gameBoard[2][1] == 2:
            self.won2 = True
            return
        elif self.gameBoard[0][2] == 1 and self.gameBoard[1][2] == 1 and self.gameBoard[2][2] == 1:
            self.won1 = True
            return
        elif self.gameBoard[0][2] == 2 and self.gameBoard[1][2] == 2 and self.gameBoard[2][2] == 2:
            self.won2 = True
            return
    
    def blur(self):
        pixel = py.surfarray.array3d(self.screen)
        blured = gaussian_filter(pixel, sigma=(5, 5, 0))
        return py.surfarray.make_surface(blured)
        
    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT or (event.type == py.KEYDOWN and event.key == py.K_ESCAPE):
                py.quit
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.update(x, y)

    def run(self):
        while True:
            self.events()

if __name__ == "__main__":
    game = Main()
    game.run()

        
