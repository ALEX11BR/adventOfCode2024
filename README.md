# Personal attempts at solving Advent of Code 2024 in Python

In every `d{day}` folder there are my solutions to that day's problems.
The day's input sits in that folder in a file named `input` (I don't publish them here).

The console programs get their input from a stdin (that might require an end of stream).
This can be accomplished, for instance, by:

- redirecting the input file into the program,
- heredocs,
- typing the input followed by a `Ctrl-D` on unix, `Ctrl-Z Enter` on windows.

Most solutions:
- were submitted within 24 hour of the problem's publishing,
- use only Python's standard library,
- make the `mypy` type checker happy, having full annotations for functions
- run pretty quickly (<1 second).

The solutions for which this doesn't fully apply have a comment at the beginning with details.
These are:
- Day 6, part 2: solution takes about 8 seconds to run (using CPython; PyPy runs it in about 1 second).
- Day 7, part 2: solution takes about 11 seconds to run (using CPython; PyPy runs it in about 1 second).
- Day 9, part 2: solution takes about 3 seconds to run (using CPython; PyPy runs it in about 0.1 seconds).
- Day 11, part 1: solution takes about 2 seconds to run (using CPython; PyPy runs it in about 1 second).
- Day 14, part 2: solution takes about 5 seconds to run (using CPython; PyPy runs it in about 1 second).
- Day 19, part 1: solution takes about 24 seconds to run (using CPython; PyPy runs it in about 2 seconds).
- Day 19, part 2: solution takes about 1.5 seconds to run (using CPython; PyPy runs it in about 0.1 seconds).
- Day 20, part 2: solution takes about 12 seconds to run (using CPython; PyPy runs it in about 3 seconds).
- Day 22, part 2: solution takes about 14 seconds to run (using CPython; PyPy runs it in about 18 seconds).

## Generate code for a new day
```sh
./generate-ex.sh ${DAY}
```
