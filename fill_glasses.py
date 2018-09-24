# fill the glasses, given hight of glass stack, amount of liquid and volume of each glass
def get_glasses_for_level(height_of_stack):
    return (height_of_stack * (height_of_stack + 1)) // 2
    
def fill_glasses(height_of_stack, volume_of_glass, amount_of_liquid):
    glasses = [0.0] * get_glasses_for_level(height_of_stack)
    
    if height_of_stack > 0:
        glasses[0] = amount_of_liquid * 1.0
        for current_level in range(1, height_of_stack):
            startIndex = get_glasses_for_level(current_level - 1)
            endIndex = get_glasses_for_level(current_level)
            for current_glass in range(startIndex, endIndex):
                if glasses[current_glass] > volume_of_glass:
                    surplus_liquid = (glasses[current_glass] - volume_of_glass)
                    glasses[current_glass + current_level] += surplus_liquid  / 2
                    glasses[current_glass + current_level + 1] +=  surplus_liquid / 2
                    glasses[current_glass] = volume_of_glass
            
    return glasses

print (fill_glasses(0, 0, 0.0))
print (fill_glasses(1, 1, 1.0))
print (fill_glasses(2, .5, 2.0))
print (fill_glasses(4, 1, 5.0))