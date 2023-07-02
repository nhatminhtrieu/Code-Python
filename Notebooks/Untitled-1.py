import numpy as np
import sympy as sp

Al_OH3 = [("Al", 1), ([("O", 1), ("H", 1)], 3)]
H2_SO4 = [("H", 2), ([("S", 1), ("O", 4)], 1)]
Al2_SO43 = [("Al", 2), ([("S", 1), ("O", 4)], 3)]
H2O = [("H", 2), ("O", 1)]

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

def balance_chemical_equation(lhs, rhs):
    "lhs là danh sách các phân tử tham gia phản ứng, rhs là danh sách các phân tử sản phẩm"
    
    # [("Al", 1), ("O", 3), ("H", 3)]], [("H", 2), ("S", 1), ("O", 4)] -> ['Al', 'O', 'H', 'S']
    lhs_copy = [parse_chemical_formula(i) for i in lhs.copy()]
    elementList = list(dict.fromkeys([j[0] for i in lhs_copy for j in i]))
    """
    Al          1           0               2               0
    O        a  3    +   b  4     =     c   12    +     d   1
    H           3           2               6               2
    S           0           1               0               0
    """
    # ứng với mỗi phân tử trong lhs, rhs xác định hệ số tương ứng
    variables = sp.symbols(' '.join(elementList))
    # v1 = [1, 3, 3, 0]
    v1 = np.array()
    print(v1)

print(balance_chemical_equation([Al_OH3, H2_SO4], [Al2_SO43, H2O]))