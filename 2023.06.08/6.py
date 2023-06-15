def orth_triangle(*, cathetus1: int = 0, cathetus2: int = 0, hypotenuse: int = 0) -> float:
    """Вычисляет третью сторону прямоугольного треугольника по двум переданным"""
    
    if hypotenuse == 0 and cathetus1 != 0 and cathetus2 != 0: # передали два катета
        side = pow(cathetus1**2 + cathetus2**2, 0.5)
    elif cathetus1 == 0 and cathetus2 != 0 and hypotenuse > cathetus2: # если нет первого катета
        side = pow(hypotenuse**2 - cathetus2**2, 0.5)
    elif cathetus2 == 0 and cathetus1 != 0 and hypotenuse > cathetus1: # если нет второго катета
        side = pow(hypotenuse**2 - cathetus1**2, 0.5)   
    else: # вычисление невозможно
        side = None
        
    return side
    
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None