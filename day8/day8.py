import math

# Time Complexity: O(N^2 log N) - Dominated by sorting N^2 distances
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
    return int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2))

def main():
    # points = points[:10]  # Take only the first 10 elements as requested
    points = parse_input('text8.txt')
    
    all_distances = []
    if len(points) >= 2:
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = calculate_distance(points[i], points[j])
                all_distances.append((dist, points[i], points[j]))
    
    # Sort by distance (first element of tuple)
    all_distances.sort(key=lambda x: x[0])
    
    print(f"Calculated {len(all_distances)} distances.")

    chains = []

    for _, p1, p2 in all_distances[:1000]:
        # Find all chains that contain p1 or p2
        params_chains_indices = set()
        for i, chain in enumerate(chains):
            if p1 in chain or p2 in chain:
                params_chains_indices.add(i)
        
        if not params_chains_indices:
            # Neither point is in any chain, create a new one
            chains.append({p1, p2})
        else:
            # Merge all found chains and the new points
            new_chain = {p1, p2}
            # We need to remove indices in reverse order to not mess up indices
            sorted_indices = sorted(list(params_chains_indices), reverse=True)
            
            for index in sorted_indices:
                new_chain.update(chains.pop(index))
            
            chains.append(new_chain)
            
    print(f"Number of chains formed: {len(chains)}")
    chain_lengths = sorted([len(c) for c in chains], reverse=True)
    print(f"All chain lengths: {chain_lengths}")
    
    # Find points not in any chain (if "alone" means not in a chain > 1?)
    # With current logic, every chain is at least size 2.
    # To track "alone", we might need to see which points from input are NOT in union(chains)
    
    points_in_chains = set()
    for c in chains:
        points_in_chains.update(c)
        
    alone_points = [p for p in points if p not in points_in_chains]
    print(f"Points alone (not in any chain): {len(alone_points)}")
    print(f"the first three elements multiplied: {chain_lengths[0]*chain_lengths[1]*chain_lengths[2]}")
"""     if alone_points:
        print(f"Alone points: {alone_points}") """
    

if __name__ == "__main__":
    main()
