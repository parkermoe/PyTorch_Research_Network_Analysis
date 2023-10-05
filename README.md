## Project Overview

In the rapidly evolving field of deep learning and artificial intelligence, libraries such as PyTorch have become foundational elements of the research landscape. This project takes a multi-dimensional approach to analyze the growth and influence of PyTorch in the scientific community. Initially centered on co-authorship networks, the project has now expanded to include multi-level citation analysis, offering a holistic view of how PyTorch has influenced and propagated throughout the research world.

---

## Objectives

1. **Data Extraction**: Collect papers pertaining to "PyTorch" from arXiv.
2. **Network Analysis**: Analyze the co-authorship network to identify key figures and trends in the community.
3. **Co-Authorship Network Analysis**: Explore the community around PyTorch research by analyzing the co-authorship network.
4. **Deep Dive**: Explore how the original PyTorch paper has influenced the research community by examining citations and their impact.
5.  **Citation Network Analysis**: Investigate the influence and propagation of PyTorch papers by constructing and analyzing a multi-level citation network.

---

## Methodology

1. **Data Collection**: Utilized the arXiv API and the Semantic Scholar API to collect papers and their citations.
2. **Data Storage**: Stored the fetched data in JSON and CSV formats for manipulation and analysis.
3. **Network Construction**: Using the `networkx` library, a co-authorship network was constructed. This network represents collaborations between authors, where nodes represent authors and edges represent collaborations. This was ultimately  extended to multi-level citation networks.
4. **Network Metrics**: Calculated various network metrics such as Degree Centrality and Betweenness Centrality to identify leading figures in the PyTorch community.
5. **Interactive Visualization**: Leveraged Plotly and Pyvis to create interactive visualizations of the networks.

---

## Insights

### Leading Figures in the Co-authorship Network

By analyzing the co-authorship network, we identified key figures within the PyTorch community based on various centrality measures:

- **Degree Centrality**: This metric provides insights into the most connected authors in the co-authorship network, signifying those who have collaborated with the most number of unique authors.
 - Notable authors include Liang Luo, Dheevatsa Mudigere, and Jianyu Huang, as can be seen in the Degree Centrality bar chart below.
  
- **Betweenness Centrality**: Authors such as Soumith Chintala and Shinji Watanabe top this list, indicating their role as bridges in the co-authorship network. Their collaborations with diverse groups of authors potentially connect separate communities within the network, as visualized in the Betweenness Centrality bar chart below.

![image](https://github.com/parkermoe/PyTorch_Research_Network_Analysis/assets/75709283/e52d9a7a-7986-483e-8b1a-860c4e6b75cb)

### Network Properties and Assumptions

The co-authorship network displays several interesting properties commonly seen in real-world collaboration networks:

![image](https://github.com/parkermoe/PyTorch_Research_Network_Analysis/assets/75709283/f1a9e2b5-acac-4512-96b0-5030526e8bfc)

1. **Average Shortest Path Length**: The average number of collaborations it takes to connect any two authors in the network is approximately \(7.18\), suggesting a relatively close-knit community.
  
2. **Power Law Degree Distribution**: The network's degree distribution follows a power-law pattern, typical of many real-world networks. While most authors collaborate with only a few others, a small subset acts as collaboration hubs. This distribution can be observed in the Degree Distribution figure below.

![image](https://github.com/parkermoe/PyTorch_Research_Network_Analysis/assets/75709283/42e660cb-201e-41aa-91a0-7e63e819e5b8)

  
4. **Network Diameter**: The longest shortest path between any two authors in the network spans 19 collaborations.
  
5. **High Clustering Coefficient**: With an average clustering coefficient of approximately \(0.902\), the co-authorship network shows that authors tend to form tight-knit clusters or groups. This pattern suggests that collaborations are not random; instead, authors often collaborate in groups, leading to high interconnectedness within these groups. The structure of these clusters can be explored in the Network Visualization figure below.





## Yearly Analysis of the Co-authorship Network

Visualizing the co-authorship network's expansion over the years provides a dynamic perspective on the PyTorch research community's growth on arXiv. From our interactive visualization (refer to the Co-authorship Network over the Years figure below), we observed:

1. **Rapid Expansion**: The network has seen a consistent growth year-on-year, reflecting the escalating interest and research activities around PyTorch.
2. **Emergence of Key Players**: Over time, certain authors have established themselves as central figures in the network, evident from their high number of collaborations. These authors often act as pillars, driving research and fostering collaborations.
3. **Collaborative Nature**: The PyTorch community showcases a strong collaborative spirit, with researchers frequently partnering to contribute to the field. This trend is underscored by the formation of tightly-knit clusters within the network.

These insights not only spotlight the growth of the PyTorch community but also underline the collaborative ethos that characterizes research in the deep learning domain.

![My Animation](https://github.com/parkermoe/PyTorch_Research_Network_Analysis/blob/main/pytorch_year_output2.gif)


By analyzing these network properties and visualizations, we can gain a deeper understanding of the collaborative dynamics of the PyTorch research community on arXiv. It's clear that while the community is vast, it remains interconnected through key figures and tight-knit collaboration clusters.

## Multi-Level Citation Network Analysis

In addition to co-authorship networks, this project also provides a multi-level citation network analysis centered around the original PyTorch paper. This analysis offers a deeper understanding of the paper's influence in the research community.

### Visualization

The visualization displays a three-level citation network:

- **Red Node**: Represents the original PyTorch paper.
- **Blue Nodes**: Papers that have cited the original PyTorch paper.
- **Green Nodes**: Papers that are cited by the blue node papers.

This enables us to see not just the direct impact of the original PyTorch paper, but also its secondary influence on subsequent research.

![PyTorch Citation Network](https://github.com/parkermoe/PyTorch_Research_Network_Analysis/blob/main/pytorch_citation_output_fast.gif)

### Applications and Insights

This kind of multi-level citation network can provide invaluable insights for various stakeholders:

1. **Influence Propagation**: The original PyTorch paper has been cited by a diverse set of research areas, indicating its wide-ranging impact.
2. **Key Influencers**: Identified papers that have been most influential in propagating the citations of the original PyTorch paper.
3. **Citation Dynamics**: Observed how citation patterns evolve over time, providing insights into emerging areas influenced by PyTorch.

#### For Researchers:
- Identify pivotal papers and trends in the PyTorch ecosystem.
- Understand the secondary influence of the original PyTorch paper on different fields of study.

#### For Companies Selling Complementary Tools:
- Companies selling tools or services that complement PyTorch can use this analysis to identify key papers and authors who are deeply involved in PyTorch-related research.
- By engaging these authors, either through collaboration or by offering specialized tools that could aid their research, companies have an opportunity to gain visibility and credibility within the research community, thereby increasing demand for their products.

By offering a multi-dimensional view that goes beyond simple citation counts, this analysis provides a nuanced understanding of influence and impact in the research landscape surrounding PyTorch.

1. **Influence Propagation**: The original PyTorch paper has been cited by a diverse set of research areas, indicating its wide-ranging impact.
2. **Key Influencers**: Identified papers that have been most influential in propagating the citations of the original PyTorch paper.
3. **Citation Dynamics**: Observed how citation patterns evolve over time, providing insights into emerging areas influenced by PyTorch.

## Future Work

- Further analysis of topic trends by examining the categories and abstracts of the papers.
- Incorporate more sophisticated network metrics to understand the complex relationships in both co-authorship and citation networks.
- Extend the multi-level citation analysis to explore the influence of other foundational papers in the deep learning landscape.


