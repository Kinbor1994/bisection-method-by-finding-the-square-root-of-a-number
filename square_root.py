def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Calculates the square root of a given number using the bisection method.

    Parameters:
        square_target (float or int): The number for which to find the square root.
        tolerance (float, optional): The acceptable difference between the square of the approximate 
                                     root value and the actual target value. Default is 1e-7.
        max_iterations (int, optional): The maximum number of iterations to perform. Default is 100.

    Returns:
        float: The approximate square root of the given number.

    Raises:
        ValueError: If square_target is a negative number.
    """
    # Check if the number is negative
    if square_target < 0:
        raise ValueError('Square root of a negative number is not defined in real numbers')

    # Special cases where the square root is known
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        # Initialize bounds for the bisection method
        low = 0
        high = max(1, square_target)
        root = None

        # Bisection method loop
        for _ in range(max_iterations):
            mid = (low + high) / 2  # Calculate the midpoint
            square_mid = mid ** 2   # Calculate the square of the midpoint

            # Check if the square of the midpoint is within tolerance of the target
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            # Adjust bounds based on comparison
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        # Check if a solution was found within the iteration limit
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')

    return root


if __name__ == "__main__":
    square_root_bisection(16)
