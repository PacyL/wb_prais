from ..neironka import * 
from ..core import *

def test_00():
    cod=1233123
    bool(cod)==False
def test_01():
    cod=1398771724
    bool(cod)==True
    
def test_02():
    artic = 225960782
    poisk(artic)[0]==True
    
def test_03():
    artic = 154859674
    poisk(artic)[0]==True

def test_04():
    artic = 15485
    poisk(artic)[0]==False
    

    
    
if __name__=="__main__":
    print(test_00())
    print(test_01())