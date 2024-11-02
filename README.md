Fill in the `get_num_sub_arrays` function in the [empty.py](src/subarrays/empty.py) file. Non optimal soltuion
can be found in the [non_optimal.py](src/subarrays/non_optimal.py) file.

The function should return the number of subarrays in the input list `arr` that have a product of its elements less than or equal to `k`.

For example, for the input list `arr = [1, 2, 3, 4]` and `k = 6`, the function should return `7` because the subarrays that have a product of its elements less than or equal to `k` are:
[1], [2], [3], [4], [1, 2], [2, 3], [1, 2, 3]

One of the test makes sure the solution works optimally when the input list is large and the product limit is small.