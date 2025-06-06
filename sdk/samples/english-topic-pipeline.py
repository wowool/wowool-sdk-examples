from wowool.sdk import Pipeline

pipeline = Pipeline("english,topics.app")
doc = pipeline("Gas supplies to Europe wounded soldiers inside Azovstal steel mill")
print(doc.topics)
