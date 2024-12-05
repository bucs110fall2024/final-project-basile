import pygame
from src.controller import Controller  # Import your Controller class

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen (width and height of the window)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Blackjack Game")

    # Load font for text display
    font = pygame.font.SysFont('ARCADECLASSIC', 24)  # Adjust font size as needed

    # Create an instance of the GameController
    game_controller = Controller(screen, font)

    # Start the game loop
    game_controller.mainloop()

    # Quit pygame when done
    pygame.quit()

if __name__ == "__main__":
    main()
