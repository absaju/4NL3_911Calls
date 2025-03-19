# Classifying 911 Calls
### Sensitive Content Disclaimer
> [!WARNING] 
> This challenge requires users to work with 911 call transcripts, which contains sensitive and potentially distressing/triggering content related to, but not limited to emergency incidents, accidents, crimes, and medical emergencies. By participating, you acknowledge the nature of the dataset and also to take breaks or seek support if you feel uncomfortable at any stage of this challenge.

### Challenge
The dataset contains transcripts of 911 calls. They are made available in the following files
- training_data.csv
- testing_data.csv
- validation_data.csv
The challenge requires users to create a model that can predict which category a 911 call falls into given the calls content. For this challenge, we label calls as requesting for 'Law_Enforcement', 'Fire_Department' or 'Paramedics'. If the calls fit none of these categories we label it as 'Non_Emergency'.
