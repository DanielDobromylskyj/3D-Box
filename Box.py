import pygame
import sys

class box():
    def __init__(self, window_name, size, map_size):
        pygame.display.set_mode(size)
        self.assets_list = []

        # Set player view point and direction
        self.camera_x = 0
        self.camera_y = 0
        self.camera_z = 0
        self.camera_direction = 0

        # get the behind the scenes stuff working basicly
        self.mini_map = []
        try:
            x, y, z = map_size
            for ry in range(x):
                data = []
                for rx in range(y):
                    data.append(0)
                self.mini_map.append(data)
        except:
            sys.exit("Invalide Data While Attempting To Start. | Please Do: window_name, (frame_x, frame_y), (x,y,z)")


    def render(self, image, coords):
        try:
            x, y, z = coords
            data = (image, x, y, z)
        except:
            sys.exit("Invalide Data While Attempting To Render: '" + image + "' | Please Do: image, (x,y,z)")
        self.assets_list.append(data)


    def load_image(self, file):
        f = open(file, "r")
        data = f.read()
        f.close()
        return data

    def gen_frame(self):
        pass




