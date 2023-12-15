from bs4 import BeautifulSoup as Soup
from bs4 import NavigableString
from git.repo import Repo

import os
with open("blank.html") as file:
    htmlFile = file.read()
    soup = Soup(htmlFile, 'html.parser')
    div = soup.find(id='list')
    for file in os.listdir('./pdf/'):
        if os.path.isfile(os.path.join('./pdf/', file)):
            aTag = soup.new_tag('a')
            aTag['href'] = "./pdf/" + file
            aTag['target'] = '_blank'
            aTag.insert(0, NavigableString(file))
            div.append(aTag)
            copyBtn = soup.new_tag('button')
            copyBtn['onclick'] = 'copyText("'+file+'")'
            copyBtn.insert(0, NavigableString("Copy path to clipboard"))
            div.append(copyBtn)
            div.append(soup.new_tag('br'))
    with open("index.html", "w") as file:
        file.write(str(soup.prettify()))