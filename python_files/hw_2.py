"""
    Given a string, return a new string where the first and last chars
    have been exchanged.
    """

"""
    Use a list comprehension to write a method named removeRange that accepts a list of
    integers and two integer values min and max as parameters and removes all elements
    values in the range min through max (inclusive).
    For example, if a list named alist stores
    [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], the call of remove_range(alist, 5, 7);
    should change the list to store [9, 4, 2, 3, 1, 8].

   *** Important: your code must use comprehensions and should not be more than
   two lines of code including the return statement ***
    """

"""
_____________________________

    Write a function named wordCount that accepts a list of strings as a parameter and
    returns a count of the number of unique words in the list. Do not worry about
    capitalization and punctuation; for example, "Hello" and "hello" and "hello!!" are
    different words for this problem.
    *** Solution should not be more than 3 lines of code (can be less)
     including the return statement ***
    """

list = ["Hello", "hi", "hi", "how","you","Hello", "how", "bean"]
print(list)

new_set = set(list)
print(new_set)
print(len(new_set))



""" 
counter_counter = 0

for i in range(len(list)):
    counter = 0
    for j in range(len(list)):
        if list[i] == list[j]:
          counter += 1
    if counter == 1:
       counter_counter += 1
     
print(counter_counter)
"""