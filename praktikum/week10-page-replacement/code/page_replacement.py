# Simulasi Page Replacement FIFO & LRU
# Dataset: reference_string.txt

def read_reference_string(file_path="reference_string.txt"):
    with open(file_path, "r") as f:
        data = f.read().strip()
    return [int(x) for x in data.split(",")]

def fifo(reference_string, frame_size):
    frames = []
    page_faults = 0
    queue_index = 0

    for page in reference_string:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[queue_index] = page
                queue_index = (queue_index + 1) % frame_size
            page_faults += 1
    return page_faults

def lru(reference_string, frame_size):
    frames = []
    page_faults = 0
    recent_use = {}

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # cari page yang paling jarang dipakai
                lru_page = min(frames, key=lambda p: recent_use[p])
                frames[frames.index(lru_page)] = page
            page_faults += 1
        recent_use[page] = i
    return page_faults

if __name__ == "__main__":
    reference_string = read_reference_string("reference_string.txt")
    frame_size = 3

    fifo_faults = fifo(reference_string, frame_size)
    lru_faults = lru(reference_string, frame_size)

    print("Reference String:", reference_string)
    print("Frame Size:", frame_size)
    print("FIFO Page Faults:", fifo_faults)
    print("LRU Page Faults:", lru_faults)