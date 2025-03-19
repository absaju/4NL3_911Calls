# Classifying 911 Calls
### Sensitive Content Disclaimer
> [!WARNING] 
> This challenge requires users to work with 911 call transcripts, which contains sensitive and potentially distressing/triggering content related to, but not limited to emergency incidents, accidents, crimes, and medical emergencies. By participating, you acknowledge the nature of the dataset and also to take breaks or seek support if you feel uncomfortable at any stage of this challenge.

## Challenge  
The challenge requires users to create a model that can predict which category a 911 call falls into based on its content. For this challenge, we label calls as requesting **'Law_Enforcement', 'Fire_Department'**, or **'Paramedics'**. If a call does not fit any of these categories, it is labeled as **'Non_Emergency'.**

## Dataset Information  

The dataset consists of **911 call transcripts** provided in CSV format.

### Columns  
- `id`: A unique identifier for each call.  
- `file_content`: The textual transcript of the 911 call.  
- `labels`: The emergency category assigned to the call (**'Law_Enforcement', 'Fire_Department', 'Paramedics', 'Non_Emergency'**). 

### Files Included  
- `training_data.csv` – Contains **597 data points** with **id, file_content, and labels** columns for model training.   
- `validation_data.csv` – Contains **75 data points** with **id, file_content, and labels** columns for model validation.  
- `testing_data.csv` – Contains **73 data points** with **id and file_content** columns for model evaluation.  

Each row in the dataset corresponds to a single 911 call. The goal is to develop a model that accurately classifies calls into their respective emergency categories. 

## Baseline Models

`baseline_models.ipynb` file contains two baseline models. It also contains code to get started with the challenge. For the baselines we have used two models, one using Majority Baseline and the next using logical regression. The models have achieved an accuracy of 0.56 and 0.53 respectively. Your challenge is to beat these baseline models.

## Submission

You should submit a csv file `submission.csv` containing columns `id`, `file_content` and `labels`. This is seen as an example in `baseline_models.ipynb` file. These `labels` should be your models prediction for each datapoint in the `testing.csv` file. 

## Evaluation

Submissions will be evaluated based on:

- **Weighted F1-score (Primary Metric)**: This metric balances precision and recall across all classes, accounting for class imbalance.
- The leaderboard ranks participants based on their **Weighted F1-score**.
![image](https://github.com/user-attachments/assets/ee9de8eb-f1af-4f63-af63-d9681a5b29d9)

Precision is the ratio of true positives to the sum of true positives and false positives, while recall is the ratio of true positive to the sum of true positive and false negative.

## Terms

The challenge is posted as an assignment for course COMPSCI 4NL3, Winter 2025, McMaster University

Dataset was transcibed from the following Kaggle Dataset : !(https://www.kaggle.com/datasets/louisteitelbaum/911-recordings)

