
# coding: utf-8

# A data science project consists of several phases. In this module, we introduce the first phase: **EDA (exploratory data analysis)**. EDA is first for good reason, because every subsequent phase of any data science project depends on it for success. As a data scientist candidate, it's essential to have a strong command of EDA before moving on to more advanced topics. 
# 
# As the name suggests, EDA is the process of exploring data to discover insights, identify patterns, establish relationships and trends, and test assumptions. The best ally a data scientist can have is the data itself. However, getting to know the data takes patience, openness, and attention. **EDA is the process of letting the data speak for itself**.
# 
# When working with a dataset, our objective might be something like:
# 
# * predicting next month's housing prices.
# * predicting customer churn
# * predicting a plant's electricity consumption for tomorrow.
# * building a mobile app that can tag people in a photo.
# * implementing a recommendation system for a streaming-video website.
# 
# All the tasks listed above can be accomplished by one or more data scientists if the relevant, clean datasets are provided. However, like money, clean datasets do not grow on trees! Usually these data come from raw, messy formats. 
# 
# In order to get the most out of the data, we need to eliminate irrelevant and potentially misleading parts while also transforming them into a format we can easily work with. Editing is a crucial aspect of EDA—improving the **quality of the data**. When we talk about improving data quality, we usually mean **data cleaning**. This process is also referred to as **data munging** or **data wrangling**. 
# 
# As we clean, we begin to notice the useful **features** that are associated with our **target**. This process, known as **data exploration**, analyzes the relationships between features as well as between the features and the target. After we have cleaned and explored our data, identifying and creating useful features is called **feature engineering**.
# 
# EDA, then, is the combination of data cleaning, data exploration, and feature engineering. Let's recap this process below. 

# 
# # What is exploratory data analysis?
# 
# Exploratory data analysis is the building block of the data-science pipeline. Before moving into the modeling phase, we need to understand the relationships in our data. The more we understand our data, the more we can successfully identify the most useful features that will help our models achieve the best performance. 
# 
# We conceptualize EDA as an iterative process consisting of three steps. The figure below depicts these steps and how the iteration occurs:
# 
# ![](assets/eda.png)
# 
# 1. **Data cleaning**: This is the first step of EDA. We take a raw dataset and eliminate problems which would prevent us from further analysis. 
# 
# 2. **Data exploration**: The second step is exploring the data to discover relationships and features. We will explore the data using both statistics and data visualization. If we identify new problems in the data during exploration, we will go back to the cleaning phase and eliminate these identified problems.
# 
# 3. **Feature engineering**: The final step of EDA is the feature engineering, where we select the most useful features or create new features from the existing ones. This phase leads us to the next phases of the data-science pipeline. However, if we detect some problems with the data in this phase, we return to the data-cleaning step. Moreover, if we transform existing features or create new ones, we will need to go back to the data-exploration phase to investigate them.
# 
# In the following checkpoints, we will consider each step of EDA more closely and then demonstrate them in Python. But first, walk through the below drills to confirm your understanding of the basics of EDA.  

# ## Assignment
# 
# To complete this assignment, submit a link to a gist file or enter text directly below with your answers to the following:
# 
# 1. What is the goal of EDA (exploratory data analysis)?
# 2. Suppose that you are given a dataset of customer product reviews for an e-commerce company. Each review is scored as a Likert-style survey item where 1 indicates a negative sentiment about the product and a 5 is positive. These reviews are collected on the company's website.
#     a. What problems do you expect to find in the raw data? 
#     b. If your task is to build features that give information about customer sentiments, how would you approach this task and what kind of methods would you apply to accomplish it?
#     c. Try to identify some potentially useful features that you might derive from the raw data. How would you derive them and how would you assess the usefulness of those features?
#     
# Submit your work below, and plan on discussing with your mentor. You can also take a look at these [example solutions](https://github.com/Thinkful-Ed/data-201-assignment-solutions/blob/master/model_prep_exploratory_data_analysis/what_is_exploratory_data_analysis_solution.ipynb).

# 1)
# EDA is for us to understand the dataset better so that we can develop features base on its characteristics. 
# 
# 2) 
# 
# a. The biased of the data. Customers tend to complain than compliment...that means we will generally have more low reviews then higher reviews. Plus, comment text is usually hard to process for sentiment analysis due to it's not regulated in stable and measurable standards. 
# 
# b. I will split the comments into each word, then group 'WORDS' into either 'positive' or 'negative' group. We can count how many times the positive and negative words shows then score each comment into different levels of feelings.
# 
# c. Possible positive words are like 'works', 'nice', 'recommended'.. etc. We can process it in different ways; words itself, or word bag include the vocabulary in front or after. Also it will be useful to add the points (stars) it comes with. 
