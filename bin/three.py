# import os
import sys
import shlex
import copy
import argparse


sys.argv.append('--!@#$%^&*()')

class EndBrace():
    pass


endbraces = EndBrace()

if not '--!@#$%^&*()' in sys.argv:
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action="store_true", help='show debug output')
    parser.add_argument('-c', '--command', action="store_true", help='show commands')
    parser.add_argument('file', default=None, nargs='?', help='easm file to run')
    args = parser.parse_args()
    # if '-d' in sys.argv or '--debug' in sys.argv:
    if args.command:
        command = True
        if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
            sys.argv.pop(1)
    else:
        command = False

    if args.debug:
        debug = True
        if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
            sys.argv.pop(1)
    else:
        debug = False

    if '-b' in sys.argv or '--binary' in sys.argv:
        print('Binary not implemented!')
        # binary = True
        binary = False
        if sys.argv[1] == '-b' or sys.argv[1] == '--binary':
            sys.argv.pop(1)
    else:
        binary = False

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            readlines = f.read().splitlines()
        interactive = False
    except:
        interactive = True

else:
    debug = False
    binary = False
    interactive = False
    readlines = r'''; The first program written for a (probably) turing complete easm!
; ----------------------------------------------------------------
;
; push 4 to the stack
pushint 4
; create a label called do
: do
; push -1 to the stack
pushint -1
; push: add the top two values on the stack to the stack
pushint add
; show: stringify: peek the top item in the stack
show string peekint
; if peekint != 1: show newline
if not eq peekint 1 show "\n"
; if peekint != 1: go to label do
if not eq peekint 1 goto do
; otherwise: (if peekint == 1) exit
else exit'''.splitlines()

exitprog = sys.exit


def pushint():
    statement = evaleasm()
    # print(statement,type(statement))
    if statement is not None and type(statement) == int:
        int_stack.append(statement)
    else:
        raiseerror('Error in pushint!')
    return None


def pushstr():
    statement = evaleasm()
    if statement and type(statement) == str:
        str_stack.append(statement)
    else:
        raiseerror('Error in pushstr!')
    return None


def pullint():
    return int_stack.pop()


def pullstr():
    return str_stack.pop()


def peekint():
    return int_stack[-1]


def peekstr():
    return str_stack[-1]


def string():
    return str(evaleasm())


def toint():
    return int(evaleasm())


def add():
    return int_stack[-1] + int_stack[-2]


def adds():
    try:
        return int(evaleasm()) + int(evaleasm())
    except:
        raiseerror('Error in adds!')


def mult():
    return int_stack[-1] * int_stack[-2]


def div():
    return str(int_stack[-1] / int_stack[-2])


def concat():
    return str_stack[-2] + str_stack[-1]


def concats():
    return str(evaleasm()) + str(evaleasm())


def strvar():
    var_name = evaleasm(isname=True)
    statement = evaleasm()
    if statement and type(statement) == str:
        str_vars.update({var_name: statement})
    else:
        raiseerror('Error in strvar!')

    return None


def intvar():
    var_name = evaleasm(isname=True)
    statement = evaleasm()
    if statement and type(statement) == int:
        int_vars.update({var_name: statement})
    else:
        raiseerror('Error in intvar!')

    return None


def eif():
    global is_if
    if bool(evaleasm()):
        is_if = True
        evaleasm()
    else:
        is_if = False


def eelse():
    global is_if
    if not is_if:
        evaleasm()
        is_if = True


def eq():
    one = evaleasm()
    two = evaleasm()
    if one == two:
        return 1
    else:
        return 0


def enot():
    return int(not evaleasm())


def ask():
    return input()


def startbrace():
    while evaleasm() != endbraces:
        pass
    return None


def endbrace():
    return endbraces


def label():
    global labels
    name = evaleasm(isname=True)
    line = r
    labels.update({name: line})


def goto():
    global r, prog
    name = evaleasm(isname=True)
    if name in labels.keys():
        r = labels[name]
        prog = copy.deepcopy(oprog)
    else:
        raiseerror('Error in goto!')
    # print(prog,oprog, name,labels[name])


def show():
    statement = evaleasm()
    # print([statement], [type(statement)])
    if statement and type(statement) == str:
        if interactive:
            print(statement)
        else:
            print(statement, end='')
    else:
        raiseerror('Error in show!')
    # print('n')

    return None


proglines = []
coms = {'pushint': pushint, 'pushstr': pushstr, 'pullint': pullint, 'pullstr': pullstr, 'peekint': peekint,
        'peekstr': peekstr, 'string': string, 'int': toint, 'concat': concat,
        'show': show, 'add': add, 'mult': mult, 'div': div, 'exit': exitprog,
        'intvar': intvar, 'strvar': strvar, 'ask': ask, 'if': eif, 'else': eelse, 'eq': eq, 'not': enot, ':': label,
        'goto': goto, '{': startbrace, '}': endbrace, 'concats': concats, 'adds': adds}
# print(coms.keys())
# coms = ['pushint', 'pushstr', 'pullint', 'pullstr', 'string', 'int', 'show']
is_if = True

str_stack = []
int_stack = []
str_vars = {}
int_vars = {}
labels = {}


def tonum(num):
    try:
        return int(num)
    except:
        return False


# tonum = int

def tostr(txt):
    if txt.startswith('"') and txt.endswith('"'):
        return txt.removeprefix('"').removesuffix('"').replace(r'\n', '\n')
    else:
        return False


# tostr = str

def iscom(com):
    if com in coms:
        return True
    else:
        return False


def isintvar(statement):
    if statement in int_vars.keys():
        return True
    else:
        return False


def isstrvar(statement):
    if statement in str_vars.keys():
        return True
    else:
        return False


# def islabel(statement):
#    if statement in labels.keys():
#        return True
#    else:
#        return False


# print('\n'.join(proglines))

def raiseerror(err):
    sys.stderr.write('Error: ' + err)
    sys.exit()


def evaleasm(isname=False):
    statement = prog[r].pop(0)
    if isname:
        return statement
    isstr = tostr(statement)
    isnum = tonum(statement)
    is_com = iscom(statement)
    is_strvar = isstrvar(statement)
    is_intvar = isintvar(statement)
    if command:
        print('statement:', [statement])

    if debug:
        # print('statement:',statement,'| is string:', [isstr],'| is num:', [isnum],'| int stack:', int_stack,'| str stack:', str_stack)

        print('statement:', [statement], 'is command:', [is_com], 'is string:', [isstr], 'is num:', [isnum],
              'is str var:', [is_strvar], 'is int var:', [is_intvar], 'int stack:', int_stack,
              'str stack:', str_stack, 'str vars:', [str_vars], 'int vars:', [int_vars], 'labels:', [labels], 'is if',
              is_if)
    # print(isnum is not None)
    if isnum is not False:
        return isnum
    if isstr is not False:
        # print(isstr)
        return isstr
    if is_com is not False:
        return coms[statement]()
    if is_strvar is not False:
        # print(str_vars, statement)
        return str_vars[statement]
    if is_intvar is not False:
        return int_vars[statement]


prog = []
oprog = []
r = 0
# k = 0
try:
    if not interactive:
        for x in readlines:
            if x:
                if not x.startswith(';'):
                    proglines.append(x)

        for x, line in enumerate(proglines):
            prog.append([])
            for com in shlex.split(line, posix=False):
                prog[x].append(com)

        oprog = copy.deepcopy(prog)
        # print(prog, oprog)
        if prog:
            for x, item in enumerate(prog):
                r = x
                if prog[r].pop(0) == ':':
                    label()
            r = 0
            prog = copy.deepcopy(oprog)
            while r < len(prog):
                # print(oprog)
                evaleasm()
                r += 1
            # for x, item in enumerate(prog):
            #    r = x
            #    evaleasm()
    else:
        if debug:
            print('Easm Interactive - Debug Mode:')
        else:
            print('Easm Interactive:')
        while True:
            prog = [[]]
            line = input('> ')
            for com in shlex.split(line, posix=False):
                prog[0].append(com)
            if prog[0]:
                for x, item in enumerate(prog):
                    r = x
                    evaleasm()

except KeyboardInterrupt:
    raiseerror('Keyboard Interrupt!')

# print(prog)
