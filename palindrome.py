text = str(input("Enter a text : "))
text1 = ""
for i in text:
    text1=i + text1
if text1==text:
    print(f"{text} is a palindrome...")
else:
    print(f"{text} is not a palindorme....")