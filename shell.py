

level = 1

def setup(raiseerror,evaleasm):
    
    
    def runcommand():
        cmd = evaleasm()
        if type(cmd) == str:
            os.system(cmd)
        else:
            raiseerror('Error in runcommand')
        
    
    return {'runcommand': runcommand}
