Annotation Guidelines for the Sentitel dataset
==============================================

The goal of this annotation task is to identify opinions expressed in a given post towards a specific entity (telecom) and it's aspects. An aspect should be chosen from a predefined list. In particular, given a sentence, the task of the annotator is to identify the following information:

### Telecom (Target Entity) ###
Telecom is the entity for which the opinion is expressed. The target telecom is usually preceded by the @ sign. The target telecom can be selected from the following list: MTN, Airtel and Africel. The review snippets below indicate the target telecom in bold.

 
* '**@mtnug** For as long as 2yrs, since I started staying in kireka! When I travel, all is very OK, only kireka, maybe u guys put an old used mast  here?!'

* '**@africellUG** Thank you africell uganda'

* '**@Airtel_Ug** your service of sending mobile money to **@mtnug** number is too slow!'

* "Their competitor **@Airtel_Ug** 's Data expires in 3 days. Problem is : Their network is too fake. MTN needs abetter competitor to take them out of business. "

### Aspect ###

Aspect (A) is a label that is given to the opinion expressed for a target telecom. Aspects will be selected from a provided list. For each identified telecom, one or more (or none) aspects can be identified based on the context of the sentence they appear in. The aspect can be selected from the following list: _sim card registration, calls, data, billing, customer service, mobile money and general_.
The aspect general describes a general feeling about a telecom without reference to a specific aspect. 

Examples of reviews expressing a general aspect:

- '@africellUG you guys are life savers'
- '@africellUG is amazing'
- 'Thanks @Airtel_Ug Happy new month y'all.'
- '@Airtel_Ug LONGLIVE AIRTEL'
- 'I really love Airtel'

#### Aspect Term Expression ####
An aspect term expression (ATE) is an explicit mention of an aspect A of entity E. This mention can be one or more words. Annotators are  required to highlight a term in the sentence that is indicative of the aspect.The ATE for the aspect general is always "null".

**Note:** 
A single word that is most indicative of the aspect should be highlighted by the annotator.

Examples;

| Opinion | ATE | Aspect |
| :---         |     :---:      |          ---: |
| "Dear @Airtel_Ug , Your mobile money service has issues.  It's bouncing all my transactions."   | mobile money |mobile money |
| '@mtnug What is wrong with your internet, the quality keeps worsening, it keeps hiccuping n this is irritating, whenever am around kireka, no matter where I sit in kireka, internet is poor!'| internet| Data|
| "Bt u MTN Uganda guys muyina kyemunonyako @mtnug just bought ma minutes to make some important call nw everything shows 'other error"| minutes|calls|
|'@africellUG u guys used to have to have best customer care helpline..what happened, just called and I was dropped, then called again they picked but ur agents were just having a conversation in the background... Disappointed..'"|customer care|customer service|
| '@Airtel_Ug Has good service and good reliable network!' | network | Network |

### Sentiment (Polarity) Annotation ###

In sentiment annotation, the goal is to identify the feeling or attitude being conveyed towards the target#aspect pair through a post on social media. Some posts express an obvious positive or negative sentiment or attitude towards target#aspect pair, and we need to select such clear and unambiguous cases.

T-ABSA is concerned with posts where the speaker expresses their opinion towards an aspect or aspects of a target entity (telcom). Most work in sentiment analysis (SA) considers three sentiment categories of Positive, Negative, and Neutral. In social media posts, it's uncommon for a social media post to mention an aspect of an entity without expressing any sentiment. This is why the sentiment class Neutral is not considered in this sentiment annotation task.

For each selected target-entity\#Aspect pair in a post, annotators are required to select a sentiment from the set P = {Positive, Negative}.

Examples of positive and negative sentiment expressions towards respective target#Aspect pairs.

| Opinion | Target-Aspect pairs | Sentiment |
| :---         |     :---:      |          ---: |
| '@mtnug What is wrong with your internet, the quality keeps worsening, it keeps hiccuping n this is irritating, whenever am around kireka, no matter where I sit in kireka, internet is poor!'| MTN\#Data | Negative |
| "Dear @Airtel_Ug , Your mobile money service has issues.  It's bouncing all my transactions."| Airtel\#Mobile Money | Negative |
| '@africellUG Your Mobile internet is off and on' | Africel\#Data | Negative |
| "@africellUG your network has been on emergency since last night. I can't make any make any call." | Africel\#Calls | Negative |
| 'As I was still enjoying my monthly free mbs booom another 1GB from @Airtel_Ug| Airtel\#Data | Positive |
| "@mtnug what's with your network, did u copy airtel?" | MTN\#Data  Airtel\#Data | Negative Negative|
| '@mtnug has been the best network i have used all my life' | MTN\#Network | Positive |
|'@mtnug Simply the Best Network for Calls, Data and Mobile Money| MTN\#Calls MTN\#Data  MTN\#Mobile Money | Positive Positive Positive |
| very affordable network, and well spread. many running promotions and many give backs, so if you are looking for easy and affordable network airtel is the answer | Airtel\#Network | Positive |

### What to skip
We are interested in posts that contain a target entity, aspect and sentiment, if any of these is missing, SKIP IT! If any of the three components is not clear please skip the post.

Posts to skip include the ones in which:

(1) The original meaning is impossible to ascertain without context (maybe because they were accompanied by photos, videos, or posted as replies to other posts):

- Ssese overwhelmed Buvuma - at the Lutoboka play ground on match day two of the  @Airtel_Ug Masaza Cup.
- @ssmusoke @Airtel_Ug You have options. Use them
- @KatumbaKatumb @mtnug Buddy freeze
- @AyellaBryan @mtnug Okey boss
- @mtnug Yes... I have :yum::wink:
- Guntalk city :sunglasses: 
- @benj_amin @mtnug Really :joy::joy::joy::joy:nga that's bad:joy:

(2) Adverts:
These are posts where the telcom company or it's brand ambassadors are promoting the it's services.

- Make your Sunday better by clearing your utility bills conveniently. Dial \*\*# and follow prompts to pay your water bill. Visit to learn more. 
- @mtnug @ChronixxMusic Lets go and skank de sweet yoooooo
- Dancing is food for the soul, good for mental health and wellness. @mtnug in collaboration with  @soulenough are giving back to the patients at  through a zumba dance session. 
- @kamaroma Join @mtnug subscribe to mtn pulse Dia \*\*# and get yourself a ticket
- Calling your friends to turn up for the amazing Xperience of  shouldnt be interrupted or limited. This is possible with the  unlimited calls valid for  hrs Dial \*\*# to activate and talk.  th May is Coming!! Powered By @africellUG

(3) Jokes:
 
Jokes may indicate the opinion of the user but it may be difficult to identify, identifying them is beyond the scope of this annotation task. Therefore the jokes should be skipped.

- @Airtel_Ug we have always been friends.Please forgive my Wewole loan:expressionless:


(4) Inquiries and Responses from the telcom:
- @mtnug @imunanira Its a promotion, right? For how long is it going to run?
- What of shared bundles 
- @AyellaBryan @mtnug You just published you phone number online fwaaaa hmmm
- @AyellaBryan @mtnug hahaha... you will get to learn it the hard way thats certainly things should stay private esp phone numbers tied to social media or online email
- @AyellaBryan @mtnug I had even forgotten the ussd codes, It really had simplified life
- @kyanda_ed Hi Kyanda,Im having a little difficult understanding your challenge. If you could explain little more, I will be able to help.
- @africellUG Most daily bundles can be renewed before the expiry date and have previous and current data  running! Does it apply here?


(5) Posts that are not related to telcos:

- Cardiac arrest almost killed me until I saw Uganda.
- @SirBrightug @mtnug Prudes and feeling self-righteous.

(6) Posts that have mixed sentiment towards the same aspect:

- Good morning @mtnug @MTNza How are you ? I have feedback on the quality of Internet service provided by you to my work place. It can be good, bad and terrible. This Monday morning it's terrible. It's moody. Some days are very good. Thank you so much. Yours faithfully: customer.


