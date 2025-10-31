# TODO: Activity Selection Problem (Greedy: choose earliest finishing activity)

from typing import List, Tuple
def activity_selection(activities: List[Tuple[int, int]]) -> List[int]:
    """
    Activities: List of (Start, End)
    Returns lit of indices (into original input) of the maximum set of non-overlapping activities.
    """
    # Attach original indices so we can return them after sorting.
    indexed = sorted(enumerate(activities), key=lambda x: x[1][1]) # Sort by end time
    selected_indices = []

    last_end = -10**18 # Small Sentinel
    for idx, (start, end) in indexed:
        if start >= last_end:
            selected_indices.append(idx)
            last_end = end

    # Return in order of selection (not necessarily sorted by original index)
    return selected_indices

def activity_selection_verbose(activities: List[Tuple[int, int]]) -> List[Tuple[int, Tuple[int, int]]]:
    """
    Same as Activity Selection but returns (original_Index, (start, end)) for clarity.
    """
    indexed = sorted(enumerate(activities), key=lambda x: x[1][1])
    selected = []
    last_end = -10**18
    for idx, (start, end) in indexed:
        if start >= last_end:
            selected.append((idx, (start, end)))
            last_end = end

    return selected

if __name__ == "__main__":
    # Example 1
    activities1 = [(1,4), (3,6), (2,3), (5,7), (8,9), (5,9)]
    # Explanation: sorted by end => (2,3),(1,4),(3,6),(5,7),(8,9),(5,9)
    # Pick (2,3), then (3,6) starts 3 >= 3 -> pick, (5,7) overlaps with (3,6) skip, (8,9) pick => result indices match original input
    print("Example 1 activities (start,end):", activities1)
    sel = activity_selection_verbose(activities1)
    print("Selected (index, interval):", sel)
    print("Selected indices (original):", activity_selection(activities1))
    print()

    # Example 2 (classic)
    activities2 = [(0,6), (1,4), (3,5), (5,7), (5,9), (8,9)]
    # optimal selection: (1,4),(4? none),(5,7),(8,9) -> indices accordingly
    print("Example 2 activities (start,end):", activities2)
    print("Selected (index, interval):", activity_selection_verbose(activities2))
    print("Selected indices (original):", activity_selection(activities2))