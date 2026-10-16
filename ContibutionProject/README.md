# Rotating Savings Group (Susu) Tracker

A modular Python command-line utility built to handle a rotating peer-to-peer savings community (Susu). The system allows tracking fixed targets, processing partial allocations, and blocking payouts if balances remain outstanding.

## Project Structure
* `Main.py` - Application orchestrator.
* `GetContributionAmount.py` - Captures and cleans the base entry amount.
* `GetAllMembers.py` - Handles unique identity instantiation.
* `sortWeeks.py` - Allocates tracking rotation matrices.
* `getContributions.py` - Coordinates loops for collecting user payments.
* `test_project.py` - Automated tracking logic assertions.

## Execution Guide

### Prerequisite
* Python 3.6 or higher installed on your computer.

### Running the Core Program
Open your terminal window inside the project directory and execute:
```bash
python Main.py
```

### Running Automated Test Suites
Run the 6 built-in logical test frameworks using the command below:
```bash
python -m unittest test_susu.py
```