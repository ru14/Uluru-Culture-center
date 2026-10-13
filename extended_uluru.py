import matplotlib.pyplot as plt
import networkx as nx

NODE_STYLES = {
    "agent": ("#6495ED", "o", 2800),
    "tool":  ("#FFD700", "s", 2600),
    "user":  ("#FF6347", "d", 2400),
    "data":  ("#90EE90", "h", 2500),
}
DEFAULT_STYLE = ("#C0C0C0", "p", 2300)


def create_diagram(title, nodes, edges, pos, node_labels=None,
                   node_types=None, edge_labels=None):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    node_labels = node_labels or {n: n.replace(" ", "\n") for n in nodes}
    node_types = node_types or {n: "agent" for n in nodes}
    edge_labels = edge_labels or {}

    missing = [n for n in nodes if n not in pos]
    if missing:
        raise ValueError(f"Missing positions for nodes: {missing}")

    plt.figure(figsize=(16, 8))
    plt.title(title, fontsize=16, fontweight="bold", pad=20)

    for node in nodes:
        color, shape, size = NODE_STYLES.get(node_types.get(node), DEFAULT_STYLE)
        nx.draw_networkx_nodes(graph, pos, nodelist=[node], node_color=[color],
                               node_shape=shape, node_size=size,
                               edgecolors="black", linewidths=1.5, alpha=0.9)

    nx.draw_networkx_edges(graph, pos, edge_color="black", arrowsize=25,
                           width=2.0, alpha=0.9, arrowstyle="-|>",
                           connectionstyle="arc3,rad=0.15",
                           node_size=2800)

    for node, (x, y) in pos.items():
        plt.text(x, y, node_labels[node], fontsize=9, ha="center", va="center",
                 fontweight="bold",
                 bbox=dict(facecolor="white", alpha=0.8, edgecolor="lightgray",
                           boxstyle="round,pad=0.4"))

    for (src, dst), label in edge_labels.items():
        x1, y1 = pos[src]
        x2, y2 = pos[dst]
        plt.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.2, label, fontsize=10,
                 ha="center", va="center", fontweight="bold", color="darkblue",
                 bbox=dict(facecolor="white", alpha=0.9, edgecolor="blue",
                           boxstyle="round,pad=0.3"))

    legend_elements = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#6495ED", markersize=15, label="Agent"),
        plt.Line2D([0], [0], marker="s", color="w", markerfacecolor="#FFD700", markersize=15, label="Tool/Resource"),
        plt.Line2D([0], [0], marker="d", color="w", markerfacecolor="#FF6347", markersize=15, label="User Interface"),
        plt.Line2D([0], [0], marker="h", color="w", markerfacecolor="#90EE90", markersize=15, label="Data Component"),
    ]
    plt.legend(handles=legend_elements, loc="upper right", fontsize=11)

    plt.axis("off")
    plt.tight_layout()

    filename = title.replace(" ", "_").replace(":", "") + ".png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    print(f"Diagram saved as: {filename}")
    plt.close()


def extended_uluru_exercise():
    nodes = [
        "Visitor Input",
        "Language Identification",
        "Arrernte Language Specialist",
        "Pitjantjatjara Language Specialist",
        "Knowledge Base Lookup",
        "Cultural Sensitivity Checker",
        "Translation Verification Agent",
    ]

    edges = [
        ("Visitor Input", "Language Identification"),
        ("Language Identification", "Arrernte Language Specialist"),
        ("Language Identification", "Pitjantjatjara Language Specialist"),
        ("Arrernte Language Specialist", "Knowledge Base Lookup"),
        ("Pitjantjatjara Language Specialist", "Knowledge Base Lookup"),
        ("Knowledge Base Lookup", "Cultural Sensitivity Checker"),
        ("Cultural Sensitivity Checker", "Arrernte Language Specialist"),
        ("Cultural Sensitivity Checker", "Pitjantjatjara Language Specialist"),
        ("Arrernte Language Specialist", "Translation Verification Agent"),
        ("Pitjantjatjara Language Specialist", "Translation Verification Agent"),
        ("Translation Verification Agent", "Visitor Input"),
    ]

    node_types = {
        "Visitor Input": "user",
        "Language Identification": "tool",
        "Arrernte Language Specialist": "agent",
        "Pitjantjatjara Language Specialist": "agent",
        "Knowledge Base Lookup": "tool",
        "Cultural Sensitivity Checker": "tool",
        "Translation Verification Agent": "agent",
    }

    edge_labels = {
        ("Knowledge Base Lookup", "Cultural Sensitivity Checker"): "Raw Knowledge",
        ("Cultural Sensitivity Checker", "Arrernte Language Specialist"): "Approved Content",
        ("Translation Verification Agent", "Visitor Input"): "Formatted Response",
    }

    h, v = 1.0, 0.7
    pos = {
        "Visitor Input": (0, 0),
        "Language Identification": (h, 0),
        "Arrernte Language Specialist": (2 * h, v),
        "Pitjantjatjara Language Specialist": (2 * h, -v),
        "Knowledge Base Lookup": (3 * h, 0),
        "Cultural Sensitivity Checker": (4 * h, 0),
        "Translation Verification Agent": (3 * h, 2 * v),
    }

    create_diagram("Uluru Cultural Center: Extended System",
                   nodes, edges, pos, None, node_types, edge_labels)


if __name__ == "__main__":
    extended_uluru_exercise()
