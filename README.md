# Usage

retrive word emb from large word emb

```
python sys.argv[0] --fword wordlist --femb word_emb_file --fout reduced_emb_file
```

## require

fire, tqdm

## wordlist

relatively small

each word perline

## word_emb_file

very large

optional `wordnum:num emb_dim:num` for the first line, see [./tests/Tencent_AILab_ChineseEmbedding_sample](./tests/Tencent_AILab_ChineseEmbedding_sample) for example. glove doesnt have this line

`word:num dim0 dim1 [<dim2, >]` for rest

read until empty line

## reduced_emb_file

where to output, format will like golve without the first line

## want to release to pip 

### ref 

[python-snippet/upload_to_pip.md at master · xsthunder/python-snippet](https://github.com/xsthunder/python-snippet/blob/master/python/upload_to_pip.md)

[xsthunder/xs_lib](https://github.com/xsthunder/xs_lib)
