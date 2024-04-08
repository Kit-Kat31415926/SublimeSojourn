# Import pygame library
import pygame
# Initialize pygame
pygame.init()

# Set up window
window = pygame.display.set_mode((500,500))

def main():
    # Run until user quits program
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        # Make background white
        window.fill((255, 255, 255))

        # Create a blue circle      color       center      radius
        # pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)

        # Create new player
        player = Player()
        # Draw the player on the screen
        window.blit(player.surf, (100, 100))

        # Flip the display
        pygame.display.flip()
    
    # Ends pygame
    pygame.quit()

# Create Player class that inherits from pygame Sprite class
class Player(pygame.sprite.Sprite):
    # Player constructor
    def __init__(self):
        # Calls parent constructor
        super().__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((100, 200, 255))
        self.rect = self.surf.get_rect()


if __name__ == '__main__':
    main()