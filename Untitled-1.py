def is_palindrome(s):
  # remove all the non-alphanumeric characters from the string
  s = ''.join(c for c in s if c.isalnum())
  
  # convert the string to lowercase 
  s = s.lower()
  
  #  check if the string is equal to its reverse
  return s == s[::-1]

# Get a string from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
  print("The string is a palindrome")
else:
  print("The string is not a palindrome")