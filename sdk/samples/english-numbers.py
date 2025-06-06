from wowool.sdk import Pipeline

text = "I have 2m euro's and ten thousand one hundred eighty-nine dollars."
pipeline = Pipeline(
    [
        "english",
        "numbers.language",
        "entity",
        "numbers.app",
    ]
)
document = pipeline(text)
print(document)
