# pfs_all_in_one
Priority first search for: Prim's minimal spanning tree
and Dijkstra's single source shortest path, plus bfs and dfs,
all in one program


Using pfs.py:

1. `pip3 install pqdict` See [priority-queue-dictionary](https://github.com/nvictus/priority-queue-dictionary) about this library.
2. `python3 pfs.py -h` to see help messages
3. The data file 2.gr is the example graph from
   [geeksforgeeks's Dijkstra tutorial](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/)

Example usages:

    python3 pfs.py -a bfs 2.gr		# breadth first search
    python3 pfs.py -a dfs 2.gr		# depth first search
    python3 pfs.py -a prim 2.gr		# Prim's minimal spanning tree
    python3 pfs.py -a dijk 2.gr		# Dijkstra's shortest path
    python3 pfs.py -a dijk -0 Z 2.gr	# Dijkstra's shortest path,
					# starting from vertex Z
