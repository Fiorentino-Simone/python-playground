temps = [221, 234, 340, 230, 356, 287, 260, 279, -9999];

# new_temps = []
# for temp in temps:
#     new_temps.append(temp/10);

# print(new_temps);

#un modo ulteriore molto più elegante
new_temps = [temp/10 for temp in temps];

#se vogliamo eliminare un elemento dalla lista o comunque mettere una condizione nella if
new_temps = [temp/10 for temp in temps if temp != -9999];
#with the else
new_temps = [temp/10 if temp != -9999 else 0 for temp in temps];
#with the else and the if
new_temps = [temp/10 if temp != -9999 else 0 for temp in temps if temp != -9999];
#with if not
#if not -9999

#the same with the sum
#return sum([float(i) for i in lst])
