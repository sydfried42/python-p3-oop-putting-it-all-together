#!/usr/bin/env python3

class Book:
    def __init__(self, title="And Then There Were None", page_count=272):
        self.title = title
        self.page_count = page_count
        self.title = title
        self.page_count = page_count
    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, page_count):
        # page_count must be an integer" if page_count is not an integer...
        if not isinstance(page_count, int):
            # return ("not an integer")
            self._page_count = "not an integer"
            # print("page_count must be an integer\n")
            print("page_count must be an integer")
        # else do nothing
        else:
            self._page_count = page_count
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
