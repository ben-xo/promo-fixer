from unittest import TestCase
from filename_parser import FilenameParser
from filename_group_normaliser import FilenameGroupNormaliser

CASES = [
    ([
        '01 - UPHONIX - Shimmer - HEART TWICE 008.wav',
        '02 - UPHONIX - Purple Dub - HEART TWICE 008.wav',
    ], [
        ('HEART TWICE 008', 'UPHONIX', 'Shimmer'),
        ('HEART TWICE 008', 'UPHONIX', 'Purple Dub'),
    ])
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
            fnp_group.normalise()
            with self.subTest(msg=', '.join(infiles)):
                for (fnp, lat) in zip(fnps, label_artist_titles):
                    assert fnp.label == lat[0], "label: expected {}, got {}".format(lat[0], fnp.label)
                    assert fnp.artist == lat[1], "artist: expected {}, got {}".format(lat[1], fnp.artist)
                    assert fnp.title == lat[2], "title: expected {}, got {}".format(lat[2], fnp.title)


