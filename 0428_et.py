import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()
print(root)
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

#print([elem.tag for elem in root.iter()])

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib, movie.text)

for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf)
b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)

for movie in root.findall("./genre/decade/movie"):
    print(movie.attrib)

tree.write("movies.xml")

for movie in root.iter('movie'): # this is a second way
    print(movie.attrib, movie.text)