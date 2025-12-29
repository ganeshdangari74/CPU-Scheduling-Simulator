# CPU Scheduling Algorithms Simulator

A Python-based simulator that implements and compares classical CPU scheduling algorithms used in Operating Systems. This project demonstrates how different scheduling strategies affect **waiting time** and **turnaround time** of processes.

---

## Overview

CPU scheduling is a fundamental concept in operating systems that determines how processes are assigned CPU time. This project provides a practical implementation of widely used scheduling algorithms and allows users to experiment with different process parameters.

---

## Algorithms Implemented

* **First Come First Serve (FCFS)**
* **Shortest Job First (SJF)** – Non-Preemptive
* **Round Robin (RR)** – User-defined Time Quantum

---

## Key Features

* Simulation of multiple CPU scheduling algorithms
* Calculates **waiting time** and **turnaround time** for each process
* Supports both **predefined example data** and **custom user input**
* Configurable **time quantum** for Round Robin scheduling
* Command-line based and easy to use

---

## Technologies Used

* **Programming Language:** Python 3
* **Core Concepts:** Operating Systems, Process Scheduling, Queues

---

## Project Structure

```
cpu-scheduling-simulator/
│
├── scheduling.py   # Implementation of scheduling algorithms
└── README.md       # Project documentation
```

---

## How to Run the Project

1. Clone the repository or download the source code
2. Navigate to the project directory
3. Run the program using:

```bash
python scheduling.py
```

---

## Example Process Data

The program first runs on predefined example data:

```python
[
  {"pid": "P1", "arrival": 0, "burst": 5},
  {"pid": "P2", "arrival": 1, "burst": 3},
  {"pid": "P3", "arrival": 2, "burst": 8},
  {"pid": "P4", "arrival": 3, "burst": 6}
]
```

---

## Output Format

For each scheduling algorithm, the following metrics are displayed:

* Process ID
* Waiting Time
* Turnaround Time

Example output:

```
P1 | Waiting: 0 | Turnaround: 5
```

---

## User Input Mode

After executing the example run, users can choose to:

* Enter the number of processes
* Provide arrival time and burst time for each process
* Specify the time quantum for Round Robin scheduling

This allows experimentation with different scheduling scenarios.

---

## Limitations

* Shortest Job First (SJF) is non-preemptive
* No Gantt chart visualization
* Average waiting and turnaround times are not calculated

---

## Future Enhancements

* Preemptive SJF (Shortest Remaining Time First)
* Priority Scheduling
* Gantt chart visualization
* Calculation of average waiting and turnaround times
* Graphical or web-based interface

---

## Academic Relevance

This project demonstrates practical understanding of:

* CPU scheduling mechanisms
* Process management in operating systems
* Algorithmic trade-offs in scheduling strategies

It is suitable for **Operating Systems labs**, **academic projects**, and **internship portfolios**.

---

## License

This project is open-source and intended for educational and academic use.

---

## Author

**Ganesh Dangari