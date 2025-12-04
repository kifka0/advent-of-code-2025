# Advent of Code 2025

My solutions for Advent of Code 2025 challenges.

## Structure

Each day's solution is organized in its own directory:
- `day1/` - Day 1 solution
- `day2/` - Day 2 solution
- `day3/` - Day 3 solution
- `day4/` - Day 4 solution (Grid neighbor analysis with cascading removal)
- `day10_20/` - Days 10-20 (work in progress)

## Day 4 Highlights

Day 4 implements a grid-based neighbor analysis algorithm that:
- Reads a 2D grid of `@` and `.` characters
- Identifies `@` symbols with fewer than 4 neighboring `@` symbols
- Iteratively removes isolated symbols in a cascading fashion
- Runs until no more symbols can be removed

**Result**: Removed 8,946 `@` symbols over 72 iterations on the full input!

## Running Solutions

Each day's solution can be run independently:
```bash
cd dayX
python3 dayX.py
```

## Input Files

- `testX.txt` - Test input for validation
- `textX.txt` - Full puzzle input
