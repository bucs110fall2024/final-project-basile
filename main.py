import pygame
from src.controller import Controller  

def main():
    
    pygame.init()

    
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Blackjack Game")

    
    font = pygame.font.SysFont('ARCADECLASSIC', 24)  

    
    game_controller = Controller(screen, font)

    
    game_controller.mainloop()

    
    pygame.quit()

if __name__ == "__main__":
    main()
