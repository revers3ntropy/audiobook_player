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
import pyttsx3
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

speaker = pyttsx3.init()

current_book = None
play_audiobook = False


def play_pause_audiobook():
    global play_audiobook

    if play_audiobook:
        play_audiobook = False
    else:
        play_audiobook = True


def tick():
    global play_audiobook
    global current_book

    if play_audiobook:
        try:
            speaker.say(current_book.text[current_book.current_location])

            speaker.runAndWait()

            if not current_book.increment_location():
                current_book = None
                play_audiobook = False

        except AttributeError:
            print('No audiobook selected')
            play_audiobook = False

        except IndexError:
            if not current_book.increment_location():
                play_audiobook = False
