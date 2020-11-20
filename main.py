from ArrayStack import *                                                             
S = ArrayStack()                                                                     
sfile = "kaynak.c"                                                                   
original = open(sfile)                                                               
for line in original:                                                                
    l = line.rstrip('\n')                                                           
    S.push(l)                                                                        
original.close()                                                                     
tfile = "hedef.c"                                                                   
output = open(tfile, 'w')  # reopening file overwrites original                      
while not S.is_empty():                                                            
    output.write(S.pop() + '\n')  # re-insert newline characters                     
output.close()                                                                       
def is_matched(expr, kaynak=None):

    lefty = '{'  # opening delimiters                                               
    righty = '}'  # respective closing delims                                       
    S = ArrayStack()                                                                 
    for c in expr:                                                                   
        if c in lefty:                                                               
            S.push(c)                                                               
            print("\n\t")                                                            
        elif c in righty:                                                            
            if S.is_empty():                                                         
                return False                                                         
            print("\t\n")                                                            
        return S.is_empty(kaynak.c)
