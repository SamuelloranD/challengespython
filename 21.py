# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# É necessário ter a música na pasta do diretório em questão.

import pygame
pygame.init()
pygame.mixer.music.load('msc.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()