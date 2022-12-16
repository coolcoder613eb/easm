# easm
 easm programming language
## requirements
### for the interpreter
- python 3(tested on 3.10)
### for the compiler
- python 3(tested on 3.10)
- nuitka

## docs

### commands
| command | description                                                                           | usage                                            |
| ------- | ------------------------------------------------------------------------------------- | ------------------------------------------------ |
| pushint | push next onto int stack                                                              | `pushint <num>                                 ` |
| pushstr | push next onto str stack                                                              | `pushstr <string>                              ` |
| pullint | pull next from int stack                                                              | `pullint                                       ` |
| pullstr | pull next from str stack                                                              | `pullstr                                       ` |
| peekint | peek at next from str stack                                                           | `peekint                                       ` |
| peekstr | peek at next from str stack                                                           | `peekstr                                       ` |
| string  | stringify                                                                             | `string <num>                                  ` |
| int     | intify                                                                                | `int <string>                                  ` |
| concat  | concatenate the top two items on the str stack                                        | `concat                                        ` |
| show    | output string to stdout, no implicit newline                                          | `show <string>                                 ` |
| add     | add the top two items on the int stack                                                | `add                                           ` |
| mult    | multiply the top two items on the int stack                                           | `mult                                          ` |
| div     | divide the top two items on the int stack                                             | `div                                           ` |
| exit    | exit program (useful in interactive)                                                  | `exit                                          ` |
| intvar  | declare an int variable                                                               | `intvar <name> <num>                           ` |
| strvar  | declare a str variable                                                                | `strvar <name> <string>                        ` |
| ask     | read a line from stdin                                                                | `ask                                           ` |
| if      | conditional statement if                                                              | `if <num> <statement>                          ` |
| else    | conditional statement else                                                            | `else <statement>                              ` |
| eq      | return whether the next two expression are equal                                      | `eq <statement> <statement>                    ` |
| not     | boolean not                                                                           | `not <num>                                     ` |
| :       | declare label                                                                         | `: <name>                                      ` |
| goto    | go to label                                                                           | `goto <name>                                   ` |
| {       | start evaluating statements until terminated by }                                     | `{ <statement> <statement> }                   ` |
| }       | finish evaluating statements started by {                                             | `{ <statement> <statement>                     ` |
| concats | concatenate the next two statements                                                   | `concats <string> <string>                     ` |
| adds    | add the next two statements                                                           | `adds <num> <num>                              ` |
| divs    | divide the next two statements(returns str)                                           | `divs <num> <num>                              ` |
| mults   | multiply the next two statements                                                      | `mults <num> <num>                             ` |
| use     | use optional command                                                                  | `use <name>                                    ` |
| rand    | random int between the next two statements(optional))                                 | `rand <num> <num>                              ` |
| <       | return whether, of the next two expressions, if the first one is less than the second | `< <num> <num>                                 ` |
| \>       | return whether, of the next two expressions, if the first one is more than the second | `> <num> <num>                                 ` |
| list    | declare a list or listify a string                                                    | `list <list>/<string>                          ` |
| [       | start adding statements to a list until terminated by ]                               | `[ <num> <num> ]                               ` |
| ]       | finish adding statements to a list started by [                                       | `[ <num> ]                                     ` |
| setitem | set the value of a list item                                                          | `setitem <name> <index> <statement>            ` |
| length  | return the length of a list                                                           | `length <list>                                 ` |
| asc     | convert to and from ascii codes                                                       | `asc <num>/<string>                            ` |
| newitem | add an item to a list                                                                 | `newitem <name> <statement>                    ` |
| askkey  | read a single key from stdin                                                          | `askkey                                        ` |
| and     | return whether the next two statements are both true                                  | `and <num> <num>                               ` |
| usepy   | use command(s) defined in a python file                                               | `usepy <name_without_ext>                      ` |

## guide
#### stacks
there are two stacks:  
the int stack,  
and the string stack  

#### types
there are three data types:  
string (in quotes): "hello world",  
list (in square brackets): [ 1 2 ]
and integer: 3  
booleans are represented by 1 or 0  

#### extensions
there is an api, for extensions written in python,  
this is the specification.  
take this example (called `showscommand.py`):
```python
# add a `shows` command to easm

level = 1

def setup(raiseerror,evaleasm):
    
    
    def shows():
        one = evaleasm()
        two = evaleasm()
        if one is not None and type(one) == str and two is not None and type(two) == str:
            print(one,two)
        
    
    return {'shows': shows}

```
##### first,  
we define level,
which is the argument level,
level 1 passes only two arguments to setup.

##### then,  
we create the `setup` function,
which must return a dictionary of command names,  
and the function to call for them.  

##### after that,  
we create the function `shows`,  
which defines what the command will actually do.  

##### finally,  
we return a dictionary,  
of the string `'shows'` and the function `shows`.

the *easm* code to use this is:
```
usepy showscommand
shows "Hello," "World!"
```
