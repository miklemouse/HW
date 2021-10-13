import numpy as np

def line_intersection(A_0, A_1, B_0, B_1, accuracy=1e-6):
    """
    A_0, A_1, B_0, B_1 - numpy arrays with the points' coordinates.
    accuracy - a float representing the greatest possible deviation

    A_0, A_1 belong to the first line
    B_0, B_1 belong to the second line.
   

    # parameter s
    A_0 * (1 - s) + A_1 * s
    =
    # parameter t
    B_0 * (1 - t) + B_1 * t

    The idea of this implementation was offered by
    George Piatsky.
    """

    matrix = np.array([A_1 - A_0, B_0 - B_1]).T
    b = B_0 - A_0
    solved = False
    dimensions = [slice(1, 3), slice(0, 3, 2), slice(0, 2)]
    for sl in dimensions:
        try:
            s, t = np.linalg.solve(matrix[sl], b[sl])
            solved = True
            break
        except np.linalg.LinAlgError:
            continue

    diff = np.abs((A_0 * (1 - s) + A_1 * s) - (B_0 * (1 - t) + B_1 * t))
    assert (diff < accuracy).all()

    return  B_0 * (1 - t) + B_1 * t



def gravity_center(A, B, C, D):
    """
    A, B, C, D - numpy arrays with the points' coordinates
    """

    E = line_intersection(A, C, B, D)
    F = C + A - E
    return ((B + D + F) / 3)


def main():

    print('Enter coordinates of A, B, C, D in each line separately')

    A = np.array(list(map(float, input().split())))
    B = np.array(list(map(float, input().split())))
    C = np.array(list(map(float, input().split())))
    D = np.array(list(map(float, input().split())))

    print('\nGravity center:')

    print(' '.join([str(x) for x in gravity_center(A, B, C, D)]))


if __name__ == '__main__':
    main()
