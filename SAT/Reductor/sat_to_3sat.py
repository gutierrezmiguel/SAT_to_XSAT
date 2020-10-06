from leer_archivo import read_file

def sat_to_3sat():
    ALL_PROBLEMS = read_file()
    FINAL_ANSWER = []
    ALL_ANSWERS= [] #this is the return of the program and its all the problems in 3sat form
    for problem in ALL_PROBLEMS:
        number_of_variables = 0 #numero de variables que contiene el problema , este es dictado por la tercer variable del primer arreglo del "problem" 
        number_of_clauses = 0 #numero de clausulas que contiene el problema ,  este es dictado por la cuarta variable del primer arreglo del "problem"
        answer = [] #aqui acumularemos las clausulas nuevas , esta es la respuesta a un problema sat
        new_clause = [] #la usaremos como ayuda para crear las nuevas clausulas de la respues
        for index,clause in enumerate(problem):
            variables_in_clause = len(clause)
            if clause[0] == "p":
                number_of_clauses = int(clause[3])
                number_of_variables = int(clause[2])
                new_variable = number_of_variables + 1
                continue
            if variables_in_clause == 1:
                #primera clausula con la variable1 y la variable2
                new_clause= clause.copy()
                new_clause.append(str(new_variable))
                new_clause.append(str(new_variable + 1))
                answer.append(new_clause)
                
                #segunda clausula con el complemento de variable1 y la variable2
                new_clause= clause.copy()
                new_clause.append(str(new_variable * -1 ))
                new_clause.append(str(new_variable + 1))
                answer.append(new_clause)
                
                #tercera clausula con la variable1 y el complemento de la variable2
                new_clause= clause.copy()
                new_clause.append(str(new_variable ))
                new_clause.append(str((new_variable + 1) * -1))
                answer.append(new_clause)
                
                #cuarta clausula con ambos complementos
                new_clause= clause.copy()
                new_clause.append(str(new_variable * -1 ))
                new_clause.append(str((new_variable + 1) * -1))
                answer.append(new_clause)
                #seteo de variables para la siguiente iteracion
                new_variable += 2 #cuando la clausula solo tiene una variable abremos creado 2 variables mas y debemos sumarlas para no repetirlas
                number_of_clauses += 3 #la clausula padre ya estaba sumada en el numero de clausulas entonces no se cuenta y las otras 3 se suman
                continue
            if variables_in_clause == 2:
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
                continue
            if variables_in_clause == 3:
                new_clause = clause.copy()
                answer.append(new_clause)
                continue
            if variables_in_clause > 3:
                
                #primer clausula
                new_clause = []
                new_clause.append(clause[0])
                new_clause.append(clause[1])
                new_clause.append(str(new_variable))
                answer.append(new_clause)
                number_of_clauses += 1 #primera clausula creada
                #concatenacion
                for i in range(2,variables_in_clause-2):
                    new_clause = []
                    new_clause.append(str(new_variable * -1))
                    new_clause.append(clause[i])
                    number_of_clauses += 1 #todas las clausulas que nacen de las variables que se encuentras en el medio
                    new_variable+=1
                    new_clause.append(str(new_variable))
                    answer.append(new_clause)
                new_clause = []
                new_clause.append(str(new_variable * -1))
                new_clause.append(clause[-2])
                new_clause.append(clause[-1])
                number_of_clauses += 1 #la clausula que cierra
                #reset variables
                answer.append(new_clause)
                new_variable += 1
                continue
        #Añadimos la solucion de sat a un arreglo FINALANSWER que contiene 3 arreglos el primero es la reduccion de sat a 3sat el segundo contiene un numero de variables y el tercero un numero de clausulas
        
        #quitamos la ultima variable extra que se creo pa no contar 1 de mas siempre
        new_variable -= 1
        p_clause = [new_variable,number_of_clauses]
        answer.append(p_clause)
        ALL_ANSWERS.append(answer)
    return ALL_ANSWERS

sat_to_3sat()