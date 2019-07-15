About the annotation
===========================

This repository contains the guidelines for annotation of the dataset.

### Files
- Guidelines:

Contains the rules that were followed while annotating the data.

- brat_annotation_interface

Contains snapshots of sample annotations that were used to guide the annotators.

### Dataset
The data was obtained from twitter and facebook. It contains reviews about 3 major telcoms in Uganda. The twitter data was collected using the twitter API for the period between 12022019 to 12072019. 
The facebook data was collected from the respective review pages of 3 telcoms in Uganda. All the reviews posted on the page from the time of creation were collected using Scraping tool in python (Scrapy).

### Tools:
- BRAT
- Twitter API
- Scrapy

### Annotators
Three undergraduate interns from the AI Research Lab, Makerere University where selected to annotate the dataset. Each anotator was required to first read the guidelines (Guidelines.md) and go through the sample annotations (brat_annotation_interface). They then annotated a subset of the data. After each round of annotation, agreements between annotators were calculated and disagreements were discussed. This procedure continued until we obtained a reasonable inter-annotation aggreement over a randomly selected subset of the dataset. Below is Inter-annotation aggreement before proceding to annotate the entire dataset. The inter-annotation aggreement was calculated using the Cohen Kappa coeffiecient. This is reported along with other correlation measures (kendall, pearson, spearman).

- Sentiment

![image](https://user-images.githubusercontent.com/43681553/61225893-26a01080-a72a-11e9-9332-8b5c73bddbd6.png)

- Aspect

![unnamed](https://user-images.githubusercontent.com/43681553/61226114-8696b700-a72a-11e9-9d0f-bb4cc01e74fc.png)

The annotators then proceded to annotate the entire dataset with each annotating a third of the entire dataset. 
