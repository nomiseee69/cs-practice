import tablestats

with open('events-small.csv', encoding='utf-8') as table:
    row = tablestats.read_rows(table)

with open('events.csv', encoding='utf-8') as table1:
    row1 = tablestats.read_rows(table)

print(row)
print(row1)