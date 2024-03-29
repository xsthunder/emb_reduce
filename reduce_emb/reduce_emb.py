#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: ./nb/reduce_emb.ipynb
from xs_lib.common import tqdm
import xs_lib

class ReadlineIter:
    def __init__(self, fp, _len=None, raise_on_unmatch_len=False):
        self.fp = fp
        self._len = _len
        self.cnt = 0
        self.raise_on_unmatch_len = raise_on_unmatch_len
        if _len is not None: assert isinstance(_len, int), f"len '{_len}' must be int"
    def __next__(self):
        line = self.fp.readline()
        if len(line) == 0:
            if self._len is not None and self.cnt != self._len:
                print(f"WARNING: in ReadlineIter line cnt {self.cnt} dont match passed len {self._len}")
                if self.raise_on_unmatch_len:
                    assert self.cnt == self._len, f"line cnt {self.cnt} dont match passed len {self._len}"
            raise StopIteration
        self.cnt += 1
        return line
    def __iter__(self):
        return self
    def __len__(self):
        return self._len

def get_word_set(fword_list):
    print(f"reading {fword_list}")
    word_set = set()
    with open(fword_list, "r") as fp:
        readlineIter = ReadlineIter(fp)
        for word in tqdm(readlineIter):
            word = word.strip()
            word_set.add(word)
    return word_set

def getEmbReadlineIter(emb_fp):
    embReadlineIter = None
    try:
        emb_word_cnt, dim = emb_fp.readline().split()
        emb_word_cnt = int(emb_word_cnt)
        print(f"emb_file has {emb_word_cnt} and {dim} dim according to first line")
        embReadlineIter = ReadlineIter(emb_fp, emb_word_cnt)
    except :
        emb_fp.seek(0)
        embReadlineIter = ReadlineIter(emb_fp)
    return embReadlineIter

def main(femb, fword, fout):
    emb_fp = open(femb, "r")
    print(f"reading emb_file:'{femb}'")
    embReadlineIter = getEmbReadlineIter(emb_fp)
    word_set = get_word_set(fword)
    print(f"word_set: {len(word_set)} word_read")
    fpout = open(fout, 'w')
    cnt = 0
    for line in tqdm(embReadlineIter):
        word = line[:line.index(' ')]
        if word in word_set:
            fpout.write(line)
            cnt += 1
    print(f"{cnt} word emb found, total {len(word_set)} word")
    fpout.close()

import fire
import os
if not xs_lib.common.IN_JUPYTER and __name__=="__main__" and os.environ.get("STOP_FIRE", "") != "true":
    fire.Fire(main)