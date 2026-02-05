# Simple Number Range Calculator

A lightweight Python utility to calculate basic metrics for integer ranges.

## Features

- Computes:
  - **Count** of numbers in a range
  - **Sum** of numbers in a range
  - **Span** (distance between start and end)
- Supports:
  - **Inclusive** ranges (default)
  - **Exclusive** end ranges (`--exclusive`)
- Handles reversed inputs (for example `10 1`) automatically.

## Requirements

- Python 3.9+

## Usage

Run the CLI with a start and end integer:

```bash
python range_calculator.py <start> <end>
```

### Inclusive mode (default)

```bash
python range_calculator.py 1 10
```

Example output:

```text
Range mode: inclusive
Count: 10
Sum: 55
Span: 9
```

### Exclusive end mode

```bash
python range_calculator.py 1 10 --exclusive
```

Example output:

```text
Range mode: exclusive
Count: 9
Sum: 45
Span: 9
```

## Reusable function

You can also import and use `calculate_range` in Python code:

```python
from range_calculator import calculate_range

result = calculate_range(1, 5)  # inclusive by default
print(result)  # {'count': 5, 'total': 15, 'span': 4}
```

## Run tests

```bash
python -m unittest -v
```
