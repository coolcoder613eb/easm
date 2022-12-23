from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ctypes
from functools import partial
import subprocess
# import shlex
import importlib
import re
import os
import sys

# Increas Dots Per inch so it looks sharper
if os.name == 'nt': ctypes.windll.shcore.SetProcessDpiAwareness(True)
sep = '\n================================================='
print("Easm Editor Shell\n(this is where your programs will be run)")
print(sep)
# Setup Tkinter
root = Tk()
root.geometry('600x300')

# Current File Path
filePath = None

# whether a file was just opened
justopened = False

justfont = False

# initial directory to be the current directory
initialdir = '.'

# Define File Types that can be choosen
validFileTypes = (
    ("EASM File", "*.easm"),
    ("All Files", "*.*")
)
applicationName = 'Easm Editor'
root.title(applicationName)
# Infos about the Document are stored here
document = 'show "Hello, World!"'
# sys.executable = sys.executable if not '.'.join(sys.executable.split('.')[0:-2])[-1] != 'w' else '.'.join(sys.executable.split('.')[0:-2])[0:-2]+'.'+sys.executable.split('.')[-1]

pause = ' & echo: & pause' if os.name == 'nt' else "; echo; read -rsp $'Press any key to continue . . . ' -n 1 key &"
easm = None


def dofont(thefontface=None, thefontsize=None):
    global fontface, fontsize, font
    if thefontface:
        fontface = thefontface
    if thefontsize:
        fontsize = thefontsize
    font = fontface + ' ' + fontsize
    editArea.configure(font=font)


def exc(name):
    global easm
    # print('"'+sys.executable+'" easm.py "'+name+'"'+pause)
    sys.argv = ["easm.py", name]
    print(name)
    # easms.append(
    if easm is None:
        easm = importlib.import_module("easm")
    else:
        importlib.reload(easm)

    # ))
    # print(easm.sys.argv)
    print(sep)
    # subprocess.Popen('"'+sys.executable+'" easm.py "'+name+'"'+pause,shell=True,creationflags=subprocess.DETACHED_PROCESS)


def shell(event=None):
    global easm
    sys.argv = ['easm.py']
    if easm is None:
        importlib.import_module("easm")
    else:
        importlib.reload(easm)  # subprocess.Popen('"'+sys.executable+'" easm.py '+pause,shell=True,creationflags=subprocess.DETACHED_PROCESS)


def quitapp(event=None): root.quit()


def newfile(event=None):
    global document, filePath, justopened
    document = 'show "Hello, World!"'
    filePath = None
    # justopened = True
    # Delete Content
    editArea.delete('1.0', END)

    # Set Content
    editArea.insert('1.0', document)
    root.title(f'{applicationName} - {filePath if filePath is not None else "Untitled"}')
    changes()


def fileManager(event=None, action=None):
    global document, filePath, justopened

    # Open
    if action == 'open':
        # ask the user for a filename with the native file explorer.
        filePath = askopenfilename(filetypes=validFileTypes, initialdir=initialdir)

        with open(filePath, 'r', encoding='utf-8') as f:
            document = f.read()

        # Delete Content
        editArea.delete('1.0', END)

        # Set Content
        editArea.insert('1.0', document)

        # Set Title
        root.title(f'{applicationName} - {filePath}')
        justopened = True
        changes()

    elif action == 'save':
        # print('save')
        document = editArea.get('1.0', END).removesuffix('\n')

        if not filePath:
            # ask the user for a filename with the native file explorer.
            newfilePath = asksaveasfilename(filetypes=validFileTypes, defaultextension='.easm', initialdir=initialdir)

            # Return in case the User Leaves the Window without
            # choosing a file to save
            # print('newfilePath',newfilePath)
            if not newfilePath: return

            filePath = newfilePath

        # if not filePath.endswith('.easm'):
        #    filePath += '.easm'

        with open(filePath, 'w', encoding='utf-8') as f:
            # print('Saving at: ', filePath)
            f.write(document)

        root.title(f'{applicationName} - {filePath}')
    elif action == 'saveas':
        # print('save')
        document = editArea.get('1.0', END).removesuffix('\n')

        # ask the user for a filename with the native file explorer.
        newfilePath = asksaveasfilename(filetypes=validFileTypes, defaultextension='.easm', initialdir=initialdir)

        # Return in case the User Leaves the Window without
        # choosing a file to save
        # print('newfilePath',newfilePath)
        if not newfilePath: return

        filePath = newfilePath

        # if not filePath.endswith('.easm'):
        #    filePath += '.easm'

        with open(filePath, 'w', encoding='utf-8') as f:
            # print('Saving at: ', filePath)
            f.write(document)

        root.title(f'{applicationName} - {filePath}')


def keyDown(event=None):
    # print(editArea.get('1.0', END).removesuffix('\n')[-1] == document[-1])
    if not editArea.get('1.0', END).removesuffix('\n') == document:
        root.title(f'{applicationName} - *{filePath if filePath is not None else "Untitled"}')
    else:
        root.title(f'{applicationName} - {filePath if filePath is not None else "Untitled"}')


# Execute the Programm
def execute(event=None):
    if filePath is not None:
        exc(filePath)
    else:
        # Write the Content to the Temporary File
        with open('run.easm', 'w', encoding='utf-8') as f:
            f.write(editArea.get('1.0', END).removesuffix('\n'))

        # Start the File in a new CMD Window
        exc('run.easm')


# Register Changes made to the Editor Content
def changes(event=None):
    global previousText, justopened, justfont

    # If actually no changes have been made stop / return the function
    if not justopened:
        if editArea.get('1.0', END) == previousText:
            return

    # if justfont:
    #    editArea.configure(font=font)

    # Remove all tags so they can be redrawn
    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")

    # Add tags where the search_re function found the pattern
    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get('1.0', END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color, selectforeground=normal)

            i += 1

    previousText = editArea.get('1.0', END)
    justopened = False


def search_re(pattern, text, groupid=0):
    matches = []

    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):
            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
            )

    return matches


def rgb(rgb):
    return "#%02x%02x%02x" % rgb


previousText = ''
# Define colors for the variouse types of tokens
normal = rgb((234, 234, 234))
keywords = rgb((234, 95, 95))
comments = rgb((95, 234, 165))
string = rgb((234, 162, 95))
function = rgb((95, 211, 234))
background = rgb((42, 42, 42))

select = rgb((128, 128, 128))
normal = rgb((0, 0, 0))
keywords = rgb((255, 119, 0))
comments = rgb((221, 0, 0))
string = rgb((0, 170, 0))
function = rgb((0, 0, 255))
background = rgb((255, 255, 255))
fontbig = '15'
fontmed = '13'
fontlit = '10'
font1 = "{Courier New}"
font2 = "Consolas"
font3 = "{Cascadia Mono}"
fontface = font2
fontsize = fontbig
font = 'Consolas 15'

# Define a list of Regex Pattern that should be colored in a certain way
######################-Improve-regular-expressions-#########################
repl = [
    [r'^[^"]*("[^"]*"[^"]*)*;.*?$', comments],
    [
        '(^| )(pushint|pushstr|pullint|pullstr|peekint|peekstr|string|int|concat|show|add|mult|div|exit|intvar|strvar|ask|if|else|eq|not|:|goto|{|}|concats|adds|use|rand|>|<|list|\[|]|newitem|askkey|and|usepy)($| )',
        keywords],
    ['".*?"', string],
    # ';(?!").*?$' #r'[^"]*;[^"]*$'
]
# repl = [
#    ['(^| )(pushint|pushstr|pullint|pullstr|peekint|peekstr|string|int|concat|show|add|mult|div|exit|intvar|strvar|ask|if|else|eq|not|:|goto|{|}|concats|adds|use|rand|>|<|list|[|]|newitem|askkey|and|usepy)($| )', keywords],
#    ['".*?"', string],
#    [r'^[^"]*("[^"]*"[^"]*)*;.*?$', comments], #';(?!").*?$' #r'[^"]*;[^"]*$'
# ]

# m|(m(m{2})+))
# Make the Text Widget
# Add a hefty border width so we can achieve a little bit of padding
editArea = Text(
    root,
    background=background,
    foreground=normal,
    insertbackground=normal,
    selectbackground=select,
    selectforeground=normal,
    relief=FLAT,
    borderwidth=30,
    undo=True,
    font=font
)

# Place the Edit Area with the pack method
editArea.pack(
    fill=BOTH,
    expand=1
)

# Insert some Standard Text into the Edit Area
editArea.insert('1.0', 'show "Hello, World!"')

# Bind the KeyRelase to the Changes Function
editArea.bind('<KeyRelease>', changes)
editArea.bind("<Key>", keyDown)

# Bind Control + R to the exec function
# root.bind('<Control-r>', execute)

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)

viewMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=viewMenu)

fontsizeMenu = Menu(viewMenu, tearoff=0)
viewMenu.add_cascade(label="Font Size", menu=fontsizeMenu)

fontsizeMenu.add_command(label="Large", command=partial(dofont, thefontsize=fontbig))
fontsizeMenu.add_command(label="Medium", command=partial(dofont, thefontsize=fontmed))
fontsizeMenu.add_command(label="Small", command=partial(dofont, thefontsize=fontlit))

fontMenu = Menu(viewMenu, tearoff=0)
viewMenu.add_cascade(label="Font", menu=fontMenu)

fontMenu.add_command(label="Courier New", command=partial(dofont, thefontface=font1))
fontMenu.add_command(label="Consolas", command=partial(dofont, thefontface=font2))
fontMenu.add_command(label="Cascadia Mono", command=partial(dofont, thefontface=font3))

runMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Run", menu=runMenu)

runMenu.add_command(label="Run Program", command=execute, accelerator='F5')
root.bind_all('<Control-r>', execute)
root.bind_all('<F5>', execute)

runMenu.add_command(label="Easm Interactive", command=shell, accelerator='Ctrl+I')
root.bind_all('<Control-i>', shell)

fileMenu.add_command(label="New", command=newfile, accelerator='Ctrl+N')
root.bind_all('<Control-n>', newfile)

fileMenu.add_command(label="Open", command=partial(fileManager, action='open'), accelerator='Ctrl+O')
root.bind_all('<Control-o>', partial(fileManager, action='open'))

fileMenu.add_command(label="Save", command=partial(fileManager, action='save'), accelerator='Ctrl+S')
root.bind_all('<Control-s>', partial(fileManager, action='save'))

fileMenu.add_command(label="Save As", command=partial(fileManager, action='saveas'), accelerator='Ctrl+Shift+S')
root.bind_all('<Control-Shift-s>', partial(fileManager, action='saveas'))

fileMenu.add_command(label="Exit", command=quitapp, accelerator='Ctrl+Q')
root.bind_all('<Control-q>', quitapp)

newfile()
changes()
root.title(f'{applicationName} - {filePath if filePath is not None else "Untitled"}')

if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        filePath = sys.argv[1]
        with open(filePath, 'r') as f:
            document = f.read()

        # Delete Content
        editArea.delete('1.0', END)

        # Set Content
        editArea.insert('1.0', document)

        # Set Title
        root.title(f'{applicationName} - {filePath}')
        justopened = True
        changes()

root.mainloop()
