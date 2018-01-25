from .Method import Method
from ..version import version


class Program:

    def __init__(self, parser, story):
        parser.program = self
        self.parser = parser
        self.story = story

    def parse_item(self, dictionary, item, parent=None):
        if isinstance(item, Method):
            print('parse item', item, parent)
            dictionary[item.lineno] = item.json()
            if parent:
                dictionary[item.lineno]['parent'] = parent.lineno

            if item.suite:
                for child in item.suite:
                    self.parse_item(dictionary, child, parent=item)

        else:
            for child in item:
                print('parse item children')
                self.parse_item(dictionary, child, parent=parent)

    def json(self):
        script_dictionary = {}
        self.parse_item(script_dictionary, self.story)
        return {'version': version, 'script': script_dictionary}
