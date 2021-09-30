from itertools import permutations


def solution(expression):
    operators = ["*", "+", "-"]
    answer =[]
    for oper in permutations(operators,3):
        temp_exp =[""]
        for exp in expression:
            if exp.isdigit() and temp_exp[-1] not in operators:
                temp_exp[-1]+=exp
            else:
                temp_exp.append(exp)
        print(temp_exp, oper)
        for j in oper:
            for i in range(len(temp_exp)):
                if(temp_exp[i]) ==j:




solution("100-200*300-500+20")
