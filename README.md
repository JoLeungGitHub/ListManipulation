# ListManipulation
UTM Hack Lab Code Golf Challenge 1

Did you know that a list of n numbers can be permuted enough times to return to the original list? This permutation can be done by reversing the list and swapping each pair of numbers. Repeating these steps will eventually return the original that we started with. 

Write the shortest Python implementation (in bytes) of a function that takes integer n as an input and outputs the permutations of the lists as described above. 

NOTE: You are not allowed to use the following functions in your implementation: Lambda, Zip, Map.

NOTE: Please don't forget to write a python function that takes in a number n as a parameter. 
Here's a hint of what to output. (Either print or return a list of lists) 
For n = 3 
Output: 
[2, 3, 1] 
[3, 1, 2] 
[1, 2, 3]

---------------------------------------------------------------------------------------

ListManipulation.py: What I had started with. Takes a list input, and prints the permutations of the lists as described above.

ListManipulationIntInput.py: Probably the most correct. Takes an integer input, and prints the permutations of the lists as described above.

ListManipulationEvenIntInput.py: Optimized rotate every 2 elements in the list part of the function... but only works for inputs that are even. Takes an even integer input, and prints the permutations of the lists as described above.

ListManipulationInput.py: New correct function, this one does the same as ListManipulationIntInput.py except it just asks for an integer instead... probably what was wanted in the first place.

The files with READABLE at the end of their names are how they were before I tried to make them as small as possible bytes wise.

# TL;DR: ListManipulationInput.py if you want the user to be prompted for int n OR ListManipulationIntInput.py if you want a function that takes parameter n