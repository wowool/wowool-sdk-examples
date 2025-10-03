from wowool.portal import Pipeline

# Define the entity relations for the graph
graph_options = {
    "links": [
        {"from": "Person", "to": "City", "relation": "PersonCity"},
        {"from": "Person", "to": "Company", "relation": "PersonCompany"},
    ]
}
# Create the pipeline with English processing, entity recognition, and graph construction
steps = ["english", "entity", {"name": "graph.app", "options": graph_options}]

pipeline = Pipeline(steps)
text = "John Smith lives in New York City. He works at OpenAI."
doc = pipeline(text)
for link in doc.entity_graph:
    print(
        f"{link.from_['label']}:{link.from_['name']} - {link.relation['label']} -> {link.to['label']}:{link.to['name']}"
    )
