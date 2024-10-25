# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

def simplify_path(path):
    # Add your implementation here
    stack = []
    if path[0] == "/": # when the provided path is valid
        
        # analyze each character in the path and pop accordingly
        for char in range(len(path)):
            stack.append(path[char])
            
            # case: for slashes that are at the end of the path
            ## it's important this if statement executes first so that later cases
            ## that assume there are more characters don't cause an exception
            if path[char] == "/" and char + 1 == len(path): 
                if stack.count("/") > 1: stack.pop()
            
            # case: for slashes followed by two periods
            ## removes slash, finds index of previous slash, pops until previous slash removed
            elif path[char] == "/" and path[char + 1] == "." and path[char + 2] == "." and stack.count("/") > 1: 
                stack.pop(); stack.reverse()
                lastSlashIndex = stack.index("/"); stack.reverse()
                lastSlashIndex = len(stack) + ~lastSlashIndex
                while len(stack) > lastSlashIndex:
                    stack.pop()
            
            # cases: for slashes followed by another slash or a period, or a period
            elif path[char] == "/" and (path[char + 1] == "/" or path[char + 1] == ".") or path[char] == ".": 
                stack.pop()
        
        # append the approved stack to the string
        simplified_path = ""
        for char in stack:
            simplified_path += char
        return simplified_path
    
    else: return "Invalid Path"
    
def main():
    # Takes Unix path as input
    path = input()

    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()
