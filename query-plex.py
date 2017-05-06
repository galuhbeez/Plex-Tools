import urllib2
import xml.etree.ElementTree as ET
import os

plex_url = 
plex_token_qs = 

#api_string = '/library/sections/'
api_string = '/library/sections/5/all'

api_call = '%s%s%s' % (plex_url, api_string, plex_token_qs)

#print ('Calling %s' % (api_call))

content = urllib2.urlopen(api_call).read()

# print content

# root = ET.fromstring(content)

# for Part in root.iter('Part'):
#     plex_titles = Part.get('file')
#     print plex_titles

# for Video in root.iter('Video'):
#     plex_titles = Video.get('title')
#     print plex_titles

f = open('text.txt', 'w' )
f.write(content)
f.close()

if 'Heat' in open('text.txt').read():
    print "save your money"
else:
    print "buy that shit!"

os.remove("text.txt")








# for Video in root.findall('Video'):
#     plex_titles = Video.find("title")
#     if plex_titles is None:
#         print "rad"
#     else:
#         print "save your money"



#hasattr('plex_titles', 'Heat')


# for child in root:
#     print child.tag, child.attrib


    # print Part.attrib
#print child.tag, child.attrib



#root[1][1]





# print root.attrib





#print content

# f = open('text.txt', 'w' )
# f.write(content)
# f.close()
