import os
import ast
import pygame
import random
from dotenv import load_dotenv

pygame.init()

window_size = 256
square_size = 16
num_squares = window_size // square_size
load_dotenv('GENERATION.env')
seed = ast.literal_eval(os.getenv('SEED'))
print("\n")

if seed is None:
    seed = random.randint(0, 10000000)
    print(f"Using randomly generated seed: {str(seed)}")
else:
    print(f"Using seed: {str(seed)}")

random.seed(seed)

window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Random Squares")

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

colors = [random_color() for i in range(num_squares * 16)]
paints = [random.randint(0, 1) for i in range(num_squares * 16)]

index = 0
running = True
while running:
    if seed is None:
        colors = [random_color() for i in range(num_squares * 16)]
        paints = [random.randint(0, 1) for i in range(num_squares * 16)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    for row in range(num_squares):
        for col in range(num_squares):
            try:
                if paints[index]:
                    x = col * square_size
                    y = row * square_size
                    try:
                        color = colors[index]
                    except:
                        index = 0
                        color = colors[index]
                    pygame.draw.rect(window, color, (x, y, square_size, square_size))
            except:
                index = 0
                pass
            index += 1

    pygame.display.flip()

pygame.quit()