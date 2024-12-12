def calculate_need(processes, resources, max_matrix, allocation_matrix):
    need = [[0] * resources for _ in range(processes)]
    for i in range(processes):
        for j in range(resources):
            need[i][j] = max_matrix[i][j] - allocation_matrix[i][j]
    return need

def is_safe_state(processes, resources, allocation, need, available):
    work = available[:]
    finish = [False] * processes
    safe_sequence = []

    while len(safe_sequence) < processes:
        found = False
        for p in range(processes):
            if not finish[p]:
                can_allocate = True
                for r in range(resources):
                    if need[p][r] > work[r]:
                        can_allocate = False
                        break
                if can_allocate:
                    for r in range(resources):
                        work[r] += allocation[p][r]
                    safe_sequence.append(p)
                    finish[p] = True
                    found = True
        if not found:
            return False, []
    return True, safe_sequence

def main():
    processes = int(input("Enter the number of processes: "))
    resources = int(input("Enter the number of resource types: "))

    max_matrix = []
    print("Enter the Maximum demand matrix:")
    for i in range(processes):
        row = list(map(int, input(f"P{i}: ").split()))
        max_matrix.append(row)

    allocation_matrix = []
    print("Enter the Allocation matrix:")
    for i in range(processes):
        row = list(map(int, input(f"P{i}: ").split()))
        allocation_matrix.append(row)

    available = list(map(int, input("Enter the Available resources: ").split()))

    need = calculate_need(processes, resources, max_matrix, allocation_matrix)

    safe, safe_sequence = is_safe_state(processes, resources, allocation_matrix, need, available)

    if safe:
        print("Safe State: Yes")
        print("Safe Sequence: ", " -> ".join([f"P{p}" for p in safe_sequence]))
    else:
        print("Safe State: No")
        print("Deadlock Risk Detected")

if __name__ == "__main__":
    main()
