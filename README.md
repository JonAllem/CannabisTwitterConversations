# CannabisTwitterConversations
The goal of this study was to identify and describe cannabis-related topics of conversation on Twitter to inform the public health community.

The full notebook can be viewed [here](https://nbviewer.jupyter.org/github/JonAllem/CannabisTwitterConversations/blob/master/Source/Analysis.ipynb) using Jupyter's notebook viewer.

## Data Preparation

`Analysis.ipynb` is the main notebook which containing the final results. In order to run this notebook, the data needs to be prepared (normalized, removal of spam, etc.) beforehand. The following sections details each script that needs to be run to prepare the data:

1. `Data/DataLoader.linq`: This is the script we used to load the tweets from our Twitter database. You can modify the script to use your own database.
2. `Source/Sample.ipnb`: Due to the large number of cannabis related tweets our found in our database, we sample tweets instead of running our analysis on all tweets. This notebook generates the final sample and also documents our sampling technique.
3. `Data/botscore.py`: This script should be run in order to generate botscores for each Twitter user in our dataset. The result of the script is stored in `Data/BotScores`.
4. `Data/clean_data.py`: This script is run on the output of the previous script, and normalizes the tweets. The cleaned data is stored as Python pickle files.
5. `Analysis.ipynb`: This is the notebook that contains the actual analysis.
