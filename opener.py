import pygame
import os



# Initialize Pygame
pygame.init()

# Define the dimensions of the window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Quki")


Title = pygame.image.load("push.png")
Title_rect = Title.get_rect()
Title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 500)

made = pygame.image.load("Made with.png")
made_rect = Title.get_rect()
made_rect.center = (WINDOW_WIDTH // 2 +150, WINDOW_HEIGHT + 75)


# Load the button image
button_image = pygame.image.load("button.png")
button_rect = button_image.get_rect()
button_rect.center = (WINDOW_WIDTH // 2 , WINDOW_HEIGHT - 175 )

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button is clicked
            if button_rect.collidepoint(event.pos):
                # Run main.py file
                os.system("python main.py")

    # Fill the background color
    window.fill((255,255,255))

    # Draw the button
    window.blit(button_image, button_rect)
    window.blit(Title , Title_rect)
    window.blit(made , made_rect)
    
    
    # Update the display
    pygame.display.update()

# Quit the program
pygame.quit()
