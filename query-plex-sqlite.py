import urllib2
import xml.etree.ElementTree as ET
import os

plex_url =
plex_token_qs =

api_string = '/library/sections/'
api_call = '%s%s%s' % (plex_url, api_string, plex_token_qs)

content = urllib2.urlopen(api_call).read()
root = ET.fromstring(content)

movie_title_list = []
movie_line = []

f = open('text.csv', 'w' )

for child in root:
    plex_section_num = child.get('key')
    api_string_sections = '/library/sections/' + plex_section_num + '/all'
    api_call = '%s%s%s' % (plex_url, api_string_sections, plex_token_qs)

    content = urllib2.urlopen(api_call).read()

    root = ET.fromstring(content)

    i = 0

    movie_header = ','.join(["movie_ID","movie_key","movie_title","movie_year","movie_rating","movie_duration"]).encode('utf-8').strip()
    f.write(movie_header + '\n')

    for Video in root.iter('Video'):
        i += 1
        movie_ID = str(i)
        movie_sectionID = Video.get('librarySectionID') if Video.get('librarySectionID') is not None else ''
        movie_title = Video.get('title')
        movie_year = Video.get('year') if Video.get('year') is not None else ''
        movie_rating = Video.get('contentRating') if Video.get('contentRating') is not None else ''
        movie_duration = Video.get('duration') if Video.get('duration') is not None else ''

        movie_key = movie_title + '_' + movie_year
        movie_line = '"' + '","'.join([movie_ID,movie_key,movie_title,movie_year,movie_rating,movie_duration]).encode('utf-8').strip() + '"'
        f.write(movie_line + '\n')

f.close()