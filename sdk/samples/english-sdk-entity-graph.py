from wowool.sdk import Pipeline
from wowool.entity_graph import EntityGraph
from wowool.utility.diagnostics import print_diagnostics
import json

text = "John Smith works for Ikea, he visited Jysk in Sweden. Bella Johansson is also working for Jysk."
pipeline = Pipeline("english,entity")
# defines a relationship: from "Person" to "Company" with the relation "VP".
grapher = EntityGraph(
    links=[
        {
            "from": "Person",
            "to": "Company",
            "relation": "VP",
        }
    ]
)
doc = pipeline(text)
doc = grapher(doc)
if doc.results("wowool_entity_graph"):
    print(json.dumps(doc.results("wowool_entity_graph"), indent=2))
else:
    print_diagnostics(doc)
