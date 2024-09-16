import pygame


WIDTH = 640
HIGH = 480
COLOR = (0, 0, 139)
LOGO_IMAGE = "assets/fish.png"
CAPTION_TEXT = "Ocean Romero"
# create a surface on screen that has the size of 640 x 480
screen = pygame.display.set_mode((WIDTH, HIGH))

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(LOGO_IMAGE)
    # set the logo of the screen
    pygame.display.set_icon(logo)
    # set the caption of the screen
    pygame.display.set_caption(CAPTION_TEXT)
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # background set to BLACK
        screen.fill(COLOR)
        # draw the screen
        pygame.display.flip()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
