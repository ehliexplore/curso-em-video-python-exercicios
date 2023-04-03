def vote(a):
    from datetime import date
    current_year = date.today().year
    age = current_year - a
    if age < 16:
        return f'{age} years: DONT VOTE.'
    if 16 <= age < 18 or age >= 65:
        return f'{age} years: OPTIONAL VOTE.'
    else:
        return f'{age} years: MANDATORY VOTE.'


birth_year = int(input('What year were you born? '))
print(vote(birth_year))










