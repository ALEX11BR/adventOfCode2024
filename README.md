# Personal attempts at solving Advent of Code 2024 in Python

In every `d{day}` folder there are my solutions to that day's problems.
The day's input sits in that folder in a file named `input` (I don't publish them here).

The programs get their input from a stdin (that might require an end of stream).
This can be accomplished, for instance, by:

- redirecting the input file into the program,
- heredocs,
- typing the input followed by a `^D`.

## Generate code for a new day
```sh
./generate-ex.sh ${DAY}
```
