# Scrivere il codice dell'esercizi qui dentro
def mydivmod(num,den):
    """ This function make a division num/den, and return a tuple with (quotient,remainder)
    Input: num type int or float. the dividend
           den type int or float. the divisor
    Output: tuple (quotient num//den, remainder num % den)
    Error in case of division by zero (if den is 0)
    Example (2,1) = (2,0) """
    if den == 0:
        raise ZeroDivisionError("Second argument to a division operation was zero")
    q = num//den #quotient
    r = num % den #remainder
    return q,r

assert(mydivmod(4,2))==(2,0) #MIGLIORAMENTO DI TRY/EXCEPT

#test mydivmod giulia. lezione
#import sys

try:
    print(mydivmod(4,0))
except ZeroDivisionError as e:
    pass #print(e)
    ## meglio usare pass così non fa nulla
    #sys.exit(0)

#list_of_number = [1,4,5] #test
def pow_list(list_of_number):
    """ This function takes a list and returns another
    list with each value raised to the power of 2
    input: list of number
    output: list of input number squared

    Example pow_list([1, 2, 3] == [1, 4, 9])
    """
    squared_list = [] #output list
    for x in list_of_number:
        squared_list.append(x ** 2) #squared each element
    return squared_list

    #elevato ad una potenza generica
    #def pow_list(list_of_number, exp):
        # squared_list = [x ** exp for x in list_of_number]
        # return squared_list

        # squared_list = [x ** exp for x in list_of_number if x == 2] limito la lista a x = due
        # [n ** 2 for n in [1,2,3,4,5,6] if n == 2]
        #operatore modulo = %
        # squared_list = [x ** exp for x in list_of_number if x % 2] limito la lista ai numeri dispari PERCHé prende il TRUE??
        # squared_list = [x ** exp for x in list_of_number if x % 2 == 0] limito la lista ai numeri pari

def count_words(s):
    """ This trivial function counts the
    number of words in the given string.
    Hint: try executing the following command in the
    Python console: 'hello world'.split(' ')
    Input: string
    Output: number of words """
    #count = len(s.split(' '))  #NOTE if there is a final space it find a word more (error)
    #return count
    """
    Scrittura compatta
    
    Try:
        string = string.strip() #tolgo spazi iniziali e finali
        return string.count(" ")+1 #conto spazi e aggiuno 1 per contare le parole
    except Exception:
        return 0 # correggere solo se c'è un problema ritorna 0. i.e. se passo una lista con tutti spazi, o con un nan, 
        #qui torna 0 sempre se c'è un errore lo nasconde. meglio specificarlo o toglierlo """

    count = 0
    word = False
    for ch in s:
        if ch != ' ':
            if not word:
                count += 1
                word = True #i'm in a word
        else:
            word = False
    return count

def reverse_string(s):

    """ This function  takes a string and returns it reversed.
    For example, 'hello' becomes 'olleh'
    reverse_string("hello") == "olleh" """
    s = s[::-1] #slicing
    return s
""" 
    s = "Maria"
    s[0] 'M'
    s[0:2] 'M'
    s[0:3] 'Mar' 
    s[5] error
    s[0:5:1] 'Maria'
    s[0:5:2] 'Mra'
    s[:] 'Maria' di default prende 0:5
    s[::1] incrementa  in avanti
    s[::-1] decrementa dalla fine verso l'inizio 'airaM'
    reversed(s)
    "".join(s) #così non inverto 'Maria'
    "".join.(reversed(s)) 'airaM'
    ",".join.(reversed(s)) 'airaM' #uso la virgola per unire 
    """

def factorial(num):
    """ This function computes the factorial of a
     given number. Factorial of n (n!) is the product of all
     positive integers from 1 to n.
     For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120 """
    """  
    while num > 0:
        num_2 = num - 1
        fact = num * num_2
        num = num_2
    return fact  """
    fact=1 #init
    for i in range(1,num+1):
        fact *= i
    return fact

def is_palindrome(s):
    """ This function checks if a given string is
    a palindrome.A palindrome reads the same forwards and
    backwards, e.g., 'racecar'.  [::-1].
    is_palindrome("racecar") == True """
    s_1 = s[::-1]
    if s_1==s:
        return True
    else:
        return False

def sum_even_numbers(ls):
    """ This function takes a list of numbers
     and returns the sum of all even numbers in the list
      Example: sum_even_numbers([1, 2, 3, 4, 5]) == 6
      Input: list of number
      Output: sum of the even number in the list  """
    summ = 0
    if ls is None:
        ls = []
    for x in ls:
        if x % 2 == 0:
            summ += x
    return summ

def find_max(ls):
    """ This function takes a list of numbers
    and returns the largest number in the list.
    Example: find_max([3, 1, 4, 1, 5]) == 5  """
    max_val = ls[0]
    for n in ls:
        if n>max_val:
            max_val=n
    return max_val(ls)
    #return max

def count_vowels(s):
    """ This function takes a string and returns the count of vowels in it.
    ('a', 'e', 'i', 'o', 'u')
    For example, count_vowels("hello world") == 3
    'hello world' contains 3 vowels. """
    count = 0
    for char in s:
        if char in 'aeiou':
            count += 1
    return count

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
#BUGS
num= 5
#LISTA
def add_number(num, li=[]):
    return li.append(num)
add_number(num,li=[])
#add_number(2)
#add_number(2,li=[])

#così non c'è più il bug
def add_number(num, li=[]):
    li.append(num) #oggetti mutabili lista
    return li

#DIZIONARIO
def add_number(num, d={}):
    d[num] = [num]#oggetti mutabili dizionatrio
    return d
add_number(3) #con il 2 non si vede il bug. dal 3 in avanti

#così non c'è più il bug
def add_number(num, d=None):
    if d is None:
        d = {}   #oggetto mutabile definito dentro la funzione . prima definito come None
    d[num] = [num]#oggetti mutabili dizionatrio
    return d  """