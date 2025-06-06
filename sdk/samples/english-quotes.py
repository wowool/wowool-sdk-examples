from wowool.sdk import Pipeline
from wowool.quotes import Quotes

text = '"Wowool has cool technology", said John Smith.'
pipeline = Pipeline(
    [
        "english",
        "quotation",
        "quotes.app",
    ]
)
document = pipeline(text)
print(document.results(Quotes.ID))
