from bs4 import BeautifulSoup as Soup
from bs4 import NavigableString

import os
with open("blank.html") as file:
    htmlFile = file.read()
    soup = Soup(htmlFile, 'html.parser')
    for file in os.listdir('./pdf/'):
        if os.path.isfile(os.path.join('./pdf/', file)):
            aTag = soup.new_tag('a')
            aTag['href'] = "./pdf/" + file
            aTag['target'] = '_blank'
            if file[:6] == "bzh - ":
                div = soup.find(id='list2')
                file = file[6:]
            else: div = soup.find(id='list')
            aTag.insert(0, NavigableString(file))
            div.append(aTag)
            div.append(soup.new_tag('br'))
    with open("index.html", "w") as file:
        file.write(str(soup.prettify()))