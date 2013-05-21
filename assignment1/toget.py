myFile = open("stream_20.json", 'w')
file = open("stream.json", 'r')
for i in range(1,21):   
    myFile.write(file.readline())