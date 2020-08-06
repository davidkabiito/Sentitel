## TABSA as a Sentence Pairs classification task using the BERT model

### Requirement
pytorch: 1.0.0

python: 3.7.1

tensorflow: 1.13.1 (only needed for converting BERT-tensorflow-model to pytorch-model)

numpy: 1.15.4

nltk

sklearn

### Step 1: Datasets
The dataset is located in the folder
Sentitel/Code/BERT/Data/

File|Description|
----|-----------|
train.tsv|training set is used to train the models|
dev.tsv|validation set is used for tuning the hyperparameters|
test.tsv|Used for evaluating the models|


### Step 2: Prepare BERT-pytorch-model

Download [BERT-Base (Google's pre-trained models)](https://github.com/google-research/bert) and then convert a tensorflow checkpoint to a pytorch model.

For example:
```
python convert_tf_checkpoint_to_pytorch.py \
--tf_checkpoint_path uncased_L-12_H-768_A-12/bert_model.ckpt \
--bert_config_file uncased_L-12_H-768_A-12/bert_config.json \
--pytorch_dump_path uncased_L-12_H-768_A-12/pytorch_model.bin
```

### Step 3: Train
Training the BERT model on the sentitel dataset.

```
!CUDA_VISIBLE_DEVICES=0,1,2,3 python run_classifier_TABSA.py \
--task_name sentihood_NLI_M \
--data_dir data/sentitel/bert-pair/ \
--vocab_file uncased_L-12_H-768_A-12/vocab.txt \
--bert_config_file uncased_L-12_H-768_A-12/bert_config.json \
--init_checkpoint uncased_L-12_H-768_A-12/pytorch_model.bin \
--eval_test \
--do_lower_case \
--max_seq_length 128 \
--train_batch_size 24 \
--learning_rate 2e-5 \
--num_train_epochs 6.0 \
--output_dir results/sentitel/NLI_M \
--seed 42
```
### Step 4: Evaluation
Evaluate the results on test set 

calculate Acc, F1, and AUC.

```
python evaluation.py --task_name sentitel_NLI_M --pred_data_dir results/sentitel/NLI_M/test_ep_4.txt

```
