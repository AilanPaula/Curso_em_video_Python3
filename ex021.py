'''
Crie um programa que abra e reproduza um arquivo mp3.
'''
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()