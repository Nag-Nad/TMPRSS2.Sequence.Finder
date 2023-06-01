# Create an empty dictionary
data = {}  

with open('Genetics/sequence.txt', 'r') as file:
    lines = file.readlines()[1:47]      # Remove the first and last line
    for line in lines:
        new_line = line.replace(' ', '').replace('\n', '')     
        for char in new_line:
            data[len(data) + 1] = char  # Assign each character to the next available key in the dictionary


# Write a range of sequence in a new text file
start = int(input('please write the first base: '))
end = int(input ('please write the last base: '))
path = input ('please add your path: ')

# Write a new file 
with open(path, 'w') as output_file:
    for key in range(start, end+ 1):
        if key in data:
            output_file.write(data[key])

print("Keys", start, "to", end, "copied to", path, "successfully.")