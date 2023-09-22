export CUDA_VISIBLE_DEVICES=3
python train.py --dataset strefer --max_lang_num 100 --work_dir log/STRefer --batch_size 8
# python train.py --dataset strefer+ --max_lang_num 100 --work_dir log/WildRefer/no_box --batch_size 14

# python train.py --dataset strefer --max_lang_num 100 --work_dir log/STRefer/box --batch_size 14 --butd
# python train.py --dataset strefer+ --max_lang_num 100 --work_dir log/WildRefer/box --batch_size 14 --butd
