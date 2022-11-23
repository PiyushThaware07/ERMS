import random
max_length = 6
character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','y']
digits = ['0','1','2','3','4','5','6','7','8','9']
combine_list = character+digits
generate = [random.choice(combine_list) for i in range(max_length)]
emp_id = ""
for item in generate:
    emp_id+=item
print(emp_id)    
