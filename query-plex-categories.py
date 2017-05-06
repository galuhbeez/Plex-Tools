import urllib2
import xml.etree.ElementTree as ET

plex_url = 'https://192-168-1-100.719f48b741ac4819b5447f3317d3cb23.plex.direct:32400'
plex_token_qs = '?X-Plex-Token=A6zyxRgkb4hpcXENw4Pb'

api_string = '/library/sections/'
#api_string = '/library/sections/5/all'

api_call = '%s%s%s' % (plex_url, api_string, plex_token_qs)

print ('Calling %s' % (api_call))

content = urllib2.urlopen(api_call).read()
#
root = ET.fromstring(content)

for child in root:
    plex_titles = child.get('title')
    print plex_titles


#     print child.tag, child.attrib

#for Part in root.iter('Part'):
    # print Part.attrib
#print child.tag, child.attrib



#root[1][1]





# print root.attrib





# print content

# f = open('text.txt', 'w' )
# f.write(content)
# f.close()