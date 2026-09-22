from  typing import List , Tuple , Union , Dict

n : int = 5 

name : str = "Asus"


def sum(a: int,b:int) -> int: 
    return a + b


#  List  of integers 
numbers : List[int] = [1,2,3,4,5] 

#  Tuple of string and integer
person : Tuple[str , int] = ("Alice" , 30)

# Dictionary with string keys and integer values
scores : Dict[str , int] = {"Alice": 90 , "Bob": 85}

# Uninon type for variabel  that  hold multiple types 
idenifire : Union[int , str] = "ID123"
idenifire = 12345 #  Also  valid 