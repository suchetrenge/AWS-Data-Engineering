def transpose_matrix(matrix):
    """
    Transpose a given 2D matrix.

    Args:
        matrix (list of list of any): The input 2D matrix.

    Returns:
        list of list of any: The transposed matrix.
    """
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input must be a 2D list.")

    return [list(row) for row in zip(*matrix)]