import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)


main()

filepath = 'tmp_files/first.txt'

print('Item exists:' + str(path.exists(filepath)))
print('Item is a file:' + str(path.isfile(filepath)))
print('Item path:' + str(path.realpath(filepath)))

# get modification time
t = time.ctime(path.getmtime(filepath))
print('Modification time:', t)

td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
    path.getmtime(filepath)
)

print('It has been', td, 'since the file was modified')