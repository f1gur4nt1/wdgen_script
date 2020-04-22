apt-get install unzip -y

unzip wdgen_script.zip

rm -rf scripts

rm wdgen_script.zip

cp -rf wdgen_script/* $PWD

rm -rf wdgen_script

rm run.sh



