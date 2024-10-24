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
    if pathList[0] == "/": # when the provided path is valid
        
        # analyze each character in the pathList and pop accordingly
        for char in range(len(pathList)):
            stack.append(pathList[char])
            
            # case: for slashes that are at the end of the path
            ## it's important this if statement executes first so that later
            ## cases assuming there are more characters don't cause an exception
            if pathList[char] == "/" and char + 1 == len(pathList): 
                if stack.count("/") > 1: stack.pop()
            
            # case: for slashes followed by two periods
            elif pathList[char] == "/" and pathList[char + 1] == "." and pathList[char + 2] == "." and stack.count("/") > 1: 
                stack.pop(); stack.reverse()
                lastSlashIndex = stack.index("/"); stack.reverse()
                lastSlashIndex = len(stack) + ~lastSlashIndex
                while len(stack) > lastSlashIndex:
                    stack.pop()
            
            # cases: for slashes followed by another slash or a period, or a period
            elif pathList[char] == "/" and (pathList[char + 1] == "/" or pathList[char + 1] == ".") or pathList[char] == ".": 
                stack.pop()
        
        # append the approved stack to the string
        for char in stack:
            path += char
        return path
    
    else: return "Invalid Path"
    
def main():
    # Takes Unix path as input
    path = input()

    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()
