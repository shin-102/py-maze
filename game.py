# ============================================================================
# GAME CONTROLLER
# ============================================================================
# This module contains the main Game class that controls all game logic
# ============================================================================

import pygame
from config import *
from entities import Player, Enemy, Coin
from renderer import MazeRenderer

class Game:
    """
    The Game class is the main controller for the entire game.
    It manages game state, updates, and interactions between objects.
    
    Attributes:
        screen (pygame.Surface): The game window
        clock (pygame.time.Clock): Controls frame rate
        running (bool): Whether the game is currently running
        game_over (bool): Whether the game has ended
        player (Player): The player object
        enemies (list): List of enemy objects
        coins (list): List of coin objects
        renderer (MazeRenderer): Object that handles drawing
    """
    
    def __init__(self):
        """
        Initialize the game.
        """
        # Initialize pygame
        pygame.init()
        
        # Create the game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MAZE GAME - Customize it!")
        
        # Create clock for controlling frame rate
        self.clock = pygame.time.Clock()
        
        # Game state
        self.running = True
        self.game_over = False
        self.won = False
        
        # Create game objects
        self.player = Player(PLAYER_START_ROW, PLAYER_START_COL)
        
        # Create enemies
        self.enemies = [
            Enemy(ENEMY1_START_ROW, ENEMY1_START_COL, COLOR_ENEMY1),
            Enemy(ENEMY2_START_ROW, ENEMY2_START_COL, COLOR_ENEMY2),
        ]
        
        # Create coins
        self.coins = self._generate_coins()
        
        # Create renderer
        self.renderer = MazeRenderer(self.screen)
    
    def _generate_coins(self):
        """
        Generate coins in all empty spaces of the maze.
        
        INTENTIONAL LEARNING POINT: The coins are placed in EVERY empty space!
        Try modifying this to place coins in fewer locations.
        Hint: Use random.choice() or check specific conditions.
        
        Returns:
            list: List of Coin objects
        """
        coins = []
        for row_index, row in enumerate(MAZE):
            for col_index, cell in enumerate(row):
                if cell == 0:  # Empty space
                    coins.append(Coin(row_index, col_index))
        return coins
    
    def handle_input(self):
        """
        Handle keyboard input and window events.
        
        INTENTIONAL LEARNING POINT: Currently the game uses arrow keys.
        Try adding WASD controls as an alternative!
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                # Handle arrow keys
                if event.key == pygame.K_UP:
                    self.player.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.player.set_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.player.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.set_direction(1, 0)
                
                # LEARNING POINT: This is a typo! Try typing 'R' to restart
                # (it won't work because the code is incomplete)
                elif event.key == pygame.K_r and self.game_over:
                    self.__init__()  # Restart the game
    
    def update(self):
        """
        Update all game objects and check for collisions.
        """
        if self.game_over:
            return
        
        # Update player position
        self.player.update_position(MAZE)
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update_position(MAZE, self.player)
        
        # Check coin collisions
        coins_collected_this_frame = 0
        for coin in self.coins:
            if coin.check_collision(self.player):
                self.player.coins_collected += 1
                coins_collected_this_frame += 1
        
        # Check enemy collisions
        for enemy in self.enemies:
            if enemy.check_collision(self.player):
                self.player.health -= 1
                # Reset player position to start
                self.player.x = PLAYER_START_COL * WALL_THICKNESS
                self.player.y = PLAYER_START_ROW * WALL_THICKNESS
        
        # Check win condition
        if self.player.coins_collected >= COINS_TO_WIN:
            self.game_over = True
            self.won = True
        
        # Check lose condition
        if self.player.health <= 0:
            self.game_over = True
            self.won = False
    
    def draw(self):
        """
        Draw all game elements to the screen.
        """
        # Fill background
        self.screen.fill(SCREEN_COLOR)
        
        # Draw maze
        self.renderer.draw_maze(MAZE)
        
        # Draw coins
        for coin in self.coins:
            coin.draw(self.screen)
        
        # Draw player and enemies
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        
        # Draw UI
        self.renderer.draw_ui(self.player, self.enemies)
        
        # Draw game over screen if needed
        if self.game_over:
            self.renderer.draw_game_over_screen(self.player, self.won)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """
        Main game loop.
        This runs continuously while the game is active.
        """
        while self.running:
            # Handle input
            self.handle_input()
            
            # Update game state
            self.update()
            
            # Draw everything
            self.draw()
            
            # Control frame rate
            self.clock.tick(FPS)
        
        # Clean up when done
        pygame.quit()
