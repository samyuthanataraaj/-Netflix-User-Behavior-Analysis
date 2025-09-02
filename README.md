

## Project Overview

This project analyzes **Netflix user viewing habits** to uncover insights about content preferences and behavior patterns.
By examining **genres, viewing time, binge-watching behavior, and ratings**, we aim to understand how users interact with Netflix content.

## Problem Statement

Streaming services want to understand what content users prefer in order to improve recommendations and engagement.

##  Objective

* Analyze Netflix dataset of viewing habits
* Identify **top genres** and **viewing trends**
* Measure **watch hours per user**
* Visualize **binge behavior**
* Compare **ratings vs. genres**

##  Dataset

The dataset contains the following columns:

| Column Name                    | Description                               |
| ------------------------------ | ----------------------------------------- |
| week                           | Week of observation                       |
| category                       | Category type (Film, Series, etc.)        |
| weekly\_rank                   | Rank of the show for the week             |
| show\_title                    | Name of the show                          |
| season\_title                  | Season details (if applicable)            |
| weekly\_hours\_viewed          | Total hours viewed in a week              |
| runtime                        | Duration of content                       |
| weekly\_views                  | Total number of views in a week           |
| cumulative\_weeks\_in\_top\_10 | Number of weeks the show stayed in Top 10 |
| is\_staggered\_launch          | Whether episodes were launched gradually  |
| episode\_launch\_details       | Launch details of episodes                |

## Requirements

* Python 3.8+
* Libraries:

  ```bash
  pip install pandas matplotlib seaborn
  ```

## Expected Outcome

* 📈 Behavioral insights into content preferences
* 🔍 Identification of binge-watching patterns
* 🎭 Genre-based popularity and engagement trends
* 🎥 Recommendations for content strategies

## How to Run

1. Clone this repository

   ```bash
   git clone https://github.com/your-username/netflix-user-behavior.git
   cd netflix-user-behavior
   ```
2. Place your dataset file as `netflix.csv` in the project folder.
3. Run the analysis script:

   ```bash
   python netflix.py
   ```

##  Visualizations

The script generates:

* Top genres by watch hours
* Weekly trends of views and hours watched
* User binge-watching patterns
* Genre vs ratings comparison

## Future Improvements

* Integrate with **machine learning models** for user recommendation
* Add **sentiment analysis** using reviews
* Extend dataset to include more user demographics

