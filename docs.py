from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header=False)
table.add_column("command")
table.add_column("description")
table.add_column("usage")
text = [('pushint', 'push next onto int stack', 'pushint <num>'),
        ('pushstr', 'push next onto str stack', 'pushstr <string>'),
        ('pullint', 'pull next from int stack', 'pullint'),
        ('pullstr', 'pull next from str stack', 'pullstr'),
        ('peekint', 'peek at next from str stack', 'peekint'),
        ('peekstr', 'peek at next from str stack', 'peekstr'),
        ('string', 'stringify', 'string <num>'),
        ('int', 'intify', 'int <string>'),
        ('concat', 'concatenate the top two items on the str stack', 'concat'),
        ('show', 'output string to stdout, no implicit newline', 'show <string>'),
        ('add', 'add the top two items on the int stack', 'add'),
        ('mult', 'multiply the top two items on the int stack', 'mult'),
        ('div', 'divide the top two items on the int stack', 'div'),
        ('exit', 'exit program (useful in interactive)', 'exit'),
        ('intvar', 'declare an int variable', 'intvar <name> <num>'),
        ('strvar', 'declare a str variable', 'strvar <name> <string>'),
        ('ask', 'read a line from stdin', 'ask'),
        ('if', 'conditional statement if', 'if <num> <statement>'),
        ('else', 'conditional statement else', 'else <statement>'),
        ('eq', 'return whether the next two expression are equal', 'eq <statement> <statement>'),
        ('not', 'boolean not', 'not <num>'),
        (':', 'declare label', ': <name>'),
        ('goto', 'go to label', 'goto <name>'),
        ('{', 'start evaluating statements until terminated by }', '{ <statement> <statement> }'),
        ('}', 'finish evaluating statements started by {', '{ <statement> <statement> '),
        ('concats', 'concatenate the next two statements', 'concats <string> <string>'),
        ('adds', 'add the next two statements', 'adds <num> <num>'),
        ('divs', 'divide the next two statements(returns str)', 'divs <num> <num>'),
        ('mults', 'multiply the next two statements', 'mults <num> <num>'),
        ('use', 'use optional command', 'use <name>'),
        ('rand', 'random int between the next two statements(optional))', 'rand <num> <num>'),
        ('<', 'return whether, of the next two expressions, if the first one is less than the second', '< <num> <num>'),
        ('>', 'return whether, of the next two expressions, if the first one is more than the second', '> <num> <num>'),
        ('list', 'declare a list or listify a string', 'list <list>/<string>'),
        ('[', 'start adding statements to a list until terminated by ]', '[ <num> <num> ]'),
        (']', 'finish adding statements to a list started by [', '[ <num> ]'),
        ('setitem', 'set the value of a list item', 'setitem <name> <index> <statement>'),
        ('length', 'return the length of a list', 'length <list>'),
        ('asc', 'convert to and from ascii codes', 'asc <num>/<string>'),
        ('newitem', 'add an item to a list', 'newitem <name> <statement>'),
        ('askkey', 'read a single key from stdin', 'askkey'),
        ('and', 'return whether the next two statements are both true', 'and <num> <num>'),
        ]  # < >
longest = len("command")
longest2 = len("description")
longest3 = len("usage")
for x in text:
    if len(x[0]) > longest:
        longest = len(x[0])

for x in text:
    if len(x[1]) > longest2:
        longest2 = len(x[1])

for x in text:
    if len(x[2]) > longest3:
        longest3 = len(x[1])
# print(longest)
for x in text:
    table.add_row(x[0], x[1], x[2])

for x, item in enumerate(text):
    text[x] = list(item)

for x, item in enumerate(text):
    if len(item[0]) < longest:
        text[x][0] += ' ' * (longest - len(item[0]))

for x, item in enumerate(text):
    if len(item[1]) < longest2:
        text[x][1] += ' ' * (longest2 - len(item[1]))

for x, item in enumerate(text):
    if len(item[2]) + 2 < longest3:
        text[x][2] += ' ' * (longest3 - (len(item[2]) + 2))
command = "command"
command += ' ' * (longest - len(command))
description = "description"
description += ' ' * (longest2 - len(description))
usage = "usage"
usage += ' ' * (longest3 - len(usage))
print('|', command, '|', description, '|', usage, '|')
print('|', '-' * longest, '|', '-' * longest2, '|', '-' * longest3, '|')
for x in text:
    print('|', x[0].replace('>', '\\>'), '|', x[1], '|','`'+x[2]+'`', '|')

# console.print(table)
