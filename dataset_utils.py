import requests
import csv
from typing import List, Dict
import xml.etree.ElementTree as ET
import networkx as nx
from itertools import combinations

class ArxivPyTorchPapers:
    """A class to interact with arXiv API to fetch, save, and load papers related to a keyword."""
    
    def __init__(self):
        """Initialize the ArxivPyTorchPapers object with base URL and an empty set for fetched paper IDs."""
        self.base_url = "http://export.arxiv.org/api/query?"
        self.fetched_paper_ids = set()
        
    def _parse_xml(self, xml_content: bytes) -> List[Dict]:
        """Parse the XML content from arXiv API and extract paper details.
        
        Args:
        - xml_content (bytes): XML content received from the arXiv API.
        
        Returns:
        - List[Dict]: A list of dictionaries, each containing details of a paper.
        """
        root = ET.fromstring(xml_content)
        
        papers = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            paper = {
                'id': entry.find("{http://www.w3.org/2005/Atom}id").text,
                'title': entry.find("{http://www.w3.org/2005/Atom}title").text,
                'authors': [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")],
                'published_date': entry.find("{http://www.w3.org/2005/Atom}published").text,
                'abstract': entry.find("{http://www.w3.org/2005/Atom}summary").text,
                'categories': entry.find("{http://arxiv.org/schemas/atom}primary_category").attrib['term']
            }
            papers.append(paper)
        return papers

    def fetch_papers(self, keyword: str = "PyTorch", max_results: int = 100) -> List[Dict]:
        """Fetch unique papers from arXiv based on the keyword.
        
        Args:
        - keyword (str): The keyword to search for in arXiv.
        - max_results (int): Maximum number of papers to fetch.
        
        Returns:
        - List[Dict]: A list of dictionaries, each containing details of a unique paper.
        """
        query_url = f"{self.base_url}search_query=all:{keyword}&start=0&max_results={max_results}"
        response = requests.get(query_url)
        all_papers = self._parse_xml(response.content)
        unique_papers = [paper for paper in all_papers if paper['id'] not in self.fetched_paper_ids]
        self.fetched_paper_ids.update([paper['id'] for paper in unique_papers])
        return unique_papers

    def extract_authors(self, papers: List[Dict]) -> List[str]:
        """Extract all unique authors from the list of papers.
        
        Args:
        - papers (List[Dict]): A list of dictionaries containing paper details.
        
        Returns:
        - List[str]: A list of unique authors.
        """
        authors = set()
        for paper in papers:
            authors.update(paper['authors'])
        return list(authors)

    def save_to_csv(self, papers: List[Dict], filename: str = "arxiv_pytorch_papers.csv"):
        """Save the paper data to a CSV file.
        
        Args:
        - papers (List[Dict]): A list of dictionaries containing paper details.
        - filename (str): The name of the CSV file to save the data.
        """
        headers = ["id", "title", "authors", "published_date", "abstract", "categories"]
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(papers)

    def load_existing_papers(self, filename: str) -> List[Dict]:
        """Load existing papers from a CSV file.
        
        Args:
        - filename (str): The name of the CSV file to load the data from.
        
        Returns:
        - List[Dict]: A list of dictionaries containing details of loaded papers.
        """
        papers = []
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    papers.append(row)
                    self.fetched_paper_ids.add(row['id'])
        except FileNotFoundError:
            pass
        return papers

    def update_csv_with_new_papers(self, filename: str, keyword: str = "PyTorch", max_results: int = 100):
        """Update the CSV with new papers.
        
        Args:
        - filename (str): The name of the CSV file to update.
        - keyword (str): The keyword to search for in arXiv.
        - max_results (int): Maximum number of new papers to fetch and add.
        """
        existing_papers = self.load_existing_papers(filename)
        new_papers = self.fetch_papers(keyword=keyword, max_results=max_results)
        combined_papers = existing_papers + new_papers
        self.save_to_csv(combined_papers, filename)

        
def build_coauthorship_network(df):
    """Build a co-authorship network from a DataFrame of papers and authors.
    
    Args:
    - df (pd.DataFrame): A DataFrame containing paper details with an 'authors' column.
    
    Returns:
    - nx.Graph: A NetworkX Graph object representing the co-authorship network.
    """
    G = nx.Graph()
    for _, row in df.iterrows():
        authors = eval(row['authors'])
        for author in authors:
            G.add_node(author, papers=G.nodes.get(author, {}).get('papers', 0) + 1)
        for author1, author2 in combinations(authors, 2):
            if G.has_edge(author1, author2):
                G[author1][author2]['weight'] += 1
            else:
                G.add_edge(author1, author2, weight=1)
    return G
