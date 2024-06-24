from example_14 import count_and_sum
from example_15 import count_and_sum_only_odd_numbers
from example_16 import count_and_sum_only_odd_numbers_until_sum_limit
from example_17 import count_and_sum_only_odd_numbers_until_sum_limit_with_tracking

my_data_list = [4]

my_function_list = [
    count_and_sum,
    count_and_sum_only_odd_numbers,
    count_and_sum_only_odd_numbers_until_sum_limit,
    count_and_sum_only_odd_numbers_until_sum_limit_with_tracking,
]

for f in my_function_list:
    try:
        print(f"Attempting to compute the function {f} on input {my_data_list}")
        count, sum = f(my_data_list)
        print(f"The count was {count} and the sum was {sum}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("")