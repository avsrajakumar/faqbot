import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")
nltk.download("stopwords")

paragraph = """A computer is an electronic device, operating under the control of instructions stored in its own memory that can accept data (input), process the data according to specified rules, produce information (output), and store the information for future use1. Any kind of computers consists of HARDWARE AND SOFTWARE."""
print("----------------Raw text------------------/n", paragraph)

tokenizer = RegexpTokenizer(r'\w+')
wordlist = tokenizer.tokenize(paragraph)
print("----------------Tokenization------------------/n", wordlist)

neccessarywordlist = [i for i in wordlist if i not in stopwords.words('english')]
print("----------------StopWords Removed------------------/n", neccessarywordlist)

stemmer = PorterStemmer()
stemmerwordlist = [stemmer.stem(i) for i in neccessarywordlist]
print("----------------After Stemming------------------/n", stemmerwordlist)

lemmatizer = WordNetLemmatizer()
lemmatizerwordlist = [lemmatizer.lemmatize(i) for i in stemmerwordlist]
print("----------------After lemmatizer------------------/n", lemmatizerwordlist)
