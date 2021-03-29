from secedgar.filings import Filing, FilingType
from bs4 import BeautifulSoup as BS
import os
from gensim.models import Word2Vec
import nltk
import numpy as np
from sklearn.cluster import KMeans
from sklearn import cluster
from sklearn import metrics
from sklearn.decomposition import PCA
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering
import re


class FetchData():

    def __init__(self, ticker):
        self.NUM_10Ks = 1
        self.ticker = ticker
        self.root = os.getcwd()
        self.ignored_folders = {'__pycache__': 1, 'deprecated': 1}
        self.bold = []
        self.sorted = {}
        self.n_clusters = 4

        # define these later for categories to sort statements into
        self.defined_categories = {'Advertising': ['advertising', 'ads', 'marketers', 'market', 'business', 'promotion', 'posting'],
                                    'Competition': ['competitive', 'competition', 'competitor', 'competitors', 'contesting', 'opposition', 'competitiveness'],
                                    'Government': ['law', 'laws', 'restrict', 'subject', 'investigations', 'rulings', 'lawsuit', 'government', 'administration', 'executive', 'authority', 'management'],
                                    'Stock': ['market', 'stocks', 'stock', 'shares', 'trading', 'growth', 'decline', 'capital', 'funds', 'assets']}

    # define bolded point as header or nonheader
    def detect_header(self, sentence):
        length = len(sentence)
        capitalized = 0
        for i in range(length):
            if sentence[i].isupper():
                capitalized += 1
        if capitalized / length > 0.5:
            return True
        else:
            return False


    # delete all current 10k files
    def delete_10ks(self):
        root = self.root + '/filings/'
        for dir in next(os.walk(root))[1]:
            if dir not in self.ignored_folders:
                try:
                    dir = root + '/' + dir + '/10-k'
                    for file in os.listdir(dir):
                        os.remove(dir + '/' + file)
                except:
                    continue


    # get 10k file of a specific company/ticker
    def get_10k(self):
        file_dir = os.getcwd() + '/filings/' + self.ticker + '/10-k/'
        file_name = ""

        if os.path.isdir(file_dir):
            # first file is the most recently downloaded
            if len(os.listdir(file_dir)) > 0:
                for file in os.listdir(file_dir):
                    file_name = file
                return file_dir + file_name

        try:
            file_dir = os.getcwd() + '/filings/'
            my_filings = Filing(cik_lookup=self.ticker, filing_type=FilingType.FILING_10K, count=self.NUM_10Ks)
            my_filings.save(file_dir)
            print(self.ticker + " 10k downloaded")
            file_dir += self.ticker + '/10-k/'
            for file in os.listdir(file_dir):
                file_name = file
            return file_dir + file_name

        except OSError as err:
            print("OS error: {0}".format(err))
            print('Unable to download ' + self.ticker + ' 10k!')
            return None



    # search by style - font-weight: bold. Only keep strings with more than 10 words.
    def bolded_points(self, file_path):
        returned = []

        with open(file_path,'r') as file:
            string = file.read()
        string = string[200000:-500000]
        soup = BS(string, 'html.parser')
        # print(soup.prettify())

        bold_p = soup.find_all('p', style=lambda value: value and 'font-weight:bold' in value)
        bold_span = soup.find_all('span', style=lambda value: value and 'font-weight:bold' in value)
        italic_p = soup.find_all('p', style=lambda value: value and 'font-style:italic' in value)
        italic_span = soup.find_all('span', style=lambda value: value and 'font-style:italic' in value)
        bold = bold_p + bold_span + italic_p + italic_span

        for i in range(len(bold)):
            bold[i] = bold[i].get_text()

        for i in range(len(bold)):
            word_count = len(bold[i].split())
            if word_count < 100 and word_count > 10:
                returned.append(bold[i])

        # remove duplicates
        returned = list(set(returned))

        if len(returned) < 5:
            print("bruh")
            patt = re.compile("font-weight:(\d+)")
            font_weights = [(tag.text.strip(), patt.search(tag["style"]).group(1)) for tag in soup.select("[style*=font-weight]")]
            font_weights = [data[0] for data in font_weights if int(data[1]) > 500 and len(data[0]) > 50]
            counter = 0
            for i in range(len(font_weights)):
                counter += 1
                if font_weights[i][:4].lower() == "item":
                    break

            font_weights = font_weights[:counter]
            returned += font_weights

        # remove bolded headings
        returned_2 = []
        for sentence in returned:
            if not self.detect_header(sentence):
                returned_2.append(sentence)

        # update object
        self.bold = returned_2
        return returned_2[:]


    # print bolded points to terminal
    def console_print(self):
        for item in self.bold:
            print(item)


    # sort bolded sentences into predefined categories
    def sort_bold(self):
        root_relevance_index = {}
        categories = {}

        categories['Miscellaneous'] = ['Miscellaneous risk factors']

        for category in self.defined_categories:
            root_relevance_index[category] = 0
            if category == "Advertising":
                categories[category] = ['Risk factors related to producing advertisements for commercial products or services']
            elif category == "Government":
                categories[category] = ['Risk factors related to governing regulations and restrictions']

            elif category == "Stock":
                categories[category] = ['Risk factors related to the capital raised by a business or corporation']

            else:
                categories[category] = ['Risk factors related to similar companies in the market space ']


        for item in self.bold:
            word_bank = {}
            relevance_index = root_relevance_index.copy()

            for word in item.split():
                word_bank[word] = 1

            for category in self.defined_categories:
                for word in self.defined_categories[category]:
                    if word in word_bank:
                        relevance_index[category] += 1

            max_val = 0
            final_category = "Miscellaneous"
            for val in relevance_index:
                temp = relevance_index[val]
                if temp > max_val:
                    max_val = temp
                    final_category = val
            categories[final_category].append(item)

        self.sorted = categories

        json_categories = {}
        counter = 0
        for key in categories:
            json_categories[key] = {"title": key, "duration": 1300 + counter, "sentences": categories[key]}
            counter += 200
        return categories


    # sort miscellaneous points into k new groups
    def sort_misc(self):
        l = []
        sentences = []
        for sentence in self.sorted["Miscellaneous"]:
            sentences.append(sentence.split(" "))
        m = Word2Vec(sentences, size=50, min_count=1, sg=1)
        for sentence in sentences:
            l.append(self.vectorizer(sentence, m))
        X = np.array(l)

        if len(X) < self.n_clusters:
            print("Not enough miscellaneous sentences to sort!")
            return None

        clf = KMeans(n_clusters=self.n_clusters, max_iter=100, init='k-means++',
                     n_init=1)
        labels = clf.fit_predict(X)

        for index, sentence in enumerate(sentences):
            label = str(labels[index])
            if label in self.sorted:
                self.sorted[label].append(str((" ").join(sentence)))
            else:
                self.sorted[label] = [str((" ").join(sentence))]


    # from https://blog.eduonix.com/artificial-intelligence/clustering-similar-sentences-together-using-machine-learning/
    def vectorizer(self, sentences, m):
        vec = []
        numw = 0
        for w in sentences:
            try:
                if numw == 0:
                    vec = m[w]
                else:
                    vec = np.add(vec, m[w])
                numw += 1
            except:
                pass
        return np.asarray(vec) / numw


    # write current sorted bolded points into text file
    def write(self):
        f = open(self.ticker + "_data.txt", "w")
        f.write(self.ticker + " data\n")
        f.write("\n")
        for category in self.sorted:
            f.write(category + '\n')
            for sentence in self.sorted[category]:
                f.write(sentence + '\n')
            f.write("\n")
        f.close()


# # driver code
# data = FetchData('fb')
# data.delete_10ks()
