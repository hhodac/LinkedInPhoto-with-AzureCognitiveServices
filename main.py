"""
Author: Hai Ho Dac - hodachai.91@gmail.com
Date: 18/8/2020
Project description:
A simple Python script to automate login LinkedIn profile and perform following tasks:
1. Login to my personal LinkedIn profile.
2. Access LinkedIn profile that I want view.
3. Get the profile photo url.
4. From the image url, detect the face and blur the background using OpenCV.
   Output blurred image is named after the profile name.
5. Apply Azure Cognitive Services' facial sentiment analysis models to detect
'gender', 'age', 'smile intensity', 'sentiment' and 'confidence level' of the 'sentiment.
"""
from processing.data_processing import blur_background
from processing.linkedin_scraper import linkedin_crawler
from evaluating.azure_model import azurecs_face

# Step 1: Login to personal LinkedIn profile
print("Step 1: Login to personal LinkedIn profile.")
crawler = linkedin_crawler()
crawler.input_username_password()
crawler.set_browser_connection()
crawler.login()
print()

# Step 2: Access LinkedIn profile that I want view
print("Step 2: Access LinkedIn profile that I want view.")
profile_name = 'haiho91'
profile_page = crawler.search_profile(profile_name)
print("Profile name: " + profile_name)
print()

# Step 3: Get the profile photo url
print("Step 3: Get the profile photo url.")
img_src = crawler.get_profile_image_url(profile_page)
print("Profile photo url: " + img_src)
print()

# Step 4: Blur the profile photo
print("Step 4: Blur the profile photo.")
blur_background(img_src, profile_name)
print("Blurred photo file name: " + profile_name + "_blurred.png")
print()

# Step 5: Apply sentiment analysis
print("Step 5: Apply Azure Cognitive Service sentiment analysis.")
## Azure model:
azurecs_face(img_src)
print()

# Quit browser
crawler.quit_browser()