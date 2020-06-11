count=0

passwd1=['naresh','anu','aishu','bunty','chinnu']

print()

while count<3:

    passwd=input('neter the passwd')

    if passwd==passwd1:

        print('access granted')

        break

    elif passwd !=passwd1[]:

        print('passwd denied')

        count = count + 1

if count>=3:

    print('passwd limit exceeded')



################TRy and exception method####################

text='hello'

print(text.find('o'))

passwd1=['naresh','anu','aishu','bunty','chinnu']

name=input('enter you name')

print(passwd1[0:])

try:

    if passwd1.index(name)==passwd1.index(name):

        print('acees granted')

        print('user', name, 'logged in')

except:

       print('No user exist')

       print('do you want to register')

       newuser=input('enter the choice: yes or no')

       if newuser=='yes':

             newuser=input('enter your name')

             passwd1.append(newuser)

             print('user' , newuser,'has been created')



print(passwd1)



####################################################################












 

