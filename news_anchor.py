import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__=='__main__':
    speak("today news headlines are...")
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=c2e211d530734931934c55c6f8f0b1c2"
    news=requests.get(url).text
    news_json=json.loads(news)
    arts=news_json["articles"]
    for article in arts:
         print(article["title"])
         print(" ")
         speak(article["title"])
         speak("and the next news is ")
    speak("here is the end of todays news")
