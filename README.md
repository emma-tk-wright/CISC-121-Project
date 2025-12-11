# CISC-121-Project

Binary search app

Decomposition of problem:
- Take a list of numbers from the user
- Sort that list
- Ask the user for a target number to search
- Reapeat:
      - Examine the middle element
      - Decide whether to go left or right
-Return the index if found
- Show tge steps so the user can easily follow along the algorithm

Pattern Recognition:
- each step compares the middle number to the target
- If the target is smaller then we only care about the numbers on the left
- If the target is bigger then we only care about the numbers on the right
- The search range gets cut in half every time

Abstratction:
- I can hide the internal details like calculations from the users
- The user can know/see
    - "Enter a list of number"
    - "Enter a target number"
  
Design of Algorithm :
- Input the list of integers and the target integer
- Convert the input string to a Python list to integers
- Sort that list
- Use binary search and keep track of each step
- Output the sorted lsit
- Output a description of the search
- Output the final result 
  
