### Reachability_Matrix

## Goal
The goal of this project is to calculate the ***reachability matrix***.

*Graphs* are made by *nodes* on which ***path*** are distributed randomly.
*ones* represent a ***path*** between two *nodes*.

If a *node* presents *successors* there will be *one* for each *successor*, meaning in lines.
If a *node* presents a predecessor there will be *ones* for each predecessor, meaning in columns.

This program starts by asking to the *user* the matrix he wants to use, so the ***transitive matrix***.
The program asks then to which ***path*** the matrix should be calculated.

If *ones* exist then in a matrix elevated to the power of a ***path***, it means that at least one ***path*** 
exists between the *predecessor* and the *successor*. In case *predecessor* and *successor* are identicals, that is called a circuit.

The ***closure*** of a matrix is when we can start from a *node*, following a ***path*** and coming back to the same *node***, called a *circuit*.

The final result of this program is the ***reachability matrix***.

## Files list

console.py         main of the program
new_matrix.py      user selection
transitive.py      path selection
multiplication.py  multiplication at the power of the path
closure.py         final result calculation

## Update
Creation - November, 4th 2020

## Advanced Technicien Certificate project
"BTS SIO SLAM"
