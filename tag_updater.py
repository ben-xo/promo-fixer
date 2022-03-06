import mutagen
from mutagen import MutagenError
from mutagen.id3 import TIT2, TALB, TPE1


class TagUpdater:

    def update_tag(self, filename: str, artist: str, title: str, album: str) -> bool:

        try:
            f = mutagen.File(filename)
            f.add_tags()
            f.tags.add(TIT2(text=[title]))
            f.tags.add(TALB(text=[album]))
            f.tags.add(TPE1(text=[artist]))
            f.save()

        except MutagenError as e:
            print("!! Could not read file: {}".format(e))
            return False
        except AttributeError as e:
            print('!! No tags found: {}'.format(e))
            return False

        return True
