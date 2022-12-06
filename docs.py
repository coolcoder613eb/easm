from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header=False)
table.add_column("command")
table.add_column("description")
text = [('pushint', 'push next onto int stack'),
        ('pushstr', 'push next onto str stack'),
        ('pullint', 'pull next from int stack'),
        ('pullstr', 'pull next from str stack'),
        ('peekint', 'peek at next from str stack'),
        ('peekstr', 'peek at next from str stack'),
        ('string', 'stringify'),
        ('int', 'intify'),
        ('concat', 'concatenate the top two items on the str stack'),
        ('show', 'output string to stdout, no implicit newline'),
        ('add', 'add the top two items on the int stack'),
        ('mult', 'multiply the top two items on the int stack'),
        ('div', 'divide the top two items on the int stack'),
        ('exit', 'exit program(usefull in interactive)'),
        ('intvar', 'declare an int variable'),
        ('strvar', 'declare a str variable'),
        ('ask', 'read a line from stdin'),
        ('if', 'conditional statement if'),
        ('else', 'conditional statement else'),
        ('eq', 'return wether the next two expression are equal'),
        ('not', 'boolean not'),
        (':', 'declare label'),
        ('goto', 'go to label'),
        ('{', 'start evaluating statements until terminated by }'),
        ('}', 'finish evaluating statements started by {'),
        ('concats', 'concatenate the next two statements'),
        ('adds', 'add the next two statements'),
        ('divs', 'divide the next two statements(returns str)'),
        ('mults', 'multiply the next two statements'),
        ('use','use optional command'),
        ('rand','random int between the next two statements(optional))')] # < >
longest = 0
longest2 = 0
for x in text:
        if len(x[0]) > longest:
                longest = len(x[0])

for x in text:
        if len(x[1]) > longest2:
                longest2 = len(x[1])
#print(longest)
for x in text:
    table.add_row(x[0], x[1])

for x,item in enumerate(text):
        text[x] = list(item)

for x,item in enumerate(text):
        if len(item[0]) < longest:
                text[x][0] += ' ' * (longest-len(item[0]))

for x,item in enumerate(text):
        if len(item[1]) < longest2:
                text[x][1] += ' ' * (longest2-len(item[1]))
command = "command"
command += ' ' * (longest-len(command))
description = "description"
description += ' ' * (longest2-len(description))
print('|',command,'|',description,'|')
print('|','-'* longest,'|','-'* longest2,'|')
for x in text:
        print('|',x[0],'|',x[1],'|')

#console.print(table)
