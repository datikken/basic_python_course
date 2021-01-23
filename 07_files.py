file = 'tmp_files/first.txt'

class Filer():
    def __init__(self, filepath):
        self.filepath = filepath

    def open_file(self, type="w+"):
        self.f = open(self.filepath, type)

    def write_to_file(self, msg):
        self.f.write(msg + "\r\n")

    def append_to_end_of_file(self):
        self.f = open(self.filepath, 'a')

    def read_file(self):
        self.open_file('r')
        content = self.f.read()
        print(content)

    def read_file_by_lines(self):
        self.open_file('r')

        content = self.f.readlines()
        for item in content:
            print(item)

    def close_file(self):
        self.f.close()


filer = Filer(file)
filer.open_file()

for i in range(10):
    filer.write_to_file('fuck' + str(i))

for i in range(3):
    filer.write_to_file('appendix' + str(i))


filer.close_file()
filer.read_file()
filer.read_file_by_lines()