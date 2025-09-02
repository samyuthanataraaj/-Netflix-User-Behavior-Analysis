
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\tamilanskills\project6\netflix.csv", encoding="ISO-8859-1")


print("Dataset Preview:")
print(df.head())


genre_hours = df.groupby("category")["weekly_hours_viewed"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
genre_hours.plot(kind="bar", color="skyblue")
plt.title("Top Genres by Weekly Hours Viewed")
plt.xlabel("Genre")
plt.ylabel("Total Weekly Hours Viewed")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_shows = df.groupby("show_title")["weekly_views"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_shows.plot(kind="barh", color="orange")
plt.title("Top 10 Shows by Weekly Views")
plt.xlabel("Total Views")
plt.ylabel("Show Title")
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(df["runtime"], df["weekly_hours_viewed"], alpha=0.6, c="green")
plt.title("Binge Behavior: Runtime vs Weekly Hours Viewed")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Weekly Hours Viewed")
plt.tight_layout()
plt.show()


weekly_trends = df.groupby("week")["weekly_hours_viewed"].sum()

plt.figure(figsize=(12, 6))
weekly_trends.plot(kind="line", marker="o", color="purple")
plt.title("Weekly Viewing Trends on Netflix")
plt.xlabel("Week")
plt.ylabel("Total Weekly Hours Viewed")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


if "ratings" in df.columns:
    genre_ratings = df.groupby("category")["ratings"].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    genre_ratings.plot(kind="bar", color="red")
    plt.title("Average Ratings by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\nAnalysis Completed ✅")
