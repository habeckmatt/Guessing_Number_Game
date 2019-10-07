import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.lyrics.com/lyric/818939/John+Lennon/Imagine'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

l = []
l.append(soup.find('pre', {'id': 'lyric-body-text'}).text)

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
constant_count = 0
for line in l:
    line = re.sub("\r\n",'. ',line.rstrip())
    for char in line:
        if char in vowels:
            vowel_count += 1
        else:
            constant_count += 1
print(vowel_count)
print(constant_count)






# r = requests.get('https://www.azlyrics.com/lyrics/johnlennon/imagine.html')


# # Create a BeautifulSoup object
# soup = BeautifulSoup(r.text, 'html.parser')

# # Pull all text from the BodyText div
# lyrics = soup.find(class_='container main-page')

# lyric_text1 = lyrics.find(class_='row')

# lyric_text2 = lyric_text1.find(class_='col-xs-12 col-lg-8 text-center')

# lyric_text3 = lyric_text2.find('div')

# lyric_text4 = lyric_text3.find('#text')

# print(lyric_text3)

# # lyric_items = lyrics.find(class_='spacer')

# # print(lyric_items)
# # # for lyric in lyric_items:
# # #     print(lyric.prettify())