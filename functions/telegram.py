import requests
import time
from functions.output import *

class tg_bot(object):
    def __init__(self, tg_api_base_link,bot_id):
       self.tg_api_base_link = tg_api_base_link
       self.bot_id=bot_id
       log("LOG_TG","【Info】Bot Init")
    def getUpdates(self):
        error=0
        while True:
            if error>50:
                return(False,"Too Many Errors")
            try:
                r=requests.get("{}/bot{}/getUpdates".format(self.tg_api_base_link,self.bot_id),timeout=5)
                return (True,r.content.decode("utf-8"))
            except Exception as ex:
                error+=1
                #print(ex)
                log("LOG_TG","【Error】{}".format(str(ex)))
                time.sleep(5)
    def sendMessage(self,chat_id,text):
        error=0
        while True:
            if error>50:
                return(False,"Too Many Errors")
            try:
                r=requests.get("{}/bot{}/sendMessage?chat_id={}&text={}".format(self.tg_api_base_link,self.bot_id,chat_id,text),timeout=5)
                return r.content.decode("utf-8")
            except Exception as ex:
                error+=1
                #print(ex)
                log("LOG_TG","【Error】{}".format(str(ex)))
                time.sleep(5)
