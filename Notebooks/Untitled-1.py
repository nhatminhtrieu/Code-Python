import numpy as np
import sympy as sp

Al_OH3 = [('Al', 1), ([('O', 1), ('H', 1)], 3)]
H2_SO4 = [('H', 2), ([('S', 1), ('O', 4)], 1)]
Al2_SO43 = [('Al', 2), ([('S', 1), ('O', 4)], 3)]
H2O = [('H', 2), ('O', 1)]
def chemical_formula(mol):
    pass # TODO
    # # Method 1
    # result = ''
    # for i in range(len(mol)):
    #     if mol[i][1] == 1:
    #         result += mol[i][0]
    #     else:
    #         result += mol[i][0] + '_{' + str(mol[i][1]) + '}'
    # return result
    
    
    # # Method 2
    # # return ''.join([x[0] if x[1] == 1 else x[0] + '_{' + str(x[1]) + '}' for x in mol])

    # # Improvement
    # result = ''
    # for i in mol:
    #     if type(i[0]) == str:
    #         result += i[0]
    #     else:
    #         result += '(' + chemical_formula(i[0]) + ')'
    #     if i[1] != 1:
    #         result += '_{' + str(i[1]) + '}'
    # return result

    result = ''.join([f'{i[0]}_{i[1]}' if type(i[0]) == str else f'({chemical_formula(i[0])})_{i[1]}' for i in mol])
    # find )_1, if remove )_1 then remove (
    result = result.replace(')_1', '')
    if (result.count(')') != result.count('(')):
        result = result.replace('(', '')
    return result.replace('_1', '')
    

def parse_chemical_formula(formula):
    # result = []
    # for i in formula:
    #     if type(i[0]) == list:
    #         # for j in i[0]:
    #         #     result.append((j[0], j[1]*i[1]))
    #         result.append((j[0], j[1]*i[1]) for j in i[0])  
    #     else:
    #         result.append(i)
    # return result
    # # https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    
    return list(dict.fromkeys([(j[0], j[1]*i[1]) if type(i[0]) == list else i for i in formula for j in i[0]]))

def count_element(formula, elementList):
    # elementList = ['Al', 'O', 'H', 'S']
    # formula = [('Al', 1), ('O', 3), ('H', 3)]]
    # return [1, 3, 3, 0]
    return [sum([j[1] for j in formula if j[0] == i]) for i in elementList]

def balance_chemical_equation(lhs, rhs):
    'lhs là danh sách các phân tử tham gia phản ứng, rhs là danh sách các phân tử sản phẩm'
    
    # [('Al', 1), ('O', 3), ('H', 3)]], [('H', 2), ('S', 1), ('O', 4)] -> ['Al', 'O', 'H', 'S']
    lhs_copy = [parse_chemical_formula(i) for i in lhs.copy()]
    rhs_copy = [parse_chemical_formula(i) for i in rhs.copy()]
    elementList = list(dict.fromkeys([j[0] for i in lhs_copy for j in i]))
    '''
    Al          1           0               2               0
    O        a  3    +   b  4     =     c   12    +     d   1
    H           3           2               0               2
    S           0           1               3               0
    '''
    
    # AX = B
 
    A = sp.Matrix(np.array([count_element(i, elementList) for i in lhs_copy] + [count_element(i, elementList) for i in rhs_copy]))
    B = sp.Matrix(A[:, len(lhs) + len(rhs)-1:]) # Cả cột cuối là B
    A = sp.Matrix(A[:, :len(lhs) + len(rhs)-1]) # Phần còn lại là A
    
    X = abs(A.solve(B))
    X = X.row_insert(X.shape[0], sp.Matrix([1]))
    X = X.applyfunc(sp.nsimplify)
    X *= np.lcm.reduce([i.denominator for i in X])
    #print(X)
    # X = [[3], [2], [1], [6]]
    
    X = [sp.nsimplify(i) for i in X]
    # X = [3, 2, 1, 6]
    # lhs = [Al_OH3, H2_SO4]
    # rhs = [Al2_SO43, H2O]
    
    # -> 3 chemical_formula([('Al', 1), ([('O', 1), ('H', 1)], 3)]) + 2 chemical_formula([('H', 2), ([('S', 1), ('O', 4)], 1)]) = 1 chemical_formula([('Al', 2), ([('S', 1), ('O', 4)], 3)]) + 6 chemical_formula([('H', 2), ('O', 1)])
    
    return ' + '.join([str(X[i]) + ' ' + chemical_formula(lhs[i]) for i in range(len(lhs))]) + '\to' + ' + '.join([str(X[i+len(lhs)]) + ' ' + chemical_formula(rhs[i]) for i in range(len(rhs))])
    
H2O = [("H", 2), ("O", 1)]
H2 = [("H", 2)]
O2 = [("O", 2)]

equation = balance_chemical_equation([H2O], [H2, O2])
# sẽ được như
# equation = r"2\text{H}_2\text{O} \to 2\text{H}_2 + \text{O}_2"

print(equation)
#Latex("$$" + equation + "$$")