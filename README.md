To do: 
outlines in detail how you will go from the output of NLPScholar to your evaluation metrics / table/ figures.

1) Grab the predictions.tsv that would be generated by the "evaluate" mode under "textclassification" based on the training data. 
   
2) Write code similar in part 2 of hw2 such that I should run/modify code that I implemented to read from the predictions. The generated model should incorporate 3 target/label in terms of each row, based on the 3 labels that I set for my data. The accuracy score could be calculated by we automating the process of going through the entire prediction file, group the rows by the actual categories (true, fake, satire). In this case we would be expected to have 3 separate predictions. For each prediction, we loop through each row to see how many times our model is able to correctly predict the classification of the given news article title. We compute the accuracy by the count/total number of rows in the 3 separate data. After that, we would be able to report a dictionary like the format of {"positive": 83%, "negative": 75%, "satire": 50%}. 
   
3) After doing so, reinforce the experiemnt/research by including some comparative fine-tunned models, train them, reiterate the entire process and compare the accuracy score such that we would be able to measure and analyze how well different models trained on the data would be able to identify whether a given news article in terms of their topic is supposed to be fake, satire, or true; and also which of the three labels are our model trained on the data is doing best at. 

4) Summarize our findings, create graphical representation/figure to help visualization of our data.