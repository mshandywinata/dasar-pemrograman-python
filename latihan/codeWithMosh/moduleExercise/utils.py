def findMax(*numbers: int) -> int:
    maxNumber = numbers[0]
    for number in numbers:
        if number > maxNumber:
            maxNumber = number
    
    return maxNumber