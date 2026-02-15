import sys

def add(a, b):
    return a + b

def process_input():
    """
    Accept multiple test cases from CLI
    Example:
    python add.py 2 10 20 30 40
    (2 test cases -> 10+20, 30+40)
    """
    args = sys.argv[1:]

    if len(args) < 3:
        print("Usage: python add.py ")
        sys.exit(1)

    t = int(args[0])
    numbers = list(map(int, args[1:]))

    if len(numbers) != t * 2:
        print("Error: Invalid number of inputs")
        sys.exit(1)

    index = 0
    results = []

    for _ in range(t):
        a = numbers[index]
        b = numbers[index + 1]
        result = add(a, b)
        results.append(result)
        index += 2

    return results


if __name__ == "__main__":
    results = process_input()
    for i, res in enumerate(results, 1):
        print(f"Test Case {i}: {res}")
