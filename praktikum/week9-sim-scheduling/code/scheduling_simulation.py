# Simulasi Algoritma Penjadwalan CPU (FCFS & SJF Non-Preemptive)

# Dataset proses
processes = [
    {"pid": "P1", "arrival": 0, "burst": 6},
    {"pid": "P2", "arrival": 1, "burst": 8},
    {"pid": "P3", "arrival": 2, "burst": 7},
    {"pid": "P4", "arrival": 3, "burst": 3},
]

# Fungsi FCFS
def fcfs(processes):
    procs = sorted(processes, key=lambda x: x["arrival"])
    time = 0
    results = []
    for p in procs:
        if time < p["arrival"]:
            time = p["arrival"]
        waiting = time - p["arrival"]
        turnaround = waiting + p["burst"]
        results.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": waiting,
            "turnaround": turnaround
        })
        time += p["burst"]
    return results

# Fungsi SJF Non-preemptive
def sjf(processes):
    procs = sorted(processes, key=lambda x: x["arrival"])
    time = 0
    ready = []
    results = []
    while procs or ready:
        while procs and procs[0]["arrival"] <= time:
            ready.append(procs.pop(0))
        if ready:
            ready.sort(key=lambda x: x["burst"])
            p = ready.pop(0)
            waiting = time - p["arrival"]
            turnaround = waiting + p["burst"]
            results.append({
                "pid": p["pid"],
                "arrival": p["arrival"],
                "burst": p["burst"],
                "waiting": waiting,
                "turnaround": turnaround
            })
            time += p["burst"]
        else:
            time = procs[0]["arrival"]
    return results

# Fungsi untuk menampilkan tabel hasil
def print_table(title, results):
    print(f"\n=== {title} ===")
    print("PID | Arrival | Burst | Waiting | Turnaround")
    print("---------------------------------------------")
    total_waiting = 0
    total_turnaround = 0
    for r in results:
        print(f"{r['pid']:>3} | {r['arrival']:>7} | {r['burst']:>5} | {r['waiting']:>7} | {r['turnaround']:>10}")
        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]
    n = len(results)
    print("---------------------------------------------")
    print(f"Rata-rata Waiting   : {total_waiting/n:.2f}")
    print(f"Rata-rata Turnaround: {total_turnaround/n:.2f}")

# Eksekusi
fcfs_result = fcfs(processes)
sjf_result = sjf(processes)

print_table("FCFS Scheduling", fcfs_result)
print_table("SJF Scheduling", sjf_result)