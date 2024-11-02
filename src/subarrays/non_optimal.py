def get_num_sub_arrays(arr: list[int], max_product: int) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub = arr[i:j+1]
            prod = 1
            for n in sub:
                prod *= n
            if prod <= max_product:
                count += 1
    return count
