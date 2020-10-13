# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : file_name.py
#
#                                       Created : July 25, 2020
#
#                                   Last Update : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                   Controls the pygame screen.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
import pygame as py
#
# ================================================================================================

screen_x = 1000
screen_y = 600
mid_x = screen_x / 2
mid_y = screen_y / 2

background_colour = (255, 255, 255)
run_FPS = 60

py.init()
screen = py.display.set_mode((screen_x, screen_y))
clock = py.time.Clock()

screen.fill((255, 255, 255))
py.display.update()
