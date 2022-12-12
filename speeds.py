import os,timeit
def easm():
    os.system('py easm.py speed.easm')
def pypyeasm():
    os.system('pypy easm.py speed.easm')
def cyeasm():
    os.system('py cyeasm.py speed.easm')
def nuitkaeasm():
    os.system('easm speed.easm')
with open('results.csv','w') as f:
    text = 'Python,Cython,PyPy,Nuitka\n'+\
    str(timeit.timeit(easm, number=10))+\
    ','+str(timeit.timeit(cyeasm, number=10))+\
    ','+str(timeit.timeit(pypyeasm, number=10))+\
    ','+str(timeit.timeit(nuitkaeasm, number=10))
    f.write(text)
