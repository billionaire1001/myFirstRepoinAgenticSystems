import pandas 
import requests

def fetch_and_clean_posts():
    # Fetch post data from API
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(
        url, timeout=10
    )
    response.raise_for_status()  # Raise an error on bad response
    posts = response.json()

    # Convert to DataFrame
    data = pandas.DataFrame(posts)

    # Basic cleaning
    data = data.rename(columns={'userId': 'user_id'})
    if 'id' in data.columns:
        data = data.drop(columns=['id'])

    return data

if __name__ == "__main__":
    df = fetch_and_clean_posts()
    print("First 5 rows of cleaned DataFrame:")
    print(df.head())

