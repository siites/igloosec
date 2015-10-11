#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import os

headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
          'Accept-Encoding': ' gzip,deflate,sdch',
          'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
          'Content-type': 'text/html; charset=EUC-KR',
          'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

 
def webpageLoad(hosturl):
        try:
            req = urllib2.Request(hosturl)
            req.addheaders = headers
            url = urllib2.urlopen(req, timeout=30)
            savedata = url.read()  
            soup = BeautifulSoup(savedata, from_encoding="euc-kr")
            saveURL = replaceName(hosturl)

            creatFolder(saveURL)
            creatFolder(saveURL +"\\img")
            creatFolder(saveURL +"\\href")
            saveFile(savedata, "index.html", saveURL)

            hrefarr = soup.findAll('a', href=True)
            for link in hrefarr:
                filesave(hosturl+"/"+str(link['href']), saveURL +"\\href")

            imgsrc = soup.findAll('img')
            for img in imgsrc:
                filesave(hosturl+"/"+str(img['src']), saveURL +"\\img")

            print "Save Site:"+hosturl

        except Exception as inst:
            print inst
            pass
        finally:
            url.close()

def creatFolder(fname):
        if os.path.exists(fname) :
           pass
        else :
           os.makedirs(fname)

def filesave(filename, savedir):
        try:
                savedata = goData(filename)
                filename = replaceName(filename)
                saveFile(savedata, filename, savedir)
        except:
                pass
def replaceName(fname):
        filename = fname.replace("http://", "")
        filename = filename.replace("/", "-")
        filename = filename.replace("?", "-")
        filename = filename.replace(":", "-")
        filename = filename.replace("=", "-")
        filename = filename.replace("&", "-")
        return filename
        
def goData(filename):
        try:
            print filename
            req = urllib2.Request(filename)
            req.addheaders = headers
            url = urllib2.urlopen(req, timeout=30)
            savedata = url.read()
            return savedata
        except:
            pass
        finally:
            url.close()
            
           
def saveFile(savedata, filename, saveURL):
    try:
        savedata = str(savedata)
        filename = str(filename)
        with open(saveURL+"\\"+filename,'wb') as f:
          f.write(savedata)
          f.close()
    except Exception as inst:
        print inst
        pass

def main():
        domain = raw_input("Target Domain Adress (http://www.example.com): ")
        if domain !="":
           webpageLoad(domain)
        else:
           exit()

if __name__ == '__main__':
        main()
