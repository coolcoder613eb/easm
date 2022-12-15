# add a `hw` command to easm
# in easm.py use importlib.import_module()
level = 1
def hw():
    print('Hello World!')

def setup(raiseerror,evaleasm):
    return {'hw':hw}
