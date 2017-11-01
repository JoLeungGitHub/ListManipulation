# ListManipulation
UTM Hack Lab Code Golf Challenge 1

Did you know that a list of n numbers can be permuted enough times to return to the original list? This permutation can be done by reversing the list and swapping each pair of numbers. Repeating these steps will eventually return the original that we started with. 

Write the shortest Python implementation (in bytes) of a function that takes integer n as an input and outputs the permutations of the lists as described above. 

NOTE: You are not allowed to use the following functions in your implementation: Lambda, Zip, Map.

ListManipulation.py: What I had started with. Takes a list input, and prints the permutations of the lists as described above.

ListManipulationIntInput.py: Probably the most correct. Takes an integer input, and prints the permutations of the lists as described above.

ListManipulationEvenIntInput.py: Optimized rotate every 2 elements in the list part of the function... but only works for inputs that are even. Takes an even integer input, and prints the permutations of the lists as described above.

The files with READABLE at the end of their names are how they were before I tried to make them as small as possible bytes wise.

# TL;DR: SUBMISSION SHOULD BE ListManipulationIntInput.py