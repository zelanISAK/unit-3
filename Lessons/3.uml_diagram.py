database = {'emp_1':{"Name":"Frank Murphy","Email":"frank.murphy5@company.xy","Position":"Driver","Age":39,"Salary":30000},
            'emp_2':{"Name":"Barney Stinson","Email":"barney.stinson@company.xy","Position":"CEO","Age":39,"Salary":30000},
            'emp_3':{"Name":"Saul Goodman","Email":"saul.goodman@company.xy","Position":"Lawyer","Age":39,"Salary":30000},
            'emp_4':{"Name":"Walther White","Email":"w.white@company.xy","Position":"Cook","Age":39,"Salary":30000},
            'emp_5':{"Name":"Homelander","Email":"homelander@company.xy","Position":"Guard","Age":39,"Salary":30000}}

def greetings(database:dict,name:str)->str:
    name,age,role,email = database[name]['Name'],database[name]['Age'],database[name]['Position'],database[name]['Email'],
    message=f'Hi, {name} you are {age} years old and work as a {role} in our company. Your email address is {email}'
    return message

print(greetings(database,"emp_1"))

#How many lines of code?
#How robust is your code to changes?

