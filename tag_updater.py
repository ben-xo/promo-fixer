import mutagen
from mutagen import MutagenError
from mutagen.id3 import ID3, TIT2, TALB, TPE1

class TagUpdater:

    def update_tag(self, filename: str, artist: str, title: str, album: str, dry_run=False) -> bool:

        try:

            f = mutagen.File(filename)
            f.tags.add(TIT2(text=[title]))
            f.tags.add(TALB(text=[album]))
            f.tags.add(TPE1(text=[artist]))

            if not dry_run:
                f.save()

        except MutagenError as e:
            print("!! Could not read file: {}".format(e))
            return False
        except AttributeError:
            print('!! No tags found: {}'.format(e))
            return False

        return True