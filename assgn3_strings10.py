#10.Reverse string by its words
string=input("Enter a string:")
s=string.split()
print(s)
reverse_s=s[::-1]
#print("Reversed string:",reverse_s)
final_string=" ".join(reverse_s)
print(final_string)
