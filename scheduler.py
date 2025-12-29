def fcfs(processes):
    time = 0
    print("\nFCFS Scheduling:")
    for p in processes:
        waiting_time = max(0, time - p["arrival"])
        turnaround_time = waiting_time + p["burst"]
        time += p["burst"]
        print(f"{p['pid']} | Waiting: {waiting_time} | Turnaround: {turnaround_time}")


def sjf(processes):
    time = 0
    ready = processes.copy()
    print("\nSJF Scheduling:")

    while ready:
        available = [p for p in ready if p["arrival"] <= time]
        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda x: x["burst"])
        waiting_time = time - shortest["arrival"]
        turnaround_time = waiting_time + shortest["burst"]
        time += shortest["burst"]
        ready.remove(shortest)

        print(f"{shortest['pid']} | Waiting: {waiting_time} | Turnaround: {turnaround_time}")


def round_robin(processes, quantum):
    time = 0
    queue = processes.copy()
    remaining = {p["pid"]: p["burst"] for p in processes}

    print(f"\nRound Robin Scheduling (Quantum = {quantum}):")

    while queue:
        p = queue.pop(0)

        if remaining[p["pid"]] > quantum:
            time += quantum
            remaining[p["pid"]] -= quantum
            queue.append(p)
        else:
            time += remaining[p["pid"]]
            waiting_time = time - p["arrival"] - p["burst"]
            turnaround_time = time - p["arrival"]
            remaining[p["pid"]] = 0
            print(f"{p['pid']} | Waiting: {waiting_time} | Turnaround: {turnaround_time}")


def run_all(processes):
    fcfs(processes)
    sjf(processes)
    round_robin(processes, quantum=2)

example_processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6}
]

print("Running Scheduling on Example Data")
run_all(example_processes)

choice = input("\nDo you want to enter your own process data? (y/n): ")

if choice.lower() == "y":
    n = int(input("Enter number of processes: "))
    user_processes = []

    for i in range(n):
        pid = f"P{i+1}"
        arrival = int(input(f"Enter arrival time for {pid}: "))
        burst = int(input(f"Enter burst time for {pid}: "))
        user_processes.append({"pid": pid, "arrival": arrival, "burst": burst})

    quantum = int(input("Enter time quantum for Round Robin: "))

    print("\nRunning Scheduling on User Input Data")
    fcfs(user_processes)
    sjf(user_processes)
    round_robin(user_processes, quantum)

else:
    print("\nProgram finished.")