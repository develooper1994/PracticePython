
def Divisors():
    try:
        num=int(input("Bölmek istediğiniz sayı nedir?").strip())
    except ValueError:
        print("sorun var.")
    AllOfNumbers=list(range(1,num+1))
    
    divisorList = []
    for number in AllOfNumbers:
        if num % number == 0:
            divisorList.append(number)
    
    print(divisorList)
    return divisorList  
