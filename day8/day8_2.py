import math

# Time Complexity: O(N^2 log N) - Dominated by sorting pairwise distances. 
# Union-Find operations are nearly O(1).
def parse_input(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                x, y, z = map(int, parts)
                points.append((x, y, z))
    return points

def calculate_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return int((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def main():
    points = parse_input('test8.txt')
    
    all_distances = []
    if len(points) >= 2:
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = calculate_distance(points[i], points[j])
                all_distances.append((dist, points[i], points[j]))
    
    # Sort by distance (first element of tuple)
    all_distances.sort(key=lambda x: x[0])
    
    print(f"Calculated {len(all_distances)} distances.")
    print(f"Calculated {len(all_distances)} distances.")
    
    # Optimization: Map point -> chain_index in the 'chains' list
    # Because we remove items from 'chains', indices shift. 
    # Whatever, let's just use sets but keep the list structure for the final output requested.
    # Actually, DSU (Union-Find) is best here.
    
    parent = {p: p for p in points}
    def find(p):
        if parent[p] != p:
            parent[p] = find(parent[p])
        return parent[p]

    def union(p1, p2):
        root1 = find(p1)
        root2 = find(p2)
        if root1 != root2:
            parent[root2] = root1
            return True # Merged
        return False # Already connected

    num_components = len(points)
    
    for _, p1, p2 in all_distances:
        root1 = find(p1)
        root2 = find(p2)
        
        if root1 != root2:
            # If 2 components left and we are merging them -> This is it!
            if num_components == 2:
                print(f"Final merge! The pair connecting the last two chains is: {p1} and {p2}")
                print(f"Distance between them: {int((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)}")
                chain_last_merge = (p1, p2)
            
            union(p1, p2)
            num_components -= 1
            
    # Now reconstruct the chains list for compatibility with existing print code
    # Group points by root
    from collections import defaultdict
    groups = defaultdict(list)
    for p in points:
        groups[find(p)].append(p)
    
    chains = list(groups.values())
            
    print(f"Number of chains formed: {len(chains)}")
    chain_lengths = sorted([len(c) for c in chains], reverse=True)
    print(f"All chain lengths: {chain_lengths}")
    
    # Check if we have 2 chains
    if len(chains) == 2:
        print(f"Product of lengths of the two chains: {chain_lengths[0] * chain_lengths[1]}")
    
    # Find the actual longest chain
    longest_chain_content = max(chains, key=len)
    print(f"Longest chain content ({len(longest_chain_content)} points):")
    print(longest_chain_content)
    
    # Find points not in any chain (if "alone" means not in a chain > 1?)
    # With current logic, every chain is at least size 2.
    # To track "alone", we might need to see which points from input are NOT in union(chains)
    
    points_in_chains = set()
    for c in chains:
        points_in_chains.update(c)
        
    alone_points = [p for p in points if p not in points_in_chains]
    print(f"Points alone (not in any chain): {len(alone_points)}")
    if alone_points:
        print(f"Alone points: {alone_points}")


if __name__ == "__main__":
    main()
