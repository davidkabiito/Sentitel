SentiTel: Targeted Aspect-Based Sentiment Analysis for Social Media Data.
================
### Summary
We used word sequence representation to extract fine-grained information from social media opinions about three major telecoms in Uganda (MTN, Airtel and Africell). The social media sites under consideration are [Twitter](https://twitter.com/) and [Facebook](https://web.facebook.com/).

Using both traditional machine learning and deep learning (BERT), we automatically extract descriptors from the opinions and use them to create a structured summary of the opinion. The structured summary can used by both the enterprise and it's customers for further analysis to gain insights from the opinions. For example the enterprise can use the summary to know which service the customers are most desatified about and also to access the performance of their competitors. The customers can use the summary to compare telecoms and make a decision on which telecom to use as their service provider.

In order to carry out supervised learning, we constructed a human annotated dataset called SentiTel. SentiTel contains 6,320 opinions and the opinions contain target telecoms ranging from one to three.

The descriptors extracted include the target telecom, aspect and the sentiment towards the aspect. This level of sentiment analysis is called Targeted Aspect-based Sentiment Analysis (TABSA). 


Paper
================
	1. Targeted Aspect-Based Sentiment Analysis for Ugandan Telecom Reviews from Twitter,  
	David Kabiito and Joyce Nakatumba-Nabende, 
	The 22nd International Conference on Artificial Intelligence (ICAI'20) ,  July 27-30, 2020, Las Vegas, USA.
	
	2. SentiTel: TABSA for Twitter reviews on Uganda Telecoms, 
	David Kabiito and Joyce Nakatumba-Nabende, 
	Widening NLP Workshop 2020, Seattle, Washington,  United States .

Requirement
=================
1. python 3.6 and above
2. tensorflow
3. Access to atleast 1 GPU or Google Colab
4. Scikit-learn
5.  [BERT-Base (Google's pre-trained models)](https://github.com/google-research/bert)
6. nltk
7. numpy: 1.15.4
8. pytorch: 1.0.0

Results
=================
The table below shows the results obtained using both machine learning and deep learning approaches. The evaluation methods used are strict accuracy, Macro-F1 and AUC. There results are reported both in terms of aspect category detection and sentiment classification.

![results_table](https://user-images.githubusercontent.com/43681553/73733163-80ab0680-474c-11ea-9dee-1e596b03236d.png)



Setting Up
=================
To run the models, go to the respective notebook under [Code](https://github.com/davidkabiito/Sentitel/tree/master/Code)


* [Random Forest TFIDF](https://github.com/davidkabiito/Sentitel/blob/master/Code/random_forest/tfidf/T-ABSA_random_forest_tfidf_model.ipynb)
* [Random Forest WORD2VEC](https://github.com/davidkabiito/Sentitel/blob/master/Code/random_forest/word2vec/T-ABSA_random_forest_word2vec_model.ipynb)
* [Logistic Regression TFIDF](https://github.com/davidkabiito/Sentitel/blob/master/Code/LR/tfidf/T-ABSA_LR_tfidf_model.ipynb)
* [Logistic Regression WORD2VEC](https://github.com/davidkabiito/Sentitel/blob/master/Code/LR/word2vec/T-ABSA_LR_word2vec_model.ipynb)
* [BERT](https://github.com/davidkabiito/Sentitel/blob/master/Code/BERT/BERT_SentiTel.ipynb)
* [LSTM](https://github.com/davidkabiito/Sentitel/tree/master/Code/LSTM)



