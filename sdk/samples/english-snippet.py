from wowool.sdk import Pipeline

text = "John Smith works for Ikea."
pipeline = Pipeline(
    [
        "english",
        "entity",
        {
            "name": "snippet.app",
            "options": {
                "source": "rule:{ Person .. Company } = PersonCompany;",
            },
        },
    ]
)
document = pipeline(text)
print(document)
