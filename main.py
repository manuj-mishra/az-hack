# from keyword import getKeywords
import yake
from freq import find_most_frequent_word
from pictures import getImage
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

# Get keywords and images
keywords = getKeywords(text)
images = [getImage(k) for k in keywords]

# Crop images

dims = []
for im in images:
  w, h = im.size
  dims.append(w)
  dims.append(h)

minDim = min(dims)
new_width = minDim
new_height = minDim

for i in range(len(images)):
  im = images[i]
  width, height = im.size

  left = (width - new_width)/2
  top = (height - new_height)/2
  right = (width + new_width)/2
  bottom = (height + new_height)/2

  images[i] = im.crop((left, top, right, bottom))

# Combine images

left_offset = 0
top_offset = 0
blank_image = Image.new("RGB", (minDim*2, minDim*2))
counter = 0

for _ in range(2):
  for _ in range(2):
    blank_image.paste(images[counter], (left_offset, top_offset))
    top_offset += new_height
    counter += 1
  left_offset += new_width


blank_image.save("final.jpg")

# Keyword printing
print("KEYWORDS:", end=" ")
for k in keywords[:-1]:
  print(k, end=", ")
print(keywords[-1])


print(find_most_frequent_word(text.splitlines(), 5, keywords[0]))

f.close()