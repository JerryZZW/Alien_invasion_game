import sys
import pygame

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # set up the background color
    bg_color = (230, 230, 230)


    # Start the main loop

    while True:
        # watch over keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # paint the screen
        screen.fill(bg_color)

        # display the screen
        pygame.display.flip()

run_game()




