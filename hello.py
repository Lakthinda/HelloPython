
txt = ["The Learn Python Challenge Casino.","Elakiri Saha Jalaya"]

def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

# result = word_search(txt,'Casino')

keywords = ["python","saha"]

dictionary = {}

print(result)

# def has_lucky_number(numbs):
#     temp_list = [num % 7 == 0 for num in numbs]
     
#     return any(temp_list)

# print(has_lucky_number([7,0,1,2,4]))

# def fashionably_late(arrivals, name):
#     """Given an ordered list of arrivals to the party and a name, return whether the guest with that
#     name was fashionably late.
#     """
#     if(name in arrivals):
#         list_length = len(arrivals)
#         startList = list_length/2 if (list_length % 2 == 0) else len(arrivals)/2 +1
#         temp_list = arrivals[int(startList):-1]
#         return True if(name in temp_list) else False
    
#     return False


# # party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# party_attendees = ['Paul', 'John', 'Ringo', 'George']

# fashionably_late(party_attendees,'John')

# if( None == 'None'):
#     print('Awesome')

#--------------
# def greet(who = "lakthinda"):
#     print ("Hello ", who)


# greet()
# greet('Thomas')
# greet('Mr.Lakthinda')
# #------------------------------

# x = -10
# y = 5
# # Which of the two variables above has the smallest absolute value?
# smallest_abs = min(abs(x), abs(y))

# print(smallest_abs)


# x = 12
# print(x.imag)

# c = 12 + 3j
# print(c.imag)
# print(x.bit_length())

