# https://www.practicepython.org/
from practice.CharacterInput import CharacterInput as CI
from practice.OddEven import OddEven as OE
from practice.LessThanTen import LessThanTen as LTT
from practice.Divisors import Divisors as Div
from practice.ListOverlap import ListOverlap as LO
from practice.palindrome import palindrome as pal
from practice.ListComprehensions import ListComprehensions as LC
from practice.RockPaperScissors import RockPaperScissors as TKM
from practice.GuessingGame import GuessingGame as GG
from practice.PrimalityFunctions import PrimalityFunctions as PF
from practice.ListEnds import ListEnds as LE
from practice.Fibonacci import Fibonacci as Fi

def main():
    n = 11 # fonksiyonlar arasında gezin.

    function_list=[ # practice fonksiyonlarının listesi.
    CI.CharacterInputSol, # 0
    OE.OddEven, # 1
    LTT.LessThanTen, #2
    Div.Divisors, # 3
    LO.ListOverlap, # 4
    pal.palindrome, # 5
    LC.ListComprehensions, # 6
    TKM.RockPaperScissors, # 7
    GG.GuessingGame, # 8
    PF.PrimalityFunctions, # 9
    LE.ListEnds, # 10
    Fi.Fibonacci, # 11
    
    ]

    current_function=function_list[n]
    current_function()


from bonus1.NumberBases import NumberBases as NB
def bonusfuncs():
    NB.NumberBases()


if __name__ == "__main__":
    main()
    #bonusfuncs()
else:
    print("lütfen main.py dosyanısını kontrol edin.\n")

