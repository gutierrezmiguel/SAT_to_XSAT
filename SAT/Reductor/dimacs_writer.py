from pysat.formula import CNF
from os import system, getcwd, walk
from os.path import join, sep
import sys

def sat_to_dimacs_format(SATANSWERS):
    sat_answers = SATANSWERS
    nombre = "sat_dimacs_format_"
    answers_dimacs =[]
    sat_cnf=CNF()
    ACTUAL_DIRECTORY = getcwd() # Get the current directory path (../SAT/Reductor)
    PARENT_DIRECTORY = sep.join(ACTUAL_DIRECTORY.split(sep)[1:-1]) # Get the parent directory (../SAT)
    PARENT_DIRECTORY = join(sep, PARENT_DIRECTORY) # Apeend SO separator to access the folder
    X_SAT_directory = join(PARENT_DIRECTORY, "X-SAT")
    for index,answer in enumerate(SATANSWERS):
        num_archivo=str(index)
        nombre_res= nombre + num_archivo
        answer.pop(-1)
        for clause in answer:
            for index,variable in enumerate(clause):
                clause[index] = int(variable)
            sat_cnf.append(clause)
        sat_cnf.to_file(join(X_SAT_directory,nombre_res+".cnf"))
        sat_cnf=CNF()
    return answers_dimacs

