from unittest import TestCase
from filename_parser import FilenameParser

CASES = [
    ('Simplification  nCamargo - Listen Up (Sl8r Remix).wav',
     ('', 'Simplification & nCamargo', 'Listen Up (Sl8r Remix)')),
    ('L-Side - Inna Di Dance.wav',
     ('', 'L-Side', 'Inna Di Dance')),
    ('Abstr4ct - Hot Up.wav',
     ('', 'Abstr4ct', 'Hot Up')),
    ('7 - Skoel  Dreaman - Starting Point.wav',
     ('', 'Skoel & Dreaman', 'Starting Point')),
    ('01 Paul T  Edward Oberon - For Our Love w Makoto  Lorna King.wav',
     ('', 'Paul T & Edward Oberon', 'For Our Love w/Makoto & Lorna King')),
    ('Creatures - Swamp Martian (Original Mix).wav',
     ('', 'Creatures', 'Swamp Martian (Original Mix)')),
    ('D9REC110_Quadrant_&_Iris_&_Jamal_-_Dial_Back_(Original_Mix).wav',
     ('D9REC110', 'Quadrant & Iris & Jamal', 'Dial Back (Original Mix)')),

]


class FilenameParserTestCase(TestCase):
    def test_filename_parsing(self):
        for infile, label_artist_title in CASES:
            with self.subTest(msg=infile):
                fnp = FilenameParser(infile)
                assert fnp.analyse()
                assert (fnp.label, fnp.artist, fnp.title) == label_artist_title
