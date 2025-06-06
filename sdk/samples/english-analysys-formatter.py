from wowool.sdk import Pipeline

text = "John Smith works for Wowool."
pipeline = Pipeline(
    [
        "english",
        "entity",
        {
            "name": "analysis-formatter.app",
            "options": {"uri": "uri", "begin_offset": "bo", "stem": "s"},
        },
    ]
)
document = pipeline(text)
print(document.results("wowool_analysis_formatter"))
