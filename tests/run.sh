set -e


# set up conda env
# https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

if test $TRAVIS
then
    source $HOME/miniconda/etc/profile.d/conda.sh
    conda activate test
    echo "done: conda activated test"
fi
_TRAVIS=$TRAVIS
export TRAVIS=true

# 生成文件
export STOP_FIRE="true"
python test_reduce_emb.py


# test_emb_file.txt
# test_fword_list.txt
# test_main_output.txt

# export TRAVIS=$_TRAVIS

export STOP_FIRE=""

# entrance test

python test_reduce_emb.py --femb test_emb_file.txt --fword test_fword_list.txt --fout cli_call_output.txt
python ../reduce_emb/reduce_emb.py --femb test_emb_file.txt --fword test_fword_list.txt --fout cli_call_output.txt

diff test_main_output.txt cli_call_output.txt && echo "test passed" || echo "pass failed"
diff test_main_output.txt cli_call_output.txt

echo """</s>
是
、""" > Tencent_AILab_ChineseEmbedding_sample_wordlist.txt

python ../reduce_emb/reduce_emb.py --femb Tencent_AILab_ChineseEmbedding_sample.txt --fword Tencent_AILab_ChineseEmbedding_sample_wordlist.txt --fout cli_call_output.txt


