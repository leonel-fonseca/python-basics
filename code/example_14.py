def count_and_sum(lst):
    """
    Simple Case: Return the count and the sum of numbers in a list
    if your list is [1,2,3], the result is (3, 6)
    """
    count = 0
    sum = 0
    for num in lst:
        count += 1
        sum += num
    return count, sum


if __name__ == "__main__":
    my_list = [4,8]
    count, sum = count_and_sum(my_list)
    print(f"The count was {count}")
    print(f"The sum was {sum}")
    print(f"The average was {sum/count}")
