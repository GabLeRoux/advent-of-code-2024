import sys
from typing import List, Tuple

import fire


class Day1:
    @staticmethod
    def how_far_apart(pair: Tuple[int, int]) -> int:
        return abs(pair[0] - pair[1])

    @staticmethod
    def find_total_distance(example_input: List[Tuple[int, int]]) -> int:
        return sum(Day1.how_far_apart(pair) for pair in example_input)

    @staticmethod
    def sort_each_keys(input_pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        x_sorted = sorted(x for x, y in input_pairs)
        y_sorted = sorted(y for x, y in input_pairs)
        return list(zip(x_sorted, y_sorted))

    @staticmethod
    def stdin_lines_to_tuples(input_lines: List[str]) -> List[Tuple[int, int]]:
        return [
            (int(parts[0]), int(parts[1]))
            for parts in (line.split() for line in input_lines)
        ]

    def solve(self) -> int:
        lines = sys.stdin.readlines()
        pairs = self.stdin_lines_to_tuples(lines)
        sorted_pairs = self.sort_each_keys(pairs)
        return self.find_total_distance(sorted_pairs)


if __name__ == "__main__":
    fire.Fire(Day1)
