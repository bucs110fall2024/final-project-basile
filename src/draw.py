import pygame
from src.card import Card

def draw_hand(screen, hand, x, y, font):
    for i, card in enumerate(hand):
        if isinstance(card, Card):  # Ensure card is an instance of Card
            card_image = pygame.image.load(f'assets/{card.rank}_of_{card.suit}.png')
            #text = font.render(f"{card.rank} of {card.suit.capitalize()}", True, (0, 0, 0))
            screen.blit(card_image, (x + i * 100, y))  # Adjust position as needed
        elif isinstance(card, pygame.Surface):  # If the card is an image (back card)
            screen.blit(card, (x + i * 100, y))  # Draw image (back of card)

# Function to draw coins at the bottom of the screen
def draw_coins(screen, coins, x, y, font):
    coin_image = pygame.image.load('assets/coin.png')  # Load coin image
    coin_image = pygame.transform.scale(coin_image, (30, 30))  # Resize the coin image
    screen.blit(coin_image, (x, y))  # Draw the coin
    coin_text = font.render(f"Coins: {coins}", True, (255, 255, 255))  # Render coins text
    screen.blit(coin_text, (x + 35, y))  # Draw the coins text next to the coin image

# Function to draw the game title or status text (e.g., "Game Over", "You Win!")
def draw_status(screen, text,y, font):
    status_text = font.render(text, True, (255, 255, 255))
    screen.blit(status_text, (250, y))  # Position the status text in the center of the screen

# Function to draw the betting amount
def draw_bet(screen, bet_amount, x, y, font):
    bet_text = font.render(f"Bet: {bet_amount} Coins", True, (255, 255, 255))
    screen.blit(bet_text, (x, y))

# Function to draw the player's total points (card value sum)
def draw_total(screen, total, x, y, font):
    total_text = font.render(f"Total: {total}", True, (255, 255, 255))
    screen.blit(total_text, (x, y))

# Function to draw the start screen or game over screen instructions
def draw_instruction(screen, message, y, font):
    instruction_text = font.render(message, True, (255, 255, 255))
    screen.blit(instruction_text, (250, y))  # Position the instruction text

