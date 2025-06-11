from neironka import bool

def test_00():
    cod=1233123
    bool(cod)==False
def test_01():
    cod=1398771724
    bool(cod)==True
    
if __name__=="__main__":
    print(test_00())
    print(test_01())