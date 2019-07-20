import math
import itertools

# the idea is to get calcuate the coordinates for center_coordinates of given matrix
# and coordinates for the largest values in the matrix
# and calcuate number of steps need to traverse from these two points
# if x is coordinate for center_coordinates and y is coorindate for the largest value
# number of swaps = distance between x and y
# distance between x and y =  abs(x[0] - y[0]) + abs(x[1] - y[1])

def get_center(length):
    if not length or length <= 1: return [0];
    length = length - 1
    if (length) % 2 != 0:
        return [math.ceil(length/2), math.floor(length/2)]

    return [length//2]

def min_swaps_required(center_coordinates, large_item_idx):
    # check if we largest values in any of the center_coordinates values
    # this also handles all the values being same...
    if any(point in center_coordinates for point in large_item_idx):
        return 0

    result = float('inf')
    for item in tuple(itertools.product(center_coordinates, large_item_idx)):
        result = min(
                    result,
                    abs(item[0][0] - item[1][0]) + abs(item[0][1] - item[1][1])
                    )

    return result

if __name__ == "__main__":
    for _ in range(int(input())):
        m, n = (int(i.strip()) for i in input().split(' '))
        # now calculate the center_coordinates ( list of point/s) of the matrix given
        center_coordinates = tuple(itertools.product(get_center(m),
                                                  get_center(n)))
        large_item = None
        large_item_idx = []
        for i in range(m):
            row_items = [int(item.strip()) for item in input().split(' ')]
            for j, item in enumerate(row_items):
                if not large_item:
                    large_item = item
                    large_item_idx.append((i,j))
                    continue

                if item < large_item:
                    continue

                if item == large_item:
                    large_item_idx.append((i,j))
                    continue

                large_item = item
                large_item_idx = [(i,j)]

        print(min_swaps_required(center_coordinates, large_item_idx))
