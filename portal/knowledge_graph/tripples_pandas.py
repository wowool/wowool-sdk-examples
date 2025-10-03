from wowool.portal import Pipeline
from wowool.entity_graph import CollectedResults
import pandas as pd

# Define the entity relations for the graph
graph_options = {
    "nodes": {"__subject__": {"label": "Subject", "name": "Subject.canonical"}},
    "links": [
        {"from": "__subject__", "relation": "VP", "to": "Object"},
    ],
}
# Create the pipeline with English processing, syntax, entity recognition, and graph construction
steps = ["english", "syntax", "entity", {"name": "graph.app", "options": graph_options}]

pipeline = Pipeline(steps)
text = "John Smith lives in New York City. He works at OpenAI."
doc = pipeline(text)
print("TEXT ", text)
links = doc.results("wowool_entity_graph")
merged_result = CollectedResults(links).merge()
df = pd.DataFrame(merged_result.rows)
print("DATAFRAME\n", df)
