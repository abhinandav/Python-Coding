with open('example.txt.','r') as file:
    content=file.read()
    with open('eg.txt','w') as file2:
        file2.write(content)



# as chunks


def write_as_chunks(source,destination,chunk_size=1024):
    with open(source,'rb') as s , open(destination,'wb') as d:
        while True:
            chunk=s.read(chunk_size)
            if not chunk:
                break
            d.write(chunk)

write_as_chunks('source.txt','destination.txt')