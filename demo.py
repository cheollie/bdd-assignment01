"""Demo comparing randomized greedy matching to a fixed-order baseline."""

import json

from matcher import greedy_match


def average_rank(assignments, preferences):
    """Calculate the average preference rank received (lower is better)."""
    total_rank = 0
    number_assigned = 0

    for hospital, doctors in assignments.items():
        for doctor in doctors:
            total_rank += preferences[doctor].index(hospital) + 1
            number_assigned += 1

    return total_rank / number_assigned


def compare_methods(preferences, capacities):
    """Run and print the baseline and randomized greedy results."""
    baseline = greedy_match(preferences, capacities)
    randomized = greedy_match(preferences, capacities, randomize=True, seed=7)

    print("Baseline assignments:", baseline)
    print("Baseline average rank:", average_rank(baseline, preferences))
    print("Randomized assignments:", randomized)
    print("Randomized average rank:", average_rank(randomized, preferences))


# Small example used as a quick sanity check.
with open("data/small_example.json") as file:
    small_data = json.load(file)

print("SMALL SANITY CHECK")
compare_methods(small_data["preferences"], small_data["capacities"])


# Larger example used for evaluation.
with open("data/large_example.json") as file:
    large_data = json.load(file)

print("\nLARGER EVALUATION")
compare_methods(large_data["preferences"], large_data["capacities"])
