from wowool.sdk import Pipeline
from wowool.entity_graph import CollectedResults
from wowool.document import Document
import pandas as pd

# Define the entity relations for the graph
graph_options = {
    "nodes": {"_doc_": {"label": "Document", "name": "document.id"}},
    "themes": {"to": "_doc_"},
    "topics": {"to": "_doc_"},
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
        "text": "John Smith works on the stock exchange market . He recommends to by OpenAI stock.",
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
    links = doc.results("wowool_entity_graph")
    merged_result = CollectedResults(links).merge()
    df = pd.DataFrame(merged_result.rows)
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)
# keep only the rows 'from_name' and 'to_name'
df = df[["from_name", "to_name", "rel_label"]]

print("DATAFRAME\n", df)
