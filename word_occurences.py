#Text: this is a collection of words of nice words this is a fun thing it is
#a : 2
#collection : 1
#fun : 1
#is : 3
#it : 1
#nice : 1
#of : 2
#thing : 1
#this : 2
#words : 2

words = {}
text = input("Type something: ")
words2 = text.split()
for word in words2:
    freq = words.get(word, 0)
    words[word] = freq + 1

words2 = list(words.keys())
words2.sort()
max_length = max((len(word) for word in words2))
for word in words2:
    print("{:{}} : {}".format(word, max_length, words[word]))