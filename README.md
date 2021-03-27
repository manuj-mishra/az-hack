# RE.PRESENT
**Your personal assistant for information visualisation.**

![RE.PRESENT logo](https://user-images.githubusercontent.com/24252542/112717386-35b9f880-8ee4-11eb-9f76-2065e0a89af5.jpeg)

*(Created for the AstraZeneca Neurodiversity Hackathon 2021).*

This is a proof-of-concept that shows that text can be transformed into:
* A short summary
* A list of ngrams (keywords/keyphrases)
* A folder of images associated with the above ngrams
* Where these keyphrases appear in the original text

To see the our proposal for a wireframe of the final products frontend, please see below:  
https://www.figma.com/file/xYVoIMvpBmZaPPbDu26vs1/Represent?node-id=0%3A1

To see the youtube video of our pitch deck, please see below:  
https://youtu.be/XQjfuX85m50

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

NOTE: this project uses our personal API keys for Google custom search and SMMRY which are both at a free tier level. The query limit is 100 API calls a day to each service. Multiple users forking and using this project might lead to queries being throttled very quickly. To remedy this, please sign up for your own account for each of these services and replace the API keys in `pictures.py` and `summary.py`. 

### Prerequisites

This project depends on YAKE (Yet Another Keyword Extractor)
```
pip install git+https://github.com/LIAAD/yake
```
### Running

Clone this repository and run the following command

```
$ python3 src/main.py
```
and enter the path to a text file with the input article.
For convenience, we have included a sample data text file. Try this!

```
$ Enter file path: data.txt
```

## Authors

* **Manuj Mishra** 
* **Akshit Goel** 
* **Josh Kotecha** 
* **Shrimat Kapoor** 

## Acknowledgments

* Jo Baker and the AstraZeneca Team for organising this hackathon
* Daniel Goude and Robert Radcliffe for their mentorship and guidance
* Shivani Raja for the advice and logo 



