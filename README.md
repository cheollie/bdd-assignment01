# Doctor-Hospital Matching

This project assigns doctors to hospitals using doctor preference rankings and hospital capacities. Hospitals do not rank doctors.

`matcher.py` contains a greedy matching function. The baseline assigns doctors in their input order. The proposed method shuffles the doctor order first so the same doctors do not always get priority.

`demo.py` loads a small sanity-check example and a larger evaluation example from the `data` folder. It prints the assignments from both approaches and compares their average assigned rank. A rank of 1 means a doctor received their first choice, so a lower average is better.

## Run

```text
python demo.py
```

## Assumptions

- Every doctor ranks every hospital once.
- Every doctor receives one assignment.
- Total hospital capacity is enough for all doctors.
- Hospitals do not have preferences.

## Contributors

- Chelsea Wong - project plan, algorithm, code, and documentation

## AI use

ChatGPT/Codex was used to help generate the dummy data.
