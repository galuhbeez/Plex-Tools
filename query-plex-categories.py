import urllib2
import xml.etree.ElementTree as ET

plex_url = 
plex_token_qs = 

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
