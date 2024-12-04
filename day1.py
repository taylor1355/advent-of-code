import numpy as np
import os
import re

def list_distance(list1, list2):
    dists = np.abs(np.sort(list2) - np.sort(list1))
    return np.sum(dists)

if __name__ == '__main__':
    # TODO: move the io stuff to a shared util file
    input_path = os.path.join(os.path.dirname(__file__), 'inputs', 'day1_input.csv')
    list1 = []
    list2 = []
    with open(input_path, 'r') as f:
        lines = f.readlines()
        # use a regex to parse each line into 2 whitespace separated ints
        for line in lines:
            match = re.match(r'(\d+)\s+(\d+)', line)
            if match:
                list1.append(int(match.group(1)))
                list2.append(int(match.group(2)))

    # Part 1
    print(list_distance(list1, list2))