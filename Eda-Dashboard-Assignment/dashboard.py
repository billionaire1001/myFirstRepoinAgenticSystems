import streamlit 
import plotly.express

# Import fetch_and_clean_posts from fetch_data.py
from fetch_data import fetch_and_clean_posts

streamlit.set_page_config(page_title="Post Data Dashboard", layout="centered")

streamlit.title("Simple Post Data Dashboard")

# Fetch and clean data
@streamlit.cache_data
def load_data():
    return fetch_and_clean_posts()

df = load_data()

# --- Exploratory Analysis ---

# Count posts per user
posts_per_user = df.groupby("user_id").size().reset_index(name="post_count")

# Add post_length column
df["post_length"] = df["body"].astype(str).apply(len)

# --- Streamlit Dashboard ---

streamlit.header("Dataset Preview")
streamlit.dataframe(df.head())

# Visualization: Posts Per User
streamlit.header("Number of Posts per User")
bar_chart = (
    posts_per_user
    .set_index("user_id")["post_count"]
)
streamlit.bar_chart(bar_chart)

# Visualization: Distribution of Post Length
streamlit.header("Post Length Distribution")
fig = plotly.express .histogram(df, x="post_length", nbins=20, title="Post Length Distribution")
streamlit.plotly_chart(fig)

streamlit.markdown("""
---
**Dashboard Features:**
- Data fetched from a public API and cleaned.
- Number of posts per user visualized as a bar chart.
- Distribution of post lengths shown as a histogram.
""")
