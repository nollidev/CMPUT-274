# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

def simplify_path(path):
    # Add your implementation here
    pathList = list(path)
    path = ""
    stack = []
    for char in range(len(pathList)):
        stack.append(pathList[char])
        if pathList[char] == "/" and char + 1 == len(pathList): 
            if char != 0: stack.pop()
        elif pathList[char] == "/" and pathList[char + 1] == "." and pathList[char + 2] == ".": 
            if stack.count("/") > 1: stack.pop(); stack.reverse()
            lastSlashIndex = stack.index("/"); stack.reverse()
            lastSlashIndex = len(stack) + ~lastSlashIndex
            while len(stack) > lastSlashIndex:
                stack.pop()
        elif pathList[char] == "/" and (pathList[char + 1] == "/" or pathList[char + 1] == ".") or pathList[char] == ".": stack.pop()
    for char in stack:
        path += char
    return path
    
def main():
    # Takes Unix path as input
    path = input()

    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()
