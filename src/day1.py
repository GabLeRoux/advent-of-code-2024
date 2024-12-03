import sys
from typing import List, Tuple

import fire


class Day1:
    @staticmethod
    def how_far_apart(pair: Tuple[int, int]) -> int:
        return abs(pair[0] - pair[1])

    @staticmethod
    def find_total_distance(pairs: List[Tuple[int, int]]) -> int:
        return sum(Day1.how_far_apart(pair) for pair in pairs)

    @staticmethod
    def sort_each_keys(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        x_sorted = sorted(x for x, y in pairs)
        y_sorted = sorted(y for x, y in pairs)
        return list(zip(x_sorted, y_sorted))

    @staticmethod
    def lines_to_tuples(lines: List[str]) -> List[Tuple[int, int]]:
        return [
            (int(parts[0]), int(parts[1]))
            for parts in (line.split() for line in lines)
        ]

    @staticmethod
    def solve_part_1() -> int:
        lines = sys.stdin.readlines()
        pairs = Day1.lines_to_tuples(lines)
        sorted_pairs = Day1.sort_each_keys(pairs)
        return Day1.find_total_distance(sorted_pairs)

    @staticmethod
    def solve_part_2():
        lines = sys.stdin.readlines()
        pairs = Day1.lines_to_tuples(lines)
        return Day1.get_similarity_score(pairs)

    @staticmethod
    def get_similarity_score(pairs):
        x_sorted = sorted(x for x, y in pairs)
        y_sorted = sorted(y for x, y in pairs)
        score = 0
        for x in x_sorted:
            score += x * y_sorted.count(x)
        return score


if __name__ == "__main__":
    fire.Fire(Day1)
