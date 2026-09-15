"""Small example comparing randomized greedy matching to a baseline."""

from matcher import greedy_match


# Dummy input data
preferences = {
    "Alice": ["Hospital 1", "Hospital 2", "Hospital 3", "Hospital 4"],
    "Bob": ["Hospital 2", "Hospital 1", "Hospital 4", "Hospital 3"],
    "Chris": ["Hospital 1", "Hospital 3", "Hospital 2", "Hospital 4"],
    "David": ["Hospital 3", "Hospital 2", "Hospital 4", "Hospital 1"],
    "Elle": ["Hospital 1", "Hospital 2", "Hospital 4", "Hospital 3"],
    "Fatima": ["Hospital 2", "Hospital 3", "Hospital 1", "Hospital 4"],
    "Grace": ["Hospital 4", "Hospital 1", "Hospital 2", "Hospital 3"],
    "Henry": ["Hospital 2", "Hospital 1", "Hospital 3", "Hospital 4"],
    "Isabel": ["Hospital 3", "Hospital 4", "Hospital 2", "Hospital 1"],
    "Jack": ["Hospital 1", "Hospital 4", "Hospital 3", "Hospital 2"],
}

capacities = {
    "Hospital 1": 3,
    "Hospital 2": 3,
    "Hospital 3": 2,
    "Hospital 4": 2,
}


def average_rank(assignments):
    """Calculate the average preference rank received (lower is better)."""
    total_rank = 0
    number_assigned = 0

    for hospital, doctors in assignments.items():
        for doctor in doctors:
            total_rank += preferences[doctor].index(hospital) + 1
            number_assigned += 1

    return total_rank / number_assigned


# Baseline: doctors are assigned in the order shown above.
baseline = greedy_match(preferences, capacities)

# Proposed method: doctor order is randomized. A seed makes the demo repeatable.
randomized = greedy_match(preferences, capacities, randomize=True, seed=7)

print("Baseline assignments:", baseline)
print("Baseline average rank:", average_rank(baseline))
print()
print("Randomized assignments:", randomized)
print("Randomized average rank:", average_rank(randomized))
