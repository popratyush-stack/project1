#function 
#1 type
age=str(45)
print(type(age))
#2 len
name= 'abracadabra'
print(len(name)) 
passcode= name
if len(passcode)>8:
    print("Valid")
else:
    print("Invalid")

grades={'ram':'a+','shyam':'a+','hari':'a'}
result= list(grades.values())
step2= result.count('a')
print(step2)
#string
user_input='i love python python python m'
result=user_input.count('python')
print(result)
#replace method
user_input= "I am venom "
result = user_input.replace('venom','spiderman')
print(result)
#remove prefix method
user= "I am unhappy "
result = user.removeprefix('I')
print(result)
#replacing multi characters
naam= "I am good" 
transition= naam.maketrans({'g':'G'})
print(naam.translate(transition)) 

#task
name='laxmi  prasad  devkota'
nospace= name.strip() 
result='_'.join(nospace.split())
print(result)

user= "i love south indian movies"
cap= user.title()
tal=cap.split()
i=''.join(reversed(tal))
print(i)