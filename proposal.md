# Assignment 1: Proposal
Chelsea Wong | Biomedical Data Design (EN.580.437)

### Objective
The objective of this assignment is to design and develop a program that assigns doctors to hospitals based on each doctor's ranked list of hospital preferences, where each hospital has a maximum capacity of doctors. Hospitals don't have preferences, so the assignment algorithm must determine a fair method of assigning doctors.

### Assumptions and Formulation
I will assume that every doctor ranks every hospital, each doctor can only be assigned to one hospital, and the total hospital capacity is enough for all doctors. Let `x[d,h]` equal 1 if doctor `d` is assigned to hospital `h` and 0 otherwise. Each doctor must have exactly one assignment, and the number of doctors assigned to a hospital cannot exceed its capacity. Assignment quality will be measured using average preference rank, where a lower average is better.

### Background
Similar matching problems have been studied through algorithms such as the **Gale-Shapley Stable Matching Algorithm**, which is commonly used in applications like the **National Resident Matching Program (NRMP)**. These algorithms consider preferences from both sides of the matching process. However, this problem differs because hospitals do not rank doctors, so a traditional stable matching approach is not directly applicable.

### Proposed Algorithm
The proposed solution is a greedy assignment algorithm with randomized doctor ordering. Before assignments begin, the list of doctors will be randomized so that no doctor consistently receives priority due to their position in the input. The algorithm will then go through each doctor and check their ranked hospitals, beginning with their first choice. If that hospital has remaining capacity, the doctor will be assigned there. Otherwise, the algorithm will continue down the doctor's preference list until it finds a hospital with space.

For comparison, the baseline will use the same greedy method but will keep doctors in their original input order. Both methods will be tested on example data and compared using average preference rank.

### Tradeoffs
This approach is simple, efficient, and prioritizes each doctor's preferences whenever possible. Randomizing doctor order reduces bias from the input order, but the algorithm does not guarantee the globally optimal assignment. Possible extensions include repeating the random assignment several times, comparing it with the Hungarian algorithm, or adding hospital preferences.

### References
1. Kuhn, H. W. (1955). “The Hungarian Method for the Assignment Problem.” *Naval Research Logistics Quarterly*, 2, 83-97.
2. Gale, D., & Shapley, L. S. (1962). “College Admissions and the Stability of Marriage.” *The American Mathematical Monthly*, 69, 9-15.
3. Bade, S. (2020). “Random Serial Dictatorship: The One and Only.” *Mathematics of Operations Research*, 45, 353-368.
