"""Simple number range calculator."""

from __future__ import annotations

import argparse


def calculate_range(start: int, end: int, inclusive: bool = True) -> dict[str, int]:
    """Calculate basic values for a numeric range.

    Returns a dictionary with:
    - count: number of integers in the range
    - total: sum of integers in the range
    - span: absolute distance between start and end
    """
    if start > end:
        start, end = end, start

    stop = end + 1 if inclusive else end
    numbers = range(start, stop)

    return {
        "count": len(numbers),
        "total": sum(numbers),
        "span": end - start,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple number range calculator")
    parser.add_argument("start", type=int, help="Range start")
    parser.add_argument("end", type=int, help="Range end")
    parser.add_argument(
        "--exclusive",
        action="store_true",
        help="Treat the end value as exclusive",
    )
    args = parser.parse_args()

    result = calculate_range(args.start, args.end, inclusive=not args.exclusive)
    mode = "inclusive" if not args.exclusive else "exclusive"

    print(f"Range mode: {mode}")
    print(f"Count: {result['count']}")
    print(f"Sum: {result['total']}")
    print(f"Span: {result['span']}")


if __name__ == "__main__":
    main()
