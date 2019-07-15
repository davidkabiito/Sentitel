## About the annotation

This repository contains our guidelines for annotation of sentiment in social media.

There are two files
- Guidelines:

Contains the rules that were followed while annotation the data.

- brat_annotation_interface

Contains snapshots of sample annotations that were used to guide the annotators.

Highlights of the annotation:

#### Tools
_BRAT_

_Twitter API_

_Scrapy_

#### Annotators: 
Three undergraduate interns from the AI Research Lab, Makerere University where selected to annotate the dataset. Each anotator was required to first read the guidelines (Guidelines.md) and go through the sample annotations (brat_annotation_interface). They then annotated a subset of the data. After each round of annotation, agreements between annotators were calculated and disagreements were discussed. This procedure continued until we obtained a reasonable inter-annotation aggreement over a randomly selected subset of the data. Below is Inter-annotation aggreement before procedding to annotate the entire dataset.


The annotators the procced to annotate the entire dataset with each annotating a third of the data. 

#### Dataset:
The data was obtained from twitter and facebook. It contains reviews about 3 major telcoms in Uganda. The twitter data was collected using the twitter API for the period between 12022019 to 12072019. 
The facebook data was collected from the respective review pages of 3 telcoms in Uganda. All the reviews posted on the page from the time of creation were collected using Scraping tool in python (Scrapy).

