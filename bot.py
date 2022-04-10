# coding: utf-8;
from tradingview_ta import TA_Handler, Interval, Exchange
import requests
from bs4 import BeautifulSoup
import time
import requests
from bs4 import BeautifulSoup
# coding: utf-8;
from tradingview_ta import TA_Handler, Interval, Exchange
from colorama import Fore, Back, Style
import time
import telegram
import telebot
from datetime import datetime
import decimal
import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json,time
import os



##############kripto_bora##############################################
#token = "1118153639:AAFJeUGi4WnWgzz2pVoGPGypAoQQKPGRLt0" #telegram token
#chat_id = "835942393" #telegram id
##############ROBOT BORA #################################################
#ROBOT BORA
token = "1001364876:AAFcONbKxMuw1Eo3HItNVjzIX5F-S-or1eY" #telegram token
chat_id = "835942393" #telegram id
##############ROBOT BORA #################################################
#TEST*TEST*TEST*TEST*TEST*TEST*
#token = "test:test-S-or1eY" #telegram token
#chat_id = "835942393" #telegram id
##########################################################################

s = requests.Session()

hidir = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
s.headers.update(hidir)


endex = "https://www.turkishbulls.com/SignalPage.aspx?lang=tr&Ticker=XU100"
r = s.get(endex)
soup = BeautifulSoup(r.content, "html.parser")
bul = soup.findAll("span",{"id":"MainContent_CompanyTicker"})[0]
bul1 = soup.findAll("span",{"id":"MainContent_LastPattern"})[0]
bul2 = soup.findAll("span",{"id":"MainContent_LastSignal"})[0]
bul3 = soup.findAll("span",{"id":"MainContent_LastClose"})[0]
bul4 = soup.findAll("span",{"id":"MainContent_ChangePercent"})[0]
print(" ",bul.text,end=" ",flush=True)
print("#",bul1.text,end="",flush=True)
print(" #",bul2.text,end=" #",flush=True)
print(" ₺",bul3.text,end=" ",flush=True)
print("(",bul4.text,end=")\n",flush=True)
xu100=(bul.text)+" "+(bul1.text)+" "+(bul2.text)+" "+(bul3.text)+" "+(bul4.text)
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': xu100}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': xu100}).json()
fiyat = "https://tr.tradingview.com/symbols/BIST-"+ bul.text +"/ideas/"
f = s.get(fiyat)
foup = BeautifulSoup(f.content, "html.parser")
fiyat = foup.findAll("p",{"class":"tv-widget-idea__description-row tv-widget-idea__description-row--clamped js-widget-idea__popup"})[0]
print(bul.text,":",fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
yorumlayici=(bul.text)+":"+(fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yorumlayici}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()


link = "https://www.turkishbulls.com/Default.aspx?lang=tr"
r = s.get(link)
soup = BeautifulSoup(r.content, "html.parser")
bul = soup.findAll("div",{"id":"MainContent_ASPxRoundPanel3_MarketCommentaryText"})[0]
print(" ",bul.text,flush=True)
durum=(bul.text)
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': durum}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': durum}).json()

link = "https://www.turkishbulls.com/Default.aspx?lang=tr"
r = s.get(link)
soup = BeautifulSoup(r.content, "html.parser")
bul = soup.findAll("div",{"id":"MainContent_ASPxRoundPanel2_ASPxCallbackPanel1_ChartTitle"})[0]
bul1 = soup.findAll("div",{"id":"MainContent_ASPxRoundPanel2_ASPxCallbackPanel1_CandleStickofTheDay"})[0]
print(" ",bul.text,flush=True)
print(" ",bul1.text,flush=True)
gununhissesi=(bul.text)+" "+(bul1.text)
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': gununhissesi}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': gununhissesi}).json()

resp = requests.get("https://hlyaos.halkyatirim.com.tr/PayTedbirleri/")
soup = BeautifulSoup(resp.content, "html.parser")
body = soup.findAll("tbody")[0]
trler = body.findAll("tr")
for tr in trler:
    tdler = tr.findAll("td")
    sembol = tdler[1].text.strip()
    bas = tdler[2].text
    bit = tdler[3].text
    gun = tdler[4].text
    tedbir = tdler[5].text.replace("*","").strip()

    print(f"\n{sembol}\nBaşlama tarihi: {bas}\nBitiş Tarihi: {bit}\nCeza Türü: {tedbir}\nCezanın bitmesine kalan gün : {gun}\n")
    cezali=(f"\n{sembol}\nBaşlama tarihi: {bas}\nBitiş Tarihi: {bit}\nCeza Türü: {tedbir}\nCezanın bitmesine kalan gün : {gun}\n")
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': cezali}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': cezali}).json()
    fiyat = "https://tr.tradingview.com/symbols/BIST-"+ sembol +"/ideas/"
    f = s.get(fiyat)
    foup = BeautifulSoup(f.content, "html.parser")
    fiyat = foup.findAll("p",{"class":"tv-widget-idea__description-row tv-widget-idea__description-row--clamped js-widget-idea__popup"})[0]
    print(sembol,":",fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
    yorumlayici=(sembol)+":"+(fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yorumlayici}).json()
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()

print("BİST YÜKSELENLER")
fiyat = "https://finans.mynet.com/borsa/seansistatistigi/"   
f = s.get(fiyat)
foup = BeautifulSoup(f.content, "html.parser")
artan = foup.findAll("table",{"class":"wfull table-data session-statistics"})[0]
print(artan.text.split()[4],
      artan.text.split()[8],
      artan.text.split()[12],
      artan.text.split()[20],
      artan.text.split()[24],
      artan.text.split()[32],
      artan.text.split()[40],
      artan.text.split()[48],
      artan.text.split()[56],
      artan.text.split()[64],
      artan.text.split()[72],
      artan.text.split()[80],
      artan.text.split()[88],
      artan.text.split()[96],
      artan.text.split()[104],
      artan.text.split()[112],
      artan.text.split()[120],
      artan.text.split()[128],
      artan.text.split()[136],
      artan.text.split()[144],
      artan.text.split()[152],
      artan.text.split()[160])
yukselenler=("Bist Yükselenler"+"\n"+artan.text.split()[4]+" "+artan.text.split()[8]+" "+artan.text.split()[12]+" "+artan.text.split()[20]+" "+artan.text.split()[24]+" "+artan.text.split()[32]+" "+artan.text.split()[40]+" "+artan.text.split()[48]+" "+artan.text.split()[56]+" "+artan.text.split()[64]+" "+artan.text.split()[72]+" "+artan.text.split()[80]+" "+artan.text.split()[88]+" "+artan.text.split()[96]+" "+artan.text.split()[104]+" "+artan.text.split()[112]+" "+artan.text.split()[120]+" "+artan.text.split()[128]+" "+artan.text.split()[136]+" "+artan.text.split()[144]+" "+artan.text.split()[152]+" "+artan.text.split()[160])
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yukselenler}).json()
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yukselenler}).json()

# burda sembol listesi oluştur 

sembol_list = ["ACSEL", "ADEL", "ADESE", "AEFES", "AFYON", "AGHOL", "AGYO", "AKBNK","AKCNS", "AKENR", "AKFGY",
               "AKGRT", "AKMGY", "AKSA", "AKSEN", "AKSGY", "AKSUE", "AKYHO","ALARK", "ALBRK", "ALCAR", "ALCTL",
               "ALGYO", "ALKA", "ALKIM", "ALMAD", "ANELE","ANHYT", "ANSGR", "ARCLK", "ARDYZ", "ARENA", "ARMDA",
               "ARSAN", "ARZUM", "ASELS","ASUZU", "ATAGY", "ATEKS", "ATLAS", "ATSYH", "AVGYO", "AVHOL", "AVISA",
               "AVOD","AVTUR", "AYCES", "AYEN", "AYES", "AYGAZ", "BAGFS", "BAKAB", "BALAT", "BANVT","BASCM", "BAYRK",
               "BERA", "BEYAZ", "BFREN", "BIMAS", "BIZIM", "BJKAS", "BLCYT","BNTAS", "BOSSA", "BRISA", "BRKO", "BRKSN",
               "BRMEN", "BRSAN", "BRYAT", "BSOKE","BTCIM", "BUCIM", "BURCE", "BURVA", "CASA", "CCOLA", "CELHA", "CEMAS",
               "CEMTS","CEOEM", "CIMSA", "CLEBI", "CMBTN", "CMENT", "COSMO", "CRDFA", "CRFSA", "CUSAN","DAGHL", "DAGI",
               "DARDL", "DENGE", "DERHL", "DERIM", "DESA", "DESPC", "DEVA","DGATE", "DGGYO", "DGKLB", "DIRIT", "DITAS",
               "DJISTf", "DMSAS", "DNISI", "DOAS","DOBUR", "DOCO", "DOGUB", "DOHOL", "DOKTA", "DURDO", "DYOBY", "DZGYO",
               "ECILC","ECZYT", "EDIP", "EGEEN", "EGGUB", "EGPRO", "EGSER", "EKGYO", "EKIZ", "EMKEL","EMNIS", "ENJSA",
               "ENKAI", "EPLAS", "ERBOS", "EREGL", "ERSU", "ESCOM", "ESEN","ETILR", "ETYAT", "EUHOL", "EUKYO", "EUYO",
               "FADE", "FENER", "FLAP", "FMIZP","FONET", "FORMT", "FRIGO", "FROTO", "GARAN", "GARFA", "GEDIK", "GEDZA",
               "GENTS","GEREL", "GLBMD", "GLDTRf", "GLRYH", "GLYHO", "GMSTRf", "GOLTS", "GOODY", "GOZDE","GRNYO", "GSDDE",
               "GSDHO", "GSRAY", "GUBRF", "HALKB", "HATEK", "HDFGS", "HEKTS","HLGYO", "HUBVC", "HURGZ", "ICBCT", "IDEAS",
               "IDGYO", "IEYHO", "IHEVA", "IHGZT","IHLAS", "IHLGM", "IHYAY", "INDES", "INFO", "INTEM", "INVEO", "IPEKE",
               "ISBIR","ISBTR", "ISCTR", "ISDMR", "ISFIN", "ISGSY", "ISGYO", "ISKPL", "ISMEN", "ISYAT","ITTFH", "IZFAS",
               "IZMDC", "IZTAR", "JANTS", "KAPLM", "KAREL", "KARSN", "KARTN","KATMR", "KCHOL", "KENT", "KERVN", "KERVT",
               "KFEIN", "KLGYO", "KLMSN", "KLNMA","KNFRT", "KONTR", "KONYA", "KORDS", "KOZAA", "KOZAL", "KRDMA", "KRDMB",
               "KRDMD","KRGYO", "KRONT", "KRSTL", "KRTEK", "KRVGD", "KSTUR", "KUTPO", "KUYAS", "LIDFA","LINK", "LKMNH",
               "LOGO", "LUKSK", "MAALT", "MAKTK", "MARKA", "MARTI", "MAVI","MEGAP", "MEPET", "MERIT", "MERKO", "METRO",
               "METUR", "MGROS", "MIPAZ", "MMCAS","MNDRS", "MPARK", "MRGYO", "MRSHL", "MSGYO", "MTRYO", "MZHLD", "NATEN",
               "NETAS","NIBAS", "NTHOL", "NUGYO", "NUHCM", "ODAS", "OLMIP", "ORGE", "ORMA", "OSMEN","OSTIM", "OTKAR", "OYAKC",
               "OYAYO", "OYLUM", "OZBAL", "OZGYO", "OZKGY", "OZRDN","PAGYO", "PAMEL", "PAPIL", "PARSN", "PEGYO", "PEKGY", "PENGD",
               "PETKM", "PETUN","PGSUS", "PINSU", "PKART", "PKENT", "PNSUT", "POLHO", "POLTK", "PRKAB", "PRKME","PRZMA", "PSDTC",
               "QNBFB", "QNBFL", "RALYH", "RAYSG", "RHEAG", "RODRG", "ROYAL","RTALB", "RYGYO", "RYSAS", "SAFKR", "SAHOL", "SAMAT",
               "SANEL", "SANFM", "SANKO","SARKY", "SASA", "SAYAS", "SEKFK", "SEKUR", "SELEC", "SELGD", "SERVE", "SEYKM","SILVR",
               "SISE", "SKBNK", "SKTAS", "SMART", "SNGYO", "SNKRN", "SNPAM", "SODSN","SOKM", "SONME", "SRVGY", "SUMAS", "TACTR",
               "TATGD", "TAVHL", "TBORG", "TCELL","TDGYO", "TEKTU", "TGSAS", "THYAO", "TIRE", "TKFEN", "TKNSA", "TKURU", "TLMAN",
               "TMPOL", "TMSN", "TOASO", "TRCAS", "TRGYO", "TRILC", "TSGYO", "TSKB", "TSPOR","TTKOM", "TTRAK", "TUCLK", "TUKAS",
               "TUPRS", "TURGG", "TURSG", "UFUK", "ULAS","ULKER", "ULUSE", "ULUUN", "UMPAS", "USAK", "USDTRf", "UTPYA", "UZERB",
               "VAKBN","VAKFN", "VAKKO", "VANGD", "VERTU", "VERUS", "VESBE", "VESTL", "VKFYO", "VKGYO","VKING", "YAPRK", "YATAS",
               "YAYLA", "YBTAS", "YESIL", "YGGYO", "YGYO", "YKBNK","YKGYO", "YKSLN", "YONGA", "YUNSA", "ZOREN"]

for sembol in sembol_list:
    strsembol=sembol
    link = "https://www.turkishbulls.com/SignalPage.aspx?lang=tr&Ticker=" + sembol
    r = s.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    bul = soup.findAll("span",{"id":"MainContent_CompanyTicker"})[0]
    bul1 = soup.findAll("span",{"id":"MainContent_LastPattern"})[0]
    bul2 = soup.findAll("span",{"id":"MainContent_LastSignal"})[0]
    bul3 = soup.findAll("span",{"id":"MainContent_LastClose"})[0]
    bul4 = soup.findAll("span",{"id":"MainContent_ChangePercent"})[0]
    close = (float(bul3.text)/1)
    sembol = TA_Handler(symbol=sembol,screener="turkey",exchange="BIST",interval=Interval.INTERVAL_1_DAY)
    fiyat=(str((sembol.get_analysis().indicators)["close"]))
    s1=(str((sembol.get_analysis().indicators)["Pivot.M.Classic.S1"]))
    s2=(str((sembol.get_analysis().indicators)["Pivot.M.Classic.S2"]))
    s3=(str((sembol.get_analysis().indicators)["Pivot.M.Classic.S3"]))
    r1=(str((sembol.get_analysis().indicators)["Pivot.M.Classic.R1"]))
    r2=(str((sembol.get_analysis().indicators)["Pivot.M.Classic.R2"]))
    r3=(str((sembol.get_analysis().indicators)["Pivot.M.Classic.R3"]))
    denge = (str((sembol.get_analysis().indicators)["Pivot.M.Classic.Middle"]))
    adx =(str((sembol.get_analysis().indicators)["ADX"]))
    rsi =(str((sembol.get_analysis().indicators)["RSI"]))
    acilis = (str((sembol.get_analysis().indicators)["open"]))

    if str(bul1).find('BOĞA') != -1 and str(close) > str(fiyat):
        print("",bul.text,end=" ")
        print("#",bul1.text,end="")
        print(" #",bul2.text,end=" #")
        print(" ₺",close,end=" ")
        print(bul4.text,"[x]",fiyat," ",end="\n")
        print("1.DESTEK :",s1,"2.DESTEK :",s2,"3.DESTEK :",s3,"PİVOT :",denge,"1.DİRENÇ :",r1,"2.DİRENÇ :",r2,"3.DİRENÇ :",r3)
        bogared=(bul.text)+" hissesinde yükseliş beklentisi "+(bul1.text)+" formasyonu "+(bul3.text)+" fiyatıyla "+(bul4.text)+" ONAYLANMADI"+"\n"+"1.DESTEK :"+s1+"\n"+"2.DESTEK :"+s2+"\n"+"3.DESTEK :"+s3+"\n"+"PİVOT :"+denge+"\n"+"1.DİRENÇ :"+r1+"\n"+"2.DİRENÇ :"+r2+"\n"+"3.DİRENÇ :"+r3
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': bogared}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': bogared}).json()
        fiyat = "https://tr.tradingview.com/symbols/BIST-"+ bul.text +"/ideas/"
        f = s.get(fiyat)
        foup = BeautifulSoup(f.content, "html.parser")
        fiyat = foup.findAll("p",{"class":"tv-widget-idea__description-row tv-widget-idea__description-row--clamped js-widget-idea__popup"})[0]
        print(bul.text,":",fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        yorumlayici=(bul.text)+":"+(fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()

        
    
    if str(bul1).find('BOĞA') != -1 and str(close) < str(fiyat):
        print("",bul.text,end=" ")
        print("#",bul1.text,end="")
        print(" #",bul2.text,end=" #")
        print(" ₺",close,end=" ")
        print(bul4.text,"[✓]",fiyat," ",end="\n")
        print("1.DESTEK :",s1,"2.DESTEK :",s2,"3.DESTEK :",s3,"PİVOT :",denge,"1.DİRENÇ :",r1,"2.DİRENÇ :",r2,"3.DİRENÇ :",r3)
        bogaonay=(bul.text)+" yükseliş beklentisi "+(bul1.text)+" formasyonu "+(bul3.text)+" fiyatıyla "+(bul4.text)+" ONAYLANDI Yükseliş devam ediyor."+"\n"+"1.DESTEK :"+s1+"\n"+"2.DESTEK :"+s2+"\n"+"3.DESTEK :"+s3+"\n"+"PİVOT :"+denge+"\n"+"1.DİRENÇ :"+r1+"\n"+"2.DİRENÇ :"+r2+"\n"+"3.DİRENÇ :"+r3
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': bogaonay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': bogaonay}).json()
        fiyat = "https://tr.tradingview.com/symbols/BIST-"+ bul.text +"/ideas/"
        f = s.get(fiyat)
        foup = BeautifulSoup(f.content, "html.parser")
        fiyat = foup.findAll("p",{"class":"tv-widget-idea__description-row tv-widget-idea__description-row--clamped js-widget-idea__popup"})[0]
        print(bul.text,":",fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        yorumlayici=(bul.text)+":"+(fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()

        
    if str(bul1).find('AYI') != -1 and str(close) > str(fiyat):
        print("",bul.text,end=" ")
        print("#",bul1.text,end="")
        print(" #",bul2.text,end=" #")
        print(" ₺",close,end=" ")
        print(bul4.text,"[x]",fiyat," ",end="\n")
        print("1.DESTEK :",s1,"2.DESTEK :",s2,"3.DESTEK :",s3,"PİVOT :",denge,"1.DİRENÇ :",r1,"2.DİRENÇ :",r2,"3.DİRENÇ :",r3)
        ayired=(bul.text)+" hissesinde düşüş beklentisi "+(bul1.text)+" formasyonu "+(bul3.text)+" fiyatıyla "+(bul4.text)+" ONAYLANMADI Yükseliş devam ediyor."+"\n"+"1.DESTEK :"+s1+"\n"+"2.DESTEK :"+s2+"\n"+"3.DESTEK :"+s3+"\n"+"PİVOT :"+denge+"\n"+"1.DİRENÇ :"+r1+"\n"+"2.DİRENÇ :"+r2+"\n"+"3.DİRENÇ :"+r3
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': ayired}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': ayired}).json()
        fiyat = "https://tr.tradingview.com/symbols/BIST-"+ bul.text +"/ideas/"
        f = s.get(fiyat)
        foup = BeautifulSoup(f.content, "html.parser")
        fiyat = foup.findAll("p",{"class":"tv-widget-idea__description-row tv-widget-idea__description-row--clamped js-widget-idea__popup"})[0]
        print(bul.text,":",fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        yorumlayici=(bul.text)+":"+(fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()

        
    if str(bul1).find('AYI') != -1 and str(close) < str(fiyat):
        print("",bul.text,end=" ")
        print("#",bul1.text,end="")
        print(" #",bul2.text,end=" #")
        print(" ₺",close,end=" ")
        print(bul4.text,"[✓]",fiyat," ",end="\n")    
        print("1.DESTEK :",s1,"2.DESTEK :",s2,"3.DESTEK :",s3,"PİVOT :",denge,"1.DİRENÇ :",r1,"2.DİRENÇ :",r2,"3.DİRENÇ :",r3)
        ayionay=(bul.text)+" hissesinde düşüş beklentisi "+(bul1.text)+" formasyonu "+(bul3.text)+" fiyatıyla "+(bul4.text)+" ONAYLANDI"+"\n"+"1.DESTEK :"+s1+"\n"+"2.DESTEK :"+s2+"\n"+"3.DESTEK :"+s3+"\n"+"PİVOT :"+denge+"\n"+"1.DİRENÇ :"+r1+"\n"+"2.DİRENÇ :"+r2+"\n"+"3.DİRENÇ :"+r3
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': ayionay}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': ayionay}).json()
        fiyat = "https://tr.tradingview.com/symbols/BIST-"+ bul.text +"/ideas/"
        f = s.get(fiyat)
        foup = BeautifulSoup(f.content, "html.parser")
        fiyat = foup.findAll("p",{"class":"tv-widget-idea__description-row tv-widget-idea__description-row--clamped js-widget-idea__popup"})[0]
        print(bul.text,":",fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        yorumlayici=(bul.text)+":"+(fiyat.text.strip().replace("ÅŸ","ş").replace("Ã¼","ü").replace("Ã¶","ö").replace("Ä±","ı").replace("Ã§","ç").replace("ÄŸ","ğ"))
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':835942393,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':763429881,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1438108325,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':942654535,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1441393065,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':727413369,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':706757897,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':519583904,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1145125246,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':925298421,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1024869257,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1055456355,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1298726210,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1050392537,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':371305611,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1384677517,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':974587203,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1713364622,'text': yorumlayici}).json()
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id':1777156557,'text': yorumlayici}).json()


    result = ""
    result += "" + bul.text + " "
    result += "" + bul2.text + " "
    result += "" + bul1.text + " "
    result += "" + bul3.text + " "
    result += "" + bul4.text + "\n"
    # ...
    # buraları yukarıdaki örneğe göre doldur
    # burası ile result değişkenini dosyaya yazdıracağız
    with open("analiz.xls", "w+") as f:
        f.write(result + "\n")
