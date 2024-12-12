# Preemptive Priority Scheduling Algorithm
def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    burst_times = list(map(int, input("Enter burst times (space-separated): ").split()))
    priorities = list(map(int, input("Enter priorities (space-separated): ").split()))

    if len(burst_times) != n or len(priorities) != n:
        print("Error: Mismatch in the number of processes and provided inputs.")
        return

    processes = [{'id': i+1, 'burst_time': bt, 'priority': p, 'remaining_time': bt} for i, (bt, p) in enumerate(zip(burst_times, priorities))]

    current_time = 0
    completed = 0
    waiting_times = [0] * n
    turnaround_times = [0] * n
    process_order = []

    while completed < n:
        # Select the process with the highest priority (lowest number) that is not completed
        available_processes = [p for p in processes if p['remaining_time'] > 0]
        if not available_processes:
            break

        next_process = min(available_processes, key=lambda p: p['priority'])

        # Execute for 1 unit of time
        next_process['remaining_time'] -= 1
        process_order.append(next_process['id'])

        # If the process completes
        if next_process['remaining_time'] == 0:
            completed += 1
            turnaround_time = current_time + 1
            waiting_time = turnaround_time - next_process['burst_time']

            turnaround_times[next_process['id'] - 1] = turnaround_time
            waiting_times[next_process['id'] - 1] = waiting_time

        current_time += 1

    # Calculate averages
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n

    # Display results
    print("\nProcess Execution Order:", process_order)
    print("\nResults:")
    for i in range(n):
        print(f"Process {i+1}: Waiting Time = {waiting_times[i]}, Turnaround Time = {turnaround_times[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

priority_scheduling()
