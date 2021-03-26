# from keyword import getKeywords
import yake
from freq import find_most_frequent_word
from pictures import getImage
from summary import getSummary
from PIL import Image

def getKeywords(text):
    language = "en"
    max_ngram_size = 3
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 4

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)

    return [word for word, score in custom_kw_extractor.extract_keywords(text)]


f = open("data.txt", mode='r')
text = f.read()

# Get summary
summary = getSummary(text)

# Get keywords
keywords = getKeywords(text)

# Save images
for k in keywords:
  getImage(k).save("output/images/"+k+".jpg")


# Summary printing
print(summary)

# Keyword printing
print("KEYWORDS:", end=" ")
for k in keywords[:-1]:
  print(k, end=", ")
print(keywords[-1])

# Frequent printing
print(find_most_frequent_word(text.splitlines(), 5, keywords[0]))

f.close()