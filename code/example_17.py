def count_and_sum_only_odd_numbers_until_sum_limit_with_tracking(lst, limit):
    """
    Simple Case: Return the count and the sum of numbers in a list
    only when they are odd.
    If your list is [1,2,3,4], then the result should be (2, 4),
    as only 1 and 3 are odd numbers.
    Stop when the sum is greater than or equal to the limit.
    Now we want to see which numbers were selected and their running total.
    Let's track those with dictionary.
    """
    count = 0
    sum = 0
    tracking = {}
    for num in lst:
        if num % 2 == 1:
            count += 1
            sum += num
            tracking[num] = sum
            if sum >= limit:
                break # This is how you exit a loop.
    return count, sum, tracking


if __name__ == "__main__":
    my_list = range(1, 100)
    count, sum, tracking = count_and_sum_only_odd_numbers_until_sum_limit_with_tracking(my_list, 33)
    print(f"The count was {count}")
    print(f"The sum was {sum}")
    print(f"The average was {sum/count}")
    print(f"The list below shows for each step what number is considered and the running sum:")
    for key in tracking:
        print(f"{key}: {tracking[key]}")
