with open('path_CGR_202211301537_acaf388_2023_06_21_11_04.txt', 'r') as file:
    lines = file.readlines()

with open('path_CGR_202211301537_acaf388_2023_06_21_11_04.txt', 'w') as file:
    for line in lines:
        file.write(line.rstrip() + '\n')
