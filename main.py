import requests
import random
import re
import os


def getRandomImage(amountOfImages=1, download=False, printOutput=True):
    allitems = []
    listOfImages = getRandomPage(amountOfImages // 50 + 1, download, printOutput)
    for turn in range(1, amountOfImages + 1):
        choise = random.choice(listOfImages)
        allitems.append(choise)
        listOfImages.remove(choise)

    return allitems


def getRandomPage(amountOfPages=1, download=False, printOutput=True):
    allitems = []
    if printOutput:
        print(f"Getting amount of pages on site...")
    response = requests.get(url="https://www.airplane-pictures.net/search.php?p=737%20700&pg=1&order=screen_timestamp")
    lastPage = re.findall("<td>Page 1 of (.*)</td>", response.text)

    for turn in range(1, amountOfPages + 1):
        randPage = random.randrange(1, int(lastPage[0]))
        if printOutput:
            print(f"Scraping page {randPage}")
        response = requests.get(
            url=f"https://www.airplane-pictures.net/search.php?p=737%20700&pg={page}order=screen_timestamp")
        items = re.findall("<img src='(.*)' alt=\".*\" title=\"(.*)\">", response.text)

        for item in items:
            allitems.append(item)

    if download:
        if not os.path.exists(os.path.join(os.getcwd(), "images")):
            os.mkdir(os.path.join(os.getcwd(), "images"))
        curimage = 1
        for item in allitems:
            if printOutput:
                print(f"Saving image {curimage} / {len(allitems)}")
            curimage += 1
            image = requests.get(url=item[0])
            imagename = "".join(x for x in item[1] if (x.isalnum() or x in "._- "))
            with open("./images/" + imagename + ".png", 'wb') as f:
                f.write(image.content)

    return allitems


def getTopPages(amountOfPages=1, download=False, printOutput=True):
    allitems = []

    for page in range(1, amountOfPages + 1):
        if printOutput:
            print(f"Scraping page {page}...")
        response = requests.get(
            url=f"https://www.airplane-pictures.net/search.php?p=737%20700&pg={page}order=screen_timestamp")

        items = re.findall("<img src='(.*)' alt=\".*\" title=\"(.*)\">", response.text)

        for item in items:
            allitems.append(item)

    if download:
        if not os.path.exists(os.path.join(os.getcwd(), "images")):
            os.mkdir(os.path.join(os.getcwd(), "images"))
        curimage = 1
        for item in allitems:
            if printOutput:
                print(f"Saving image {curimage} / {len(allitems)}")
            curimage += 1
            image = requests.get(url=item[0])
            imagename = "".join(x for x in item[1] if (x.isalnum() or x in "._- "))
            with open("./737_700/" + imagename + ".png", 'wb') as f:
                f.write(image.content)
    return allitems

AmountOfPages=50
Download=1
PrintOutput=1
getTopPages(AmountOfPages, Download, PrintOutput)


###  https://www.airplane-pictures.net/search.php?p=737+800&Submit=Search
###  https://www.airplane-pictures.net/search.php?p=737%20800&pg=2&order=screen_timestamp
###  https://www.airplane-pictures.net/search.php?p=737%20800&pg=1&order=screen_timestamp