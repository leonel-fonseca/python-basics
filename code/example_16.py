def count_and_sum_only_odd_numbers_until_sum_limit(lst, limit):
    """
    Simple Case: Return the count and the sum of numbers in a list
    only when they are odd.
    If your list is [1,2,3,4], then the result should be (2, 4),
    as only 1 and 3 are odd numbers.
    Stop when the sum is greater than or equal to the limit.
    """
    count = 0
    sum = 0
    for num in lst:
        if num % 2 == 1:
            count += 1
            sum += num
            if sum >= limit:
                break # This is how you exit a loop.
    return count, sum

if __name__ == "__main__":
    my_list = range(1, 100)
    count, sum = count_and_sum_only_odd_numbers_until_sum_limit(my_list, 33)
    print(f"The count was {count}")
    print(f"The sum was {sum}")
    print(f"The average was {sum/count}")
