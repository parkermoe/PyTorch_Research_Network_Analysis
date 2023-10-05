import requests
from tqdm import tqdm

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
