from wowool.sdk import Pipeline
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

try:
    from wowool.entity_graph import CollectedResults
except ImportError:
    # Fallback if wowool.entity_graph is not available
    CollectedResults = None

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


def plot_knowledge_graph(df):
    """
    Plot a knowledge graph from a dataframe of triples with label-based coloring
    """
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges from the dataframe
    for _, row in df.iterrows():
        # Add nodes with their labels
        G.add_node(row["from_name"], label=row["from_label"], node_type="entity")
        G.add_node(row["to_name"], label=row["to_label"], node_type="entity")

        # Add edge with relationship label
        G.add_edge(
            row["from_name"],
            row["to_name"],
            relation=row["rel_name"],
            label=row["rel_label"],
        )

    # Create the plot
    plt.figure(figsize=(14, 10))

    # Use spring layout for better node positioning
    pos = nx.spring_layout(G, k=3, iterations=50, seed=42)

    # Define color mapping based on node labels
    label_colors = {
        "Subject": "#FF6B6B",  # Red for Subject (usually Person)
        "Object": "#4ECDC4",  # Teal for Object (can be Location, Organization, etc.)
        "Person": "#FF6B6B",  # Red for Person
        "Location": "#4ECDC4",  # Teal for Location
        "City": "#4ECDC4",  # Teal for City
        "Organization": "#45B7D1",  # Blue for Organization
        "Company": "#45B7D1",  # Blue for Company
        "VP": "#FFA07A",  # Light salmon for Verb Phrase
        "Verb": "#FFA07A",  # Light salmon for Verb
        "default": "#95A5A6",  # Gray for unknown types
    }

    # Get node colors and sizes based on their labels
    node_colors = []
    node_sizes = []
    node_labels_dict = {}

    for node in G.nodes(data=True):
        node_name = node[0]
        node_data = node[1]
        node_label = node_data.get("label", "default")

        # Get color based on label
        color = label_colors.get(node_label, label_colors["default"])
        node_colors.append(color)

        # Set size based on node type (Subject nodes are typically larger)
        if node_label == "Subject":
            node_sizes.append(3500)  # Increased size for better text fit
        else:
            node_sizes.append(3000)  # Increased size for better text fit

        # Create display label with truncated name if too long
        if len(node_name) > 12:
            short_name = node_name[:10] + "..."
        else:
            short_name = node_name

        # Create display label with both name and type
        display_label = f"{short_name}\n({node_label})"
        node_labels_dict[node_name] = display_label

    # Draw the nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        node_size=node_sizes,
        alpha=0.8,
        edgecolors="black",
        linewidths=2,
    )

    # Draw edges
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="gray",
        arrows=True,
        arrowsize=20,
        arrowstyle="->",
        width=2,
        alpha=0.7,
        connectionstyle="arc3,rad=0.1",
    )

    # Add node labels with both name and type
    nx.draw_networkx_labels(
        G,
        pos,
        labels=node_labels_dict,
        font_size=8,  # Reduced font size for better fit
        font_weight="bold",
        font_color="white",
        verticalalignment="center",
        horizontalalignment="center",
    )

    # Add edge labels (relationships)
    edge_labels = {}
    for edge in G.edges(data=True):
        # Use both relation name and label for edge labels
        rel_name = edge[2]["relation"]
        rel_label = edge[2]["label"]
        edge_labels[(edge[0], edge[1])] = f"{rel_name}\n({rel_label})"

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels,
        font_size=8,
        font_color="darkred",
        bbox=dict(
            boxstyle="round,pad=0.3", facecolor="white", alpha=0.9, edgecolor="gray"
        ),
    )

    plt.title(
        "Wowool Knowledge Graph: Relationships and Entities",
        fontsize=14,
        fontweight="bold",
        pad=20,
    )
    plt.axis("off")
    plt.tight_layout()

    # Create dynamic legend based on actual labels in the graph
    unique_labels = set()
    for node in G.nodes(data=True):
        unique_labels.add(node[1].get("label", "default"))

    legend_elements = []
    for label in sorted(unique_labels):
        color = label_colors.get(label, label_colors["default"])
        # Create a simple rectangle patch for legend
        legend_elements.append(
            Rectangle((0, 0), 1, 1, facecolor=color, edgecolor="black", label=label)
        )

    plt.legend(
        handles=legend_elements,
        loc="upper right",
        fontsize=10,
        title="Node Types",
        title_fontsize=11,
    )

    plt.show()

    return G


# Plot the network
print("\n" + "=" * 50)
print("PLOTTING KNOWLEDGE GRAPH")
print("=" * 50)
graph = plot_knowledge_graph(df)

# Print graph statistics
print("\nGraph Statistics:")
print(f"Number of nodes: {graph.number_of_nodes()}")
print(f"Number of edges: {graph.number_of_edges()}")
print(f"Nodes: {list(graph.nodes())}")
print(f"Edges: {list(graph.edges())}")
