from wowool.sdk import Pipeline
from wowool.anonymizer import Anonymizer, DefaultWriter
from json import dumps

# replace all characters of a entities with dot's
english = Pipeline("english,entity")
document = english("John Smith works for Ikea.")
writer = DefaultWriter(formatters={"default": "{'.'*len(literal)}"})
writer = DefaultWriter(formatters={"default": "###{anonymized_literal}"})
anonymizer = Anonymizer(writer=writer)
document = anonymizer(document)
results = document.results(Anonymizer.ID)
print(dumps(results, indent=2))
