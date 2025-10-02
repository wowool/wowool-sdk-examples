from wowool.sdk import Pipeline

# Define the entity relations for the graph
graph_options = {
    "nodes": {
        "__subject__": {
            "label": "Subject",
            "name": "Subject.canonical",
        }
    },
    "links": [
        {
            "from": "__subject__",
            "relation": "VP",
            "to": "Object",
        },
    ],
}
# Create the pipeline with English processing, syntax, entity recognition, and graph construction
steps = [
    "english",
    "syntax",
    "entity",
    {"name": "graph.app", "options": graph_options},
]

pipeline = Pipeline(steps)
text = "John Smith lives in New York City. He works at OpenAI."
doc = pipeline(text)
print("TEXT ", text)
print("-" * 80)
for link in doc.entity_graph:
    print(
        f"{link.from_['label']}: {link.from_['name']:<20} - {link.relation['label']}: {link.relation['name']:<20} -> {link.to['label']}: {link.to['name']}"
    )
