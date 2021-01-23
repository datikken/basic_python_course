from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1

        print('Encountered attrs:', attrs)
        pos = self.getpos()
        print('\tAt line:', pos[0], 'position', pos[1])

        if attrs.__len__() > 0:
            for a in attrs:
                print('\t', a[0], "=", a[1])

    def handle_endtag(self, tag):
        pos = self.getpos()

        print('Encountered tag:', tag)
        print('\tAt line:', pos[0], 'position', pos[1])

    def handle_data(self, data):
        if (data.isspace()):
            return

        print('Encountered data:', data)
        pos = self.getpos()
        print('\tAt line:', pos[0], 'position', pos[1])

    def handle_comment(self, data):
        print('Encountered comment:', data)
        pos = self.getpos()
        print('\tAt line:', pos[0], 'position', pos[1])

def main():
    parser = MyHTMLParser()
    f = open('tmp_files/sample.html')
    if f.mode == 'r':
        contents = f.read()
        print(contents)

        parser.feed(contents)


main()
