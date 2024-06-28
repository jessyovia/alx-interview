# Pascal's Triangle

This project involves creating a function that generates Pascal's Triangle with `n` rows.

## Description

Pascal's Triangle is a triangular array of the binomial coefficients. The rows of Pascal's Triangle are conventionally enumerated starting with row `n = 0` at the top (the 0th row). The entries in each row are the coefficients of the binomial expansion of `(x + y)^n`.

## Function

The function `pascal_triangle(n)` generates the first `n` rows of Pascal's Triangle.

### Function Signature

```python
def pascal_triangle(n):
    """
    Generates Pascal's Triangle with n rows.
    
    Parameters:
    n (int): Number of rows in the triangle.
    
    Returns:
    List[List[int]]: A list of lists representing Pascal's Triangle.
    """
```

### Parameters

- `n` (int): The number of rows in Pascal's Triangle. If `n` is less than or equal to 0, the function returns an empty list.

### Returns

- `List[List[int]]`: A list of lists, where each inner list represents a row of Pascal's Triangle.

## Example

Here is an example of how to use the `pascal_triangle` function:

```python
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
    
    print_triangle(pascal_triangle(5))
```

Output:

```plaintext
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Requirements

- Python 3.x

## How to Run

1. Ensure you have Python installed on your machine.
2. Save the `pascal_triangle` function in a file named `0-pascal_triangle.py`.
3. Create a test file named `0-main.py` with the following content:

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

4. Run the test file:

```bash
python3 0-main.py
```

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

```
