from sat_to_3sat import sat_to_3sat
from dimacs_writer import sat_to_dimacs_format

def xsat_to_x1sat(SATPROBLEMS): #coge losproblemas en k-sat y los pasa a k+1-sat
    sat_problems = SATPROBLEMS
    ALL_ANSWERS =[]
    for problem in SATPROBLEMS:
        p_clause = problem[-1]
        problem.pop(-1)
        new_variable = p_clause[0]
        number_of_clauses= p_clause[1]
        new_clause = []
        new_variable += 1
        answer = []
        for clause in problem:
            #primer clausula con la variable
            new_clause= clause.copy()
            new_clause.append(str(new_variable))
            answer.append(new_clause)
            #segunda claucula con el complemento de la variable
            new_clause = clause.copy()
            new_clause.append(str(new_variable * -1))
            answer.append(new_clause)
            #seteo de variables para la proxima interaccion
            new_variable += 1 #aumentamos una variable
            number_of_clauses += 1 #la clausula padre ya estaba contada y solo sumamos una            
        new_variable-=1
        p_clause = [new_variable,number_of_clauses]
        answer.append(p_clause)
        ALL_ANSWERS.append(answer)
    return ALL_ANSWERS


def loop_to_ksat():
    k = input("Digite el numero X al que quieres reducir las instancias SAT, sat->Xsat: ")
    ksat = int(k)
    ksat_answer = sat_to_3sat()
    if ksat == 3:
        ksat_answer = ksat_answer
    if ksat > 3:
        for loop in range(3,ksat,1):
            ksat_answer = xsat_to_x1sat(ksat_answer)
    sat_to_dimacs_format(ksat_answer)    
    return ksat_answer


loop_to_ksat()




