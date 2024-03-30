# Football Player Analysis Project

## Overview
This project focuses on conducting comprehensive data analysis on football player statistics sourced from TransferMarkt and FBRef. The primary objective is to provide recommendations for potential player acquisitions based on their performance metrics and market valuation. The project encompasses various stages including data scraping, cleaning, merging, analysis, and prediction using machine learning techniques.

## Process
1. **Data Scraping**: Scraping data from multiple websites including TransferMarkt and FBRef to gather comprehensive player statistics and market information.
2. **Data Cleaning and Merging**: Cleaning the scraped data to ensure consistency and accuracy, followed by merging relevant tables to create a unified dataset for analysis.
3. **Data Analysis**: Performing in-depth analysis on player statistics to identify key performance indicators and trends that can influence player valuation and potential.
4. **Data Visualization**: Creating a dashboard to show key performance indicators using Tableau [Premier League Dashboard](https://public.tableau.com/views/PremierLeagueDashboard_17114368574660/PremierLeagueDashboard?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

5. **Recommendation System**: Utilizing cosine similarity to recommend similar players based on selected criteria, aiding decision-making in player acquisitions.
6. **Market Value Prediction**: Implementing machine learning algorithms to predict the market value of players based on their performance metrics and market trends.

## Repository Structure
- `analysis/`: Jupyter notebooks detailing the analysis and recommendation similar players.
- `data/`: Contains the raw and processed datasets.
- `models/`: Saved machine learning models for market value prediction.
- `scraping and preprocessing/`: Jupyter notebooks detailing the data scraping and cleaning.
- `valuation/`: Jupyter notebooks detailing the predicting valuation using machine learning.
- `streamlit/`: Code to make streamlit.
- `README.md`: Comprehensive documentation detailing project overview, processes, and instructions.

## Usage
1. Clone the repository.
2. Install the required dependencies listed in `requirements.txt`.
3. In the main folder, run the following command in your terminal:

```bash
streamlit run streamlit/app.py
```
You can access the Streamlit app [here](https://premierleaguerecommend.streamlit.app/).

## Future Improvements
- There are numerous additional statistics that could be incorporated for analysis and machine learning purposes.
- The RMSE (Root Mean Square Error) outcome is notably poor, typically ranging between 15-18.
- Furthermore, the training dataset utilized for predicting player valuations comprises only the top 100 highest-valued players in the Premier League. This limitation is problematic as the model may only accurately predict valuations within the range of the top 100 players. Additionally, it's observed that the model consistently overvalues players who, in reality, possess lower valuations.

## Acknowledgements
Special thanks to TransferMarkt and FBRef for providing valuable football player statistics.
