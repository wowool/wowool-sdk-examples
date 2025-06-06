from wowool.sdk import Pipeline
from wowool.topic_identifier import TopicIdentifier

english = Pipeline("english")
number_of_topics = 5
topic_it = TopicIdentifier(language="english", count=number_of_topics)
# display the results of every file, by iterating over every file.
document = topic_it(english("This is the effect of the green house gases"))
for topic in document.topics:
    print(f" - {topic}")
