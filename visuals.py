import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from itertools import combinations
import plotly.graph_objects as go
from networkx import spring_layout


def visualize_graph(G):
    """Visualize the co-authorship graph."""
    
    # Define node positions using a spring layout
    pos = nx.spring_layout(G)
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=50, alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.7)
    
    # Display the graph
    plt.title("Co-authorship Network")
    plt.axis("off")
    plt.show()



def build_network_for_year(df, year):
    """
    Build a co-authorship network for papers up to the given year.
    
    Parameters:
    - df (pd.DataFrame): DataFrame containing paper details.
    - year (int): The year up to which the papers should be considered.
    
    Returns:
    - NetworkX Graph: Co-authorship network for the specified year range.
    """
    
    # Filter the DataFrame for papers up to the given year
    df_year = df[df['year'] <= year]
    
    # Initialize an empty graph
    G = nx.Graph()
    
    # Iterate over each row in the DataFrame to extract authors
    for _, row in df_year.iterrows():
        authors = eval(row['authors'])  # Convert the string representation of list to an actual list
        
        # Add nodes (authors) to the graph
        for author in authors:
            if G.has_node(author):
                G.nodes[author]['papers'] += 1  # Increment paper count for the author
            else:
                G.add_node(author, papers=1)   # Initialize with 1 paper for the author
        
        # Add edges between co-authors
        for author1, author2 in combinations(authors, 2):
            if G.has_edge(author1, author2):
                G[author1][author2]['weight'] += 1  # Increase weight if edge already exists
            else:
                G.add_edge(author1, author2, weight=1)  # Initialize edge with weight 1
    
    return G

def prepare_data_for_plotly(G):
    """
    Prepare data from a NetworkX graph for Plotly visualization.
    
    Parameters:
    - G (NetworkX Graph): The graph to be visualized.
    
    Returns:
    - tuple: Tuple containing data required for Plotly visualization.
    """
    
    # Get positions for the nodes in G
    pos = spring_layout(G)
    
    # Create lists to hold node and edge data
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]
    
    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('# of connections: '+str(len(adjacencies[1])))
    
    return edge_x, edge_y, node_x, node_y, node_adjacencies, node_text

def visualize_network_with_slider(yearly_networks):
    """Create an interactive network visualization with a time-slider (corrected version)."""
    
    # List to hold plotly figures for each year
    fig_data = []
    
    for year, G in yearly_networks.items():
        edge_x, edge_y, node_x, node_y, node_adjacencies, node_text = prepare_data_for_plotly(G)
        
        # Create edge trace for Plotly
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')
        
        # Create node trace for Plotly
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))
        
        node_trace.marker.color = node_adjacencies
        node_trace.text = node_text
        
        fig_data.append([edge_trace, node_trace])
    
    # Create the figure with a slider for each year
    fig = go.Figure(data=fig_data[0], layout=go.Layout(
        title='Co-authorship Network for PyTorch over the Years',
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        updatemenus=[dict(type='buttons', showactive=False,
                          buttons=[dict(label='Play',
                                        method='animate', args=[None, dict(frame=dict(duration=1000, redraw=True), fromcurrent=True)])])],
        sliders=[dict(steps=[])]
    ))
    
    # Add frames for each year
    frames = [go.Frame(data=fig_data[i], name=str(year)) for i, year in enumerate(yearly_networks.keys())]
    fig.frames = frames
    
    # Corrected: Add slider steps
    slider_steps = []
    for i, year in enumerate(yearly_networks.keys()):
        step = dict(
            args=[[str(year)], dict(frame=dict(duration=1000, redraw=True), mode='immediate')],
            method='animate',
            label=str(year)
        )
        slider_steps.append(step)
    fig.layout.sliders[0]['steps'] = slider_steps
    
    fig.show()