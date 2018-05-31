import numpy as np
from model import generate_recommendations

client_id = 3008756
already_rated = [32261,26617,52041,30764,82408,94590,81097,71491,9123,172]
k = 5
user_map = np.load("tmp/model/user.npy")
item_map = np.load("tmp/model/item.npy")
row_factor = np.load("tmp/model/row.npy")
col_factor = np.load("tmp/model/col.npy")

user_idx = np.searchsorted(user_map, client_id)
user_rated = [np.searchsorted(item_map, i) for i in already_rated]
print(user_rated)

recommendations = generate_recommendations(user_idx, user_rated, row_factor, col_factor, k)

community_recommendations = [item_map[i] for i in recommendations]
print(community_recommendations)
