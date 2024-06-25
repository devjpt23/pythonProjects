from difflib import SequenceMatcher

a = ['This is page 1', 'This is page 2']
b = ['hello  my name is devpatel']

stringA = str(a)
stringB = str(b)

seq = SequenceMatcher(a=stringA, b=stringB)
print(seq.ratio())