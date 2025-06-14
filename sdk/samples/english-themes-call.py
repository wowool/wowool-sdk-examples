from wowool.sdk import Pipeline
from wowool.semantic_themes import Themes

analysis = Pipeline("english,entity,semantic-theme")
themes = Themes(count=2)
# run the document analysis
document = themes(analysis("EyeOnID works on cybercrime prevention"))
assert document.themes is not None, "Themes should not be None"
for item in document.themes:
    print(f" - {item.name}: {item.relevancy}")
