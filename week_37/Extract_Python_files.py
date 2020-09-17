import sys
import os
import subprocess
from zipfile import ZipFile


def main(argv):
    input_check(argv)

    # A
    # list all files in folder
    x = os.listdir(argv[1])

    # list all .py files
    pyfiles = [i for i in x if i[-3:] == '.py']

    # create new dir
    os.mkdir(argv[3])

    # copy all files in list --todir
    for i in pyfiles:
        subprocess.run(['cp', i, argv[3]])

    # B
    with ZipFile(argv[3] + '/archive.zip', 'w') as zf:
        for file in pyfiles:
            zf.write(file)


def input_check(argv):
    if len(argv) < 2:
        print('Usage: python extract.py [.] [--todir <<tmp/>>] {--zip <<filename.zip>>}')
        sys.exit()
    if len(argv) == 3 and argv[2] != '--todir':
        print('Usage: python extract.py [.] [--todir <<tmp/>>] {--zip <<filename.zip>>}')
        sys.exit()


main(sys.argv)