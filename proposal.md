# Assignment 1: Proposal
Chelsea Wong | Biomedical Data Design (EN.580.437)

### Objective:
The objective of this assignment is to design and develop a program that assigns doctors to hospitals based on each doctor's ranked list of hospital preferences, where each hospital has a maximum capacity of doctors. Hospitals don't have preferences, so the assignment algorithm must determine a fair method of assigning doctors.


### Background:
Similar matching problems have been studied through algorithms such as the **Gale-Shapley Stable Matching Algorithm**, which is commonly used in applications like the **National Resident Matching Program (NRMP)**. These algorithms aim to create stable assignments by considering preferences from both sides of the matching process (e.g., doctors and hospitals). However, this problem differs because hospitals do not provide rankings for doctors, meaning a traditional stable matching approach is not directly applicable. Instead, this project draws inspiration from these algorithms by prioritizing participant preferences while introducing a fair tie-breaking mechanism through randomization.

### Proposed Algorithm
The proposed solution is a greedy assignment algorithm with randomized doctor ordering.Before assignments begin, the list of doctors will be randomized so that no doctor consistently receives priority due to their position in the input. The algorithm will then iterate through each doctor one at a time. For each doctor, it will examine their ranked list of preferred hospitals, beginning with their first choice. If the preferred hospital has remaining capacity, the doctor will be assigned to that hospital. Otherwise, the algorithm will continue down the doctor's preference list until it finds a hospital with available capacity. Once a doctor has been assigned, the algorithm moves on to the next doctor. This process continues until all doctors have been assigned to a hospital. Because the total hospital capacity is assumed to be sufficient, every doctor is guaranteed to receive an assignment.

### Tradeoffs
Since hospitals do not rank doctors, conflicts must be resolved when multiple doctors prefer the same hospital. Randomizing the doctor order prevents systematic bias from the input order, though the algorithm does not guarantee the globally optimal assignment. Instead, it provides a fair and practical solution while respecting hospital capacities and doctor preferences.
