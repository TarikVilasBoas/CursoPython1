import pygame

pygame.init()
pygame.mixer.music.load('nirvana.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # Espera tocar
    pygame.time.Clock().tick(10)