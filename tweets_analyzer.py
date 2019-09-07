import pandas as pd
import numpy as np
from helper_functions import clean_tweet, extract_locations
from matplotlib import pyplot as plt

def create_cindy_df():
    cindy_df = pd.read_json('data/Vote Cindy.json', orient='records')
    cindy_df['clean_tweet'] = cindy_df['tweet'].apply(lambda x: clean_tweet(x))
    cindy_df['housemate_name'] = 'Cindy'
    cindy_df.drop_duplicates(subset=['name'], keep='first', inplace=True)
    return cindy_df

def create_esther_df():
    esther_df = pd.read_json('data/Vote Esther.json', orient='records')
    esther_df['clean_tweet'] = esther_df['tweet'].apply(lambda x: clean_tweet(x))
    esther_df['housemate_name'] = 'Esther'
    esther_df.drop_duplicates(subset=['name'], keep='first', inplace=True)
    return esther_df

def create_frodd_df():
    frodd_df = pd.read_json('data/Vote Frodd.json', orient='records')
    frodd_df['clean_tweet'] = frodd_df['tweet'].apply(lambda x: clean_tweet(x))
    frodd_df['housemate_name'] = 'Frodd'
    frodd_df.drop_duplicates(subset=['name'], keep='first', inplace=True)
    return frodd_df

def create_sirdee_df():
    sirdee_df = pd.read_json('data/Vote Sir Dee.json', orient='records')
    sirdee_df['clean_tweet'] = sirdee_df['tweet'].apply(lambda x: clean_tweet(x))
    sirdee_df['housemate_name'] = 'Sir Dee'
    sirdee_df.drop_duplicates(subset=['name'], keep='first', inplace=True)
    return sirdee_df

def create_tacha_df():
    tacha_df = pd.read_json('data/Vote Tacha.json', orient='records')
    tacha_df['clean_tweet'] = tacha_df['tweet'].apply(lambda x: clean_tweet(x))
    tacha_df['housemate_name'] = 'Tacha'
    tacha_df.drop_duplicates(subset=['name'], keep='first', inplace=True)
    return tacha_df

def create_venita_df():
    venita_df = pd.read_json('data/Vote Venita.json', orient='records')
    venita_df['clean_tweet'] = venita_df['tweet'].apply(lambda x: clean_tweet(x))
    venita_df['housemate_name'] = 'Venita'
    venita_df.drop_duplicates(subset=['name'], keep='first', inplace=True)
    return venita_df

def join_dfs():
    cindy_df = create_cindy_df()
    esther_df = create_esther_df()
    frodd_df = create_frodd_df()
    sirdee_df = create_sirdee_df()
    tacha_df = create_tacha_df()
    venita_df = create_venita_df()

    frames = [cindy_df, esther_df, frodd_df, venita_df, sirdee_df, tacha_df]

    housemates_df = pd.concat(frames, ignore_index=True)
    return housemates_df

def analyze():
    housemates_df = join_dfs()
    # Number of Fans by Housemate
    fans_by_housemate = housemates_df.groupby('housemate_name')['name'].count().reset_index()
    fans_by_housemate.columns = ['housemate', 'no_of_fans']

    # Locations of Fans by Housemate
    housemates_df['location'] = housemates_df['location'].apply(lambda location: extract_locations(location))
    fans_by_location = pd.DataFrame(housemates_df.groupby('housemate_name')['location'].value_counts().rename('count')).reset_index()

    # Average no of followers of fans by housemate
    followers_of_fans_by_hm = housemates_df.groupby('housemate_name')['followers'].mean().reset_index()
    followers_of_fans_by_hm.columns = ['housemate', 'average_no_of_followers_of_fans']

    return (fans_by_housemate, fans_by_location, followers_of_fans_by_hm)

def plot_graphs():
    analysis_details = analyze()
    fans_by_housemate, fans_by_location, _ = analysis_details

    #Bar Chat for numbers of fans of housmates
    fig1, ax1 = plt.subplots()
    ax1.bar(fans_by_housemate['housemate'], fans_by_housemate['no_of_fans'], label='fans by housemate')
    ax1.set_xlabel('Housemate')
    ax1.set_ylabel('Number of twitter Fans')
    ax1.set_title('Number of Twitter Fans by Housemate')

    # Bar Chart for locations of fans of housemates
    ax2 = fans_by_location.pivot(index='housemate_name', columns='location', values='count').T.plot(kind='bar', label='fans by location')
    ax2.set_xlabel('Locations')
    ax2.set_ylabel('Number of Twitter Fans')
    ax2.set_yticks(np.arange(0, 300, 15))
    ax2.set_title('Location of Twitter Fans of Housemates')
    ax2.figure.set_size_inches(10, 17)

    list_of_figures = [plt.figure(i) for i in plt.get_fignums()]
    return list_of_figures

if __name__ == "__main__":
    plot_graphs()
    