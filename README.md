# Personal attempts at solving Advent of Code 2024 in Python

In every `d{day}` folder there are my solutions to that day's problems.
The day's input sits in that folder in a file named `input` (I don't publish them here).

The programs get their input from a stdin (that might require an end of stream).
This can be accomplished, for instance, by:

- redirecting the input file into the program,
- heredocs,
- typing the input followed by a `^D`.

Most solutions:
- were submitted within 24 hour of the problem's publishing,
- use only Python's standard library,
- run pretty quickly (<1 second).

The solutions for which this doesn't fully apply have a comment at the beginning with details.
These are:
- Day 6, part 2: solution takes about 8 seconds to run.
- Day 7, part 2: solution takes about 11 seconds to run.

## Generate code for a new day
```sh
./generate-ex.sh ${DAY}
```
