''' Assignment-2
Yash Raj Singh, bt21107074'''

# Question-1

print("Question 1")
sent = "Python is a case sensitive language"
length_sent = len(sent)
print(length_sent)
reversed_sent = sent[length_sent::-1]
print(reversed_sent)
sliced_sent = sent[10:26]
print(sliced_sent)
sent_2 = sent
print(sent_2.replace("a case sensitive","object oriented"))
print(sent.index("a"))
print(sent.replace(" ",""))
print("----------------------------------------------------")

# Question 2

print("Question 2")
name = "Yash Raj Singh"
SID = "21107074"
dep_name = "Mechanical"
CGPA = "9.3"
print(f"Hey, {name} here!\nMy SID is {SID}\nI'm from {dep_name} department and my CGPA is {CGPA}")
print("----------------------------------------------------")

# Question 3

print("Question 3")
a = 56
b = 10
print("a & b = ",a & b)
print("a | b = ",a | b)
print("a ^ b = ",a ^ b)
c = a << 2
d = b << 2
print("a and b after left shifting 2 bits : ",c,d)
e = a >> 2
f = b >> 4
print("a after right shifting 2 bits and b after right shifting 4 bits : ",e,f)
print("----------------------------------------------------")

# Question 4

print("Question 4")
sentence = str(input("Enter your sentence here : "))
a = sentence.find("name")
if a == -1:
    print("No")
else:
    print("Yes")
print("----------------------------------------------------")
# Question 5

print("Question 5")
a, b, c = list(map(float,input("Enter 3 sides of triangle separated by space : ").split()))
sumlist = []
new = int(bool(a > b + c))
sumlist.append(new)
new_2 = int(bool(b > a + c))
sumlist.append(new_2)
new_3 = int(bool(c > b + a))
sumlist.append(new_3)
print(sumlist)

answer = bool(sumlist[0] + sumlist[1] + sumlist[2] > 0)
match answer:
    case True:
        print("No")
    case False:
        print("yes")
print("----------------------------------------------------")

# Question 6

print("Question 6")
n1 = int(input("Enter a : "))
n2 = int(input("Enter b : "))
n3 = bin(n1 ^ n2)
n3str = str(n3).count('1')
print("Number of bits needed to be flipped are : ",n3str)
print("----------------------------------------------------")
