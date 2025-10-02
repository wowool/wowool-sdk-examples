from wowool.sdk import Pipeline
from wowool.entity_graph import EntityGraph
from wowool.utility.diagnostics import print_diagnostics
import json

text = "John Smith works for Ikea, he visited Jysk in Sweden. Bella Johansson is also working for Jysk."
pipeline = Pipeline("english,syntax,entity")
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
if doc.entity_graph:
    for link in doc.entity_graph:
        print(f"Link: {link.from_} -> ({link.relation}) ->  {link.to}")
else:
    print_diagnostics(doc)
