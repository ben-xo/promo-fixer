from unittest import TestCase
from filename_parser import FilenameParser

CASES = [
    # (filename,
    #  (label, artist, title)),

    # 2 parts with spaces
    ('L-Side - Inna Di Dance.wav',
     ('', 'L-Side', 'Inna Di Dance')),
    ('Abstr4ct - Hot Up.wav',
     ('', 'Abstr4ct', 'Hot Up')),
    ('Creatures - Swamp Martian (Original Mix).wav',
     ('', 'Creatures', 'Swamp Martian (Original Mix)')),
    ('T.R.A.C. - The Pursuit feat. Paul SG  MC Conrad (Artificial Intelligence Remix).wav',
     ('', 'T.R.A.C.', 'The Pursuit feat. Paul SG & MC Conrad (Artificial Intelligence Remix)')),
    ('Unkoded - Wax It!!.wav',
     ('', 'Unkoded', 'Wax It!!')),

    # double-space implies missing ampersand
    ('Simplification  nCamargo - Listen Up (Sl8r Remix).wav',
     ('', 'Simplification & nCamargo', 'Listen Up (Sl8r Remix)')),

    # 2 parts but there is a track number
    ('01 Paul T  Edward Oberon - For Our Love w Makoto  Lorna King.wav',
     ('', 'Paul T & Edward Oberon', 'For Our Love w/Makoto & Lorna King')),
    ('L-Side  GQ - Zaga Dan.wav',
     ('', 'L-Side & GQ', 'Zaga Dan')),

    # looks like 3 parts, but actually the first part is a track number
    ('7 - Skoel  Dreaman - Starting Point.wav',
     ('', 'Skoel & Dreaman', 'Starting Point')),

    # 2 parts with underscores, but there is a catalogue number
    ('D9REC110_Quadrant_&_Iris_&_Jamal_-_Dial_Back_(Original_Mix).wav',
     ('D9REC110', 'Quadrant & Iris & Jamal', 'Dial Back (Original Mix)')),
    ('TRUST025_Trex_&_Benny_V_-_Tundra_(Myth_Remix).wav',
     ('TRUST025', 'Trex & Benny V', 'Tundra (Myth Remix)')),
]


class FilenameParserTestCase(TestCase):

    def test_filename_parsing(self):
        for infile, label_artist_title in CASES:
            with self.subTest(msg=infile):
                fnp = FilenameParser(infile)
                assert fnp.analyse()
                assert (fnp.label, fnp.artist, fnp.title) == label_artist_title
