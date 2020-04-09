
import os
import urllib
import requests
from bs4 import BeautifulSoup

    
def dork():


    f = input(" Enter Dork: ")
    page = 1

    PageDepth = int(input('How many pages to scrape? '))
    for dork in f:
        if dork == "":
            continue
        for k in range(0, PageDepth):
            bingurl = "https://www.bing.com/search?q=" + dork +"&first=" + str(page) + "&FORM=PERE"
            page += 10
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
            try:
                pageSource = requests.get(bingurl, headers=headers).text
            except requests.exceptions.HTTPError:
                continuecontinue
            except requests.exceptions.ConnectionError:
                continue
            except requests.exceptions.Timeout:
                continue
            da = pageSource.split('<li class="b_algo"><h2><a href="')
            domains = []
            for i in range(0, 10):
                try:
                    domains.append(da[i+1].split('"')[0])
                except:
                    pass
            for l in domains:
                open('ALL_Result.txt', 'a+').close()
                l = l.split('/')
                l = l[0] + '//' + l[1] + l[2]
                if l not in open('ALL_Result.txt', 'r').read():
                    open('ALL_Result.txt', 'a+').write(l + '\n')
                    print(l)
    print("SAved To All_Result.txt !!")

def loaddork():
    import requests
    f = open("dork.txt", "r").read().split("\n")
    page = 1
    PageDepth = int(input('How many pages to scrape? '))
    for dork in f:
        if dork == "":
            continue
        for k in range(0, PageDepth):
            bingurl = "https://www.bing.com/search?q=" + dork +"&first=" + str(page) + "&FORM=PERE"
            page += 10
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
            try:
                pageSource = requests.get(bingurl, headers=headers).text
            except requests.exceptions.HTTPError:
                continuecontinue
            except requests.exceptions.ConnectionError:
                continue
            except requests.exceptions.Timeout:
                continue
            da = pageSource.split('<li class="b_algo"><h2><a href="')
            domains = []
            for i in range(0, 10):
                try:
                    domains.append(da[i+1].split('"')[0])
                except:
                    pass
            for l in domains:
                open('Load_dork.txt', 'a+').close()
                l = l.split('/')
                l = l[0] + '//' + l[1] + l[2]
                if l not in open('Load_dork.txt', 'r').read():
                    open('Load_dork.txt', 'a+').write(l + '\n')
                    print(l)
    print("saved to Load_dork.txt!!")
               
while True:
    print()
    print('''<=============== DORKER BY DIBO237# V 1.1 ================>

MAke YOUr SeleCtIonS:
              ''')
    
    print('''              1.Search For Dork.
              2.Check dork.txt
              3.Load from dork.txt
              4.Clear Entries.
              5.Exit. ''')
              
    print()
    select= input("Enter The NUmber: ")      
    
              


    def clearlist():
        open("ALL_Result.txt", "w").close()
        print("LIst Has Been Cleared !!!")
        
    if select=='1':
        dork()
    elif select=='2':
         file1 = open("dork.txt","r")
         print(file1.read())
    elif select=='3':
         loaddork()
    elif select=='4':   
         clearlist()
    elif select=='5':
         exit() 
    else:
        print("Invalid INPut")
        exit()

