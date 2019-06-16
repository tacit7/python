
# Table of Contents

1.  [Python](#org0a5c61b)
    1.  [Resources](#org46dd333)
    2.  [Data Structures](#org782b037)
        1.  [Lists](#org431eed9)
    3.  [Lambdas](#orga3e48e1)
    4.  [Tools](#orgf58f54d)
    5.  [Terms](#org232448e)
    6.  [Data Structures and Algorithms in Python](#org103fde1)
        1.  [Chapter 4 Recursion](#org76369ed)
2.  [The Zen of Python](#orga494b4e)


<a id="org0a5c61b"></a>

# Python

Repo containing python scripts and stuff.


<a id="org46dd333"></a>

## Resources

-   [A Byte of Python](https://python.swaroopch.com/)
-   


<a id="org782b037"></a>

## Data Structures


<a id="org431eed9"></a>

### Lists

Pretty much like ruby's arrays.

    list = ["a", "b", "c", "d"]
    
    # accessing elements
    list[0]
    
    # adding elements
    list.append("e")

Python is not as object-oriented as ruby, so you have to use function to work on lists.

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


<a id="orga3e48e1"></a>

## Lambdas

    l = lambda var : var * var
    print(l(5))


<a id="orgf58f54d"></a>

## Tools

-   **[ptpython](https://github.com/prompt-toolkit/ptpython):** Nice REPL for python

    pip install ptpython

-   **[anaconda-mode](https://github.com/proofit404/anaconda-mode):** Code navigation, documentation lookup and completion for Python.


<a id="org232448e"></a>

## Terms

-   **Iterator:** an object that can be iterated upon. EG lists, tuples, strings.

An iterator must implement the methods \_\_iter\_\_() and \_\_next\_\_()


<a id="org103fde1"></a>

## Data Structures and Algorithms in Python


<a id="org76369ed"></a>

### Chapter 4 Recursion

    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    
    print(factorial(3))


<a id="orga494b4e"></a>

# The Zen of Python

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

