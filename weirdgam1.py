import pygame, sys
from pygame import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.LOW)

pygame.init()
BLACK = (0,0,0)
WIDTH = 100
HEIGHT = 100
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)
x = 0
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
            pygame.quit()
            sys.exit()
      if event.type == KEYDOWN:
         key = event.key
         if key == pygame.K_p:
            if x == 0:
               GPIO.output(26,GPIO.HIGH)
               x = 1
            else:
               GPIO.output(26,GPIO.LOW)
               x = 0
