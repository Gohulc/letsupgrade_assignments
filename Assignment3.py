# Write a Python program to reverse a string
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str
s = ("LetsUpgrade")
print(s)
print(reverse(s))
