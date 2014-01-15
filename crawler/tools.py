from bs4 import BeautifulSoup
from urllib import request
from queue import Queue
import json
import os

MAX_CRAWLED = 6
START_LINK = "http://en.wikipedia.org/wiki/Information_retrieval"
LINK_PREFIX = "http://en.wikipedia.org"


def crawler():
    links_viewed = []
    result = {}
    result['content'] = []
    linkqueue = Queue(MAX_CRAWLED*10)
    linkqueue.put(START_LINK)
    counter = 0
    while counter < MAX_CRAWLED and linkqueue.qsize() > 0:
        try:
            newLink = linkqueue.get()
            if newLink in links_viewed:
                continue
            links_viewed.append(newLink)
            new_result = pageParser(newLink)
        except Exception:
            print ("some error happend during fetching a link here")
            continue
        result['content'].append(new_result)
        counter = counter + 1
        for link in new_result['links']:
            linkqueue.put(LINK_PREFIX + link)
    for resulttemp in result['content']:
        print("url: ",resulttemp['url'])
    print (" finished fetching ",counter,"pages.")
    variable = json.dumps(result)
    file = open("tempFile" , 'w')
    file.write(variable)

def getLink( url ):
    handle = request.urlopen(url)
    content = handle.read()
    print ("got the ",url," correctly")
    return content

def pageParser (url):
    content = getLink(url)
    soup = BeautifulSoup(content)
    result = {}
    result['url'] = url
    result['title'] = soup.find(id="firstHeading").string
    result['body'] = str(soup.find(id="mw-content-text"))
    # print("body is " , result['body'])
    # result["title"] = soup.title.string.split(" - Wikipedia")[0]
    links = soup.find(id="mw-content-text").find_all("a")
    result['links'] = []
    for link in links:
        href = link.get("href")
        if link.get("href").startswith("/wiki/") and ('#' not in href) and '.' not in href and ':' not in href:
            # print( link.get("href"))
            result['links'].append(link.get('href'))
    result['links'] = result['links'][0:5]
    print ("links exracted ", result['links'])
    return result

if __name__ == "__main__":
    # print ("content: ",getLink(START_LINK))
    # crawler()
    os.system("java -jar /home/roohy/Desktop/haha.jar index /home/roohy/PycharmProjects/MirFinal/crawler/tempFile")
    os.system("java -jar /home/roohy/Desktop/haha.jar search /home/roohy/PycharmProjects/MirFinal/crawler/indexDIR information retrieval")
    # os.system("javac /home/roohy/workspace/'pa2 (copy)'/src/main/java/edu/sharif/ce/fall92/mir/pa2/base/EntryPoint.java")
    # /home/roohy/workspace/pa2 (copy)/target/classes/edu/sharif/ce/fall92/mir/pa2/base