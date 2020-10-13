# ================================================================================================
# |------------------------------------={ Project Name }=----------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : file_name.py
#
#                                       Created : Month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import global_data
import buttons
import writing
import library_manager
import renderer
import player
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

back_button = buttons.StandardButton(120, 30, writing.retro_8x10, 'back')

select_buttons = []

scroll_pos = 0
scroll_amount = 20


def init():
    global select_buttons

    for i in range(len(library_manager.Audiobooks)):
        button = buttons.StandardButton(renderer.mid_x, renderer.mid_y + 50 * i - 200, writing.retro_8x10, library_manager.Audiobooks[i].title)
        select_buttons.append(button)


up_button = buttons.StandardButton(renderer.screen_x - 120, renderer.mid_y - 25, writing.retro_8x10, 'up')
down_button = buttons.StandardButton(renderer.screen_x - 120, renderer.mid_y + 25, writing.retro_8x10, 'down')


def update_button_pos():
    for j in range(len(select_buttons)):
        button = select_buttons[j]
        button.hit_box = (
            renderer.mid_x - button.size_x / 2 - 7,
            scroll_pos + renderer.mid_y + 50 * j - writing.fonts[button.font][writing.size_y] / 2 - 207,
            button.size_x + 14,
            writing.fonts[button.font][writing.size_y] + 14
        )
        button.y = scroll_pos + renderer.mid_y + 50 * j - 200


def run():
    global scroll_pos

    update_button_pos()

    if back_button.run():
        return global_data.main_menu

    if up_button.run():
        scroll_pos += scroll_amount

    if down_button.run():
        scroll_pos -= scroll_amount

    for i in range(len(select_buttons)):
        if select_buttons[i].run():
            player.current_book = library_manager.Audiobooks[i]
            return global_data.main_menu

    return global_data.library
