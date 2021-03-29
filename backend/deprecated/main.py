from edgar import Company, XBRL, XBRLElement, TXTML, Edgar, Document
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import sys

# company = Company("INTERNATIONAL BUSINESS MACHINES CORP", "0000051143")
# company2 = Company("twitter", "0001418091")
# company3 = Company("Oracle Corp", "0001341439")
company4 = Company("GOOGLE INC", "0001288776")

# edgar = Edgar()
# possible_companies = edgar.find_company_name("Cisco System")
#
# print(possible_companies)

doc = company4.get_10K()
text = TXTML.parse_full_10K(doc)

print('1')

f = open("text2.txt", "w+")
f.write(text)
f.close()


# f = open('text.txt', 'r')
# for line in f:
#     print(line)
#     print()
#     print()
#     print()


text2 = text.lower()

cutoff = 1000
index = 0
string = 'risk factors'
string_length = len(string)
counter = 0
bool = True
while bool:
    index = text2.find(string, cutoff)
    cutoff = index + string_length

    counter2 = 0
    while True:
        if text2[cutoff + counter2:cutoff + counter2 + 1].isalpha():
            index = cutoff + counter2
            bool = False
            break
        elif text2[cutoff + counter2:cutoff + counter2 + 1] == '\n':
            counter2 += 1
            continue
        else:
            break


    counter += 1
    if counter > 100:
        print('could not find!')
        sys.exit()

text3 = text2[index:]
index2 = text3.find('unresolved staff comments')
text4 = text[cutoff:cutoff + index2]

print('2')

# print(text4)


LANGUAGE = "english"
# parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
parser = PlaintextParser.from_string(text4, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = TextRankSummarizer(stemmer)

summarizer.stop_words = get_stop_words(LANGUAGE)

print('3')

num_sentences = 5

result = ''
counter = 0
for sentence in summarizer(parser.document, num_sentences):
    counter += 1
    result += ' ' + str(sentence)


print(result)
