import json
import pprint

file_name="ac1"
commands = None

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


with open(file_name, 'r') as f:
    commands = json.load(f)

for k,v in commands.items():
    label = k
    seq = v[2:]
    bits=[]
    for i in seq:
        if i == 1243:
            bits.append(1)
            #print(1, end='')
        if i == 397:
            bits.append(0)
            #print(0, end='')
    # print bits
    bit_chunks = (list(chunks(bits, 8)))

    # print ''.join([str(x) for x in bits])
    # print bit_chunks[8:-15], k
    print(bit_chunks, k)

    # for i,chunk in enumerate(bit_chunks):
    #     print i, chunk

    #print(k, len(v), v)
    #print(k, len(v[2:]), v[2:])

