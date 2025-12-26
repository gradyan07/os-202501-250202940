#!/usr/bin/env python3
"""
Deadlock Detection (Wait-For Graph approach)
- Dataset: CSV dengan kolom Process,Allocation,Request
- Asumsi: satu instance per resource type (R1, R2, ...)
- Logika: Jika Pi meminta resource Rx yang sedang dialokasikan ke Pj, maka ada edge Pi -> Pj.
- Deadlock terdeteksi jika terdapat siklus pada wait-for graph.

Contoh CSV:
Process,Allocation,Request
P1,R1,R2
P2,R2,R3
P3,R3,R1
"""

import csv
import sys
from pathlib import Path

def read_dataset(csv_path):
    processes = []
    allocations = {}  # resource -> process yang memegangnya
    requests = {}     # process -> resource yang diminta (bisa kosong)

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = row['Process'].strip()
            a = row['Allocation'].strip() if row.get('Allocation') else ''
            r = row['Request'].strip() if row.get('Request') else ''
            processes.append(p)
            if a:
                allocations[a] = p
            requests[p] = r if r else None
    return processes, allocations, requests

def build_wait_for_graph(processes, allocations, requests):
    """
    Wait-For Graph (WFG): directed edges P_i -> P_j jika P_i menunggu resource yang dipegang P_j.
    """
    graph = {p: [] for p in processes}
    for p in processes:
        req_res = requests.get(p)
        if req_res:
            holder = allocations.get(req_res)
            if holder and holder != p:
                graph[p].append(holder)
    return graph

def detect_cycles(graph):
    """
    Deteksi siklus pada directed graph menggunakan DFS (coloring: 0=unvisited,1=visiting,2=visited).
    Return:
      - has_cycle: bool
      - cycles_nodes: set of nodes yang berada pada siklus (aproksimasi sederhana dari back-edges)
    """
    color = {u: 0 for u in graph}
    parent = {u: None for u in graph}
    cycles_nodes = set()

    def dfs(u):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 0:
                parent[v] = u
                if dfs(v):
                    return True
            elif color[v] == 1:
                # back-edge u -> v: ada siklus
                # kumpulkan node pada path kembali sampai v
                cycles_nodes.add(v)
                w = u
                cycles_nodes.add(w)
                while parent[w] is not None and parent[w] != v:
                    w = parent[w]
                    cycles_nodes.add(w)
                return True
        color[u] = 2
        return False

    has_cycle = False
    for u in graph:
        if color[u] == 0:
            if dfs(u):
                has_cycle = True
                # lanjutkan untuk menemukan semua siklus yang mungkin
    return has_cycle, cycles_nodes

def print_table(processes, allocations, requests, graph, has_cycle, cycles_nodes):
    # Tabel hasil proses
    print("\n=== Hasil Deteksi Deadlock (Wait-For Graph) ===")
    print(f"{'Proses':<8} | {'Allocation':<10} | {'Request':<10} | {'Terlibat Deadlock':<18}")
    print("-" * 60)
    for p in processes:
        a = next((res for res, holder in allocations.items() if holder == p), "-")
        r = requests.get(p) or "-"
        involved = "Ya" if p in cycles_nodes else "Tidak"
        print(f"{p:<8} | {a:<10} | {r:<10} | {involved:<18}")

    # Ringkasan sistem
    verdict = "DEADLOCK TERDETEKSI" if has_cycle else "TIDAK ADA DEADLOCK"
    print("\nRingkasan Sistem:", verdict)

    # Tampilkan wait-for edges
    print("\nWait-For Edges (Pi -> Pj artinya Pi menunggu Pj):")
    any_edge = False
    for u, vs in graph.items():
        for v in vs:
            any_edge = True
            print(f"  {u} -> {v}")
    if not any_edge:
        print("  (Tidak ada edge; tidak ada proses yang saling menunggu)")

def main():
    # Path default dataset
    default_path = Path(__file__).parent / "dataset_deadlock.csv"
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path

    if not csv_path.exists():
        print(f"Error: file dataset tidak ditemukan: {csv_path}")
        sys.exit(1)

    processes, allocations, requests = read_dataset(csv_path)
    graph = build_wait_for_graph(processes, allocations, requests)
    has_cycle, cycles_nodes = detect_cycles(graph)
    print_table(processes, allocations, requests, graph, has_cycle, cycles_nodes)

    # Exit code: 0 jika tidak deadlock, 2 jika deadlock (opsional untuk CI)
    sys.exit(2 if has_cycle else 0)

if __name__ == "__main__":
    main()