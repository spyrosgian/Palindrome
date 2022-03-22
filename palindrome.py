#---------------------------------------------------------------------------------------
#Palindrome
#---------------------------------------------------------------------------------------

#Input string
s0 = input ('Please enter string: ') ; print ('')

#if statement to check if input is more than 4 characters.
if len (s0) > 10:
    print ('String too long.')
    exit (3)

#if statement to check if input contains digits.
if s0.isalpha() == False:
    print ('Invalid input.')
    exit (2)

#Tranform everything to lowercase letters
s1 = s0.lower()

#Check if word is a palindrome
if len(s1) == 1:
    print ('String is a palindrome.')

elif len (s1) % 2 == 0: #Even number

    tf=0

    for i in range (0, (int(len (s1)/2))):

        if s1 [i] == s1[-i-1]:
             tf = tf+1

        else:
            print ('String is not a palindrome')
            exit (1)

        if tf == (len(s1)/2):
            print ('String is a palindrome.')

else: #Odd number

    tf=0

    for i in range (0, (int((len (s1)-1)/2))):

        if s1 [i] == s1[-i-1]:
             tf = tf+1

        else:
            print ('String is not a palindrome')
            exit (0)

        if tf == ((len(s1)-1)/2):
            print ('String is a palindrome.')

#---------------------------------------------------------------------------------------
