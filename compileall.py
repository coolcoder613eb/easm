import os,sys
for x in os.listdir():
    if x.endswith('.easm'):
        os.system('"'+sys.executable+'" compiler.py '+x)
