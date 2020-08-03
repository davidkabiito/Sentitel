# How to run the Attentive LSTM models

This model is run on each target-aspect pair. The labels for the reviews are "Positive", "Negative" and "None".


After runing the model for each target-aspect pair, the results are averaged to obtain the evaluation metrics Strict accuracy, Macro-F1 and Sentiment accuracy.



### Train
To train the model with sample data,
```
$ python train.py
```
Train data is split to train set(85%) and validation set(15%). Every 2000 steps, the classification accuracy is tested with validation set and the best model is saved.


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
$ python test.py
```

To use custom data,
```
$ python test.py --test_tsv=<CUSTOM_TSV>
```


### Sample Test Results
Trained and tested with default hyper-parameters,

 | africell_calls | africell_data | africell_general | africell_network|  airtel_calls | airtel_data | airtel_general | airtel_network | mtn_calls | mtn_data | mtn_general | mtn_network
 
 :---: | :---: | :---:   | :---: | :---: |:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
 
aspect_strict_Acc | 0.809815951 | 0.419753086 | 0.722222222 | 0.648148148 | 0.623931624 | 0.648464164 | 0.796581197 | 0.697435897 | 0.846938776 | 0.787723785 | 0.647959184 | 0.806122449

sentiment_Acc | 0.809815951 | 0.419753086 | 0.722222222 | 0.648148148 | 0.623931624 | 0.648464164 | 0.796581197 | 0.697435897 | 0.846938776 | 0.787723785 | 0.647959184 | 0.806122449

aspect_Macro_F1 | 0.111111111 | 0.625 | 0.121212121 | 0.195121951 | 0.342465753 | 0.284722222 | 0.105263158 | 0.191176471 | 0.088888889 | 0.303030303 | 0.348837209 | 0.054545455
