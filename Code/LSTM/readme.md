# How to run the Attentive LSTM models

This model is run on each target-aspect pair. An attentive-LSTM model is trained for each target-aspect pair.
The labels for the reviews are "Positive", "Negative" and "None".

After runing the model for each target-aspect pair, the results are averaged to obtain the evaluation metrics Strict accuracy, Macro-F1 and Sentiment accuracy.



### Train
To train the for each target-aspect pair model, Follow the steps below

1. Download each target-aspect pair file.
2. Copy the following files: *models folder, data_utils.py, download_glove.py, evaluating_LSTM.py, test.py*, and *train.py* from the africel-calls folder to the current target-aspect folder.
3. Run the *train.py* scrict to train the model for that target-aspect pair.

```
test.py
```


#### Additional Hyperparameters
The folowing parameters can be set before running the models


Parameter|Description|Type|Default Value|Option|
---------|-----------|----|-------------|------|
train_tsv|Train tsv file|str|"data/train_dev_data_oversampled.tsv"|-|
model|model type|str|"att"|"naive or att"|
glove|Use glove as initial word embedding|-|-|-|-|
embedding_size|Word embedding size|int|200|50, 100, 200, 300|
num_hidden|RNN Network size|int|100|-|
num_layers|RNN Network depth|int|2|-|
learning_rate|Learning rate|float|1e-3|-|
batch_size|Batch size|int|64|-|
num_epochs|Number of epochs|int|10|-|
keep_prob|Dropout keep probability|float|0.8|-|
checkpoint_dir|Checkpoint directory|str|"saved_model"|-|


### Test
To test classification accuracy for test data, run the **test.py** code with test_tsv parameter set to the test dataset.

```
test.py --test_tsv="/data/test.tsv"
```


### Sample Test Results
Trained and tested with the default hyper-parameters,


~|africell_calls|africell_data|africell_general|africell_network|airtel_calls|airtel_data|airtel_general|airtel_network|mtn_calls|mtn_data|mtn_general|mtn_network|Average|
-|--------------|-------------|----------------|----------------|------------|-----------|--------------|--------------|---------|--------|-----------|-----------|-------|
sentiment_Acc|0.810|0.420|0.722|0.648|0.624|0.648|0.797|0.697|0.847|0.788|0.648|0.806|**0.705**|
aspect_Macro_F1|0.111|0.625|0.121|0.195|0.342|0.285|0.105|0.191|0.089|0.303|0.349|0.055|**0.231**|
 
  
  
