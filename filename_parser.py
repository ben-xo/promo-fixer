import re
from typing import Optional, Match


class FilenameParser:

    def __init__(self, infile: str):
        self.infile = infile
        self.label = ''
        self.artist = ''
        self.title = ''

    def match_3part_underscores(self) -> Optional[Match[str]]:
        m = re.match(r'^(?:\d+_(?:-_)?)?(?P<label>[a-zA-Z0-9]{2,}(?:_+[a-zA-Z0-9()]+)*)_*-_*'
                     r'(?P<artist>[a-zA-Z0-9.,&-]+(?:_+[a-zA-Z0-9().,&-]+)*)_*-_*'
                     r'(?P<title>[a-zA-Z0-9.,&]+(?:_+[a-zA-Z0-9().,&!]+)*)\.',
                     self.infile)
        if m:
            self.label = self.normalise_underscore(m.group('label'))
            self.artist = self.normalise_underscore(m.group('artist'))
            self.title = self.normalise_underscore(m.group('title'))

        return m

    def match_3part_underscores_cat_no_variation(self) -> Optional[Match[str]]:
        m = re.match(r'^(?:\d+_(?:-_)?)?(?P<label>[A-Z0-9]{2,})_'
                     r'(?P<artist>[a-zA-Z0-9.,&-]+(?:_+[a-zA-Z0-9().,&-]+)*)_*-_*'
                     r'(?P<title>[a-zA-Z0-9.,&]+(?:_+[a-zA-Z0-9().,&!]+)*)\.',
                     self.infile)
        if m:
            self.label = self.normalise_underscore(m.group('label'))
            self.artist = self.normalise_underscore(m.group('artist'))
            self.title = self.normalise_underscore(m.group('title'))

        return m

    def match_2part_underscores(self) -> Optional[Match[str]]:
        m = re.match(r'^(?:\d+_(?:-_)?)?(?P<artist>[a-zA-Z0-9.,&-]+(?:_+[a-zA-Z0-9().,&-]+)*)_*-_*'
                     r'(?P<title>[a-zA-Z0-9.,&]+(?:_+[a-zA-Z0-9().,&!]+)*)\.',
                     self.infile)
        if m:
            self.artist = self.normalise_underscore(m.group('artist'))
            self.title = self.normalise_underscore(m.group('title'))

        return m

    def match_3part_spaces(self) -> Optional[Match[str]]:
        m = re.match(r'^(?:\d+\s(?:-\s)?)?(?P<label>[a-zA-Z0-9]{2,}(?:\s+[a-zA-Z0-9()]+)*)\s+-\s+'
                     r'(?P<artist>[a-zA-Z0-9.,&-]+(?:\s+[a-zA-Z0-9().,&-]+)*)\s*-\s*'
                     r'(?P<title>[a-zA-Z0-9.,&]+(?:\s+[a-zA-Z0-9().,&!]+)*)\.',
                     self.infile)
        if m:
            self.label = self.normalise(m.group('label'))
            self.artist = self.normalise(m.group('artist'))
            self.title = self.normalise(m.group('title'))

        return m

    def match_2part_spaces(self) -> Optional[Match[str]]:
        m = re.match(r'^(?:\d+\s(?:-\s)?)?(?P<artist>[a-zA-Z0-9.,&-]+(?:\s+[a-zA-Z0-9().,&-]+)*)\s*-\s*'
                     r'(?P<title>[a-zA-Z0-9.,&]+(?:\s+[a-zA-Z0-9().,&!]+)*)\.',
                     self.infile)
        if m:
            self.artist = self.normalise(m.group('artist'))
            self.title = self.normalise(m.group('title'))

        return m

    def normalise(self, part: str) -> str:
        return part.replace('  ', ' & ').replace(' w ', ' w/')

    def normalise_underscore(self, part: str) -> str:
        return self.normalise(part.replace('_', ' '))

    def analyse(self) -> bool:

        m = self.match_3part_underscores()
        if not m:
            m = self.match_3part_underscores_cat_no_variation()
        if not m:
            m = self.match_2part_underscores()
        if not m:
            m = self.match_3part_spaces()
        if not m:
            m = self.match_2part_spaces()
        if not m:
            return False

        return True
