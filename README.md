# Classifying 911 Calls
### Sensitive Content Disclaimer
> [!WARNING] 
> This challenge requires users to work with 911 call transcripts, which contains sensitive and potentially distressing/triggering content related to, but not limited to emergency incidents, accidents, crimes, and medical emergencies. By participating, you acknowledge the nature of the dataset and also to take breaks or seek support if you feel uncomfortable at any stage of this challenge.

## Challenge  

The dataset contains transcripts of 911 calls. They are made available in the following files:  

- `training_data.csv`  
- `testing_data.csv`  
- `validation_data.csv`  

The challenge requires users to create a model that can predict which category a 911 call falls into based on its content. For this challenge, we label calls as requesting **'Law_Enforcement', 'Fire_Department'**, or **'Paramedics'**. If a call does not fit any of these categories, it is labeled as **'Non_Emergency'.**
