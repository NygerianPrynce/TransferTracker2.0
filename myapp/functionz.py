import requests
from bs4 import BeautifulSoup
import random
import re
import datetime
from . import transferObject
from . import playerSearchObject
from . import clubSearchObject
from . import leagueSearchObject

userAgents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15'
'Mozilla/5.0 (Windows NT 10.0; rv:114.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
'Mozilla/5.0 (Windows NT 10.0; rv:113.0) Gecko/20100101 Firefox/113.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.2.625 Yowser/2.5 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36']



# Fix the url to include the current date
def date_fix(url, today):    
    word1 = url.index("/plus")
    word2 = url.index("/datum")
    front = url[:word2+7]
    back = url[word1:]
    url = (front + str(today) + back)
    print(url)
    return url
#Find the max number of pages on the current date's page -- -1 if no pages(no transfers)
def findMaxPages(url):
    page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
    soup = BeautifulSoup(page.content, "html5lib")
    if ((soup.find("li", class_="tm-pagination__list-item tm-pagination__list-item--icon-last-page") == None) and (soup.find("tr", class_=["odd", "even"]))):
        return 1
    elif ((soup.find("li", class_="tm-pagination__list-item tm-pagination__list-item--icon-last-page") == None)):
        return -1
    a = soup.find("li", class_="tm-pagination__list-item tm-pagination__list-item--icon-last-page")
    b = a.find("a", title=re.compile("^(?!http).*"))
    sentence = b['title'] 
    word1 = sentence.index("(page ")
    word2 = sentence.index(")")
    num = int(sentence[word1+6:word2])
    return num 
#Create a list of all the transfers on the current date's page that apply to the users database       
def createTransfers(url, num, pId, clubId, leagueId):
    print("CREATING Transfers")
    print(pId)
    print(clubId)
    print(leagueId)
    print(url)
    print(num)
    transfers = []
    for x in range(num):
        #print("PAGE, ", x)
        pageIndex = url.index("page/")
        url = url[:pageIndex+5] + str(x+1)
        page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
        soup = BeautifulSoup(page.content, "html5lib")
        table = soup.find("table", class_="items")
        row = table.find_all("tr", class_=["odd", "even"])
        playerId = -1
        name = ""
        age = -1
        position = ""
        img = ""
        clubLeftName = ""
        clubLeftId = -1
        clubJoinedName = ""
        clubJoinedId = -1
        leagueLeftName = ""
        leagueLeftId = -1
        leagueJoinedName = ""
        leagueLeftId = -1
        leagueJoinedName = ""
        leagueJoinedId = -1
        fee = ""
        for x, r in enumerate(row):
            #print("LENGTH: ", len(row), "ROW NUMBER: ", x)
            col = r.find_all("td", recursive=False)
            prereqs = findPrereqs(col[0], col[3], col[4])
            toBeFound = False
            for p in pId:
                if(p == str(prereqs[0])):
                    toBeFound = True
                    print("FOUND PLAYER ID")
            for c in clubId:
                if(c == str(prereqs[1]) or c == str(prereqs[2])):
                    toBeFound = True
                    print("FOUND CLUB ID")
            for l in leagueId:
                if(l == str(prereqs[3]) or l == str(prereqs[4])):
                    toBeFound = True
                    print("FOUND LEAGUE ID")
            if(not toBeFound):
                continue
            for x in range(len(col)):
                #print("RUNINININININ")
                if(x+1 == 1):
                    player = findPlayer(col[x])
                    playerId = player[0]
                    name = player[1]
                    img = player[2]
                    position = player[3]
                    #print(playerId, name, img, position)
                if(x+1 == 2):
                    age = findAge(col[x])
                    #print(age)
                if(x+1 == 3):
                    clubLeft = findClub(col[x+1])
                    clubLeftId = clubLeft[0]
                    clubLeftName = clubLeft[1]
                    clubLeftImage = clubLeft[2]
                    leagueLeftName = clubLeft[3]
                    leagueLeftImg = clubLeft[4]
                    leagueLeftId = clubLeft[5]
                    #print(clubLeftId, clubLeftName, clubLeftImage, leagueLeftName, leagueLeftImg, leagueLeftId)
                if(x+1 == 4):
                    #replicate for clubJoined
                    clubJoined = findClub(col[x+1])
                    clubJoinedId = clubJoined[0]
                    clubJoinedName = clubJoined[1]
                    clubJoinedImage = clubJoined[2]
                    leagueJoinedName = clubJoined[3]
                    leagueJoinedImg = clubJoined[4]
                    leagueJoinedId = clubJoined[5]
                    #print(clubJoinedId, clubJoinedName, clubJoinedImage, leagueJoinedName, leagueJoinedImg, leagueJoinedId)
                if(x+1 == 5):
                    fee = findFee(col[x])
                    #print(fee)
            if(toBeFound):
                transfer = str(transferObject.transferObject(playerId, name, age, position, img, clubLeftName, clubLeftId, clubLeftImage, clubJoinedName, clubJoinedId, clubJoinedImage, leagueLeftName, leagueLeftId, leagueLeftImg, 
                                                         leagueJoinedName, leagueJoinedId, leagueJoinedImg, fee))
                transfers.append(transfer)    
    
    return transfers       

def findPrereqs(c1, c2, c3):
    #Player ID
    spot = str(c1.find("a")['href']).index("spieler/")
    pid = int((c1.find("a")['href'])[spot+8:])
    
    #Club1 ID
    if c2.find('a') and (("/startseite/") in str(c2.find('a')['href'])):
        key = str(c2.find('a')['href']).index("/verein/")
        cid1 = int(str(c2.find('a')['href'])[key+8:])
    else: 
        cid1 = -1
    
    #Club2 ID
    if c3.find('a') and (("/startseite/") in str(c3.find('a')['href'])):
        key = str(c3.find('a')['href']).index("/verein/")
        cid2 = int(str(c3.find('a')['href'])[key+8:])    
    else:
        cid2 = -1
        
    #League1 ID
    if(c2.findAll('td')[2].find('img')):
       if(c2.findAll('td')[2].find('a') == None):
            lid1 = c2.findAll('td')[2].text.strip()
       else:
            #print(c2.findAll('td')[2].find('a')['href'])
            key = str(c2.findAll('td')[2].find('a')['href']).index("bewerb/")
            lid1 = str(c2.findAll('td')[2].find('a')['href'])[key+7:]
    else:
        if((c2.find('td', class_='hauptlink').string) and ("Retired" in c2.find('td', class_='hauptlink').string)):
            lid1 = "Retired"
        else:
            lid1 = "NA"
        
    #League2 ID
    if(c3.findAll('td')[2].find('img')):
       if(c3.findAll('td')[2].find('a') == None):
            lid2 = c3.findAll('td')[2].text.strip()
       else:
            key = str(c3.findAll('td')[2].find('a')['href']).index("bewerb/")
            lid2 = str(c3.findAll('td')[2].find('a')['href'])[key+7:]
    else:
        if((c3.find('td', class_='hauptlink').string) and ("Retired" in c3.find('td', class_='hauptlink').string)):
            lid2 = "Retired"
        else:
            lid2 = "NA"
    #print("AND THE RESLT IS")
    #print(pid, cid1, cid2, lid1, lid2)
    return[pid, cid1, cid2, lid1, lid2]
    
def findPlayer(c):
    #print(c)
    img = c.find("img")['data-src']
    position = re.sub('-', ' ', c.findAll("tr")[1].find("td").string)
    link = c.find("a")
    key = str(link['href'])
    #print(key)
    front = key.index("spieler/")
    id = int(key[front+8:])
    #print(id, end="\n")
    return [id, link['title'], img, position]
     
def findAge(c):
    #print(c)
    if(c.string == "-"):
        return "-"
    elif(c.string == "N/A"):
        return "-"
    age = (c.string)
    return age

def findClub(c):
    leagueId = ""
    name = ""
    id = 0
    if(c.findAll('td')[2].find('img')):
        if(c.findAll('td')[2].find('a')):
            league = c.findAll('td')[2].find('a')['title']
        else:
            league = c.findAll('td')[2].find('img')['title']     
        leagueImg = c.findAll('td')[2].find('img')['src'] #change to big if needed
        if(c.findAll('td')[2].find('a') == None):
            leagueId = c.findAll('td')[2].text.strip()
        else:
            indx = c.findAll('td')[2].find('a')['href'].index("werb/")
            leagueId = c.findAll('td')[2].find('a')['href'][indx+5:]
    else:
        if((c.find('td', class_='hauptlink').string) and ("Retired" in c.find('td', class_='hauptlink').string)):
            league = "Retired"
            leagueImg = "Retired"
            name = "Retired"
            id = 0
            img = "https://tmssl.akamaized.net/images/wappen/big/123.png?lm=1456997286"
            leagueId = "Retired"
            return [id, name, img, league, leagueImg, leagueId]
        else:
            league = "NA"
            leagueImg = "NA"
            name = "NA"
            id = -1
            img = "https://tmssl.akamaized.net/images/wappen/big/515.png?lm=1456997255"
            leagueId = "NA"
            return [id, name, img, league, leagueImg, leagueId]
    tag = c.find('a')
    img = tag.find('img')['src'].replace("small", "big") #change to big if needed
    #print(img, league, leagueImg)
    if tag and (("/startseite/") in str(tag['href'])):
        key = str(tag['href'])
        front = key.index("/verein/")
        name = tag['title']
        id = int(key[front+8:])
        #print(tag['title'])
        #print(id)
    return [id, name, img, league, leagueImg, leagueId]

def findFee(c):
    fee = c.find('a').string
    if(fee == None):
        return "-"
    return fee

def findPlayerPS(c):
    img = str(c.find("img")['src']).replace("small", "big")
    club = re.sub('-', ' ', c.findAll("tr")[1].find("td").string)
    if club == "   ": 
        club = "No Longer Alive"
    clubID = 0
    if "Career break" in club:
        clubID = -1
    elif "Retired" not in club and "---" not in club:
        clubID = c.findAll("tr")[1].find("td").find("a")['href']
        front = clubID.index("/verein/")
        clubID = int(clubID[front+8:])
    else:
        clubID = -1
    link = c.findAll("a")[1]
    key = str(link['href'])
    #print(key)
    front = key.index("spieler/")
    id = int(key[front+8:])
    #print(id, end="\n")
    print(club, clubID)
    return [id, link['title'], img, club, clubID]
    #playerId - x, name - x, age, position, image - x, clubName - x, clubID, clubImage, nationality, marketValue

def findPositionPS(c):
    position = c.string
    return position

def findNationalityPS(c):
    if(c.find("img") == None):
        print("bang bang")
        return ["N/A", "https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=152069999"]
    elif c.find("br") == None:
        return [c.find("img")['title'], c.find("img")['src']] #name, img
    else:
        return [c.findAll("img")[0]['title'], c.findAll("img")[0]['src'], c.findAll("img")[1]['title'], c.findAll("img")[1]['src']] #name, img, name, img

def findMarketValuePS(c):
    mv = c.string
    return mv

def findSearchables(search):
    #players, clubs, leagues - represented as etiher 0 or 1
    x = 0
    searchables = [None, None, None]
    spots = [None, None, None]
    search = re.sub(' ', '+', search)
    url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?Spieler_page=1&ajax=yw0&query=" + search
    page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
    soup = BeautifulSoup(page.content, "html5lib")
    possibleTables = soup.findAll("div", class_="row")
    for x, p in enumerate(possibleTables):
        if(p.find("h2", class_="content-box-headline")):
            if("players" in p.find("h2").string):
                print("PLAYER TABLE FOUND")
                searchables[0] = p
                spots[0] = x
            elif("Clubs" in p.find("h2").string):
                print("CLUB TABLE FOUND")
                spots[1] = x
                searchables[1] = p
            elif("competitions" in p.find("h2").string):
                print("LEAGUE TABLE FOUND")
                spots[2] = x
                searchables[2] = p
                
    return [searchables, spots]

def findMaxPagesSearch(searchable):
    if (searchable.find("li", class_="tm-pagination__list-item tm-pagination__list-item--icon-last-page") == None):
        return -1
    a = searchable.find("li", class_="tm-pagination__list-item tm-pagination__list-item--icon-last-page")
    b = a.find("a", title=re.compile("^(?!http).*"))
    sentence = b['title'] 
    word1 = sentence.index("(page ")
    word2 = sentence.index(")")
    num = int(sentence[word1+6:word2])
    return num 

def executeSearchables(searchables, search):
    searchObjects = [None, None, None]
    if(searchables[0][0] != None):
        maxPages = findMaxPagesSearch(searchables[0][0])
        print("player search is being executed with ", maxPages, " pages")
        searchObjects[0] = playerSearch(search, maxPages, searchables[1][0])
    if(searchables[0][1] != None):
        maxPages = findMaxPagesSearch(searchables[0][1])
        print('club search is being executed with ', maxPages, "pages")
        searchObjects[1] = clubSearch(search, maxPages, searchables[1][1])
        #searches
    if(searchables[0][2] != None):
        maxPages = findMaxPagesSearch(searchables[0][2])
        print('league search is being executed with ', maxPages, " pages")
        searchObjects[2] = leagueSearch(search, maxPages, searchables[1][2])
        #searches
    return searchObjects
    
def playerSearch(search, maxPages, spot):
    searchResults = []
    search = re.sub(' ', '+', search)
    url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=aguero&Spieler_page=1"
    url = re.sub('aguero', search, url)
    page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
    soup = BeautifulSoup(page.content, "html5lib")
    if(maxPages != -1):
        for x in range(maxPages):
            urlz = re.sub('1', str(x+1), url)
            print(urlz)
            page = requests.get(urlz, headers={'User-Agent': random.choice(userAgents)})
            soup = BeautifulSoup(page.content, "html5lib")
            table = soup.findAll("table", class_="items")[spot]
            row = table.find_all("tr", class_=["odd", "even"])
            for r in row:
                col = r.find_all("td", recursive=False)
                playerInfo = findPlayerPS(col[0])
                #print(playerInfo) #id, name, img, club, clubId
                age = findAge(col[3]) #age
                position = findPositionPS(col[1])#position
                findClubImg = col[2].find("img")['src'] #clubImg
                nationality = findNationalityPS(col[4]) #nationality
                marketValue = findMarketValuePS(col[5]) #marketValue
                searchResults.append(str(playerSearchObject.playerSearchObject(playerInfo[0], playerInfo[1], age, position, playerInfo[2], playerInfo[3], playerInfo[4], findClubImg, nationality,marketValue)))
                #playerId - x, name - x, age - x, position, image - x, clubName - x, clubID - x, clubImage, nationality, marketValue
    elif(soup.find("tr", class_=["odd", "even"])):
        table = soup.find_all("table", class_="items")[spot]
        row = table.find_all("tr", class_=["odd", "even"])
        for x, r in enumerate(row):
            col = r.find_all("td", recursive=False)
            print(col[0])
            playerInfo = findPlayerPS(col[0])
            
            #print(playerInfo) #id, name, img, club, clubId
            age = findAge(col[3]) #age
            
            position = findPositionPS(col[1])#position
            print(x, "CHECK STOP")
            findClubImg = col[2].find("img")['src'] #clubImg
            nationality = findNationalityPS(col[4]) #nationality
            marketValue = findMarketValuePS(col[5]) #marketValue
            
            searchResults.append(str(playerSearchObject.playerSearchObject(playerInfo[0], playerInfo[1], age, position, playerInfo[2], playerInfo[3], playerInfo[4], findClubImg, nationality,marketValue)))
            
            #playerId - x, name - x, age - x, position, image - x, clubName - x, clubID - x, clubImage, nationality, marketValue
    else:
        print("No Results Found")
    return searchResults

def clubSearch(search, maxPages, spot):
    searchResults = []
    search = re.sub(' ', '+', search)
    url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=Real&Verein_page=1"
    url = re.sub('Real', search, url)
    page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
    soup = BeautifulSoup(page.content, "html5lib")
    if(maxPages != -1):
        for x in range(maxPages):
            urlz = re.sub('1', str(x+1), url)
            page = requests.get(urlz, headers={'User-Agent': random.choice(userAgents)})
            soup = BeautifulSoup(page.content, "html5lib")
            table = soup.findAll("table", class_="items")[spot]
            row = table.find_all("tr", class_=["odd", "even"])
            for r in row:
                col = r.find_all("td", recursive=False)
                image = col[0].find('img')['src'].replace("small", "big")
                id = col[1].find('a')['href'][(col[1].find('a')['href'].index("/verein/"))+8:]
                name = col[1].find('a')['title']
                nationality = [col[2].find('img')['alt'],col[2].find('img')['src']]
                marketValue = col[4].text
                searchResults.append(str(clubSearchObject.clubSearchObject(image, id, name, nationality, marketValue)))
    elif(soup.find("tr", class_=["odd", "even"])):
        table = soup.find_all("table", class_="items")[spot]
        row = table.find_all("tr", class_=["odd", "even"])
        for r in row:
            print(r)
            col = r.find_all("td", recursive=False)
            image = col[0].find('img')['src'].replace("small", "big")
            id = col[1].find('a')['href'][col[1].find('a')['href'].index("/verein/")+8:]
            name = col[1].find('a')['title']
            nationality = [col[2].find('img')['alt'],col[2].find('img')['src']]
            marketValue = col[4].text
            searchResults.append(str(clubSearchObject.clubSearchObject(image, id, name, nationality, marketValue)))
    else:
        print("No Results Found")
    return searchResults

def leagueSearch(search, maxPages, spot):
    searchResults = []
    search = re.sub(' ', '+', search)
    url = "https://www.transfermarkt.com//schnellsuche/ergebnis/schnellsuche?Spieler_page=1&ajax=yw3&query=Premier&Wettbewerb_page="
    url = re.sub('Premier', search, url)
    page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
    soup = BeautifulSoup(page.content, "html5lib")
    if(maxPages != -1):
        for x in range(maxPages):
            if(x!=0):
                url = url[:len(url)-1]
            url = url + str(x+1)
            page = requests.get(url, headers={'User-Agent': random.choice(userAgents)})
            soup = BeautifulSoup(page.content, "html5lib")
            table = soup.findAll("table", class_="items")[spot]
            row = table.find_all("tr", class_=["odd", "even"])
            for r in row:
                col = r.find_all("td", recursive=False)
                for c in col:
                    if("\xa0" in c.contents or c.contents == []):
                        c.contents = "-"
                if(col[0].contents != "-"):
                    image = col[0].find('img')['src'].replace("mediumsmall", "header")
                    print(image)
                else:
                    image = "-"
                id = col[1].find('a')['href'][col[1].find('a')['href'].index("bewerb/")+7:]
                name = col[1].find('a')['title']
                nationality = [col[2].find('img')['alt'],col[2].find('img')['src']]
                numOfTeams = col[3].contents
                numOfPlayers = col[4].contents
                marketValue = col[5].contents
                association = col[7].contents
                
                searchResults.append(str(leagueSearchObject.leagueSearchObject(image, id, name, nationality, numOfTeams, numOfPlayers, marketValue, association)))
                #self, image, id, name, nationality, clubNums, playerNums,  marketValue, association
    elif(soup.find("tr", class_=["odd", "even"])):
        table = soup.find_all("table", class_="items")[spot]
        row = table.find_all("tr", class_=["odd", "even"])
        for r in row:
            col = r.find_all("td", recursive=False)
            image = col[0].find('img')['src'].replace("mediumsmall", "header")
            print(image)
            id = col[1].find('a')['href'][col[1].find('a')['href'].index("bewerb/")+7:]
            name = col[1].find('a')['title']
            nationality = [col[2].find('img')['alt'],col[2].find('img')['src']]
            numOfTeams = col[3].text
            numOfPlayers = col[4].text
            marketValue = col[5].text
            association = col[7].text
            searchResults.append(str(leagueSearchObject.leagueSearchObject(image, id, name, nationality, numOfTeams, numOfPlayers, marketValue, association)))
    else:
        print("No Results Found")
    return searchResults

def findDailyTransfers(pIDs, cIDs, lIDs):
    today = datetime.datetime.now().date()
    print(today)
    URL = "https://www.transfermarkt.com/transfers/transfertagedetail/statistik/top/land_id_ab//land_id_zu//leihe//datum/2023-07-05/plus/1/galerie/0/page/1"
    URL = date_fix(URL, today)
    maxPages = findMaxPages(URL)
    if(maxPages != -1):
        return createTransfers(URL, maxPages, pIDs, cIDs, lIDs)
        #returns transfer item
                                  #playerId, ClubID, LeagueID
    else:
        return None

def findSearchedItem(search):
    return executeSearchables(findSearchables(search), search)
    #returns array of club, player, and league search objects





