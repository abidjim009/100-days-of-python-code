import pygame
import random
import os
import requests
from io import BytesIO

# Initialize Pygame
pygame.init()

# Global variables
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Assets folder
ASSETS_DIR = "assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# URLs for assets (images + sounds)
ASSET_URLS = {
    "bg.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",  # landscape
    "intro1.jpg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",  # ocean
    "outro.jpg": "https://images.unsplash.com/photo-1496309732348-3627f3f040ee",  # dark bg
    "bgm1.mp3": "https://file-examples.com/storage/feff73e8c0a25cc8ec886f4/2017/11/file_example_MP3_700KB.mp3",
    "bgm2.mp3": "https://file-examples.com/storage/feff73e8c0a25cc8ec886f4/2017/11/file_example_MP3_1MG.mp3"
}

# Download helper
def download_asset(name, url):
    path = os.path.join(ASSETS_DIR, name)
    if not os.path.exists(path):
        print(f"Downloading {name}...")
        r = requests.get(url)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
    return path

# Load image (robust)
def load_image(name):
    path = download_asset(name, ASSET_URLS[name])
    try:
        return pygame.image.load(path).convert()
    except pygame.error:
        print(f"Error loading {name}")
        return None

# Load audio
def load_audio(name):
    return download_asset(name, ASSET_URLS[name])

# Text display
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Draw snake
def plot_snake(win, color, snk_list, size):
    for x, y in snk_list:
        pygame.draw.rect(win, color, [x, y, size, size])

# Welcome screen
def welcome():
    intro_img = load_image("intro1.jpg")
    while True:
        gameWindow.blit(pygame.transform.scale(intro_img, (screen_width, screen_height)), (0, 0))
        text_screen("Welcome to Snake Game!", (255, 255, 255), 220, 250)
        text_screen("Press Space To Play", (255, 255, 255), 260, 300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameLoop()

# Main game loop
def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)
    score = 0
    snake_size = 30
    fps = 60

    bg_img = load_image("bg.jpg")
    eat_sound = load_audio("bgm1.mp3")
    gameover_sound = load_audio("bgm2.mp3")

    while not exit_game:
        if game_over:
            outro_img = load_image("outro.jpg")
            gameWindow.blit(pygame.transform.scale(outro_img, (screen_width, screen_height)), (0, 0))
            text_screen("Game Over! Press Enter To Restart", (255, 255, 255), 180, 250)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameLoop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snk_length += 5
                pygame.mixer.music.load(eat_sound)
                pygame.mixer.music.play()

            gameWindow.blit(pygame.transform.scale(bg_img, (screen_width, screen_height)), (0, 0))
            text_screen(f"Score: {score}", (255, 255, 255), 5, 5)
            pygame.draw.rect(gameWindow, (255, 0, 0), [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Collision
            if head in snk_list[:-1] or snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load(gameover_sound)
                pygame.mixer.music.play()

            plot_snake(gameWindow, (0, 255, 0), snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()

# Start
welcome()
