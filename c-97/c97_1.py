introstring=input("enter string")
charecterCount=0
wordCount=1
for i in introstring:
    charecterCount=charecterCount+1
    if(i == ' '):
        wordCount=wordCount+1

print("Number of words in string")
print(wordCount)
print("Number of charecter in string")
print(charecterCount)
