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
- `training_data.csv` – Contains **id, file_content, and labels** for model training.  
- `validation_data.csv` – Contains **id, file_content, and labels** for model validation.  
- `testing_data.csv` – Contains **id and file_content only**, for model evaluation.  

Each row in the dataset corresponds to a single 911 call. The goal is to develop a model that accurately classifies calls into their respective emergency categories. 
