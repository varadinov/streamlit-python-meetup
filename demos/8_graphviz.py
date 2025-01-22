import streamlit as st
import graphviz

# Title of the App
st.title("Code Block Diagram with Graphviz (Conditional Blocks)")

# Sidebar Input for Nodes and Edges
st.sidebar.header("Diagram Input")
nodes_input = st.sidebar.text_area(
    "Enter block names and types (format: name:type, one per line)", 
    "Start:rect\nDecision:diamond\nProcess:rect\nEnd:rect"
)
edges_input = st.sidebar.text_area(
    "Define connections (format: from -> to, one per line)", 
    "Start -> Decision\nDecision -> Process\nProcess -> End\nDecision -> End"
)

# Parse nodes and edges
def parse_nodes(nodes_input):
    nodes = {}
    for line in nodes_input.splitlines():
        try:
            name, block_type = line.split(":")
            nodes[name.strip()] = block_type.strip()
        except ValueError:
            st.warning(f"Invalid node format: {line}. Use 'name:type'.")
    return nodes

def parse_edges(edges_input):
    edges = []
    for line in edges_input.splitlines():
        try:
            from_node, to_node = line.split("->")
            edges.append((from_node.strip(), to_node.strip()))
        except ValueError:
            st.warning(f"Invalid edge format: {line}. Use 'from -> to'.")
    return edges

# Generate Graphviz Diagram
def create_diagram(nodes, edges):
    graph = graphviz.Digraph()
    # Add nodes with shapes
    for node, block_type in nodes.items():
        graph.node(node, shape=block_type)  # Default shape
    # Add edges
    for from_node, to_node in edges:
        graph.edge(from_node, to_node)
    return graph

# Parse inputs
nodes = parse_nodes(nodes_input)
edges = parse_edges(edges_input)

# Render the Diagram
diagram = create_diagram(nodes, edges)
st.graphviz_chart(diagram)