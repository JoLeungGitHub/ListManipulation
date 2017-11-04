# ListManipulation
UTM Hack Lab Code Golf Challenge 1

Did you know that a list of n numbers can be permuted enough times to return to the original list? This permutation can be done by reversing the list and swapping each pair of numbers. Repeating these steps will eventually return the original that we started with. 

Write the shortest Python implementation (in bytes) of a function that takes integer n as an input and outputs the permutations of the lists as described above. 

NOTE: You are not allowed to use the following functions in your implementation: Lambda, Zip, Map.

ListManipulation.py: What I had started with. Takes a list input, and prints the permutations of the lists as described above.

ListManipulationIntInput.py: Probably the most correct. Takes an integer input, and prints the permutations of the lists as described above.

ListManipulationEvenIntInput.py: Optimized rotate every 2 elements in the list part of the function... but only works for inputs that are even. Takes an even integer input, and prints the permutations of the lists as described above.

ListManipulationInput.py: New correct function, this one does the same as ListManipulationIntInput.py except it just asks for an integer instead... probably what was wanted in the first place.

The files with READABLE at the end of their names are how they were before I tried to make them as small as possible bytes wise.

Noticed the competitions guide lines actually leave a lot to the participants to decide; print as output? list of list? print every step or print after every step is complete? I have pretty much decided to just go with what seems cleanest to me, printing out the "list" every time a full step is complete as well as at the start and end. Even though it would be smaller bytes wise to just concatenate the print statements and remove the beggining xor end print, but then it would print out every rotation and wouldent be as clear what it's doing.

# TL;DR: SUBMISSION SHOULD BE ListManipulationInput.py