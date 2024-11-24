import pygame
import random
import sys


# Initialize Pygame
pygame.init()


# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60
BIKE_WIDTH, BIKE_HEIGHT = 60, 80
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 60, 40
OBSTACLE_SPEED = 5


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Bike Game")


# Bike settings
bike_x = WIDTH // 2
bike_y = HEIGHT - BIKE_HEIGHT - 20
bike_speed = 10


# Font for score
font = pygame.font.SysFont('Arial', 36)


# Function to display score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


# Function to generate obstacles
def generate_obstacle():
    x_pos = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    return pygame.Rect(x_pos, -OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)


# Main game loop
def game_loop():
    global bike_x
    score = 0
    clock = pygame.time.Clock()


    # List to hold obstacles
    obstacles = []
   
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Get player input (move bike left and right)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bike_x > 0:
            bike_x -= bike_speed
        if keys[pygame.K_RIGHT] and bike_x < WIDTH - BIKE_WIDTH:
            bike_x += bike_speed


        # Generate obstacles
        if random.randint(1, 60) == 1:  # Random chance to generate a new obstacle
            obstacles.append(generate_obstacle())


        # Move obstacles down the screen
        for obstacle in obstacles:
            obstacle.y += OBSTACLE_SPEED


        # Remove obstacles that have gone off-screen
        obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]


        # Check for collision with obstacles
        bike_rect = pygame.Rect(bike_x, bike_y, BIKE_WIDTH, BIKE_HEIGHT)
        for obstacle in obstacles:
            if bike_rect.colliderect(obstacle):
                pygame.quit()
                sys.exit()  # End game on collision


        # Update the score
        score += 1


        # Fill the screen with background color
        screen.fill(BLACK)


        # Draw the bike (green rectangle)
        pygame.draw.rect(screen, GREEN, (bike_x, bike_y, BIKE_WIDTH, BIKE_HEIGHT))


        # Draw obstacles (red rectangles)
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)


        # Display score
        display_score(score)


        # Update the screen
        pygame.display.update()


        # Frame rate control
        clock.tick(FPS)


# Run the gam   e
game_loop()



