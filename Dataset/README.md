## SentiTel Dataset


The dataset is a human annotated dataset containing 6,320 reviews for the period between February 2019 and September 2019. This dataset is called SentiTel. 5,973 reviews in SentiTel have a single telecom entity mentioned while 347 reviews mention two or three telecom entities.  The total numner of opinions in SentiTel is 6,683 since some reviews have multiple opinions. All the reviews are related to telecom reviews made by twitter user on the major three telecoms in Uganda. The telecom entity names in the reviews are all normalised to *"MTN"*, *"Airtel"* and *"Africell"*.

Each tweet in SentiTel is labelled with telecom entity, aspect and opinion polarity towards the aspect. The predefined aspect categories are *data, customer service, general, network, calls, mobile money* and *application*. The table below shows the distributions of opinions across the aspect categories. The "Negative" sentiment is the dominant opinion polarity, this indicates that twitter user prefer to reviews when they are facing challenges with a service or product otherwise they remain silent. The *data* aspect is the most frequent aspect with over 2,400 reviews while the aspect *application* appears in less than 150 reviews.



Sentiment | data|Customer service|general|network|calls|mobile money| application|
----------| ----|----------------|-------|-------|-----|------------|------------|
Positive | 377 | 74 | 450 |  81 | 35 | 23 | 8 |
Negative | 2,064 |  928 | 418 | 740 | 442 | 244 | 139|


