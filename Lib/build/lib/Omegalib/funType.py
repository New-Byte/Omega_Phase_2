import json
# os.system("python backend.py")
def findReturnType():
    f = open("SymbolTableManager.json","r")
    stm = json.load(f)
    x=0
    pos=0
    while x!=len(stm["tokens"]):
        token=stm['tokens'][x][0]
        if token=='def':
            pos=x
            while token!='return':         
                x+=1
                token=stm['tokens'][x][0]  
            print('find return var= '+stm['tokens'][x+1][0])
            returnvar=stm['tokens'][x+1][0]
            returntype=stm['tokens'][x+1][1]
            if(returntype=="IDENTIFIER" or returntype=="SYMBOL"):
                print("find var type")
                x=pos
                token=stm['tokens'][x][0] 
                while token!=returnvar:
                    x+=1
                    token=stm['tokens'][x][0]
                print('find var= ',token,"index of x is ",x)        
                tokenval=stm['tokens'][x][1] 
                eq=''
                while tokenval!='INDENT':
                    print("equation is "+eq)
                    eq+=stm['tokens'][x][0]
                    x+=1
                    tokenval=stm['tokens'][x][1] 
                print(eq)
                try:
                    print("this is eq "+eq[2:])
                    print(str(type(eval(eq[2:])))[8:-2])
                except NameError:
                    print("String")
            else:
                print("this is return type= "+returntype)
        else:
            x+=1
# python scanner.py ../../test/fun.py
findReturnType()