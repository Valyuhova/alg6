import random
import time


def merge(arr, left, mid, right, stats):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    stats["asg"] += len(left_part) + len(right_part)

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        stats["cmp"] += 1
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            stats["asg"] += 1
            i += 1
        else:
            arr[k] = right_part[j]
            stats["asg"] += 1
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        stats["asg"] += 1
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        stats["asg"] += 1
        j += 1
        k += 1


def merge_sort(arr, left, right, stats):
    if left < right:
        mid = (left + right) // 2
        stats["asg"] += 1

        merge_sort(arr, left, mid, stats)
        merge_sort(arr, mid + 1, right, stats)
        merge(arr, left, mid, right, stats)


def generate_array(n, mode):
    if mode == "random":
        return [random.randint(0, 100000) for _ in range(n)]
    elif mode == "ascending":
        return list(range(n))
    elif mode == "descending":
        return list(range(n, 0, -1))
    else:
        return []


def main():
    sizes = [10, 100, 1000, 5000, 10000]
    modes = ["random", "ascending", "descending"]

    results = []

    for n in sizes:
        for mode in modes:
            arr = generate_array(n, mode)
            data = arr[:]

            stats = {"cmp": 0, "asg": 0}

            start_time = time.perf_counter()
            merge_sort(data, 0, len(data) - 1, stats)
            end_time = time.perf_counter()

            elapsed = end_time - start_time

            results.append({
                "n": n,
                "mode": mode,
                "time": elapsed,
                "cmp": stats["cmp"],
                "asg": stats["asg"]
            })

  
    print("РЕЗУЛЬТАТИ ДОСЛІДЖЕННЯ АЛГОРИТМУ СОРТУВАННЯ ЗЛИТТЯМ\n")
    print(f"{'n':>7} {'тип послідовності':>20} {'час, с':>12} {'порівняння':>15} {'присвоєння':>15}")
    print("-" * 75)

    for res in results:
        mode_name = {
            "random": "випадкова",
            "ascending": "зростаюча",
            "descending": "спадна"
        }[res["mode"]]

        print(f"{res['n']:7d} {mode_name:>20} {res['time']:12.6f} {res['cmp']:15d} {res['asg']:15d}")


if __name__ == "__main__":
    main()