import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse('tmp_files/samplexml.xml')

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName('skill')
    print('%d skills: ' % skills.length)

    for skill in skills:
        print(skill.getAttribute('name'))

main()