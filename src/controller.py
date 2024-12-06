
import pygame
import sys
import time
from src.card import Card
from src.deck import Deck
from src.player import Player
from src.dealer import Dealer
from src.draw import draw_hand, draw_coins, draw_status, draw_bet, draw_total
from random import shuffle

class Controller:
    def __init__(self, screen, font):
      #Initializes a Controller object
      #self.screen - Surface where the game is drawn
    #self.font - The font used to render text on screen
    #self.state - str: String representing current state of game
    #self.player - Player:An instance of the Player class
    #self.dealer - Dealer: An instance of the Dealer class
    #self.deck - Deck: An instance of the Deck class
    #self.bet_amount - int: Amount being bet on a game
    #self.result - string: String result of the game
    #self.back_card_image - Back image of the card, used by dealer
      
        self.screen = screen
        self.font = font
        self.state = 'menuloop'  # Game starts at the menu loop
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet_amount = 2
        self.result = ""  # To store result message like "You Win", "Dealer Wins", etc.

        # Load back card image (for hidden cards)
        self.back_card_image = pygame.image.load('assets/back_card.png')

    def mainloop(self):
        # Main loop to handle the game flow
        while True:
            if self.state == 'menuloop':
                self.menuloop()
            elif self.state == 'press_d_to_deal':
                self.press_d_to_deal()
            elif self.state == 'gameloop':
                self.gameloop()
            elif self.state == 'gameoverloop':
                self.gameoverloop()
            elif self.state == 'youwinloop':
                self.youwinloop()

    def menuloop(self):
        # Main menu loop, displayed until enter is pressed
        self.screen.fill((1, 68, 33))  # Pine green background
        draw_status(self.screen, "Welcome to Blackjack!", 250, self.font)
        draw_status(self.screen, "Press Enter to Start", 300, self.font)
        draw_status(self.screen, "H to Hit!", 350, self.font)
        draw_status(self.screen, "S to Stand!", 400, self.font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = 'press_d_to_deal'  

    def press_d_to_deal(self):
        # "Press D to Deal" screen with betting instructions, displayed until D is pressed
        self.screen.fill((1, 68, 33))  # Pine green 
        draw_status(self.screen, "Press D to Deal", 250, self.font)
        draw_status(self.screen, "Press Up Arrow to Increase Bet", 300, self.font)
        draw_status(self.screen, "Press Down Arrow to Decrease Bet", 350, self.font)
        draw_bet(self.screen, self.bet_amount, 600, 50, self.font)  # Display current bet
        draw_status(self.screen, f"Total Coins: {self.player.coins}", 400, self.font)  # Display total coins

        pygame.display.update()

        # key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.state = 'gameloop'  
                    self.start_game()
                elif event.key == pygame.K_UP:  # Increase bet
                    if self.bet_amount < self.player.coins:  # Ensure the bet doesn't exceed available coins
                        self.bet_amount += 2
                elif event.key == pygame.K_DOWN:  # Decrease bet
                    if self.bet_amount > 2:  
                        self.bet_amount -= 2

    def start_game(self):
        # Initialize deck and shuffle
        self.deck.shuffle_deck()
        self.player.reset()
        self.dealer.reset()

        # Deals cards to player + dealer
        self.animate_deal()

    def gameloop(self):
        # Game play loop, ends when player presses S
        self.screen.fill((1, 68, 33))  

        # Draw the player's and dealer's hands
        draw_hand(self.screen, self.player.hand, 50, 400, self.font)
        # Back card image for dealers second card
        draw_hand(self.screen, [self.dealer.hand[0], self.back_card_image], 50, 100, self.font)  
        draw_coins(self.screen, self.player.coins, 600, 550, self.font)
        draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
        draw_total(self.screen, self.player.total, 50, 350, self.font)
        draw_total(self.screen, self.dealer.total, 50, 50, self.font)
        # Player action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:  # Player chooses to hit
                    card = self.deck.deal_card()
                    self.animate_card_deal(card, self.player)  # Animate card deal
                    
                    time.sleep(1)
                    if self.player.total > 21:
                          # If player busts, gameoverloop
                        self.result = "You Bust! Dealer Wins!"
                        self.player.coins -= self.bet_amount
                        self.state = 'gameoverloop'
                elif event.key == pygame.K_s:  
                    self.dealer_move()
                    self.check_winner()

        pygame.display.update()

    def animate_deal(self):
    # Animate the cards moving from top-left corner to final hand positions
      target_positions_player = [(50 + (i * 100), 400) for i in range(2)]  # Final position for player
      target_positions_dealer = [(50 + (i * 100), 100) for i in range(1)]  # Final position for dealer

      cards_to_deal = [self.deck.deal_card(), self.deck.deal_card(), self.deck.deal_card(), self.deck.deal_card()]

    
      for i, card in enumerate(cards_to_deal):
        
          if i < 2:
            start_x, start_y = 100, 0  # Starting position 
            end_x, end_y = target_positions_player[i]
        
          elif i == 2:
            start_x, start_y = 100, 0  # Starting position 
            end_x, end_y = target_positions_dealer[0]

        # Animate the movement
          x, y = start_x, start_y
          while x < end_x and y < end_y:
            self.screen.fill((1, 68, 33))  
            # Move card towards target
            x += (end_x - start_x) / 40  
            y += (end_y - start_y) / 40  

            # Draw the player's and dealer's hands
            draw_hand(self.screen, self.player.hand, 50, 400, self.font)
            draw_hand(self.screen, self.dealer.hand, 50, 100, self.font)

            draw_coins(self.screen, self.player.coins, 600, 550, self.font)
            draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
            draw_total(self.screen, self.player.total, 50, 350, self.font)

            # Draw the card at the target position
            if isinstance(card, Card):  
                card_image = pygame.image.load(f'assets/{card.rank}_of_{card.suit}.png')  # Load the  card image
                card_rect = pygame.Rect(x, y, 71, 96)  # card size 71 by 96
                self.screen.blit(card_image, card_rect)
            elif isinstance(card, pygame.Surface):  # If the card is an image (back card) - only for the dealers second card
                self.screen.blit(card, (x, y))

            pygame.display.update()
            time.sleep(0.01) 
        # After animation, add card 
          if i < 2:
            self.player.add_card(card)
          elif i == 2:
            self.dealer.add_card(card)
    
    def dealer_move(self):
    
      card = self.deck.deal_card()
      self.dealer.add_card(card)  
      
    # Animate dealer's second card reveal
      self.animate_dealer_card(card)
      self.dealer.update_total()
      
      time.sleep(1)

    # Dealer goes until their total is 17 ot over
      while self.dealer.total < 17:
        next_card = self.deck.deal_card()
        self.dealer.add_card(next_card)  
        
          # Animate the dealer's card
        self.dealer.update_total()
        self.animate_dealer_card(next_card)
        
        time.sleep(1)

    
      self.check_winner()  
    def animate_card_deal(self, card, target_player):
    # This function animates the card movement for the players hand
      start_x = 100
      start_y = 0  
      end_x = 50 + (len(target_player.hand) * 100)
      end_y = 400

    # Animate the card movement from start to end position
      x, y = start_x, start_y
      while x < end_x and y < end_y:
        self.screen.fill((1, 68, 33))  
        
        
        x += (end_x - start_x) / 40  
        y += (end_y - start_y) / 40  

        # Redraw the player's and dealer's hands
        draw_hand(self.screen, self.player.hand, 50, 400, self.font)
        draw_hand(self.screen, [self.dealer.hand[0], self.back_card_image], 50, 100, self.font)  
        draw_total(self.screen, self.player.total, 50, 350, self.font)
        draw_total(self.screen, self.dealer.total, 50, 50, self.font)
        draw_coins(self.screen, self.player.coins, 600, 550, self.font)
        draw_bet(self.screen, self.bet_amount, 600, 50, self.font)

        # Draw the card image
        card_image = pygame.image.load(f'assets/{card.rank}_of_{card.suit}.png')
        self.screen.blit(card_image, (x, y))

        pygame.display.update()
        time.sleep(0.01)  

    # Finalize card position
      target_player.add_card(card)  

    def animate_dealer_card(self, card):
    # Position for the dealer's cards, increment for each card dealt
      card_width = 71
      card_height = 96
      start_x = 150  
      start_y = 100  
      card_offset = 100  

    # Determine the position based on how many cards the dealer has
      card_index = len(self.dealer.hand) - 1  # Index of the card being dealt
      x_pos = start_x + card_index * card_offset  # Increment position for each new card

    
      card_image = pygame.image.load(f'assets/{card.rank}_of_{card.suit}.png')
      card_rect = pygame.Rect(x_pos, start_y, card_width, card_height)

    # Animate the card moving from the start position to the final position
      x = 100
      y = start_y 
      end_x = x_pos
      end_y =  start_y  

      while x < end_x:
        self.screen.fill((1, 68, 33))  # Clear the screen with pine green
        # Move card towards target
        x += (end_x - start_x) / 20  # Adjust the divisor to control the speed of the animation
        

        # Redraw other game elements (cards, coins, bet, etc.)
        draw_hand(self.screen, self.player.hand, 50, 400, self.font)
        draw_hand(self.screen, self.dealer.hand, 50, 100, self.font)
        draw_coins(self.screen, self.player.coins, 600, 550, self.font)
        draw_bet(self.screen, self.bet_amount, 600, 50, self.font)
        draw_total(self.screen, self.player.total, 50, 350, self.font)
        draw_total(self.screen, self.dealer.total, 50, 50, self.font)
        

        pygame.display.update()

        time.sleep(0.005)  # Control the animation speed

    # After the animation finishes, finalize the card position
      self.screen.blit(card_image, card_rect)
      
    def check_winner(self):
        # Check the result of the game after both player and dealer have finished
        if self.player.total > 21:
            self.result = "You Bust! Dealer Wins!"
            self.player.coins -= self.bet_amount/2
        elif self.dealer.total > 21:
            self.result = "Dealer Busts! You Win!"
            self.player.coins += self.bet_amount/2
        elif self.player.total > self.dealer.total:
            self.result = "You Win!"
            self.player.coins += self.bet_amount/2    
        elif self.player.total < self.dealer.total:
            self.result = "Dealer Wins!"
            self.player.coins -= self.bet_amount/2
            
        else:
            self.result = "It's a Tie!"

        self.state = 'gameoverloop'

    def gameoverloop(self):
        # End of game screen (game over)
        self.screen.fill((1, 68, 33))  # Pine green background
        draw_status(self.screen, self.result, 250, self.font)
        if self.player.coins <= 0:
          self.screen.fill((1,68,33))
          draw_status(self.screen,"GAME OVER, GAME CLOSING", 250, self.font)
          time.sleep(2)
          pygame.quit()
          exit()
        draw_status(self.screen, "Press Enter to Restart", 300, self.font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = 'press_d_to_deal'  # Restart the game and go back to the main menu

