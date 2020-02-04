SentiTel: Targeted Aspect-Based Sentiment Analysis for Social Media Data.
================
### Summary
We used word sequence representation to extract fine-grained information from social media opinions about three major telecoms in Uganda (MTN, Airtel and Africell). The social media sites under consideration are [Twitter](https://twitter.com/) and [Facebook](https://web.facebook.com/).

Using both traditional machine learning and deep learning (BERT), we automatically extract descriptors from the opinions and use them to create a structured summary of the opinion. The structured summary can used by both the enterprise and it's customers for further analysis to gain insights from the opinions. For example the enterprise can use the summary to know which service the customers are most desatified about and also to access the performance of their competitors. The customers can use the summary to compare telecoms and make a decision on which telecom to use as their service provider.

In order to carry out supervised learning, we constructed a human annotated dataset called SentiTel. SentiTel contains 6,320 opinions and the opinions contain target telecoms ranging from one to three.

The descriptors extracted include the target telecom, aspect and the sentiment towards the aspect. This level of sentiment analysis is called Targeted Aspect-based Sentiment Analysis (TABSA). 


Paper
================
Paper generated 

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


Project
=================
Here is where a brief description of the project should go.

It may be worthwhile to list major project contributors here, especially if this is a closed source project as one might need to reach out for questions later on.

Setting Up
=================
To run the traditional machine learning models (Random Forest and Logistic Regression) just run the notebooks



