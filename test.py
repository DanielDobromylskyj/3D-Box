from Box import box
import pygame

rbox = box("Test Box", (500, 500), (5,5,1))

rbox.render("easports", (10, 10, 1))


while True:
    pygame.display.update()