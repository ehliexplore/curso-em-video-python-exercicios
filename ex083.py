exp = str(input('Enter a expression: '))
parents = list()
for simb in exp:
    if simb == '(':
        parents.append('(')
    elif simb == ')':
        if len(parents) > 0:
            parents.pop()
        else:
            parents.append(')')
            break
if len(parents) == 0:
    print('The number of parentheses are correct.')
else:
    print('The number of parentheses are WRONG.')

