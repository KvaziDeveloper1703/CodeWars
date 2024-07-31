"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
"""

def solution(lst):
    if not lst:
        return ""

    ranges = []
    start = lst[0]
    current = lst[0]

    for num in lst[1:]:
        if num == current + 1:
            current = num
        else:
            if current - start >= 2:
                ranges.append(f"{start}-{current}")
            else:
                ranges.extend(map(str, range(start, current + 1)))
            start = current = num

    if current - start >= 2:
        ranges.append(f"{start}-{current}")
    else:
        ranges.extend(map(str, range(start, current + 1)))

    return ",".join(ranges)

# Example usage
print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# Output: "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"