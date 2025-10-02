from wowool.sdk import Pipeline
from wowool.document.analysis.document import AnalysisDocument
from pathlib import Path
import json

english_analysis = Pipeline("english,entity")
text = "John Smith works for Ikea in France."
doc = english_analysis(text)
print(doc)
# store the document as a json object/or string
doc_serialized_json_str = doc.to_json()
# display the serialized document
print(json.dumps(doc_serialized_json_str, indent=2))
# store to database
#  --------------------------------------------------------
# load from database
doc_serialized = json.loads(doc_serialized_json_str)
analysis_document = AnalysisDocument.from_dict(doc_serialized)
this_dir = Path(__file__).parent
# second pass with custom rules folder
custom_rules = Pipeline(str(this_dir / "rules"))
doc_with_custom_rules: AnalysisDocument = custom_rules(analysis_document)  # noqa: F841
print(doc_with_custom_rules)
