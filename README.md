# Project: Prime Sum Combinations Script

## Description
This Python script finds all possible prime number combinations that sum up to a given integer. It then determines which combination yields the largest product when its elements are multiplied together.

## Features
- Takes a user input (integer).
- Generates all possible prime number combinations that sum to the given number.
- Computes the product of each combination.
- Identifies the combination with the largest product.
- Displays the largest product and the corresponding prime sum combination.

## Usage
1. Run the script using Python:
   ```sh
   python main.py
   ```
2. Enter a number when prompted.
3. The script will:
   - Find prime numbers up to the given number.
   - Determine all prime sum combinations.
   - Calculate the product of each combination.
   - Output the combination that yields the largest product.

## Example Output
```
Enter a number: 10

Largest product: 25
5+5
```

## Notes
- Uses a sieve algorithm to generate prime numbers efficiently.
- Recursively finds prime sum combinations.
- May not handle very large numbers efficiently due to recursion depth and performance constraints.

## License
This project is open-source. Feel free to modify and use it as needed.

## Author
Mazarin

