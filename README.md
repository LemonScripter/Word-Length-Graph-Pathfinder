# Word Length Graph Pathfinder

## Overview
This project implements a specialized graph-based text analysis tool that creates paths between words and phrases based on their lengths. The algorithm can find word patterns in texts while handling inflected forms of words (particularly important for agglutinative languages like Hungarian).

## Algorithm Logic

The algorithm works in several phases:

1. **Text Processing**
   - Splits text into words and phrases
   - Creates groups based on word and phrase lengths
   - Handles special characters and accented letters

2. **Graph Construction**
   - Creates nodes for each word/phrase length
   - Builds edges between adjacent lengths
   - Weights connections based on frequency

3. **Path Finding**
   - Implements both optimized and breadth-first search
   - Handles word variations and inflected forms
   - Creates paths between different length patterns

## Performance Analysis

We compared our optimized search algorithm with breadth-first search (BFS). The results show significant improvements:

![Algorithm Comparison](https://github.com/LemonScripter/Word-Length-Graph-Pathfinder/blob/main/comparasion.png)

The graphs show three key metrics:
- **Runtime Comparison**: Our optimized algorithm shows significantly better performance (near-zero runtime compared to BFS)
- **Nodes Visited**: Both algorithms visit the same number of nodes, ensuring thorough coverage
- **Edges Traversed**: The optimized algorithm examines fewer edges (113 vs 621), demonstrating better efficiency

## Graph Structure

![Phrase Length Graph](https://github.com/LemonScripter/Word-Length-Graph-Pathfinder/blob/main/phrae_lengt.png)

The graph visualization shows:
- Nodes representing different phrase lengths (numbers indicate character count)
- Node size indicating number of phrases of that length
- Edges showing connections between different lengths
- Clear clustering of common phrase lengths in the center

## Future Development

Currently, the algorithm has only been compared with breadth-first search. Future work will include:
- Comparison with Dijkstra's algorithm
- Implementation of A* search
- Testing against other pathfinding algorithms
- Optimization for larger text corpora

## Installation and Usage

For detailed installation and running instructions, please check the `futtatas_running.txt` file in the repository.

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License.

## Contact

- Website: [lemonscript.info](https://lemonscript.info)
- Author: László SZŐKE
