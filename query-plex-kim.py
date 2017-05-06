import urllib2
import xml.etree.ElementTree as ET
import os

movie_input = raw_input("Enter movie title: ")

plex_url =
plex_token_qs =

api_string = '/library/sections/'
api_call = '%s%s%s' % (plex_url, api_string, plex_token_qs)

# print ('Calling %s' % (api_call))

content = urllib2.urlopen(api_call).read()
root = ET.fromstring(content)

movie_title_list = []

for child in root:
    plex_section_num = child.get('key')
    api_string_sections = '/library/sections/' + plex_section_num + '/all'
    api_call = '%s%s%s' % (plex_url, api_string_sections, plex_token_qs)

    content = urllib2.urlopen(api_call).read()

    root = ET.fromstring(content)

    for Video in root.iter('Video'):
        movie_title = Video.get('title')
        movie_title_list.append(movie_title)
        #print movie_title

# print movie_title_list
movie_list = str(movie_title_list)

f = open('text.txt', 'w' )
f.write(movie_list)
f.close()

movie_search = movie_input
if movie_search in open('text.txt').read():
    print "save your money"
else:
    print "buy that shit!"

#os.remove("text.txt")


#    print movie_titles

#     plex_titles = child.get('title')
#     print plex_titles

# for Video in root.iter('Video'):
#     movie_title = Video.get('title')
#     print movie_title

# root[0][1]





#print root.attrib





#print content

# f = open('text.txt', 'w' )
# f.write(content)
# f.close()

