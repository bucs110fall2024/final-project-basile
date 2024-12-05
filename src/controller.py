import pygame
import time
from src.card import Card
from src.deck import Deck
from src.player import Player
from src.dealer import Dealer
from src.draw import draw_hand, draw_coins, draw_status, draw_bet, draw_total
from random import shuffle


class Controller:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.state = 'menuloop'  # Game starts at the menu loop
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet_amount = 5
        self.result = ""  # To store result message like "You Win", "Dealer Wins", etc.
        self.card_back_image = pygame.image.load("assets/back_card.png")  # Load card back image

    def mainloop(self):
        # Main loop to handle the game flow
        while True:
            if self.state == 'menuloop':
                self.menuloop()
            elif self.state == 'gameloop':
                self.gameloop()
            elif self.state == 'gameoverloop':
                self.gameoverloop()
            elif self.state == 'youwinloop':
                self.youwinloop()

    def menuloop(self):
        # Start menu loop
        self.screen.fill((1, 68, 33))  # Pine green background
        draw_status(self.screen, "Welcome to Blackjack!", 250, self.font)
        draw_status(self.screen, "Press Enter to Start", 300, self.font)
        draw_status(self.screen, "Instructions: Press H to Hit!", 350, self.font)
        draw_status(self.screen, "S to Stand!", 400, self.font)
        draw_status(self.screen, "Get to 40 Coins to Win!", 450, self.font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = 'gameloop'  # Move to the game loop

    def gameloop(self):
        # Game play loop
        self.screen.fill((1, 68, 33))  # Set background to pine green

        # Initial game setup
        if not self.player.hand and not self.dealer.hand:
            self.deck.shuffle_deck()

            # Animate cards coming from the top left corner to player's and dealer's hands
            self.animate_deal()

        # Draw the player's and dealer's hands
        draw_hand(self.screen, self.player.hand, 50, 400, self.font)
        draw_hand(self.screen, self.dealer.hand, 50, 100, self.font)
        draw_coins(self.screen, self.player.coins, 600, 550, self.font)
        draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
        draw_total(self.screen, self.player.total, 50, 350, self.font)

        # Check if the player has run out of coins or reached the win condition
        if self.player.coins <= 0:
            self.state = 'gameoverloop'
        elif self.player.coins >= 40:
            self.state = 'youwinloop'

        # Event handling: Player chooses action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:  # Player chooses to hit
                    self.player.add_card(self.deck.deal_card())
                    if self.player.total > 21:
                        self.state = 'gameoverloop'  # If player busts, game over
                elif event.key == pygame.K_s:  # Player chooses to stand
                    # End player animation, and start dealer's animation
                    self.dealer_move()
                    self.check_winner()
                    if self.player.coins <= 0:
                        self.state = 'gameoverloop'  # If player runs out of coins, game over
                    else:
                        self.state = 'gameoverloop'  # Player wins or loses, display results

        pygame.display.update()

    def animate_deal(self):
    # Animate the cards moving from top-left (100, 0) to final hand positions
      target_positions_player = [(50 + (i * 100), 400) for i in range(2)]  # Position for player
      target_positions_dealer = [(50 + (i * 100), 100) for i in range(2)]  # Position for dealer

      cards_to_deal = [self.deck.deal_card(), self.deck.deal_card(), self.deck.deal_card(), self.deck.deal_card()]

    # Animate each card
      for i, card in enumerate(cards_to_deal):
        # Player's cards first
        if i < 2:
            start_x, start_y = 100, 0  # Starting position for animation (top left)
            end_x, end_y = target_positions_player[i]
            card_image = pygame.image.load("assets/back_card.png")  # Back of the card for the player
        # Dealer's cards second
        else:
            start_x, start_y = 100, 0  # Starting position for animation (top left)
            end_x, end_y = target_positions_dealer[i - 2]
            card_image = pygame.image.load("assets/back_card.png")  # Back of the card for the dealer

        # Scale the back card image to fit the card size
        card_image = pygame.transform.scale(card_image, (71, 96))

        # Animate the movement
        x = start_x
        y = start_y
        while x < end_x and y < end_y:
            self.screen.fill((1, 68, 33))  # Clear the screen with pine green
            
            # Move card towards target
            x += (end_x - start_x) / 20  # Increase the speed by decreasing this divisor
            y += (end_y - start_y) / 20  # Increase the speed by decreasing this divisor

            # Draw the player's and dealer's hands (but only the back of the cards)
            draw_hand(self.screen, [card for card in self.player.hand if card is not None], 50, 400, self.font)
            draw_hand(self.screen, [card for card in self.dealer.hand if card is not None], 50, 100, self.font)
            draw_coins(self.screen, self.player.coins, 600, 550, self.font)
            draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
            draw_total(self.screen, self.player.total, 50, 350, self.font)

            # Draw the card at the new position
            self.screen.blit(card_image, (x, y))  # Draw the back card image
            pygame.display.update()

            # Make the animation faster by reducing sleep time
            time.sleep(0.01)  # Shorter delay between frames

        # After animation, reveal the actual card image at the final position
        if i < 2:
            # Player's card - Show the front of the card
            card_image = pygame.image.load(card.image)  # Load the card's front image
            card_image = pygame.transform.scale(card_image, (71, 96))  # Scale to fit card size
            self.player.add_card(card)  # Add card to player's hand
        else:
            # Dealer's card - Show the front of the card
            card_image = pygame.image.load(card.image)  # Load the card's front image
            card_image = pygame.transform.scale(card_image, (71, 96))  # Scale to fit card size
            self.dealer.add_card(card)  # Add card to dealer's hand

        # Redraw the player's and dealer's hands with the actual cards
        self.screen.fill((1, 68, 33))  # Clear screen with pine green
        draw_hand(self.screen, self.player.hand, 50, 400, self.font)
        draw_hand(self.screen, self.dealer.hand, 50, 100, self.font)
        draw_coins(self.screen, self.player.coins, 600, 550, self.font)
        draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
        draw_total(self.screen, self.player.total, 50, 350, self.font)

        # Draw the revealed card in its final position
        self.screen.blit(card_image, (end_x, end_y))
        pygame.display.update()



    def dealer_move(self):
        # Dealer plays automatically according to basic Blackjack rules
        while self.dealer.total < 17:  # Dealer must hit if under 17
            card = self.deck.deal_card()  # Deal a card to the dealer
            self.dealer.add_card(card)  # Add the card to the dealer's hand

            # Animate dealer's card movement
            

            # Update dealer's total after card is drawn
            self.dealer.update_total()

            # Pause for a short duration (e.g., 1 second) between each card draw
            time.sleep(2)

            # If dealer busts, the player wins
            if self.dealer.total > 21:
                self.result = "Dealer Busts! You Win!"
                self.player.coins += self.bet_amount
                self.state = 'gameoverloop'
                return

            # Update the game display with the new dealer's total
            self.screen.fill((1, 68, 33))  # Pine green background
            draw_hand(self.screen, self.player.hand, 50, 400, self.font)
            draw_hand(self.screen, self.dealer.hand, 50, 100, self.font)
            draw_coins(self.screen, self.player.coins, 600, 550, self.font)
            draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
            draw_total(self.screen, self.player.total, 50, 350, self.font)
            draw_status(self.screen, "Dealer's Turn", 250, self.font)
            
            


            pygame.display.update()

    def check_winner(self):
        # Check who won the game (player or dealer)
        if self.player.total > 21:
            self.result = "You Bust! Dealer Wins!"
            self.player.coins -= self.bet_amount
        elif self.dealer.total > 21:
            self.result = "Dealer Busts! You Win!"
            self.player.coins += self.bet_amount
        elif self.player.total > self.dealer.total:
            self.result = "You Win!"
            self.player.coins += self.bet_amount
        elif self.player.total < self.dealer.total:
            self.result = "Dealer Wins!"
            self.player.coins -= self.bet_amount
        else:
            self.result = "Push! It's a Tie!"

