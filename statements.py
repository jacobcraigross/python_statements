#Print only the words starting with the S.
s_words = 'The important thing is that short and strenuous reverence be paid to the spirit of discipline. Three things keep a body of troops in fighting form: fighting spirit, strength and discipline.'

for word in s_words.split():
    if word[0] == 's':
        print word

# short
# strenuous
# spirit
# spirit
# strength
# ---------

# Use range() to print all the even numbers from 1 - 50

print range(0, 51, 2)

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


# use list comprehension to create a list of numbers from 1 to 50 that are div. by 3

print [x for x in range(50) if x % 3 == 0]

# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


# Iterate the string and if the word has an even amt of letters, print even!

string = 'The important thing is that short and strenuous reverence be paid to the spirit of discipline. Three things keep a body of troops in fighting form: fighting spirit, strength and discipline.'

for word in string.split():
    if len(word) % 2 == 0:
        print word + " <-- is even!"

# is <-- is even!
# that <-- is even!
# be <-- is even!
# paid <-- is even!
# to <-- is even!
# spirit <-- is even!
# of <-- is even!
# things <-- is even!
# keep <-- is even!
# body <-- is even!
# of <-- is even!
# troops <-- is even!
# in <-- is even!
# fighting <-- is even!
# fighting <-- is even!
# strength <-- is even!
# ---------------------


# Fizz Buzz

for num in xrange(1, 101):
    if num % 5 == 0 and num % 3== 0:
        print 'FizzBuzz'
    elif num % 3 == 0:
        print 'Fizz'
    elif num % 5 == 0:
        print 'Buzz'
    else:
        print num


# Create a list of the first letters for every word in this string.

string_two = 'Python will get you out of a pinch and then some!'

print [word[0] for word in string_two.split()]

# ['P', 'w', 'g', 'y', 'o', 'o', 'a', 'p', 'a', 't', 's']
