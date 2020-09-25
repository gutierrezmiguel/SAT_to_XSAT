clause = [-7 ,-86 ,157 ,1 ,2 ,3 ,4 ,5]
answer = []
new_clause = []
new_variable = 8


#priemra clausula
new_clause= clause.copy()
new_clause.append(new_variable)
new_clause.append(new_variable + 1)
print(new_clause)
answer.append(new_clause)
print(answer)
#segunda clausula
new_clause= clause.copy()
new_clause.append(new_variable * -1 )
new_clause.append(new_variable + 1)
print(new_clause)
answer.append(new_clause)
print(answer)
#tercera clausula
new_clause= clause.copy()
new_clause.append(new_variable )
new_clause.append((new_variable + 1) * -1)
print(new_clause)
answer.append(new_clause)
print(answer)
#cuarta clausula
new_clause= clause.copy()
new_clause.append(new_variable * -1 )
new_clause.append((new_variable + 1) * -1)
print(new_clause)
answer.append(new_clause)
print(answer)


new_clause.append(clause[-1])
new_clause.append(clause[-2])

print(clause[-1])
print(clause[-2])


for i in range(3,5,1):
    print("hola" + str(i))