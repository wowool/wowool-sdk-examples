from wowool.portal import Pipeline
import pandas as pd

# Define the entity relations for the graph
graph_options = {
    "nodes": {"__subject__": {"label": "Subject", "name": "Subject.canonical"}},
    "links": [
        {"from": "__subject__", "relation": "VP", "to": "Object"},
    ],
    "output_format": "table",
}
# Create the pipeline with English processing, syntax, entity recognition, and graph construction
steps = ["english", "syntax", "entity", {"name": "graph.app", "options": graph_options}]

pipeline = Pipeline(steps)
text = "John Smith lives in New York City. He works at OpenAI."
doc = pipeline(text)
print("TEXT ", text)
df = pd.DataFrame(doc.entity_graph)
print(df)
