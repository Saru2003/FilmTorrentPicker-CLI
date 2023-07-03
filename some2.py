import requests
from bs4 import BeautifulSoup
import re
import sys
from pprint import pprint
def main():
    p=sys.argv[1].split()
    # print(p)
    l=""
    for i in range(len(p)):
        l+=p[i]
        if(i!=len(p)-1):
            l+="%20"
    url = f"https://knaben.eu/search/{l}/0/1/seeders"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    tde=soup.find_all('td',{'class':'text-wrap w-100'})
    file_sizes=[td.find_next('td').text.strip() for td in tde]
    # print(file_sizes)

    t=soup.find_all("td",class_="text-wrap w-100")
    t2=soup.find_all("td",class_="d-sm-none d-xl-table-cell")

    link=[]
    src=[]
    title=[]
    magnet=[]
    for I in t2:
        A=I.find_all("a")
        for J in A:
            H=J.get("href")
            # print(J.text)
            link.append(H)
            src.append(J.text)
    for i in t:
        a=i.find_all("a")
        for j in a:
            h=j.get("href")
            t=j.get("title")
            # print(t,h)
            # print("\n")
            title.append(t)
            magnet.append(h)
    f=[]
    arr=[]
    # y=len(title)
    for i in range(len(title)):
            f.append(title[i]+'\t['+src[i]+']['+file_sizes[i]+']')
        # print(title[i],link[i],src[i],magnet[i],file_sizes[i])
        # print("\n")
            if src[i] in ('1337x',"RuTracker"):
                # print('j')
                # print(src[i]+' '+magnet[i])
                try:
                    link_=magnet[i]
                    response_=requests.get(link_)
                    soup_=BeautifulSoup(response_.content,'html.parser')
                    magnet_link = soup_.find('a', {'id': 'dl'})['href']

                    # print(magnet_link)
                except Exception as e:
                    d=str(e)
                    # print(e)
                    try:
                        magnet_link = re.search(r"magnet:\?[^']+", d).group()
                        magnet[i]=magnet_link
                        # print(src[i]+' '+magnet[i])          
                        # print()
                    except:
                        magnet[i]="no"
                        arr.append(i)
                        
            # print(src[i]+' '+magnet[i])
            # print(title[i]+'\t['+src[i]+']['+file_sizes[i]+']')

    # for i in range(len(arr)):
    #     magnet.pop(arr[i])
    #     f.pop(arr[i])

    # for i in range(len(f)):
    #     print(f[i]+'\n'+magnet[i]+'\n'+'\n')
    # output = ','.join(map(str, f)) + ';' + ','.join(magnet)
    # print(output)
    output = ';'.join([','.join(map(str, f)), ','.join(magnet)])
    print(output)

if __name__=="__main__":
    main()
