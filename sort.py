def sort(length, width, height, mass):
    # First check if any input is None or not a number
    
    for dim in [length, width, height, mass]:
        if dim is None or not isinstance(dim, (int, float)):
            raise ValueError("Dimension and mass must be a number and cannot be None.")
        elif dim <= 0:
            raise ValueError("Dimension and mass cannot be less than or equal to 0 and cannot be None.")
    
    volume = width * height * length
    
    # check if package is heavy
    is_package_heavy = False
    if mass >=20:
        is_package_heavy=True
   
    # check if package is bulky
    is_package_bulky = False
    if volume >=1000000 or width >=150 or height >=150 or length >=150:
        is_package_bulky=True
   

    if is_package_heavy and is_package_bulky:
        return "REJECTED"
    elif is_package_heavy or is_package_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"
    
    
# print(sort(50,50,"a",10))
 
