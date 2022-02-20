---
aliases: confusion matrix, accuracy, specificity, precision, sensitivity
tags: #regression, #data, #ML
---
Back to [[Data Driven World|DDW]]
# Confusion Matrix and Metrics
In Linear Regression, we use the correlation coefficient and some mean square errors as metrics to see if our model fits the data well. What kind of metrics we can use in the case of classification problems?
In this lesson we will use confusion matrix and a few metrics to evaluate our classification model.
## Confusion Matrix
First, we need to separate the dataset into training set and test set. The training set is used to build the model or to train the model. Our model for classification which we discussed in the previous lessson was called Logistic Regression. After we train the model, we would like to measure how good the model is using the **test set**. We can write a table with the result of how many data is predicted correctly and not correctly as shown below.

|actual\predicted| +ve | -ve|
|---|---|---|
|+ve|True +ve|False -ve|
|-ve| False +ve| True -ve|
This is a confusion matrix.
Vertical rows are labels for actual data, horizontal columns are labels for predicted data.
**Positive** case refers to the point of interest.
## Metrics
Knowing the confusion matrix allows us to compute several other metrix that are useful to evaluate the model.
### Accuracy
$$
\text{accuracy} = \dfrac{\text{TP + TN}}{\text{Total Cases}}
$$
"Fraction of the diagonal (correctly predicted) over all the entries"

Given the accuracy we have another metric called the ***error rate***, where
$$\text{error rate} = 1 - \text{accuracy}$$
### Precision
$$\text{precision} = \dfrac{\text{TP}}{\text{Total Predicted Positives}}$$
"Fraction of true positives and all positives"
### Sensitivity
Also known as Recall
$$\text{sensitivity} = \dfrac{\text{TP}}{\text{Total Actual Positives}}$$
"Fraction of correctly predicted postive and sum of correctly predicted positives and wrongly predicted negatives"
### Specificity
Also known as True Negative Rate
$$\text{specificity} = \dfrac{\text{TN}}{\text{Total Actual Negatives}}$$
"Fraction of true negatives over sum of true negatives and false positives"
## Confusion Matrix for Multiple Classes
$$\text{accuracy} = \dfrac{\sum_iM_{ii}}{\sum_i\sum_jM{ij}}$$
$$\text{sensitivity}_i = \dfrac{M_{ii}}{\sum_jM{ij}}$$
$$\text{precision}_i = \dfrac{M_{ii}}{\sum_jM{ji}}$$
**Notice that the indices are swapped for the denominator**. For precision, instead of summing over all the columns, we **sum over all the rows** in column _i_ which is the total cases when class _i_ is _predicted_.