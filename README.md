## Project Overview

In the evolving landscape of deep learning and artificial intelligence, libraries and frameworks play a pivotal role. PyTorch, as one of the leading libraries in this domain, has seen exponential growth and adoption. This project aims to provide a network analysis of papers related to PyTorch from arXiv, offering insights into the growth of the community, leading figures, and the influence of foundational papers.

---

## Objectives

1. **Data Extraction**: Collect papers pertaining to "PyTorch" from arXiv.
2. **Network Analysis**: Analyze the co-authorship network to identify key figures and trends in the community.
3. **Deep Dive**: Explore how the original PyTorch paper has influenced the research community by examining citations and their impact.

---

## Methodology

1. **Data Collection**: Leveraged the arXiv API to fetch papers related to PyTorch.
2. **Data Storage**: Stored the fetched data in a CSV format for easy access and manipulation.
3. **Network Construction**: Using the `networkx` library, a co-authorship network was constructed. This network represents collaborations between authors, where nodes represent authors and edges represent collaborations.
4. **Network Metrics**: Calculated various network metrics such as Degree Centrality and Betweenness Centrality to identify leading figures in the PyTorch community.

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


By analyzing these network properties and visualizations, we gain a deeper understanding of the collaborative dynamics of the PyTorch research community on arXiv. It's clear that while the community is vast, it remains interconnected through key figures and tight-knit collaboration clusters.

## Future Work

- Delve deeper into the influence of the original PyTorch paper by exploring its citations.
- Analyze the growth of the PyTorch community over time by examining publication dates and new authors entering the community.
- Explore topic trends by analyzing the categories and abstracts of the papers.


