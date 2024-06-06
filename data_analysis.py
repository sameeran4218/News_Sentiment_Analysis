from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('News.csv')
def getAnalysis(score):
    if score>0:
        return 'postive'
    elif score==0:
        return 'neutral'
    else:
        return 'negative'
# create a new Series to store the polarity
df['Polarity']=df['Polarity Score'].apply(getAnalysis)

#create a bar graph to show the frequecny of polarity of the news
plt.style.use('dark_background')
colors=['red','orange','yellow']
plt.figure(figsize=(7,5))
df['Polarity'].value_counts().plot(kind='bar',color=colors)
plt.xticks(rotation=0)
plt.xlabel(xlabel='Sentiment Polarity')
plt.ylabel(ylabel='Count')
plt.title('Frequency of Sentiments')
plt.show()

# create a pie chart to show proportion of the polarity for the news
color=('cyan','blue','violet')
df['Polarity'].value_counts().plot(kind='pie',autopct='%.2f %%',colors=color)
plt.ylabel(ylabel='')
plt.title('Proportion of Sentiments')
plt.show()

# create a wordcloud to display the most frequently used words in the news
news_text = df['news'].str.cat(sep='\n')  # Combine all news articles

# Preprocess the text (optional)
text = TextBlob(news_text).lower()  # Convert to lowercase
text = text.words  # Extract words

# Remove stop words (optional)
stop_words = set(STOPWORDS)
filtered_words = [word for word in text if word not in stop_words]

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=600, background_color='white').generate(' '.join(filtered_words))

# Display the wordcloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('WordCloud of News Articles')
plt.show()
