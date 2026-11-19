f = open("parth.txt", "a+")  # Open in append and read mode
f.seek(10)  # Move to the 10th byte
data = f.read(5)  # Read 5 bytes from that position
f.close()

print(data)
