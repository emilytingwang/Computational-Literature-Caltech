import nltk
import urllib
from urllib import urlopen
from nltk import word_tokenize
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
          'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
          'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
          'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

for state in states:
    url = 'https://en.wikipedia.org/wiki/'+state
    html = urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html, "lxml").get_text()
    tokens = word_tokenize(raw)
    tokens = tokens[:1450]
    text = nltk.Text(tokens)

    letters_only = re.sub("[^a-zA-Z]", " ", raw)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    meaningful_words = " ".join( meaningful_words )

    f = open(state, "w")
    f.write("".join(map(lambda x: str(x), meaningful_words)))
    f.close()


# for state in states:
#     url = 'https://en.wikipedia.org/wiki/'+ state
#     response = urllib.request.urlopen(url)
#     raw = response.read().decode('utf8')
