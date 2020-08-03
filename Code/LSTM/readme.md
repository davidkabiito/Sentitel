# How to run the Attentive LSTM models

This model is run on each target-aspect pair. An attentive-LSTM model is trained for each target-aspect pair.
The labels for the reviews are "Positive", "Negative" and "None".

After runing the model for each target-aspect pair, the results are averaged to obtain the evaluation metrics Strict accuracy, Macro-F1 and Sentiment accuracy.



### Train
To train the model with sample data,
```
$ python train.py
```
Every 2000 steps, the classification accuracy is tested with development set and the best model is saved.


To use Glove pre-trained vectors as initial embedding,
```
$ python train.py --glove
```

#### Additional Hyperparameters
```
$ python train.py -h
usage: train.py [-h] [--train_tsv TRAIN_TSV] [--model MODEL] [--glove]
                [--embedding_size EMBEDDING_SIZE] [--num_hidden NUM_HIDDEN]
                [--num_layers NUM_LAYERS] [--learning_rate LEARNING_RATE]
                [--batch_size BATCH_SIZE] [--num_epochs NUM_EPOCHS]
                [--keep_prob KEEP_PROB] [--checkpoint_dir CHECKPOINT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --train_tsv TRAIN_TSV
                        Train tsv file.
  --model MODEL         naive | att
  --glove               Use glove as initial word embedding.
  --embedding_size EMBEDDING_SIZE
                        Word embedding size. (For glove, use 50 | 100 | 200 | 300)
  --num_hidden NUM_HIDDEN
                        RNN Network size.
  --num_layers NUM_LAYERS
                        RNN Network depth.
  --learning_rate LEARNING_RATE
                        Learning rate.
  --batch_size BATCH_SIZE
                        Batch size.
  --num_epochs NUM_EPOCHS
                        Number of epochs.
  --keep_prob KEEP_PROB
                        Dropout keep prob.
  --checkpoint_dir CHECKPOINT_DIR
                        Checkpoint directory.
```



### Test
To test classification accuracy for test data,

```
$ python test.py --test_tsv="/data/test.tsv"
```


### Sample Test Results
Trained and tested with default hyper-parameters,


~|africell_calls|africell_data|africell_general|africell_network|airtel_calls|airtel_data|airtel_general|airtel_network|mtn_calls|mtn_data|mtn_general|mtn_network|Average|
-|--------------|-------------|----------------|----------------|------------|-----------|--------------|--------------|---------|--------|-----------|-----------|-------|
sentiment_Acc|0.810|0.420|0.722|0.648|0.624|0.648|0.797|0.697|0.847|0.788|0.648|0.806|**0.705**|
aspect_Macro_F1|0.111|0.625|0.121|0.195|0.342|0.285|0.105|0.191|0.089|0.303|0.349|0.055|**0.231**|
 
  
  
