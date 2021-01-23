from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
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