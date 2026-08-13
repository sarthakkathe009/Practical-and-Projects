from pprint import pprint

# A1. Hard‑coded catalogue (list of dictionaries)
movies = [
    {"title": "Inception",        "year": 2010, "genre": "Sci‑Fi",   "rating": 8.8},
    {"title": "Interstellar",     "year": 2014, "genre": "Sci‑Fi",   "rating": 8.6},
    {"title": "The Dark Knight",  "year": 2008, "genre": "Action",   "rating": 9.0},
    {"title": "Parasite",         "year": 2019, "genre": "Thriller", "rating": 8.5},
    {"title": "Whiplash",         "year": 2014, "genre": "Drama",    "rating": 8.5},
    {"title": "The Godfather",    "year": 1972, "genre": "Crime",    "rating": 9.2},
    {"title": "Toy Story",        "year": 1995, "genre": "Animation","rating": 8.3},
    {"title": "Spirited Away",    "year": 2001, "genre": "Animation","rating": 8.6},
    {"title": "The Matrix",       "year": 1999, "genre": "Sci‑Fi",   "rating": 8.7},
]

# A2. Pretty‑print the dataset
pprint(movies)

recent_titles = {m["title"] for m in movies if m["year"] > 2010}
print(recent_titles)

has_perfect = any(m["rating"] == 10.0 for m in movies)
print("Perfect‑score exists?:", has_perfect)

index_by_title = {m["title"]: m for m in movies}
print(index_by_title)
print("Lookup example – Inception →", index_by_title["Inception"])

grouped = {}
for m in movies:
    genre = m["genre"]
    if genre not in grouped:
        grouped[genre] = []
    grouped[genre].append(m)

count_by_genre = {g: len(lst) for g, lst in grouped.items()}
print("Movies per genre:", count_by_genre)

avg_rating_by_genre = {
    g: round(sum(m["rating"] for m in lst)/len(lst),1)
    for g, lst in grouped.items()
}

top_overall = max(movies, key=lambda m:m["rating"])

top_by_genre = {
    g: max(lst, key=lambda m:m["rating"])["title"]
    for g, lst in grouped.items() 
}

print("Average rating by genre:", avg_rating_by_genre)
print("Top movie overall:", top_overall["title"], "→", top_overall["rating"])
print("Top movie in each genre:", top_by_genre)


new_movie = {"title": "Dune: Part Two", "year": 2024, "genre": "Sci‑Fi", "rating": 8.9}
movies.append(new_movie)

# E2. Sync index_by_title
index_by_title[new_movie["title"]] = new_movie

print("Added movie:", new_movie)
print("Total catalog size:", len(movies))

def banner(text: str):
    print("\n" + "=" * (len(text) + 4))
    print(f"  {text}")
    print("=" * (len(text) + 4))

# Simple dashboard
banner("Mini‑Movie Dashboard")

print("Total films :", len(movies))
print("Genres      :", ", ".join(sorted(grouped)))

print("\nRecent releases:", recent_titles)

print("\nAverage rating by genre:")
for g, avg in avg_rating_by_genre.items():
    print(f"  {g:<10} → {avg}")

print("\nTop picks by genre:")
for g, title in top_by_genre.items():
    print(f"  {g:<10} → {title}")

print("\nTop film overall :", top_overall['title'], '→', top_overall['rating'])