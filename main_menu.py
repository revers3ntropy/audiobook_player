# ================================================================================================
# |----------------------------------={ Audiobook Player }=--------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : main_menu.py
#
#                                       Created : October 11, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import global_data
import buttons
import writing
import player
import renderer
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
#
# ================================================================================================

quit_button = buttons.StandardButton(120, 30, writing.retro_8x10, 'quit')

play_text = 'play'
pause_text = 'pause'
play_pause_button = buttons.SwitchButton(renderer.mid_x, renderer.mid_y + 50, writing.retro_8x10, (play_text, pause_text), 0)

library_button = buttons.StandardButton(renderer.mid_x, renderer.mid_y - 150, writing.retro_8x10, 'library')


def run():
    if quit_button.run():
        global_data.go = False

    writing.write(writing.retro_8x10, 'current audiobook:', (renderer.mid_x, renderer.mid_y - 50))

    try:
        current_title = player.current_book.title
    except:
        current_title = 'none selected'
    writing.write(writing.retro_8x10, current_title, (renderer.mid_x, renderer.mid_y))

    if play_pause_button.run() is not False:
        player.play_pause_audiobook()

    if library_button.run():
        return global_data.library

    if player.play_audiobook:
        try:
            writing.write(writing.retro_8x10, f'- {player.current_book.text[player.current_book.current_location]} -', (renderer.mid_x, renderer.mid_y + 100))
        except:
            pass
    return global_data.main_menu
