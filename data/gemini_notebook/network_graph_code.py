import os
import re
import networkx as nx
import matplotlib.pyplot as plt

# 1. Define name mapping to standardize variant mentions
NAME_MAP = {
    r"\b(Charles|Baxter|MY DEAR BAXTER)\b": "Charles Baxter",
    r"\b(Sidney|Colvin|MY DEAR COLVIN)\b": "Sidney Colvin",
    r"\b(Henley|MY DEAR HENLEY|MY DEAR LAD)\b": "W. E. Henley",
    r"\b(Gosse|Edmund Gosse|Weg)\b": "Edmund Gosse",
    r"\b(Burlingame|MY DEAR BURLINGAME)\b": "E. L. Burlingame",
    r"\b(Meredith|George Meredith)\b": "George Meredith",
    r"\b(Low|W. H. Low)\b": "W. H. Low",
    r"\b(Fanny|my wife)\b": "Fanny Stevenson",
    r"\b(father|papa|my father)\b": "Thomas Stevenson",
    r"\b(mother|MY DEAR MOTHER)\b": "Mrs. Thomas Stevenson",
    r"\b(Tembinoka|King of Apemama)\b": "Tembinoka",
    r"\b(Shaw|Mr. Shaw)\b": "George Bernard Shaw",
    r"\b(Archer)\b": "William Archer",
    r"\b(Stoddard)\b": "C. W. Stoddard",
}

def extract_people_from_text(text):
    found = set()
    for pattern, canonical_name in NAME_MAP.items():
        if re.search(pattern, text, re.IGNORECASE):
            found.add(canonical_name)
    return found

# 2. Process files and build edge weights
folder_path = "./letters/"  # Path to your text files
graph = nx.Graph()

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
            content = f.read()
            people = list(extract_people_from_text(content))
            
            # Add edges for co-occurring pairs
            for i in range(len(people)):
                for j in range(i + 1, len(people)):
                    p1, p2 = people[i], people[j]
                    if graph.has_edge(p1, p2):
                        graph[p1][p2]["weight"] += 1
                    else:
                        graph.add_edge(p1, p2, weight=1)

# 3. Layout and plot
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(graph, k=0.8, seed=42)

# Node sizes based on degree
node_sizes = [graph.degree(node) * 150 for node in graph.nodes()]

nx.draw_networkx_nodes(graph, pos, node_size=node_sizes, node_color="#2b5c8f", alpha=0.85)
nx.draw_networkx_edges(graph, pos, alpha=0.3, edge_color="gray")
nx.draw_networkx_labels(graph, pos, font_size=9, font_weight="bold")

plt.title("Network of People Mentioned Across RLS Letters", fontsize=14, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.savefig("people_network.png", dpi=300)
plt.show()