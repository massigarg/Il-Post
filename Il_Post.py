from bs4 import BeautifulSoup
import requests
from time import sleep
from wordcloud import WorldCloud, STOPWORDS
from PIL import Image
import os


currdir=os.path.dirname(__file__)

page=1
a_list=[]
while page<2:
    url=f"https://www.ilpost.it/italia/page/{page}"

    request=requests.get(url).text

    soup=BeautifulSoup(request, "html.parser")

    articles=soup.find_all("div", class_="entry-content")

    bits=soup.find(class_="widget bits")
    bits=bits.find_all("li")

    for article in articles:
        try:
            title=article.find("h2", class_="entry-title").a["title"]
            a_list.append(title)
        except:
            pass
        try:
            description=article.find("p").find("a").text
            description=description.replace("\t","").strip()
            a_list.append(description)
        except:
            pass
    page+=1
    #sleep(3)

text="".join(a_list)

def create_wordcloud(text):
	stopwords=set(STOPWORDS)

	wc=WorldCloud(background_color="white",
					max_words=100,
					stopwords=stopwords
					)
	wc.to_file(os.path.join(currdir, "wc.png"))

create_wordcloud(text)


# title=article.find("h2", class_="entry-title").a["title"]
# description=article.find("p").a["title"]

# def get_title(article):
#     try:
#         return article.find("h2", class_="entry-title").a["title"]
#     except:
#         return
#
# def get_description(article):
#     try:
#         return article.find("p").find("a")["title"]
#     except:
#         return


# for bit in bits:
#     try:
#         print(bit.a["title"])
#     except:
#         pass



# print(bits)