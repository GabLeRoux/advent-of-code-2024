from src.day1 import Day1


class TestDay1:
    example_input_pairs = [
        (3, 4),
        (4, 3),
        (2, 5),
        (1, 3),
        (3, 9),
        (3, 3),
    ]

    expected_sorted_pairs = [
        (1, 3),  # distance: 2
        (2, 3),  # distance: 1
        (3, 3),  # distance: 0
        (3, 4),  # distance: 1
        (3, 5),  # distance: 2
        (4, 9),  # distance: 5
    ]

    def test_how_far_apart(self):
        assert Day1.how_far_apart((3, 4)) == 1
        assert Day1.how_far_apart((4, 3)) == 1

    def test_find_total_distance(self):
        example_1 = [
            (3, 4),  # distance: 1
            (4, 3),  # distance: 1
        ]  # distance: total = 2
        assert Day1.find_total_distance(example_1) == 2

    def test_find_total_distance_on_sorted_pairs(self):
        assert Day1.find_total_distance(self.expected_sorted_pairs) == 11

    def test_sort_pairs(self):
        assert (
            Day1.sort_each_keys(self.example_input_pairs) == self.expected_sorted_pairs
        )

    def test_stdin_lines_to_tuples(self):
        assert Day1.stdin_lines_to_tuples(["3   4", "4   3"]) == [
            (3, 4),
            (4, 3),
        ]
