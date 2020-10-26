## require

fire, tqdm

## Usage

retrive word emb from large word emb

```
python ./reduce_emb/reduce_emb.py --fword wordlist --femb word_emb_file --fout reduced_emb_file
```

### wordlist

relatively small txt

each word perline

### word_emb_file

very large txt

optional `wordnum:num emb_dim:num` for the first line, see [./tests/Tencent_AILab_ChineseEmbedding_sample](./tests/Tencent_AILab_ChineseEmbedding_sample) for example. glove doesnt have this line

`word:num dim0 dim1 [<dim2, >]` for rest

read until empty line

## reduced_emb_file

txt where to output, format will like golve without the first line

## want to release to pip 

### ref 

[python-snippet/upload_to_pip.md at master · xsthunder/python-snippet](https://github.com/xsthunder/python-snippet/blob/master/python/upload_to_pip.md)

[xsthunder/xs_lib](https://github.com/xsthunder/xs_lib)
