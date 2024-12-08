from collections import defaultdict, deque


def longest_puzzle_sequence(puzzle_parts: list[str]) -> str:
    if not puzzle_parts:
        return ""

    # Create a map to store the prefixes
    prefix_map = defaultdict(list)
    for part in puzzle_parts:
        prefix = part[:2]
        prefix_map[prefix].append(part)

    # Helper function to find the longest sequence using DFS
    def sample_dfs(current, visited, sequence):
        visited.add(current)
        suffix = current[-2:]
        
        max_sequence = sequence
        for next_part in prefix_map[suffix]:
            if next_part not in visited:
                sequence += next_part[2:]
                candidate_sequence = sample_dfs(next_part, visited, sequence)
                if len(candidate_sequence) > len(max_sequence):
                    max_sequence = candidate_sequence

        return max_sequence

    # Start DFS for each part and find the longest sequence
    max_sequence = ""
    for part in puzzle_parts:
        visited = set()
        sequence = part
        candidate_sequence = sample_dfs(part, visited, sequence)
        if len(candidate_sequence) > len(max_sequence):
                    max_sequence = candidate_sequence

    return max_sequence

if __name__ == "__main__":
    puzzle_parts = []
    with open("source.txt") as file:
        lines = file.readlines()
        for line in lines:
            puzzle_parts.append(line.strip())

    longest = longest_puzzle_sequence(puzzle_parts)

    print(f"\nМаксимальна послідовність:\n\n{longest}")
    print(f"\nДовжина максимальної послідовності:\n{len(longest)}")

    with open("output.txt", "w") as file:
        file.write(longest)
