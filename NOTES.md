# Cracking Code Interview Notes

---
## Big O

<u>Big O, Big Omega, Big Theta</u>

- Big O describes an upper bound on time/space - i.e. upper limiting behaviour of a function.

- Big Omega describes a lower bound on time/space - i.e. lower limiting behaviour of a function.

- Big Theta describes a tight bound on time/space - i.e.tight limiting behaviour of a function.

<u>Best, Worst, Expected Case</u>

- Best Case - input which output shortest time/space.

- Worst Case - input which output longest time/space.

- Average Case - input which output average time/space.


**Note**: There is no correlation between Big O and Worst Case; the former describes the runtime upper bound whilst the latter describes for a particular set of input.


General Rules on Asymptotic Algebra:

```sh
# Drop Constants
O(kN) -> O(N)
# Drop Non-Dominant
O(N^2 + N) -> O(N^2)
# Addition
O(N) + O(M) -> O(N + M) 
# Multiplication
O(N) * O(M) -> O(N * M) 
```

<u>Ammortized Time</u>

Ammortized time is a way of describing fluctuating time complexity depending on state of algorithm. 
Ammortized time accounts for the Worse Cases in its analysis.



## Data Structures

<u>Hash Table</u>

A Hash Table is a data structure that maps keys to values for highly efficient lookup.

Implementation:
1. Hash Key to an `int` or `float`.
2. For a map of size `N` (i.e. with N indexes), create a mapping from hash to index. 
    e.g. `hash -> hash%N`
    Note: as there are infinite keys but finite indexes, there will be **collisions**.
3. At every index, create a Linked List containing keys as values.

<u>Linked List</u>

A Linked List is a data structure that represents a sequence of Nodes.

Each node of a *singly* Linked List points to the next Node.

Each node of a *doubly* Linked List points to both the next and previous Nodes.

Unlike in Arrays that have O(1) lookups, Linked Lists have O(N) time as lookup involve iterating over the Nodes.

The benefits of a Linked List is that you can add and remove Npdes in the beginning in O(1) time.