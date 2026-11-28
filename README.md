# learn-python

## How to run

Open the terminal and run:

```bash
python3 06-final-project/main.py
```

## Features

- Addition (option 1)
- Subtraction (option 2)
- Multiplication (option 3)
- Division (option 4)
- Exit the program (option 0)
- Repeats until the user chooses 0
- Handles division by zero
- Handles unknown options

## Limitations

- The user must enter numbers in a correct format.
- Only four arithmetic operations are supported.
- Division by zero is not allowed.

## Tests

| Operation | Input | Expected result |
|---|---|---|
| Addition | 1, 2, 3, 0 | 5 |
| Subtraction | 2, 2, 5, 0 | -3 |
| Multiplication | 3, 4, 2.5, 0 | 10 |
| Division | 4, 9, 2, 0 | 4.5 |
| Division by zero | 4, 1, 0, 0 | Error message |
| Unknown option | 7, 0 | Unknown option |
| Several operations | 1, 2, 3, 3, 4, 2.5, 0 | 5 and 10 |
| Exit | 0 | End of program |