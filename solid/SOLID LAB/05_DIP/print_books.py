from abc import ABC
import unittest


class Item(ABC):
    def __init__(self, content):
        self.content = content


class GenericFormatter(ABC):
    def format(self, item: Item) -> str:
        return item.content


class Book(Item):
    pass


class Formatter(GenericFormatter):
    pass


class Printer:
    def get_item(self, item: Item, formatter: GenericFormatter):
        formatted_book = formatter.format(item)
        return formatted_book

