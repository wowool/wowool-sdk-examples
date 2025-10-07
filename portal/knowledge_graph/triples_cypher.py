from wowool.portal import Pipeline

# Define the entity relations for the graph
graph_options = {
    "nodes": {"__subject__": {"label": "Subject", "name": "Subject.canonical"}},
    "links": [
        {"from": "__subject__", "relation": "VP", "to": "Object"},
    ],
}
# Create the pipeline with English processing, syntax, entity recognition, and graph construction
steps = [
    "english",
    "syntax",
    "entity",
    {"name": "graph.app", "options": graph_options},
    "cypher(counters=['Subject']).app",
]

pipeline = Pipeline(steps)
text = "John Smith lives in New York City. He works at OpenAI."
doc = pipeline(text)
print("TEXT ", text)
print("-" * 80)
cypher_results = doc.results("wowool_cypher")
for cypher in cypher_results["cypher"]:
    print(cypher)
