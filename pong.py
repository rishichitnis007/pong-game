import pygame
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
PADDLE_SPEED = 6

# Ball dimensions
BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
MAX_BALL_SPEED = 8

class Paddle:
    """Represents a paddle in the pong game."""
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
    
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    """Represents the ball in the pong game."""
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
    
    def update(self, paddle_left, paddle_right):
        """Update ball position and handle collisions."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - BALL_SIZE))
        
        # Bounce off paddles
        if self.rect.colliderect(paddle_left.rect):
            if self.speed_x < 0:
                self.speed_x = -self.speed_x
                self.rect.left = paddle_left.rect.right
                # Add spin based on where ball hits paddle
                hit_pos = (self.rect.centery - paddle_left.rect.centery) / (PADDLE_HEIGHT / 2)
                self.speed_y += hit_pos * 2
        
        if self.rect.colliderect(paddle_right.rect):
            if self.speed_x > 0:
                self.speed_x = -self.speed_x
                self.rect.right = paddle_right.rect.left
                # Add spin based on where ball hits paddle
                hit_pos = (self.rect.centery - paddle_right.rect.centery) / (PADDLE_HEIGHT / 2)
                self.speed_y += hit_pos * 2
        
        # Cap ball speed
        if abs(self.speed_y) > MAX_BALL_SPEED:
            self.speed_y = MAX_BALL_SPEED if self.speed_y > 0 else -MAX_BALL_SPEED
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
    
    def reset(self):
        """Reset ball to center."""
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

class PongGame:
    """Main pong game class."""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        
        # Create paddles
        self.paddle_left = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.paddle_right = Paddle(SCREEN_WIDTH - 10 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        
        # Create ball
        self.ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)
        
        # Scores
        self.score_left = 0
        self.score_right = 0
    
    def handle_input(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        keys = pygame.key.get_pressed()
        # Left paddle: W and S keys
        if keys[pygame.K_w]:
            self.paddle_left.move_up()
        if keys[pygame.K_s]:
            self.paddle_left.move_down()
        
        # Right paddle: UP and DOWN arrow keys
        if keys[pygame.K_UP]:
            self.paddle_right.move_up()
        if keys[pygame.K_DOWN]:
            self.paddle_right.move_down()
        
        return True
    
    def update(self):
        """Update game state."""
        self.ball.update(self.paddle_left, self.paddle_right)
        
        # Check if ball is out of bounds
        if self.ball.rect.left < 0:
            self.score_right += 1
            self.ball.reset()
        elif self.ball.rect.right > SCREEN_WIDTH:
            self.score_left += 1
            self.ball.reset()
    
    def draw(self):
        """Draw everything on screen."""
        self.screen.fill(BLACK)
        
        # Draw center line
        for y in range(0, SCREEN_HEIGHT, 20):
            pygame.draw.line(self.screen, WHITE, (SCREEN_WIDTH // 2, y), (SCREEN_WIDTH // 2, y + 10), 2)
        
        # Draw paddles and ball
        self.paddle_left.draw(self.screen)
        self.paddle_right.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Draw scores
        score_text = self.font.render(f"{self.score_left}  {self.score_right}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(score_text, score_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PongGame()
    game.run()
