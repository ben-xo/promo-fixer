import os
import shlex
import argparse
from glob import glob

from filename_parser import FilenameParser
from filename_group_normaliser import FilenameGroupNormaliser
from tag_updater import TagUpdater


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert wavs into tagged aiffs by being clever.')
    parser.add_argument('--dir', help='location of wav files to fix', default='.')
    parser.add_argument('--dry-run', help="don't do it for real", action='store_true')

    args = parser.parse_args()
    os.chdir(args.dir)

    if args.dry_run:
        print("** dry-run **")

    # assess metadata from filename
    fnps = {}
    for wavfile in glob('*.wav'):
        filename_parser = FilenameParser(wavfile)
        if filename_parser.analyse():
            fnps[wavfile] = filename_parser
            print(f"Parsed  {wavfile}")
        else:
            print(f"Ignored {wavfile}")

    # make adjustments which can only be determined by looking at the files together
    normaliser = FilenameGroupNormaliser(fnps.values())
    normaliser.normalise()

    tagger = TagUpdater()

    for wavfile in fnps.keys():
        # convert to AIFF
        outfile = os.path.splitext(wavfile)[0] + '.aiff'

        if not args.dry_run:
            print(f"Encoding {wavfile} to {outfile}…")

            infile_escaped = shlex.quote(wavfile)
            outfile_escaped = shlex.quote(outfile)

            os.system(f'ffmpeg -i {infile_escaped} {outfile_escaped}')
        else:
            print(f"(--dry-run) would have encoded {wavfile} to {outfile}")

        # write tags to AIFF
        fnp = fnps[wavfile]
        print(f"Tagging {outfile} with artist='{fnp.artist}', title='{fnp.title}', album='{fnp.label}'")
        if not args.dry_run:
            tagger.update_tag(outfile, artist=fnp.artist, title=fnp.title, album=fnp.label)

        print("**")
        print("")
