## TABSA as a Sentence Pairs classification task using the BERT model

### Requirement
pytorch: 1.0.0
python: 3.7.1
tensorflow: 1.13.1 (only needed for converting BERT-tensorflow-model to pytorch-model)
numpy: 1.15.4
nltk
sklearn

### Step 1: prepare datasets


### Step 2: prepare BERT-pytorch-model

### Step 3: train

### Step 4: evaluation
Evaluate the results on test set (calculate Acc, F1, etc.).

For example, BERT-pair-NLI_M task on Sentitel dataset:

python evaluation.py --task_name sentihood_NLI_M --pred_data_dir results/sentihood/NLI_M/test_ep_4.txt
