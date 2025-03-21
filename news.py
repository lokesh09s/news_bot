# import requests
# from bs4 import BeautifulSoup
# import random
# def news():
    
#     url = 'https://apnews.com/business'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     title = soup.select('.PagePromo-content')
#     paper = random.randint(0,(len(title) -1))
#     header = title[paper].find("a").text
#     url = title[paper].find("a").get("href")
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     data = soup.find_all('p')
#     news = []
#     for i in data:
#         news.append(i.text)
#     content = " ".join(news)

#     return header, content
import requests
from bs4 import BeautifulSoup
import random

def news():
    # Fetch the business section of AP News
    url = 'https://apnews.com/business'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Select the headlines (titles) of the articles
    title = soup.select('.PagePromo-content')
    
    # Select a random article
    paper = random.randint(0, 10)
    
    # Get the headline of the selected article
    header = title[paper].find("a").text
    
    # Get the article's URL and fetch its content
    article_url = title[paper].find("a").get("href")
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the paragraphs of the article (main content)
    data = soup.find_all('p')
    news_content = []
    
    # Collect all the paragraphs' text
    for paragraph in data:
        news_content.append(paragraph.text)
    
    # Join the paragraphs into a single string
    content = " ".join(news_content)
    j = [header, content]
    # Return headline and content
    return j

print(news()[0])



