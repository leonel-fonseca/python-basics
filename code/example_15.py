def count_and_sum_only_odd_numbers(lst):
    """
    Simple Case: Return the count and the sum of numbers in a list
    only when they are odd.
    If your list is [1,2,3,4], then the result should be (2, 4),
    as only 1 and 3 are odd numbers.
    """
    count = 0
    sum = 0
    for num in lst:
        if num % 2 == 1:
            count += 1
            sum += num
    return count, sum

if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    count, sum = count_and_sum_only_odd_numbers(my_list)
    print(f"The count was {count}")
    print(f"The sum was {sum}")
    print(f"The average was {sum/count}")
