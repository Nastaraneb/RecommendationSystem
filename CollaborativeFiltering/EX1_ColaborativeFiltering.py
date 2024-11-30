import random
import warnings
import math
import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)  # skip pandas Future Warnings
warnings.simplefilter(action='ignore', category=RuntimeWarning)  # skip pandas Runtime Warning

# ---

data = pd.read_csv('ml-latest-small/ratings.csv')
print(f"Number of dataset rows: {data.shape[0]}")
print(data.head(4))

# ----
# User-based Approach
# ----

data = data[:2000]  # Limit Data for fast run


def user_based_sim(rates_by_a, rates_by_b):
    rate_avg_a = rates_by_a.rating.mean()
    rate_avg_b = rates_by_b.rating.mean()

    similar_rated_movies = [x for x in list(rates_by_a.movieId) if x in list(rates_by_b.movieId)]

    if len(similar_rated_movies) == 0:
        return 0

    fraction_top = 0
    fraction_bottom_a = 0
    fraction_bottom_b = 0

    for mid in similar_rated_movies:
        rate_of_a = rates_by_a.where(lambda x: x.movieId == mid).dropna().rating.mean()
        rate_of_b = rates_by_b.where(lambda x: x.movieId == mid).dropna().rating.mean()

        fraction_top += (rate_of_a - rate_avg_a) * (rate_of_b - rate_avg_b)
        fraction_bottom_a += (rate_of_a - rate_avg_a) ** 2
        fraction_bottom_b += (rate_of_b - rate_avg_b) ** 2

    return fraction_top / (math.sqrt(fraction_bottom_a) * math.sqrt(fraction_bottom_b))


def user_based_pred(rates_by_a, p):
    rate_avg_a = rates_by_a.rating.mean()

    N = data.where(lambda x: x.movieId == p).dropna().userId

    fraction_top = 0
    fraction_bottom = 0

    for b in N:
        rates_by_b = data.where(lambda x: x.userId == b).dropna()
        rate_avg_b = rates_by_b.rating.mean()
        rate_of_b = rates_by_b.where(lambda x: x.movieId == p).dropna().rating.mean()

        similarity = user_based_sim(rates_by_a, rates_by_b)
        fraction_top += similarity * (rate_of_b - rate_avg_b)
        fraction_bottom += similarity

    return rate_avg_a + fraction_top / fraction_bottom


userIds = data.userId.unique()
selected_user = random.randint(0, len(userIds) - 1)
selected_user_rates = data.where(lambda x: x.userId == selected_user).dropna()

similar_users = []
for userId in userIds:
    rates_by_userId = data.where(lambda x: x.userId == userId).dropna()
    similar_users.append({
        'userId': userId,
        'similarity': user_based_sim(selected_user_rates, rates_by_userId)
    })

similar_users = sorted(similar_users, key=lambda i: i['similarity'], reverse=True)  # sort

print("--------")
print(f"Top 10 Similar Users to userId:{selected_user} by user-based approach")
idx = 1
for each in similar_users:
    print(f"{idx}. userId:{each['userId']} with sim:{each['similarity']}")
    idx += 1

    if idx > 10:
        break

# -----

print("--------")
print(f"Top 10 Recommended Movies to userId:{selected_user} by user-based approach")

recommended = []
for movieId in data.movieId.unique():
    recommended.append({
        'movieId': movieId,
        'rate': user_based_pred(selected_user_rates, movieId)
    })

recommended = sorted(recommended, key=lambda i: i['rate'], reverse=True)  # sort

idx = 1
for each in recommended:
    print(f"{idx}. movieId:{each['movieId']} with pred:{each['rate']}")
    idx += 1

    if idx > 10:
        break


# ----
# Item-based Approach
# ----


def item_based_sim(a, b):
    users_rated_a = data.where(lambda x: x.movieId == a).dropna()
    users_rated_b = data.where(lambda x: x.movieId == b).dropna()
    user_rated_both = [x for x in list(users_rated_a.userId) if x in list(users_rated_b.userId)]

    if len(user_rated_both) == 0:
        return 0

    fraction_top = 0
    fraction_bottom_a = 0
    fraction_bottom_b = 0

    for uid in user_rated_both:
        user_rate_avg = data.where(lambda x: x.userId == uid).dropna().rating.mean()
        rate_to_a = users_rated_a.where(lambda x: x.userId == uid).dropna().rating.mean()
        rate_to_b = users_rated_b.where(lambda x: x.userId == uid).dropna().rating.mean()

        fraction_top += (rate_to_a - user_rate_avg) * (rate_to_b - user_rate_avg)
        fraction_bottom_a += (rate_to_a - user_rate_avg) ** 2
        fraction_bottom_b += (rate_to_b - user_rate_avg) ** 2

    return fraction_top / (math.sqrt(fraction_bottom_a) * math.sqrt(fraction_bottom_b))


def item_based_pred(rated_by_u, p):
    if len(rated_by_u.movieId) == 0:
        return 0

    fraction_top = 0
    fraction_bottom = 0

    for i in rated_by_u.movieId:
        rate_to_i = rated_by_u.where(lambda x: x.movieId == i).dropna().rating.mean()
        similarity = item_based_sim(i, p)

        fraction_top += similarity * rate_to_i
        fraction_bottom += similarity

    return fraction_top / fraction_bottom


print("--------")
print(f"Top 10 Recommended Movies to userId:{selected_user} by item-based approach")


recommended = []
for movieId in data.movieId.unique():
    recommended.append({
        'movieId': movieId,
        'rate': item_based_pred(selected_user_rates, movieId)
    })

recommended = sorted(recommended, key=lambda i: i['rate'], reverse=True)  # sort

idx = 1
for each in recommended:
    print(f"{idx}. movieId:{each['movieId']} with pred:{each['rate']}")
    idx += 1

    if idx > 10:
        break
