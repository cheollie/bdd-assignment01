"""Functions for assigning doctors to hospitals."""

import random

def greedy_match(preferences, capacities, randomize=False, seed=None):
    """Assign each doctor to their highest-ranked hospital with space.

    preferences is a dictionary mapping each doctor to a ranked hospital list.
    capacities is a dictionary mapping each hospital to its maximum capacity.
    """
    doctor_order = list(preferences.keys())

    # The proposed method randomizes priority. The baseline keeps input order.
    if randomize:
        random.Random(seed).shuffle(doctor_order)

    assignments = {hospital: [] for hospital in capacities}

    for doctor in doctor_order:
        for hospital in preferences[doctor]:
            if len(assignments[hospital]) < capacities[hospital]:
                assignments[hospital].append(doctor)
                break

    return assignments
