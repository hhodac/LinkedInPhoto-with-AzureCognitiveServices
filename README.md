# LinkedInPhoto-with-AzureCognitiveServices
This repository demonstrates how to use Azure Cognitive Services to extract facial sentiments from LinkedIn profile photo.

## Author
Hai Ho Dac | hodachai.91@gmail.com

Date: 18/8/2020

## Project description
A simple Python script to automate login LinkedIn profile and perform following tasks:
1. Login to my personal LinkedIn profile.
2. Access LinkedIn profile that I want to view.
3. Get the profile photo url.
4. From the image url, detect the face and blur the background using OpenCV.
   Output blurred image is named after the profile name.
5. Apply 2 different sentiment analytic models:
   - Personal developed emotion detection model.
     Detect 'smile', 'sentiment' and 'confidence level' of the 'sentiment.
   - Microsoft Azure cognitive service face API.
     Detect 'gender', 'age', 'smile intensity', 'sentiment' and 'confidence level' of the 'sentiment.
     
     
## Directory structure
```
project
|--evaluating
|   |-azure_model.py
|   |-Azure_CognitiveServices_Resources.png
| 
|--processing
|   |--data_processing.py
|   |--linkedin_scraper.py
|   
|--main.py
|--requirements.txt
|--README.md
|--chromedriver_mac64.zip
```