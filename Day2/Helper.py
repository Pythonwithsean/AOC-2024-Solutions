import re

def parse_input(input_data):
    # Split input by lines
    lines = input_data.strip().splitlines()
    
    # Split each line into words
    words = [line.split() for line in lines]
    
    # Extract all numbers from input (across all lines)
    numbers = list(map(int, re.findall(r'-?\d+', input_data)))
    
    return lines, words, numbers

def parseFile(path): 
    with open(path, "r") as f: 
        return parse_input(f.read())
    
