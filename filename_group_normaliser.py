from typing import List

from filename_parser import FilenameParser


class FilenameGroupNormaliser:

    def __init__(self, fnps: List[FilenameParser]):
        self.fnps = fnps

    def normalise(self) -> int:
        mutation_count = 0
        if len(self.fnps) > 1:
            mutation_count += self.fix_three_part_artist_title_label()
        return mutation_count

    def fix_three_part_artist_title_label(self) -> int:
        mutation_count = 0
        three_part_fnps = [fnp for fnp in self.fnps if fnp.label != '']

        # start a list of fnps with titles that are identical.
        while len(three_part_fnps):

            # the first three_part_fnp will always go into this list. But will there be more?
            identical_titles = [three_part_fnps[0]] + [
                fnp for fnp in three_part_fnps[1:]
                if fnp.title == three_part_fnps[0].title and fnp.artist != three_part_fnps[0].artist
            ]

            if len(identical_titles) > 1:
                # at least 2 files have the same title but different artists.
                # this implies that instead of label - artist - title it's actually artist - title - label
                for fnp in identical_titles:
                    (fnp.label, fnp.artist, fnp.title) = (fnp.title, fnp.label, fnp.artist)
                    mutation_count += 1

            # base case is equivalent to .pop() the first element
            for fnp in identical_titles:
                three_part_fnps.remove(fnp)

        return mutation_count
