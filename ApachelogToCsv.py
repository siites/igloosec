# -*- coding: cp949 -*-
from __future__ import division
import re
import time
import sys
import os
import glob

folder =""

def searchFolder(dir,patternStr):
    retlist = glob.glob(os.path.join(dir, patternStr))
    return retlist

class Check():
    def __init__(self, gotext):
            self.gotext = gotext
            self.result_arrry =[]

    def checkList(self):
            gotext = self.gotext.split('\n')
            goarray = []
            title = ["ip", "date","request","user agent"]
            goarray.append(title)

            for goline in gotext:
                rawdata1 = goline.split(" - - [")
                ipaddr = rawdata1[0]
                rawdata2 = rawdata1[1].split("]")
                datetime = rawdata2[0]
                rawdata3 = rawdata2[1].split('"-"')
                wrequest= rawdata3[0].replace('"', "")
                userAgent = rawdata3[1].replace('"', "")
                temparray =[ipaddr, datetime, wrequest, userAgent]
                goarray.append(temparray)

            return goarray


def fileopen(filename):
    text =""
    print filename
    try:
        with open(filename, "r") as f:
            text = f.read()
            f.close()
    except Exception as inst:
        print "file retry error:" + str(inst)
    return text

def main():
    try:
        folder = str(sys.argv[1])
    except:
        print '사용법: 폴더명 '
        print "ApacheToCsv.py config"
        exit(-1)
    try:
        result = searchFolder(folder,'*.*')
        try:
            with open("result.csv", "wb") as f:
                for fn in result:
                    ftxt = fileopen(fn)
                    dataparser= Check(ftxt)
                    dataArr = dataparser.checkList()

                    for gorata in dataArr:
                        f.write(gorata[0]+", " +gorata[1]+", "+gorata[2] +", "+gorata[3]+"\n")
            print "\nCreate Csv File!!!"
        except Exception as inst:
            print  str(inst.args)
            pass

    except IOError:
        print 'no such directory'
        exit(-1)

if __name__ == '__main__':
    main()
