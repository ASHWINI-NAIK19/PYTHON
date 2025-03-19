name=input("Enter Student Name:")
eng=float(input("Enter English Marks:"))
hin=float(input("Enter Hindi Marks:"))
Kan=float(input("Enter Kannada Marks:"))
sci=float(input("Enter Science Marks:"))
social=float(input("Enter Social Marks:"))
math=float(input("Enter Maths Marks:"))
print("---REPORT CARD----",name)
total=eng+hin+Kan+sci+social+math
print("Total marks scored:",total)
percent=total/6
print("Total Percentage scored:",percent)
if percent>40:
    print("Congratulations! you are passed")

