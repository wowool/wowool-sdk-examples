from wowool.sdk import Pipeline
from wowool.anonymizer import Anonymizer, DefaultWriter

# note you can use the default pseudonyms if you want
# from wowool.anonymizer.core.anonymizer_config import DEFAULT_PSEUDONYMS
from json import dumps

# replace all characters of a entities with dot's
english = Pipeline("english,entity")
document = english("John Smith works for Ikea.")
pseudonyms = {
    "Person": ["Batman"],
    "Company": ["Monster Inc."],
}
writer = DefaultWriter(pseudonyms)
anonymizer = Anonymizer(writer=writer)
document = anonymizer(document)
results = document.results(Anonymizer.ID)
print(dumps(results, indent=2))
