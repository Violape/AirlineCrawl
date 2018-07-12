import urllib.request
from bs4 import BeautifulSoup
def deparr(string,lb1,rb1,lb2,rb2):
    index1 = string.find(lb1)
    index2 = string.find(rb1)
    solut1 = string[index1+len(lb1):index2-1].strip()
    string = string[index2-1:]
    index1 = string.find(lb2)
    index2 = string.find(rb2)
    solut2 = string[index1+len(lb2):index2-1].strip()
    return solut1 + ',' + solut2
inpath = 'aprs.txt'
infile = open(inpath,'r')
aprs = infile.readline().strip()
while(aprs != ''):
    for page in range(100):
        url = r'http://flights.ctrip.com/schedule/'+ aprs +'-outmap-'+str(page+1)+'.html'
        html = urllib.request.urlopen(url).read().decode('gbk')
        soup   = BeautifulSoup(html)
        table  = soup.find_all('table')
        trs    = table[0].find_all('tr')
        pgdata = []
        for i, tline in enumerate(trs):
            if(i==0):
                continue;
            tds    = tline.find_all('td')
            deparrt= deparr(str(tds[1]),'>','<br/>','>','</td>')+','
            deparra= deparr(str(tds[2]),'>','<br/>','>','</td>')
            icons  = tds[4].find_all('i')
            weekava= ','
            for i in range(7):
                if(str(icons[i]).find('none')==-1):
                    weekava += '1,'
                else:
                    weekava += '0,'
            flinum = deparr(str(tds[6]),'>','<br/>','">','</a>')
            airline= deparrt+deparra+weekava+flinum
            pgdata.append(airline)
        if(len(pgdata)==0):
            break
        outpath = 'Result.txt'
        outfile = open(outpath, 'a', encoding='gb18030',errors='ignore')
        for i in range(len(pgdata)):
            print(pgdata[i],file=outfile)
        print("Airport "+ aprs +" page "+str(page+1)+" completed.")
    aprs = infile.readline().strip()
