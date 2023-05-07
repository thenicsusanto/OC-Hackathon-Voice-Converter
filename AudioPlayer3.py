import pygame
def playAudio(file):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)