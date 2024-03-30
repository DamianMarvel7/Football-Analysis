import streamlit as st
import numpy as np
import pandas as pd
import pickle

def recommend_similar_players(player_name,similarity_matrix, df,top_n=5):
    if player_name not in df['Player'].values:
        return f"Error: Player '{player_name}' not found in the dataset."
    
    player_index = df.index[df['Player'] == player_name][0]
    similar_players_indices = similarity_matrix[player_index].argsort()[-top_n-1:-1][::-1]
    similar_players = df.iloc[similar_players_indices]['Player'].tolist()
    return similar_players

def predict_valuation(df,name,model):
    df=df[df['Player']==name]
    df = df.select_dtypes(include=['float64', 'int64'])
    result = model.predict(df)
    return result
    # print(name,'valuation: ', result[0])

def main():
    df = pd.read_csv('../data/all_stats.csv')
    
    with open('../model.pkl', 'rb') as file:
        model = pickle.load(file)
    # Title of the web app
    st.title("Player Recommendation")
    st.write("Write the player name and we will give you recommendation to the most similar player and the valuation")

    # User input for their name
    # input_player = st.text_input("Enter the player name")
    
    selected_team = st.selectbox("Select a Team", df['Team'].unique())
    filtered_df = df[df['Team'] == selected_team]
    input_player = st.selectbox("Select a Player", filtered_df['Player'])
    
    similarity_matrix = np.loadtxt('../data/player_similarity.csv', delimiter=',')
 
    # print(f"Players similar to {input_player}: {similar_players}")

    # Greeting message based on the user's input
    if st.button("Recommend"):
        similar_players = recommend_similar_players(input_player,similarity_matrix,df)
        st.write(f"Players similar to {input_player}:")
        for player in similar_players:
            valuation = predict_valuation(df,player,model)[0]
            rounded_valuation = round(valuation,1)
            st.write(f"- {player}, valuation: {rounded_valuation:.1f} million €")

if __name__ == "__main__":
    main()
