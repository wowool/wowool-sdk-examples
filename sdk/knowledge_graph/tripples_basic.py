from wowool.sdk import Pipeline

# Define the entity relations for the graph
graph_options = {
    "links": [
        {"from": "Subject", "relation": "VP", "to": "Object"},
    ],
}
# Create the pipeline with English processing, syntax, entity recognition, and graph construction
steps = ["english", "syntax", {"name": "graph.app", "options": graph_options}]

pipeline = Pipeline(steps)
text = "John Smith lives in New York City. He works at OpenAI."
doc = pipeline(text)
print("TEXT ", text)
print("-" * 80)
for link in doc.entity_graph:
    print(
        f"{link.from_['label']}: {link.from_['name']:<20} - "
        f"{link.relation['label']}: {link.relation['name']:<10} "
        f"-> {link.to['label']}: {link.to['name']}"
    )
