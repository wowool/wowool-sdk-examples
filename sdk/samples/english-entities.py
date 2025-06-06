from wowool.sdk import Pipeline

text = """John Smith met with Emily Chen at the Wayfair office in Antwerp.
Later, they visited Gent to discuss the new project.
Sarah Johnson from Jysk joined them for lunch at a local café.
The team planned to present their findings at the Ikea headquarters in Stockholm."""

pipeline = Pipeline("english,entity")
document = pipeline(text)

for entity in document.entities:
    print(
        f"({entity.begin_offset:>3},{entity.end_offset:>3}): {entity.uri:<12} -> {entity.canonical}"
    )
