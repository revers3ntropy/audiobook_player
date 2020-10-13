# ================================================================================================
# |----------------------------------={ Audiobook player }=--------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : library_manager.py
#
#                                       Created : Month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import PyPDF2
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================
Audiobooks = []


class Audiobook:
    def __init__(self, file_name):
        self.title = ''
        self.current_location = 0
        self.text = []

        self.set_text(file_name)

    def set_title(self, file_name):
        self.title = file_name
        check = ['f', 'd', 'p', '.']
        for i in range(4):
            self.title = [char for char in self.title]
            if self.title[-1] == check[i]:
                self.title.pop(-1)
            else:
                raise Exception('file type not PDF')
            self.title = ''.join(self.title)

    def set_text(self, file):
        raw_book = open(file, 'rb')
        current_book = PyPDF2.PdfFileReader(raw_book)

        for page_id in range(current_book.numPages):
            page = current_book.getPage(page_id)
            page_text = page.extractText()
            self.text.append(page_text)

        self.set_title(file)

    def increment_location(self):
        if self.current_location < len(self.text):
            self.current_location += 1
            return True

        else:
            self.current_location = 0
            print('Audiobook finished')
            return False
