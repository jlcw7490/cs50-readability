from cs50 import get_string

text = get_string("Text:")

letter=0
word=1
sent=0


#One fish. Two fish. Red fish. Blue fish.
for i in range(len(text)):
    if (text[i]>= 'a' and text[i]<='z') or (text[i]>='A' and text[i]<='Z'):
     letter+=1
  
    elif text[i]== ' ':
     word+=1
  
    elif text[i]=='.' or text[i]=='?' or text[i]=='!':
     sent+=1



grade = round(0.0588*(100*letter/word)-0.296*(100* sent/word)-15.8)
if grade<1:
    print("Before Grade 1")
elif grade < 16:
    print(f"Grade {grade}")
else :
    print("Grade 16+");
    
 
