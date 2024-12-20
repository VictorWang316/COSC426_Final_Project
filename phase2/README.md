[Overview]
Here's the update since our last meeting with the professors:

We are managed to update our dataset accordingly with more entries, we mangae to acquire "FAKE", "TRUE", and "SATIRE" news data for 
both the title and the article text. 

We proceed with focusing on news title as our first step to demonstarte next week. 

Our dataset comprises of 60,000+ total entires, we split them accordingly based on 8:1:1 ratio for training, validating, and testing. 

In our data, all column headers are verified, with "textid", "text", "condition"(which we set as default to 'news'), and "label"(or "target" for testing data)

In terms of the label, "0" is classified as true news, "1" is classified as fake news, and "2" is classified as satire news. 

A reference to our true and fake news: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/data

A reference to our satire news: https://www.humortimes.com/123429/thomas-homan-named-bizarre-czar/, https://theonion.com/front-page-archive/

[Progress_Update]
We manage to run training mode via NLPScholar on our data, we are able to attain a valid model from training mode. 

We in turn use the model to run evaluate mode on our testing data, and are able to attain a valid prediction.tsv file. 

[Findings]
We found that the model trained on news title is generally pretty applicable of correctly predicting the associated label with a given news title. Performances diverge in ways that the model is doing a better job at predicting true from fake, whereas satire has less prediction accuracy. This partially validates our study approach of incorporating "satire" as an additional tag for news classification. This also partialy confirms our initial hypothesis that the naming pattern of a title serve a valid purpose. The naming as our current finding suggests are not random or expecting to have a low accuracy. Therefore, we believe we could faithfully proceed with more data as we accept both the news title and news article text(which we already have). 







