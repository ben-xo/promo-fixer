import os
import shlex
from filename_parser import FilenameParser






if __name__ == '__main__':

    # assess metadata from filename

    # convert to AIFF
    infile_escaped = shlex.quote(infile)
    outfile_escaped = shlex.quote(os.path.splitext(infile)[0] + '.aiff')
    os.system(f'ffmpeg -i {infile_escaped} {outfile_escaped}')

    # write tags to AIFF


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
