# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

def fractal_eval(expr):
    if "[" in expr and "]" in expr:
        firstSplit = expr.split("[", 1)
        left, enclosedInSquare = firstSplit[0], firstSplit[-1] # enclosedInSquare is right of the [
        secondSplit = enclosedInSquare.rsplit("]", 1)
        enclosedInSquare, right = secondSplit[0], secondSplit[-1] # enclosedInSquare is left of the ]
        squareOfEnclosed = fractal_eval(enclosedInSquare) ** 2
        expr = left + str(squareOfEnclosed) + right
    return eval(expr)
                
def main():
    exp = input()
    print(round(fractal_eval(exp)))

if __name__ == "__main__":
    main()