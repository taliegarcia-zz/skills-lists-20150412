# To work on the intermediate problems, set to True
INTERMEDIATE = False

# To work on the advanced problems, set to True
ADVANCED = True


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    odd_list = []
    for num in number_list:
        if num % 2 != 0:
            odd_list.append(num)


    return odd_list

all_odd([1, 2, 7, -5])
all_odd([2, -6, 8])

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_list = []
    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)


    return even_list

all_even([2, 6, -1, -2])
all_even([-1, 3, 5])

def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """    
    for item in my_list:
        print my_list.index(item), item  

print_indeces(["Toyota", "Jeep", "Volvo"])

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_word_list = []
    for string in word_list:
        if len(string) > 4:
            long_word_list.append(string)

    return long_word_list

long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
long_words(["all", "are", "tiny"])


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    if number_list == []:
        smallest = None # None can be used in boolean too! 
            # could have starte diwth comparing all nums to smallest = None, and 
            # python would know that integers are greater than none!
    else:
        number_list.sort()
        smallest = number_list[0] # need square brackets for list index #

    return smallest

smallest_int([-5, 2, -5, 7])
smallest_int([])

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    if number_list == []:
        largest = None # None can be used in boolean too! 
            # could have starte diwth comparing all nums to smallest = None, and 
            # python would know that integers are greater than none!
    else:
        number_list.reverse()
        largest = number_list[0] # need square brackets for list index #

    return largest

largest_int([-5, 2, -5, 7])
largest_int([])

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are floats, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halved_list = []
    for num in number_list:
        halved_list.append(float(num) / 2.0)

    return halved_list

halvesies([2, 6, -2])
halvesies([1, 5])

def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    length_list = []
    for word in word_list:
        length_list.append(len(word))

    return length_list

word_lengths(["hello", "hey", "hello", "spam"])

def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    summed = 0
    for num in number_list:
        summed = summed + num

    return summed

sum_numbers([1, 2, 3, 10])
sum_numbers([])

def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    product = 1

    for num in number_list:
        product = product * num

    # this works for empty list, product = 1! is this because:
    # for an empty list, python just doesnt iterate?
    return product

mult_numbers([1, 2, 3])
mult_numbers([10, 20, 0, 50])
mult_numbers([])

def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    words_joined = ""
    for w in word_list:
        words_joined = words_joined + w

    return words_joined

join_strings(["spam", "spam", "bacon", "balloonicorn"])
join_strings([])

def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    summed = 0.0

    for num in number_list:
        summed = summed + float(num)

    avg = summed / float(len(number_list))
    return avg

average([2, 12, 3])


# ##############################################################################
# # END OF SKILLS TEST; YOU CAN STOP HERE.


# def intermediate_join_strings(list_of_words):
#     """Return a single string with each word from the input list
#     separated by a comma.

#     Do this with a list comprehension. See
#     https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
#     for more info.

#     >>> intermediate_join_strings(["Labrador", "Poodle", "French Bulldog"])
#     'Labrador, Poodle, French Bulldog'

#     As above, if the list given is empty, it's fine if this function
#     raises an error.
#     """
#     return ""


# def adv_find_unique_long_words(my_string):
#     """Return a list of words that only appeared only once
#     within the input string and are at least 6 characters long.

#     >>> adv_find_unique_long_words("I ate popcorn, more popcorn, nachos, kale, and coffee.")
#     ['nachos', 'coffee']

#     """
#     return []


##############################################################################
# You can ignore everything after here


if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            if k.startswith('intermediate') and not INTERMEDIATE:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
