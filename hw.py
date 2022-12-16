# add a `hw` command to easm

level = 1

def setup(raiseerror,evaleasm):
    
    
    def hw():
        print('Hello World!')
        
    
    return {'hw': hw}
