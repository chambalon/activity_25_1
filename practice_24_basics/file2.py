with open('in_file.txt','r') as infile, open('out_file.txt','w') as outfile:
    for line in infile:
        outfile.write(line)

with open('out_file.txt','r') as outfile:
    print(outfile.read())
