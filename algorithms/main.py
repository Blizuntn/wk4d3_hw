#exercise 1
#reverse the order of the list

# words = ['this' , 'is', 'a', 'sentence', '.']
# def swap(data, front, back):
#     temp = data[front]
#     data[front] = data[back]
#     data[back] = temp
#
# def bsi(data):
#     front = 0
#     back = len(data) - 1
#     while front <= back:
#         swap(data,front,back)
#         front += 1
#         back -= 1
#     print(data)
# bsi(words)

#exercise 2
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data ' \
         'type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an ' \
         'array of buckets or slots from which the desired value can be found'
# def get_count(string):
number = 0
count = {}

new_string = a_text.split()
for i in range(len(new_string)):
    for word in new_string:
        if new_string[i].lower() ==  word.lower():
            number += 1
            count[word]= number
print(count)


#exercsise 3

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False