from os import system, getcwd, walk
from os.path import join, sep
import sys

def read_file():
    ALL_PROBLEMS = [] # Store all the SAT problems in format Problems->[Problem->[Clause->[variables]]]
    ACTUAL_DIRECTORY = getcwd() # Get the current directory path (../SAT/Reductor)
    PARENT_DIRECTORY = sep.join(ACTUAL_DIRECTORY.split(sep)[1:-1]) # Get the parent directory (../SAT)
    PARENT_DIRECTORY = join(sep, PARENT_DIRECTORY) # Apeend SO separator to access the folder
    SAT_instances_directory = join(PARENT_DIRECTORY, "InstanciasSAT") # Joins the parent directory with InstanciasSAT to get into (../SAT/instanciasSAT)
    _, _, SAT_instances = next(walk(SAT_instances_directory))
    for SAT_instance in SAT_instances:
        SAT_file = open(join(SAT_instances_directory, SAT_instance), 'r')
        problem = []
        for line in SAT_file:
            if line[0] == "c":
                continue
            if line[0] == "p" and not problem:
                ALL_PROBLEMS.append(problem)
                problem.append(line[:-1].split(" "))
                continue
            if line[0] == "p":
                ALL_PROBLEMS.append(problem)
                problem = []
                problem.append(line[:-1].split(" "))
                continue
            if problem:
                problem.append(line[:-3].split(" "))
    return ALL_PROBLEMS