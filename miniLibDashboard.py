from pprint import pprint

books = [
    {"title": "1984",               "author": "George Orwell",   "year": 1949,
     "genre": "Dystopian",   "pages": 328, "rating": 9.2},
    {"title": "The Hobbit",         "author": "J.R.R. Tolkien",  "year": 1937,
     "genre": "Fantasy",     "pages": 310, "rating": 8.9},
    {"title": "Sapiens",            "author": "Yuval Noah Harari","year": 2011,
     "genre": "Non‑Fiction", "pages": 498, "rating": 8.6},
    {"title": "Dune",               "author": "Frank Herbert",   "year": 1965,
     "genre": "Sci‑Fi",      "pages": 412, "rating": 9.0},
    {"title": "The Catcher in the Rye","author": "J.D. Salinger","year": 1951,
     "genre": "Classic",     "pages": 277, "rating": 7.8},
    {"title": "The Martian",        "author": "Andy Weir",       "year": 2014,
     "genre": "Sci‑Fi",      "pages": 369, "rating": 8.7},
    {"title": "Educated",           "author": "Tara Westover",   "year": 2018,
     "genre": "Memoir",      "pages": 334, "rating": 8.5},
    {"title": "To Kill a Mockingbird","author": "Harper Lee",    "year": 1960,
     "genre": "Classic",     "pages": 281, "rating": 9.1},
    {"title": "Mistborn",           "author": "Brandon Sanderson","year": 2006,
     "genre": "Fantasy",     "pages": 541, "rating": 8.8},
    {"title": "Project Hail Mary",  "author": "Andy Weir",       "year": 2021,
     "genre": "Sci‑Fi",      "pages": 476, "rating": 9.0},
]

pprint(books)

recent_titles = [b["title"] for b in books if b["year"] > 2000]
print("Recent Titles: ",recent_titles)

has_perfect = any(b["rating"] == 10.0 for b in books)
print("Any perfect‑10 rating?:", has_perfect)

index_by_author = {}
for b in books:
    auth = b["author"]
    index_by_author.setdefault(auth, []).append(b)

print("Books by Andy Weir:", [x["title"] for x in index_by_author["Andy Weir"]])


grouped = {}
for b in books:
    genre = b["genre"]
    if genre not in grouped:
        grouped[genre]=[]
    grouped[genre].append(b)

count_by_genre = {g: len(lst) for g, lst in grouped.items()}
print("Count by genre:", count_by_genre)

avg_pages_by_genre = {
    g:round(sum(b["pages"] for b in lst)/len(lst), 1)
    for g, lst in grouped.items()
}

top_overall = min(
    (b for b in books if b["rating"] == max(b["rating"] for b in books)),
    key=lambda b: b["year"]
)

# Simpler: compute directly
max_rating = max(b["rating"] for b in books)
candidates = [b for b in books if b["rating"] == max_rating]
top_overall = min(candidates, key=lambda b: b["year"])

# D3. Top book per genre
top_by_genre = {}
for g, lst in grouped.items():
    best = max(lst, key=lambda b: (b["rating"], -b["year"]))  # if tie, newer wins
    top_by_genre[g] = best["title"]

print("Average pages by genre:", avg_pages_by_genre)
print("Top overall:", top_overall["title"], "→", top_overall["rating"])
print("Top book per genre:", top_by_genre)

new_book = {"title": "The Silmarillion", "author": "J.R.R. Tolkien",
            "year": 1977, "genre": "Fantasy", "pages": 365, "rating": 8.4}

# Append to list
books.append(new_book)

# Sync author index
index_by_author.setdefault(new_book["author"], []).append(new_book)

print("Added:", new_book["title"])
print("Total books:", len(books))
# Note: grouped & stats would need recomputation to include the new book.

def banner(text):
    print("\n" + "=" * (len(text) + 4))
    print(f"  {text}")
    print("=" * (len(text) + 4))

banner("Mini‑Library Dashboard")

print("Total books:", len(books))
print("Genres     :", ", ".join(sorted(grouped)))

print("\nRecent titles (post‑2000):", recent_titles)

print("\nAverage page count by genre:")
for g, pages in avg_pages_by_genre.items():
    print(f"  {g:<12} → {pages} pages")

print("\nTop book per genre:")
for g, title in top_by_genre.items():
    print(f"  {g:<12} → {title}")

print("\nTop‑rated book overall:", top_overall['title'],
      f"by {top_overall['author']} – rating {top_overall['rating']}")