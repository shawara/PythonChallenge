import random


def pick_balls(total_balls=50, to_be_select=10):
    assert to_be_select <= total_balls
    nums = [i + 1 for i in range(total_balls)]
    random.shuffle(nums)
    result = nums[:to_be_select]
    result.sort()
    return result


