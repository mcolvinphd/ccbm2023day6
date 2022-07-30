import random
import statistics

# Copy the generate_numbers function over to the other folder but exclude the doc string

def generate_numbers(n):
    """Generate a list of numbers of length n, ranging from 1 to 300

    Args:
        n (int): length of list

    Returns:
        list: list of integers
    """

    return random.sample(range(1, 301), n)


def my_avg(val, n):
    """Calculates an average

    Args:
        val (int): integer value representing the sum of a sequence
        n (int): integer value representing the length of the sequence

    Returns:
        float: float value representing an average
    """
    avg = val/n
    return avg


def running_average(numbers):
    """[Calculates the running average of a given sequence]
    Args:
        numbers ([list]): [list of integer values]
    Returns:
        [list]: [list of floats representing the running average in the sequence]
    """
    avgs = []
    val_total = 0
    for idx, num in enumerate(numbers):
        val_total += num
        current_avg = my_avg(val_total, idx+1)
        avgs.append(round(current_avg, 2))
    return avgs


def highest_running_avg(numbers):
    """[Calculates a running average from a sequence and extracts the maximum average value]
    Args:
        numbers ([list]): [a list of integers values]
    Returns:
        [float]: [maximum float value from a running average]
    """
    averages = running_average(numbers)
    return max(averages)




if __name__ == "__main__":

    # Demonstrate adding doc strings
    nums = generate_numbers(6)
    print(f"{'List of numbers':<38}  {(nums)}")

    run_avgs = running_average(nums)
    print(f'List of running averages from sequence: {run_avgs}')

    # Demonstrate automatic formatting
    print(f'Mean of list:  {statistics.mean(nums):>31.2f}')

    print(
        f'The highest running average value:  {highest_running_avg(nums) :>10.2f}')
    print()
    