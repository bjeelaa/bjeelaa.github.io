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
            div.append(soup.new_tag('br'))
    with open("index.html", "w") as file:
        file.write(str(soup))

repo = Repo('./')
files = ['./index.html']
for file in os.listdir('./pdf/'):
    if os.path.isfile(os.path.join('./pdf/', file)):
        files.append('./pdf'+file)
repo.index.add(files)
repo.index.commit('new pdf files')

origin = repo.remotes[0]
origin.push()