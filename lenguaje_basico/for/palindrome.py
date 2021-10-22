 
def esPalindrome(s):
    return s == s[::-1]
 
 
s = "anitalavalatina"
ans = esPalindrome(s)
 
if ans:
    print("Es Palindrome")
else:
    print("No es palindrome")
