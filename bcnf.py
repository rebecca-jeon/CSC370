# Counts the number of steps required to decompose a relation into BCNF.

from relation import *
from functional_dependency import *

# You should implement the static function declared
# in the ImplementMe class and submit this (and only this!) file.
# You are welcome to add supporting classes and methods in this file.

check_relations = set()

class ImplementMe:

    # Returns the number of recursive steps required for BCNF decomposition
    #
    # The input is a set of relations and a set of functional dependencies.
    # The relations have *already* been decomposed.
    # This function determines how many recursive steps were required for that
    # decomposition or -1 if the relations are not a correct decomposition.
    @staticmethod
    
    def DecompositionSteps( relations, fds ):
        num_recursions = 0
        relations_set = relations.relations
        num_relations = len(relations_set)
        fd_set = fds.functional_dependencies
        num_fds = len(fd_set)
        og_r = og_relation(relations_set)
        s_key, num_recursions, passed_fd = violation(og_r, fd_set, relations_set, num_recursions)

        if num_relations <= 1:
            return s_key
        
        if s_key == 0 and num_relations > 1:
            return -1
        
    
        return num_recursions




def og_relation(relations_set):
    og_set = set()
    for relation in relations_set:
        attributes = relation.attributes
        og_set = og_set.union(attributes)

    return og_set

def violation (og_r, fd_set, relations_set, num_recursions):
    """
    This function checks if every functional dependencies' keys are superkeys.
    If they are then the function returns 0 and it not, they return -1(BCNF violation).
    """
    passed_fd = set()

    for fd in fd_set:
        fd_closure = set()

        fd_closure = fd_closure.union(fd.left_hand_side, fd.right_hand_side)
          
        f_d = set()
        f_d.add(fd)
        other_fd_set = fd_set - f_d

          
        while len(other_fd_set) != 0:
            length = len(other_fd_set)
            for other_fd in other_fd_set:
                other = set()
                other.add(other_fd)
                lhs = other_fd.left_hand_side
                rhs = other_fd.right_hand_side

                if lhs.issubset(fd_closure):
                    fd_closure = fd_closure.union(rhs)
                    other_fd_set = other_fd_set - other
                
            if length == len(other_fd_set):
                num_recursions = other_Relations(fd, og_r, fd_closure, relations_set, num_recursions, fd_set)
                return -1, num_recursions, passed_fd

        if fd_closure != og_r:
            num_recursions = other_Relations(fd, og_r, fd_closure, relations_set, num_recursions, fd_set)
            return -1, num_recursions, passed_fd


        passed_fd.add(fd)


    return 0, num_recursions, passed_fd
            
      
def other_Relations(fd, og_r, fd_closure, relations_set, num_recursions, fd_set):
    key = fd.left_hand_side

    other_r = og_r - fd_closure
    other_r = other_r.union(key)

    num_recursions += 1

    cl_fd = find_fd_closure(fd_closure, fd_set)

    other_fd = find_fd_closure(other_r, fd_set)

    if len(cl_fd) == 0 :
        answer = False
        fd_closure = Relation(fd_closure)
        for relation in relations_set:
            if fd_closure == relation:
                answer = True

        if answer == False:
            num_recursions = -1
            return num_recursions

        other_key, num_recursions, passed_fd = violation(other_r, other_fd, relations_set, num_recursions)
        if len(passed_fd) >= 1:
            answer = is_fd_in_relation(passed_fd, relations_set)
            if answer == False:
                return -1

    if len(other_fd) == 0:
        answer = False
        other_r = Relation(other_r)
        for relation in relations_set:
            if other_r == relation:
                answer = True
           

        if answer == False:
            num_recursions = -1
            return num_recursions

        cl_key, num_recursions, passed_fd = violation(fd_closure, cl_fd, relations_set, num_recursions)

        if len(passed_fd) >= 1:
            answer = is_fd_in_relation(passed_fd, relations_set)

            if answer == False:
                return -1

    if len(other_fd)>=1 and len(cl_fd)>= 1:

        cl_key, num_recursions, passed_fd = violation(fd_closure, cl_fd, relations_set, num_recursions)
        if len(passed_fd) >= 1:
            answer = is_fd_in_relation(passed_fd, relations_set)

            if answer == False:
                return -1

        other_key, num_recursions, passed_fd = violation(other_r, other_fd, relations_set, num_recursions)
        if len(passed_fd) >= 1:
            answer = is_fd_in_relation(passed_fd, relations_set)
            if answer == False:
                return -1
   
    
    return num_recursions


def find_fd_closure (fd_closure, fd_set):
    other_fd = set()

    for fd in fd_set:
        fd_i = set()
        fd_i = fd_i.union(fd.left_hand_side, fd.right_hand_side)

        if fd_i.issubset(fd_closure):

            other_fd.add(fd)
        
    return other_fd

    

def is_fd_in_relation(fd_closure, relations_set):
    answer = False

    big_closure = set()
    for fd in fd_closure:
        closure = set()
        closure = closure.union(fd.left_hand_side, fd.right_hand_side)
        big_closure = big_closure.union(fd.left_hand_side, fd.right_hand_side)
        fd = Relation(closure)
        for relation in relations_set:
            if fd == relation :
                answer = True


    big_closure = Relation(big_closure)
    for relation in relations_set:
        if big_closure == relation:
            answer = True
    
    return answer



