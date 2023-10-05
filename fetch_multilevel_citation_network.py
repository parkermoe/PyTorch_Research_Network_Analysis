import requests
from tqdm import tqdm
import json
import networkx as nx

headers = {
    "User-Agent": "...",
    "Accept": "application/json"
}

class DeepCitationNetwork:
    def __init__(self):
        self.papers = {}
    
    def fetch_paper_details(self, paper_id):
        """Fetch detailed information of a specific paper using its ID."""
        base_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
        print(f"Fetching details for paper: {paper_id} from {base_url}")
        response = requests.get(base_url, headers=headers)
        return response.json()
    
    def fetch_paper_citations(self, paper_id, offset=0, limit=100):
        """Fetch citations for a specific paper using its ID."""
        base_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations?fields=contexts,intents,isInfluential,abstract,authors,year,venue,publicationVenue,externalIds,referenceCount,citationCount,fieldsOfStudy,publicationTypes,publicationDate,journal&offset={offset}&limit={limit}"
        print(f"Fetching citations for paper: {paper_id} with offset: {offset}")
        response = requests.get(base_url, headers=headers)
        data = response.json()
        return data.get("data", [])
    
    def expand_network(self, root_paper_id, depth=2):
        """Expand the citation network starting from a specific paper."""
        to_process = [root_paper_id]
        for depth_level in tqdm(range(depth), desc="Expanding citation depth", unit="level"):
            next_to_process = []
            for paper_id in tqdm(to_process, desc="Fetching papers at current depth", unit="paper"):
                if paper_id not in self.papers:
                    details = self.fetch_paper_details(paper_id)
                    offset = 0
                    limit = 100  # we can adjust this
                    citations = []
                    while True:
                        batch_citations = self.fetch_paper_citations(paper_id, offset, limit)
                        if not batch_citations:
                            break
                        citations.extend(batch_citations)
                        offset += limit
                    self.papers[paper_id] = details
                    # If processing the root paper, filter by influential citations only
                    if depth_level == 0:
                        print(f"Paper {paper_id} has {len(citations)} citations.")
                        citations = [citation for citation in citations if citation.get("isInfluential", False)]
                    self.papers[paper_id]['citations'] = citations
                    next_to_process.extend([citation["citingPaper"]["paperId"] for citation in citations])
            to_process = next_to_process


def construct_graph(file_path, original_paper_id):
    with open(file_path, 'r') as f:
        papers_data = json.load(f)
    # Initialize empty dictionaries to store extracted titles, years, and levels
    titles = {}
    years = {}
    levels = {}

    # Iterate through each paper in the dataset
    for paper_id, paper_data in papers_data.items():
        # Extract title
        titles[paper_id] = paper_data.get('title', 'Unknown Title')

        # Extract year
        if 'citingPaper' in paper_data:
            years[paper_id] = paper_data['citingPaper'].get('year', 'N/A')
        else:
            # For the root paper (PyTorch paper), set the year to 2019 as discussed
            years[paper_id] = 2019
    # Level 0: The PyTorch paper
    levels[original_paper_id] = 0
    
    # Level 1: Direct citations of the PyTorch paper
    for citation in papers_data[original_paper_id]['citations']:
        levels[citation['citingPaper']['paperId']] = 1

    # Extract Level 2 papers without modifying the dictionary during iteration
    level_2_papers = []

    for paper_id in list(levels.keys()):
        if levels[paper_id] == 1:
            for citation in papers_data[paper_id].get('citations', []):
                if citation['citingPaper']['paperId'] not in levels:
                    level_2_papers.append(citation['citingPaper']['paperId'])

    # Add Level 2 papers to the levels dictionary
    for paper_id in level_2_papers:
        levels[paper_id] = 2

    # Constructing the graph G using NetworkX
    G = nx.DiGraph()

    # Adding nodes to the graph with attributes title, year, and level
    for paper_id in papers_data.keys():
        G.add_node(paper_id, title=titles[paper_id], year=years[paper_id], level=levels[paper_id])

    # Adding edges to the graph based on citations
    for paper_id, paper_data in papers_data.items():
        for citation in paper_data.get('citations', []):
            citing_paper_id = citation['citingPaper']['paperId']
            if citing_paper_id and paper_id:  # Check for None values
                # Add edge from the citing paper to the current paper
                G.add_edge(citing_paper_id, paper_id)

    # Verifying the graph construction by inspecting the attributes of the first few nodes
    node_attributes = [(node, G.nodes[node]['title'], G.nodes[node]['year'], G.nodes[node]['level']) for node in list(G.nodes)[:5]]
    return node_attributes
