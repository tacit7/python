
# Table of Contents

1.  [Python](#org4694cbc)
    1.  [The Zen of Python](#org5ceaa67)
    2.  [Resources](#orgc4b0e86)
    3.  [Tools](#org019b1c5)
    4.  [Data Structures](#org3620cfa)
        1.  [Lists](#org613eb40)
    5.  [Lambdas](#org9fffb32)
    6.  [Terms and language specific](#org84315f9)
    7.  [Data Structures and Algorithms in Python](#org40c5a85)
        1.  [Chapter 4 Recursion](#org53e20e6)
    8.  [Reloading module](#org1eaebc8)
    9.  [Sample code](#org1beba98)
        1.  [Shortest range in k sorted lists](#org988ba92)
        2.  [Heap](#org8ecc52f)
    10. [Q&A](#orgea45d90)
2.  [Algorithms and Data Structures](#orgb9ce2e9)
    1.  [Recursion](#orgfde8b28)
        1.  [Some points](#org4b58edc)
        2.  [Examples](#org284fedd)
    2.  [When optimizing and algorithm](#orged57989)
    3.  [Data structures](#orgc9520a8)
        1.  [Trees](#orged0d83a)
        2.  [Graphs](#org130f776)
    4.  [Questions](#org1ea83f1)
        1.  [Find the middle of a linked list](#org5cc13ef)



<a id="org4694cbc"></a>

# Python

Repo containing python scripts and stuff.


<a id="org5ceaa67"></a>

## The Zen of Python

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one&#x2013; and preferably only one &#x2013;obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than **right** now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea &#x2013; let's do more of those!


<a id="orgc4b0e86"></a>

## Resources

-   [A Byte of Python](https://python.swaroopch.com/)
-   [python.org](https://docs.python.org/3/tutorial/index.html)
-   [Installing pyenv](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial)


<a id="org019b1c5"></a>

## Tools

-   **[anaconda-mode](https://github.com/proofit404/anaconda-mode):** Code navigation, documentation lookup and completion for Python.
-   **IPython:** Pry for python
    pip install ipython
    
        from IPython import embed
        embed()
-   **[ptpython](https://github.com/prompt-toolkit/ptpython):** Nice REPL for python

    pip install ptpython

-   **pyenv:** python version management tool. Equivalent of rbenv.

-   **[anaconda-mode](https://github.com/proofit404/anaconda-mode):** Code navigation, documentation lookup and completion for Python.


<a id="org3620cfa"></a>

## Data Structures


<a id="org613eb40"></a>

### Lists

Pretty much like ruby's arrays.

    list = ["a", "b", "c", "d"]
    
    # accessing elements
    list[0]
    
    # adding elements
    list.append("e")

Python is not as object-oriented as ruby, so you have to use function to work on lists.

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #             __________________ lambda expression!
    even = filter(lambda x: x%2 == 0, numbers)
    print(even)

1.  Methods

    -   append()
    -   **extend(iterable):** appends items from an iterable.
        
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            numbers.extend([11,12,13])
            print(numbers)
    
    -   insert(x,y)
        
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            index = 0
            value = 999
            numbers.insert(index, value)
            print(numbers)
    
    -   remove(value)
    
    **Returns an error if there is no such item.**
    
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        numbers.remove(5)
        numbers.remove(6)
        numbers.remove(7)
        print(numbers)
    
    -   pop([value])
    
    Removes item at the given position and returns it.
    If no value is given, it returns the last element and removes it.
    See note on optional parameters


<a id="org9fffb32"></a>

## Lambdas

    l = lambda var : var * var
    print(l(5))


<a id="org84315f9"></a>

## Terms and language specific

-   **<a id="org7aaa9c1">optional parameters</a>:** Brackets in method signatures denote that the value is in the bracket is optional.
-   **Iterator:** an object that can be iterated upon. EG lists, tuples, strings.

An iterator must implement the methods \_\_iter\_\_() and \_\_next\_\_()


<a id="org40c5a85"></a>

## Data Structures and Algorithms in Python


<a id="org53e20e6"></a>

### Chapter 4 Recursion

    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    
    print(factorial(3))


<a id="org1eaebc8"></a>

## Reloading module

    import importlib
    importlib.reload(module)


<a id="org1beba98"></a>

## Sample code


<a id="org988ba92"></a>

### Shortest range in k sorted lists

Given k sorted lists of integers of size n each, find the smallest range that
includes at least one element from each of the k lists.
If more than one smallest ranges are found, print any one of them.

    list1 = [4, 10, 15, 24]
    list2 = [0,  9, 12, 20]
    list3 = [5, 18, 22, 30]
    
          for numbers in a:
              min 


<a id="org8ecc52f"></a>

### Heap

    class MyHeap:
        def __init__(self, lst):
            self.heap = [0]
            self.heap = self.heap.append(lst)
    
        def heap:
            return heap;
    
        def left_index(self, index):
            return 2 * index
    
        def right_index(self, index):
            return 2*index + 1
    
        def parent_index(self, index):
            return (index/2) + 1
    
        def swap(self, index1, index2):
            temp = self.heap[index1]
            sh


<a id="orgea45d90"></a>

## Q&A

Whats the difference between == and is?

==  evaluates value equality
\`is\`  

How do you print on the same line?

    print("same", end ="") 
    print(" line", end ="") 


<a id="orgb9ce2e9"></a>

# Algorithms and Data Structures


<a id="orgfde8b28"></a>

## Recursion

-   You must describe the task at hand in terms of itself
-   Each function call must perform one task
    -   Each function is a worker doing a **part** of the worker

-   Every recursive algorithm involves at least 2 cases:
    
    -   **<a id="orgda42f1d"></a> base case:** Simple occurrence that can be answered directly
    
    -   <a id="orgc5649cb"></a> recursive::  A complex occurrence that cannot be answered
        directly. Instead, it can be described in terms of smaller occurrences of
        the same problem.
    
    Usually, the [3.1](#orgda42f1d) is the case where the problem has been solved. 
    
    Key: Ask yourslef, How can I describe this algorithm in terms of a smaller or
    simpler version of itself?


<a id="org4b58edc"></a>

### Some points

-   All the work usually starts at the end, so think what is the last thing i need to do ([3.1](#orgda42f1d))
-   Trust that all the function call are doing their work.
-   Where you call your function recursively matters.
    -   Should you place it before or after your function performs their task?
-   Can the base case be 'do nothing'? 
    IE return an empty array, empty string, etc.


<a id="org284fedd"></a>

### Examples

1.  Print the number of stars

        def print_stars(number_stars):
            if number_stars == 1: # base case
                print("*")
            else:
                print("*") # You can move both prints to the top of the function
                print_stars(number_stars - 1)
        
        print_stars(5)

2.  Power

        def power(base, exp): # you  had power(base, power) and the function sig was conflicting with the var
            if exp == 0:
                return 1
            else:
                return base * power(base, exp - 1)
        
        print(power(3, 0))
        print(power(3, 1))
        print(power(3, 3))
    
        1
        3
        27

3.  Palindrome

        
        def is_palindrome(string):
            if len(string) <= 2:
                return True
            else:
                if string[0] == string[-1]:
                    return is_palindrome(string[1:-1])
                else:
                    return False
        
        print(is_palindrome('racecar'))
        print(is_palindrome('palindrome'))
        print(is_palindrome('oliilo'))
    
        True
        False
        True

4.  Print binary

        def print_binary(number):
            if number < 2:
                print(1, end = '')
            else:
                last_digit = number % 2 # See note 1
                rest_of_digits = number // 2 # see note 2
                print_binary(rest_of_digits)
                print(str(last_digit),end = '') # this wont be reached until the very last digit because of the previous line
        print_binary(10)
    
        1010
    
    -   Note 1
        Just like when you want to pop a number in decimal.
        EG
        14 % 10 = 4
        
        11  % 2 = 1
        or 1010
    
    -   Note 2
        The '//' operator is floor division. If you use regular division, you will get decimals.

5.  Reverse array

        def reverse_array(ar):
            print(ar)
            if len(ar) == 0:
                return []
            else:
                last = ar.pop()
                rev = reverse_array(ar)
                rev.insert(0, last)
                print(rev)
                return rev
        
        print(reverse_array([4, 3,2,1,0 ]))
    
        [4, 3, 2, 1, 0]
        [4, 3, 2, 1]
        [4, 3, 2]
        [4, 3]
        [4]
        []
        [4]
        [3, 4]
        [2, 3, 4]
        [1, 2, 3, 4]
        [0, 1, 2, 3, 4]
        [0, 1, 2, 3, 4]


<a id="orged57989"></a>

## When optimizing and algorithm

Bottlenecks
Necessary work
Duplicate Work


<a id="orgc9520a8"></a>

## Data structures


<a id="orged0d83a"></a>

### Trees

1.  Ordering

    -   **inorder:** 
    
    -   **postorder:** 
    
    -   **preorder:** 


<a id="org130f776"></a>

### Graphs

-   **graph:** A graph represents a relationship that exist between pairs of objects.
    These objects are called vertices.
    The object have a pairwise connection called edges.
    
    Graphs can be applied to mapping, transportation, computer networks,
    and electrical engineering.
    
    Graphs are not function plots, histograms, etc.

-   **directed graph:** a set of nodes that are unidirectional.

-   **undirected graph:** a set of nodes that are bidirectional.

-   **degree:** number of edges connecting to a vertex.

-   **indegree:** number of incoming edges connecting to a vertex.

-   **outdegree:** number of incoming edges connecting to a vertex.


<a id="org1ea83f1"></a>

## Questions


<a id="org5cc13ef"></a>

### Find the middle of a linked list

We can:
First approach

-   traverse the list once
-   get size
-   traverse to half the length

Space O(n)
Space O(1)

A better approach:

-   You slow and fast pointer
    
    -   slow goes at 1 speed
    -   fast goes at 2^n speed
        
        Time:  O(n/2)
        Space: O(1)
    
    Example.

    |------------+-----------------------|
    | iternation | list                  |
    |   starting | f                     |
    |            | s                     |
    |            | [0][1][2][3][4][5][6] |
    |------------+-----------------------|
    |          1 | -------f              |
    |            | ----s                 |
    |            | [0][1][2][3][4][5][6] |
    |------------+-----------------------|
    |          2 | -------------f        |
    |            | -------s              |
    |            | [0][1][2][3][4][5][6] |
    |------------+-----------------------|
    |          3 | -------------------f  |
    |            | ----------s           |
    |            | [0][1][2][3][4][5][6] |
    |------------+-----------------------|

