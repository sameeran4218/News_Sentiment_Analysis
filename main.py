# neccessary imports
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

# create a function to scrape news from a given website using Beautiful Soup
# here i have created the code to extract data from the IndianExpress webpage
# if you want another website you might have to alter the code
def scrape_news(url):
    # get the html content of the webpage and create a beautiful soup object
    html_content = requests.get(url)
    soup = BeautifulSoup(html_content.text, 'lxml')

    #scrape all the news articles and store their text in a list , then return that list
    articles = soup.find_all('div', class_='articles')
    headlines=[]
    for article in articles:
        headline=article.p.get_text()
        headlines.append(headline)
    return headlines

#create a function to perform the sentiment analysis using TextBlob
def sentiment_analysis(news_content):

    # take input of a list and for each item perform the sentiment analysis and print it
    for news in news_content:
        sa = TextBlob(news).sentiment
        print(news)
        print(sa)
        print()

# create the main fucntion to call both  scrape_news(url) and sentiment_analysis(news_content)
def main():
    news_content=scrape_news(url='https://indianexpress.com/latest-news/')
    sentiment_analysis(news_content=news_content)

if __name__ == "__main__":
    main()