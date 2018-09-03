import os
import pickle
from last_fm_recommender.settings import BASE_DIR
import pandas as pd


def get_artist_recommendations(artist_name, number=5):
    model_path = os.path.join(BASE_DIR, "recommender_app/ml_model/nn_recommender.sav")
    data_path = os.path.join(BASE_DIR, "recommender_app/ml_model/wide_artist.csv")
    data = pd.read_csv(data_path).pivot(index='artist_name', columns='user_id',
                                        values='artist_total_plays').fillna(0)
    nn_model = pickle.load(open(model_path, 'rb'))
    dist, indices = nn_model.kneighbors(data.ix[artist_name].values.reshape(1, -1), n_neighbors=number+1)
    results = []
    for x in range(1, len(dist.flatten())):
        results += [data.index[indices[0][x]]]
    print(results)
    return results
