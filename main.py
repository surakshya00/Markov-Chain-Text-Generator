import random
def read_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file_handle:
        s = str(file_handle.read())
        return s

def create_chain(s):
    d=dict()
    splitted= s.replace(".", "").split()
    for i in range(len(splitted)-1):
        if splitted[i] in d:
            if splitted[i+1] in d[splitted[i]]:
                d[splitted[i]][splitted[i+1]]+=1
            else:
                d[splitted[i]][splitted[i+1]]=1
        else:
            d[splitted[i]]= {splitted[i+1]:1}
    return d

def get_next_word(chain, prev_word):
    if prev_word not in chain:
        return random.choice(list(chain.keys()))
    else:
        total = 0
        for key, vals in chain[prev_word].items():
            total += vals
        v=random.randint(1,total)
        for key, vals in chain[prev_word].items():
            if v>vals:
                v=v-vals
        else:
            return key

def generate_text(chain, length):
    new_word=random.choice(list(chain.keys()))
    chain_word=[new_word]
    for i in range(length-1):
        words=get_next_word(chain,chain_word[-1])
        chain_word.append(words)
    return ' '.join(chain_word)



def write_file(file_path, contents):
    with open(file_path, "w", encoding="utf8") as my_output_file:
        my_output_file.write(contents)

def run(input_path, output_path, length):
    text = read_file(input_path)
    chain = create_chain(text)
    result = generate_text(chain, length)
    write_file(output_path, result)


