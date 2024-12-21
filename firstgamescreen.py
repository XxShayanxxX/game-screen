import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

# Load and resize the image
# Use raw string (prefix with `r`) or replace backslashes with forward slashes
image = pygame.image.load(r"c:\Users\arumu\Downloads\radio-times-marvel-rivals-character-list-spider-man-4d3508c.jpg")
image = pygame.transform.scale(image, (300, 300))

# Calculate the position to center the image
image_rect = image.get_rect(center=(250, 250))

# Set the background color
background_color = (58, 58, 58)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the image at the center
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

