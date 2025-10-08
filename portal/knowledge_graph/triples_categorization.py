from wowool.portal import Pipeline
from wowool.document import Document
import pandas as pd

# Define the entity relations for the graph
graph_options = {
    "nodes": {"_doc_": {"label": "Document", "name": "document.id"}},
    "themes": {"to": "_doc_"},
    "topics": {"to": "_doc_"},
    "output_format": "table",
}
# Create the pipeline with English processing, syntax, entity recognition, and graph construction
steps = [
    "english",
    "syntax",
    "entity",
    "semantic-theme",
    "themes.app",
    "topics.app",
    {"name": "graph.app", "options": graph_options},
]

documents = [
    {
        "id": "doc_finance.txt",
        "text": "John Smith works on the stock exchange market . He recommends to buy OpenAI stock.",
    },
    {
        "id": "doc_sports.txt",
        "text": "John Smith has played football in the national team. He also likes basketball",
    },
]


pipeline = Pipeline(steps)
dfs = []
for data in documents:
    doc = Document.create(data=data["text"], id=data["id"])
    doc = pipeline(doc)
    df = pd.DataFrame(doc.entity_graph)
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)
# keep only the rows 'from_name' and 'to_name'
df = df[["from_name", "to_name", "rel_label"]]

print("Topics and themes per document\n", df)
