import pygame
pygame.mixer.init()
pygame.init()
#precisa iniciar o pygame e o mixer
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
