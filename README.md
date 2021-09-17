# Linux-SHecker
Mac/Linux checker for Competitive Programming
---
## How to use:

Copy input testcases to Input folder.  
Copy output testcases to Output folder.  
Copy cpp file to Code folder.
Run SHecker.py

---
## Types of testcases accepted:
 - file.[num].in
 - [num].in
 - file.in.[num]
 
---
## Making a custom grader:
To create a custom grader create a function grader(str input,str answer,str output) in grader.py who returns a boolean if it is a correct answer.
The current grader compares answer and input, in the future it will be replaced with a better grader.

### To do:
 - Make a better grader.
 - Calculate Memory (MLE)
 - Make posible run different codes and make a table.

> Needs termcolor module to work `pip install termcolor`
