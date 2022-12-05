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
| command | description                                       |
| ------- | ------------------------------------------------- |
| pushint | push next onto int stack                          |
| pushstr | push next onto str stack                          |
| pullint | pull next from int stack                          |
| pullstr | pull next from str stack                          |
| peekint | peek at next from str stack                       |
| peekstr | peek at next from str stack                       |
| string  | stringify                                         |
| int     | intify                                            |
| concat  | concatenate the top two items on the str stack    |
| show    | output string to stdout, no implicit newline      |
| add     | add the top two items on the int stack            |
| mult    | multiply the top two items on the int stack       |
| div     | divide the top two items on the int stack         |
| exit    | exit program(usefull in interactive)              |
| intvar  | declare an int variable                           |
| strvar  | declare a str variable                            |
| ask     | read a line from stdin                            |
| if      | conditional statement if                          |
| else    | conditional statement else                        |
| eq      | return wether the next two expression are equal   |
| not     | boolean not                                       |
| :       | declare label                                     |
| goto    | go to label                                       |
| {       | start evaluating statements until terminated by } |
| }       | finish evaluating statements started by {         |
| concats | concatenate the next two statements               |
| adds    | add the next two statements                       |
| divs    | divide the next two statements(returns str)       |
| mults   | multiply the next two statements                  |

### guide
#### stacks
there are two stacks:  
the int stack,  
and the string stack  

#### types
there are two data types:  
string (in quotes): "hello world",  
and integer: 3  
booleans are represented by 1 or 0  
