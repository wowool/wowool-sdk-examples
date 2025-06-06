from wowool.sdk import Pipeline
from wowool.phones.app_id import APP_ID

text = "I live in Antwerp and my phone number is 03/230 30 46."
pipeline = Pipeline(
    [
        "english",
        "contact-info",
        "phones.app",
    ]
)
document = pipeline(text)
print(document.results(APP_ID))
