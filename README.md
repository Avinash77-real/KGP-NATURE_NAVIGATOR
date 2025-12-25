# KGP-NATURE_NAVIGATOR

Project OverviewDeveloped by Avinash , a second-year Computer Science and Engineering student at IIT Kharagpur. This project applies advanced Data Structures and Algorithms  to a real-world campus setting. This navigator was inspired by my love for nature and "sky-gazing," aiming to provide more than just the fastest route—it provides the most refreshing one.Core PhilosophyStandard navigation tools often overlook the user's environment. In this implementation, the campus is modeled as a weighted graph where edges contain both physical distance and a "greenery index."
Users can toggle between: Shortest Path Mode: Standard Dijkstra implementation to minimize travel time.
Scenic Mode: A custom-weighted pathfinding experience that favors tree-lined roads and open spaces.Technical ImplementationGraph Representation: Adjacency list modeling 10+ key landmarks at IIT Kharagpur.Algorithm: Dijkstra’s Algorithm utilizing a Priority Queue (Min-Heap) for $O(E \log V)$ efficiency.
Custom Heuristic: A dynamic cost function : $$Cost =  \frac{Distance}{1 + (Greenery\\_Score \times 0.2)}$$
