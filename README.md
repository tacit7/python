
# Table of Contents

1.  [Python](#org8277c99)
    1.  [The Zen of Python](#org3de0dcd)
    2.  [Resources](#org0b07f52)
    3.  [Tools](#orgcb994f1)
    4.  [Data Structures](#org79e9207)
        1.  [Lists](#org131cb09)
    5.  [Lambdas](#orgfefe8e7)
    6.  [Terms and language specific](#orgb464352)
    7.  [Data Structures and Algorithms in Python](#orgac50a81)
        1.  [Chapter 4 Recursion](#org9c3b1e8)
    8.  [Reloading module](#orgaeb7539)
    9.  [Sample code](#org365f809)
        1.  [Shortest range in k sorted lists](#org7f7c42b)
        2.  [Heap](#org41036ca)
    10. [Q&A](#orgcf901bd)
2.  [Algorithms and Data Structures](#org1b5b9cf)
    1.  [Recursion](#orgd51dd97)
        1.  [Some points](#org9a7c8be)
        2.  [Examples](#orgd2fd941)
    2.  [When optimizing and algorithm](#orga97f124)
    3.  [Data structures](#orgae0c6bc)
        1.  [Trees](#org6df04cf)
        2.  [Graphs](#orgcdac5af)
    4.  [Questions](#org2214deb)
        1.  [Find the middle of a linked list](#org30f80cf)



<a id="org8277c99"></a>

# Python

Repo containing python scripts and stuff.


<a id="org3de0dcd"></a>

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


<a id="org0b07f52"></a>

## Resources

-   [A Byte of Python](https://python.swaroopch.com/)
-   [python.org](https://docs.python.org/3/tutorial/index.html)
-   [Installing pyenv](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial)


<a id="orgcb994f1"></a>

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


<a id="org79e9207"></a>

## Data Structures


<a id="org131cb09"></a>

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


<a id="orgfefe8e7"></a>

## Lambdas

    l = lambda var : var * var
    print(l(5))


<a id="orgb464352"></a>

## Terms and language specific

-   **<a id="org551caf9">optional parameters</a>:** Brackets in method signatures denote that the value is in the bracket is optional.
-   **Iterator:** an object that can be iterated upon. EG lists, tuples, strings.

An iterator must implement the methods \_\_iter\_\_() and \_\_next\_\_()


<a id="orgac50a81"></a>

## Data Structures and Algorithms in Python


<a id="org9c3b1e8"></a>

### Chapter 4 Recursion

    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    
    print(factorial(3))


<a id="orgaeb7539"></a>

## Reloading module

    import importlib
    importlib.reload(module)


<a id="org365f809"></a>

## Sample code


<a id="org7f7c42b"></a>

### Shortest range in k sorted lists

Given k sorted lists of integers of size n each, find the smallest range that
includes at least one element from each of the k lists.
If more than one smallest ranges are found, print any one of them.

    list1 = [4, 10, 15, 24]
    list2 = [0,  9, 12, 20]
    list3 = [5, 18, 22, 30]
    
          for numbers in a:
              min 


<a id="org41036ca"></a>

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


<a id="orgcf901bd"></a>

## Q&A

Whats the difference between == and is?

==  evaluates value equality
\`is\`  

How do you print on the same line?

    print("same", end ="") 
    print(" line", end ="") 


<a id="org1b5b9cf"></a>

# Algorithms and Data Structures


<a id="orgd51dd97"></a>

## Recursion

-   You must describe the task at hand in terms of itself
-   Each function call must perform one task
    -   Each function is a worker doing a **part** of the worker

-   Every recursive algorithm involves at least 2 cases:
    
    -   **<a id="orgc7f7b14"></a>:** Simple occurrence that can be answered directly
    
    -   **<a id="org2b2f7fd"></a>:** A complex occurrence that cannot be answered
        directly. Instead, it can be described in terms of smaller occurrences of
        the same problem.
    
    Usually, the [3.1](#orgc7f7b14) is the case where the problem has been solved. 
    
    Key: Ask yourslef, How can I describe this algorithm in terms of a smaller or
    simpler version of itself?


<a id="org9a7c8be"></a>

### Some points

-   All the work usually starts at the end, so think what is the last thing i need to do ([3.1](#orgc7f7b14))
-   Trust that all the function call are doing their work.
-   Where you call your function recursively matters.
    -   Should you place it before or after your function performs their task?
-   Can the base case be 'do nothing'? 
    IE return an empty array, empty string, etc.


<a id="orgd2fd941"></a>

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


<a id="orga97f124"></a>

## When optimizing and algorithm

Bottlenecks
Necessary work
Duplicate Work


<a id="orgae0c6bc"></a>

## Data structures


<a id="org6df04cf"></a>

### Trees

1.  Ordering

    -   **inorder:** 
    
    -   **postorder:** 
    
    -   **preorder:** 


<a id="orgcdac5af"></a>

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


<a id="org2214deb"></a>

## Questions


<a id="org30f80cf"></a>

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

