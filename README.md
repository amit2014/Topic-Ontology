# Topic-Ontology

Project by Diya Das ([@InfH](https://github.com/InfH)), Tristan Miller ([@tristanlmiller](https://github.com/tristanlmiller/)), Ali Sanaei ([@asanaei](https://github.com/asanaei)), and Simon Segert ([@SimonSegert](https://github.com/simonsegert))

Our goal is to create a topic ontology of Wikipedia articles and place any English Wikipedia article within this classification scheme, based on its text content.

This project is an experiment using Python to parse text and run classification algorithms. Dependencies include [pandas](https://pypi.python.org/pypi/pandas), [NumPy](https://pypi.python.org/pypi/numpy), [lxml](https://pypi.python.org/pypi/lxml), [wikipedia](https://pypi.python.org/pypi/wikipedia/), [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4/4.5.0), and [NLTK](https://pypi.python.org/pypi/nltk/3.2.1). Note: we are using Python 3.5. This code has not been tested on Python 2 or older versions of Python 3.

##### Detailed overview
1. We extract a list of all articles in English Wikipedia from one of the XML Wikipedia dumps located [here](https://dumps.wikimedia.org/enwiki/). We are using the dump from 07-01-2016, as more recent dumps had not been finished at the start of our project. Any MediaWiki-formatted XML should do. (We used a Simple Wikipedia dump as input for testing.)
2. We randomly sample to get a subset of these articles, excluding redirects and other non-"pages", for constructing our main tree. The choice of number of articles depends largely on processing constraints. 
3. We extract summary text for the selected articles and perform natural language processing. We calculate tf-idf to weight the features and perform PCA to maximize information content. We select the first 400 PCs for use in the remaining analysis.  
4. We perform iterative clustering on the PCA-rotated data, to identify groups of textually similar articles and construct our hierarchy.
5. When presented with an article not in the tree, we will perform tf-idf and transpose the article vector into the PCA rotated space. We calculate the distance from the medoids of the clusters, and use this information to place the article in the most similar cluster.
