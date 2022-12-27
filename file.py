

level = 1

def setup(raiseerror,evaleasm):
    
    
    def writefile():
        file = evaleasm()
        text = evaleasm()
        try:
            with open(file,'w',encoding='utf-8') as f:
                f.write(text)
        except:
            raiseerror('Error in writefile')
        
    
    return {'writefile': writefile}
