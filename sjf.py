# Python program to implement Shortest Job First (SJF) scheduling

def calculate_sjf_scheduling(n, burst_times):
    # Initialize process details
    processes = [{'id': i + 1, 'burst_time': bt} for i, bt in enumerate(burst_times)]

    # Sort processes by burst time (Shortest Job First)
    processes.sort(key=lambda x: x['burst_time'])

    # Initialize variables
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time and turnaround time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1]['burst_time']

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i]['burst_time']

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Display results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]['id']}\t\t{processes[i]['burst_time']}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if __name__ == "__main__":
    # Input number of processes
    n = int(input("Enter the number of processes: "))

    # Input burst times for each process
    burst_times = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process P{i + 1}: "))
        burst_times.append(bt)

    # Call the SJF scheduling function
    calculate_sjf_scheduling(n, burst_times)
