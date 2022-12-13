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
| command | description                                                                           | usage                    |
| ------- | ------------------------------------------------------------------------------------- | ------------------------ |
| pushint | push next onto int stack                                                              | pushint <num\>            |
| pushstr | push next onto str stack                                                              | pushstr <string\>         |
| pullint | pull next from int stack                                                              | pullint                  |
| pullstr | pull next from str stack                                                              | pullstr                  |
| peekint | peek at next from str stack                                                           | peekint                  |
| peekstr | peek at next from str stack                                                           | peekstr                  |
| string  | stringify                                                                             | string <num\>             |
| int     | intify                                                                                | int <string\>             |
| concat  | concatenate the top two items on the str stack                                        | concat                   |
| show    | output string to stdout, no implicit newline                                          | show <string\>            |
| add     | add the top two items on the int stack                                                |                          |
| mult    | multiply the top two items on the int stack                                           |                          |
| div     | divide the top two items on the int stack                                             |                          |
| exit    | exit program(usefull in interactive)                                                  |                          |
| intvar  | declare an int variable                                                               |                          |
| strvar  | declare a str variable                                                                |                          |
| ask     | read a line from stdin                                                                |                          |
| if      | conditional statement if                                                              |                          |
| else    | conditional statement else                                                            |                          |
| eq      | return whether the next two expression are equal                                      |                          |
| not     | boolean not                                                                           |                          |
| :       | declare label                                                                         |                          |
| goto    | go to label                                                                           |                          |
| {       | start evaluating statements until terminated by }                                     |                          |
| }       | finish evaluating statements started by {                                             |                          |
| concats | concatenate the next two statements                                                   |                          |
| adds    | add the next two statements                                                           |                          |
| divs    | divide the next two statements(returns str)                                           |                          |
| mults   | multiply the next two statements                                                      |                          |
| use     | use optional command                                                                  |                          |
| rand    | random int between the next two statements(optional))                                 |                          |
| <       | return whether, of the next two expressions, if the first one is less than the second |                          |
| \>       | return whether, of the next two expressions, if the first one is more than the second |                          |
| list    | declare a list or listify a string                                                    |                          |
| [       | start adding statements to a list until terminated by ]                               |                          |
| ]       | finish adding statements to a list started by [                                       |                          |
| setitem | set the value of a list item                                                          |                          |
| length  | return the length of a list                                                           |                          |
| asc     | convert to and from ascii codes                                                       |                          |
| newitem | add an item to a list                                                                 |                          |
| askkey  | read a single key from stdin                                                          |                          |
| and     | return whether the next two statements are both true                                  |                          |

### guide
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
