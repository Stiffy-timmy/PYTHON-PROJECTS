with open ("story.txt","r") as fobj:
    story=fobj.read()

words=set()
starts_with="<"
ends_with=">"
word_index=-1

# TO GET UNIQUE WORDS, FIRST DECLARE set() datatype and then use .ADD() INSTEAD OF .APPEND()
for i,char in enumerate(story):
    if char==starts_with:
        word_index=i
    
    if char == ends_with and word_index != -1:
        word=story[word_index:i+1]
        words.add(word)
print(words)

#Creating a Dictionary 
answers={}
for word in words:
    answer=input("Enter your alternate word for " + word + " :")
    answers[word]=answer
    
print()
print(answers)
print()
print()
print("The modified story is as follows:")

#you have to store the string generated by .replace() method by creating a python object
for word in words:
    # DON'T DO THIS:- modified_story=story.replace(word, answers[word]), it'll show error
    story=story.replace(word, answers[word])

print(story)
    

    

    
    
   
   
