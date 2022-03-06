from unittest import TestCase
from filename_parser import FilenameParser
from filename_group_normaliser import FilenameGroupNormaliser
from test_filename_parser import CASES as NEGATIVE_CASES

CASES = [
    ([
        '01 - UPHONIX - Shimmer - HEART TWICE 008.wav',
        '02 - UPHONIX - Purple Dub - HEART TWICE 008.wav',
    ], [
        ('HEART TWICE 008', 'UPHONIX', 'Shimmer'),
        ('HEART TWICE 008', 'UPHONIX', 'Purple Dub'),
    ]), ([
        'SEXTASY - check point - HEART TWICE 006.wav',
        'SEXTASY - far beyond - HEART TWICE 006.wav',
        'SEXTASY - give it back - HEART TWICE 006.wav',
    ], [
        ('HEART TWICE 006', 'SEXTASY', 'check point'),
        ('HEART TWICE 006', 'SEXTASY', 'far beyond'),
        ('HEART TWICE 006', 'SEXTASY', 'give it back'),
    ]),
]


class FilenameGroupNormaliserTestCase(TestCase):

    def test_filename_group_normalising(self):
        for infiles, label_artist_titles in CASES:
            fnps = []
            for infile in infiles:
                with self.subTest(msg=infile):
                    fnp = FilenameParser(infile)
                    assert fnp.analyse()
                    fnps.append(fnp)

            assert len(fnps) == len(infiles)

            fnp_group = FilenameGroupNormaliser(fnps)
            mutation_count = fnp_group.normalise()
            assert mutation_count > 0
            with self.subTest(msg=', '.join(infiles)):
                for (fnp, lat) in zip(fnps, label_artist_titles):
                    assert fnp.label == lat[0], "label: expected {}, got {}".format(lat[0], fnp.label)
                    assert fnp.artist == lat[1], "artist: expected {}, got {}".format(lat[1], fnp.artist)
                    assert fnp.title == lat[2], "title: expected {}, got {}".format(lat[2], fnp.title)

    def test_filename_group_normalising_doesnt_break_ordinary_things(self):
        # this is a little contorted because the NEGATIVE_CASES are pairs of (filename, (label, artist, title))

        # convert it to a list of (FilenameParser(filename), (label, artist, title)) and analyse them
        fnps = [(FilenameParser(infile), lat) for infile, lat in NEGATIVE_CASES]
        assert len(fnps) == len(NEGATIVE_CASES)
        for fnp in fnps:
            fnp[0].analyse()

        # now we need just a list of the FilenameParsers.
        fnp_group = FilenameGroupNormaliser([fnp[0] for fnp in fnps])
        mutation_count = fnp_group.normalise()
        assert mutation_count == 0

