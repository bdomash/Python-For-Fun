'''
Created on Sep 23, 2016

@author: Brandon
'''
"""
import urllib2
response = urllib2.urlopen('https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC')
html = response.read()
print html
"""
import urllib
import datetime

dow = "https://finance.yahoo.com/quote/%5EDJI?ltr=1"
sp ="https://finance.yahoo.com/quote/%5EGSPC?ltr=1"
vix = "https://finance.yahoo.com/quote/%5EVIX?ltr=1"
ust = "https://finance.yahoo.com/quote/%5ETNX"
snuff = "https://finance.yahoo.com/quote/RAI?p=RAI"
key = {dow:"Dow Jones",sp:"S&P 500",vix:"Vix Index", ust:"US Treasurey"}
#open = {dow:18279.6,sp:2164.33,vix:13.75,ust:1.6}
digits = {dow:5,sp:4,vix:2,ust:2}
arr = [dow, sp, vix,ust] #dow jones, s&p 500, vix index, us treasury 10 yr index
close = []
open = []
for stock in arr:
    day = datetime.datetime.today().weekday()
    dayWord = "night" ###changed from "night"
    if day == 0:
        dayWord = "Friday"
    link = stock
    f = urllib.urlopen(link)
    myfile = f.read()
    #print myfile
    indexOpen = myfile.index("regularMarketOpen")
    indexClose = myfile.index("previousClose")
    subOpen = myfile[indexOpen:len(myfile)]
    subClose = myfile[indexClose:len(myfile)]
    #print sub
    #openNum = float(subOpen[26:26+3+digits[stock]])
    #closeNum = float(subClose[22:22+3+digits[stock]])
    openNum = float(subOpen[26: subOpen.index(",")]) ###coment this in
    closeNum = float(subClose[22:subClose.index(",")])
    open.append(openNum)
    close.append(closeNum)
    change = openNum - closeNum 
    up = change > 0   
    percent = change/closeNum
    print "%s opened this morning at: %s" % (key[stock], round(openNum,3))
    print "%s closed last %s at: %s" % (key[stock], dayWord, round(closeNum,3))
    if up:
        print "Up %s (%s percent)" % (round(change,3),100*round(percent,3))
    else:
        print "Down %s (%s percent)" % (-1*round(change,3), -100*round(percent,3))
    print


        