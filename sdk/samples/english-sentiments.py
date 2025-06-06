from wowool.sdk import Pipeline

# Note that the sentiment object has resolve the text from 'he sucks' to 'John Dow sucks'.
# you can also insert your own sentiment domains before the sentiment app.
# You need to create a custom domain that contains the sentiment entities
# PositiveSentiment, NegativeSentiment and sub-annotations SentimentObject, ExprNeg, AdjPos, ...

text = "John Dow is a very nice person, but he sucks at football."
pipeline = Pipeline(
    [
        "english",
        "entity",
        "sentiment",
        "sentiments.app",
    ]
)
document = pipeline(text)
print(document)
sentiments = document.sentiments
assert sentiments is not None, "Sentiments should not be None"
for sentiment in sentiments.locations:
    print(f"polarity = {sentiment.polarity}")
    print(f"text     = {sentiment.text}")
    print(f"offsets  = {sentiment.begin_offset},{sentiment.end_offset}")
    if sentiment.object:
        print(f"object = {sentiment.object}")
    if sentiment.adjective:
        print(f"adjective = {sentiment.adjective}")
    if sentiment.expression:
        print(f"expression = {sentiment.expression}")
    if sentiment.comp:
        print(f"comp = {sentiment.comp}")
    if sentiment.verb:
        print(f"verb = {sentiment.verb}")
    print("-" * 40)
