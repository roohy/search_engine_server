from bs4 import BeautifulSoup
from urllib import request
from queue import Queue
from crawler.pageRank import ranks
import json
import os
import crawler.localConf as configs
from subprocess import Popen,PIPE

MAX_CRAWLED = 6
START_LINK = "http://en.wikipedia.org/wiki/Information_retrieval"
LINK_PREFIX = "http://en.wikipedia.org"


def crawler(start_link = START_LINK , max_crawled = MAX_CRAWLED):
    links_viewed = []
    result = {}
    result['content'] = []
    linkqueue = Queue(max_crawled*10)
    linkqueue.put(start_link)
    counter = 0
    while counter < max_crawled and linkqueue.qsize() > 0:
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
            link = LINK_PREFIX + link
    result = updateRanks(result)

    print (" finished fetching ",counter,"pages.")
    variable = json.dumps(result)
    file = open(configs.JSON_DIR , 'w')
    file.write(variable)

def updateRanks(results):
    vector = ranks(results['content'],0.1)
    for i in range(0,len(results['content'])):
        results['content'][i]['rank'] = vector[i]
    return results

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
    result['links'] = result['links'][0:min(10,len(result['links']))]
    print ("links exracted ", result['links'])
    return result
def indexJson():
    os.system("java -jar "+ configs.JARFILELOCATION +" index "+ configs.INDEX_DIR)

def search(query):
    process = Popen(['java','-jar',configs.JARFILELOCATION, 'search' ,configs.INDEX_DIR,query], stdout=PIPE)
    # process = Popen(['ls','-a'],stdout=PIPE)
    (output,error) = process.communicate()
    exit_code = process.wait()

    outputList = output.decode('utf-8').split('\n')
    firstResultIndex = 0
    print("output list ",outputList)
    for i in range(0,len(outputList)):
        firstResultIndex = i
        if "http://" in outputList[i]:
            break

    if firstResultIndex == len(outputList)-1:
        return None
    print(len(outputList)," ------ ",firstResultIndex)
    result = []
    while firstResultIndex < len(outputList)-1:
        temp = {}
        temp['url'] = outputList[firstResultIndex]
        temp['title'] = outputList[firstResultIndex+1]
        result.append(temp)
        # print ("item ",outputList[firstResultIndex], outputList[firstResultIndex+1])
        firstResultIndex += 2
    return result
    # os.system("java -jar /home/roohy/Desktop/haha.jar search /home/roohy/PycharmProjects/MirFinal/indexDIR "+query)

if __name__ == "__main__":
    # print ("content: ",getLink(START_LINK))
    # crawler()
    process = Popen(['java','-jar','/home/roohy/Desktop/haha.jar', 'search' ,'/home/roohy/PycharmProjects/MirFinal/indexDIR'," information"], stdout=PIPE)
    # process = Popen(['ls','-a'],stdout=PIPE)
    (output,error) = process.communicate()
    exit_code = process.wait()

    outputList = output.decode('utf-8').split('\n')
    firstResultIndex = 0
    for i in range(0,len(outputList)):
        firstResultIndex = i
        if "http://" in outputList[i]:
            break
    print(len(outputList)," ------ ",firstResultIndex)
    while firstResultIndex < len(outputList)-1:
        print ("item ",outputList[firstResultIndex], outputList[firstResultIndex+1])
        firstResultIndex += 2
    # os.system("java -jar /home/roohy/Desktop/haha.jar index /home/roohy/PycharmProjects/MirFinal/crawler/tempFile")
    # os.system("java -jar /home/roohy/Desktop/haha.jar search /home/roohy/PycharmProjects/MirFinal/crawler/indexDIR information retrieval")
    # os.system("javac /home/roohy/workspace/'pa2 (copy)'/src/main/java/edu/sharif/ce/fall92/mir/pa2/base/EntryPoint.java")
    # /home/roohy/workspace/pa2 (copy)/target/classes/edu/sharif/ce/fall92/mir/pa2/base'''