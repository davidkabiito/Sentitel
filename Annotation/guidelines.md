# T-ABSA Annotation Guidelines for the Sentitel dataset #

The goal of this annotation task is to identify opinions expressed in a given sentence for specific entities (telecoms) and their aspects. An aspect should be chosen from a predefined list. In particular, given a sentence, the task of the annotator is to identify the following information:

### Telecom (Target Entity) ###
Telecom is the entity for which the opinion is expressed. The target telecom is usually preceded by the @ sign. The target telecom can be selected from the following list: MTN, Airtel and Africel. The review snippets below indicate the target telecom in bold.

 
* '**@mtnug** For as long as 2yrs, since I started staying in kireka! When I travel, all is very OK, only kireka, maybe u guys put an old used mast  here?!'

* '**@africellUG** Thank you africell uganda'

* '**@Airtel_Ug** your service of sending mobile money to **@mtnug** number is too slow!'

* "Their competitor **@Airtel_Ug** 's Data expires in 3 days. Problem is : Their network is too fake. MTN needs abetter competitor to take them out of business. "

### Aspect ###

Aspect (A) is a label that is given to the opinion expressed for a target telecom. Aspects will be selected from a provided list. For each identified telecom, one or more (or none) aspects can be identified based on the context of the sentence they appear in. The aspect can be selected from the following list: _sim card registration, calls, data, billing, customer service, mobile money and general_.
The aspect general describes a general feeling about a telecom without reference to a specific aspect. Sample reviews are provided below:

* '**@africellUG** Thank you africell uganda'

* "**@mtnug** and **@Airtel_Ug** , what's the problem? "

### Aspect Term Expression ###
An aspect term expression (ATE) is an explicit mention of an aspect A of entity E. This mention can be one or more words.

Examples;

* "Dear @Airtel_Ug , Your mobile money service has issues.  It's bouncing all my transactions." 

{ATE: mobile money, A: mobile money}

* '@mtnug What is wrong with your internet, the quality keeps worsening, it keeps hiccuping n this is irritating, whenever am around kireka, no matter where I sit in kireka, internet is poor!' 

{ATE: internet, A: internet}


* "Bt u MTN Uganda guys muyina kyemunonyako @mtnug just bought ma minutes to make some important call nw everything shows 'other error"

{ATE: minutes, A: calls}

#### Note: Annotate only a single most representative word in the ATE ####


### Sentiment (Polarity) ###
Each identified E#A pair in a sentence has to be given a polarity, from a set P = {positive, negative}.


