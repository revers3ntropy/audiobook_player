import pygame as py
import glob

import renderer
import global_data
import main_menu
import library_manager
import player
import library
import cursor


def init():
    files = glob.glob('*.pdf')
    for file in files:
        book = library_manager.Audiobook(file)
        library_manager.Audiobooks.append(book)
    library.init()


def tick():
    player.tick()

    if global_data.current_state == global_data.main_menu:
        global_data.current_state = main_menu.run()

    elif global_data.current_state == global_data.library:
        global_data.current_state = library.run()

    # ---------------------------------------------------------------------------------------------

    py.display.flip()
    renderer.clock.tick(renderer.run_FPS)

    renderer.screen.fill(renderer.background_colour)
    cursor.update_mouse_clicked()

    if global_data.typing_sticky_keys > 0:
        global_data.typing_sticky_keys -= 1


def main_loop():
    init()

    while global_data.go:
        tick()

    py.quit()


main_loop()
