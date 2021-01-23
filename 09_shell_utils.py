import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

filepath = 'tmp_files/first.txt'

def main():
    if path.exists(filepath):
        src = path.realpath(filepath)

        #make a copy of a file
        dst = src + '.bak'
        shutil.copy(src, dst)
        #copy metadata
        shutil.copystat(src, dst)

        #rename file
        #new_file_path = 'tmp_files/first.txt'
        #os.rename(filepath, new_file_path)

        #root_dir, tail = path.split(src)
        #shutil.make_archive('archive', 'zip', root_dir)

        with ZipFile('tmp_files/archive.zip', 'w') as newzip:
            newzip.write('tmp_files/first.txt')
            newzip.close()


main()