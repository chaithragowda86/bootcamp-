def split_and_join(line):
    # write your code here
    lines="this is a string"
    lines=line.split(" ")

    lines="-".join(line)
    
    


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)