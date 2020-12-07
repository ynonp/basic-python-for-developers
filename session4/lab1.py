interfaces = []
with open('regexp_lab.txt', 'r') as f:
    data = f.read()
    #print(data)
    interfaces = data.split("\n\n")

print(f"There are {len(interfaces)} network interfaces")

for ith in interfaces:
    print(ith)
