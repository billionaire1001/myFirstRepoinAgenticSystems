import pandas 

if __name__ == "__main__":
    df = pandas.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Score": [85, 88, 90, 82, 87],
        "Passed": [True, True, True, False, True],
        "Category": ["A", "B", "A", "B", "A"]
    })
    new_df = df[["Name", "Score"]].copy()
    df_indexed = new_df.set_index("Name")
    # Select a single column
    print("\n--- Names ---")
    print(df["Name"])

    # Select multiple columns into a new DataFrame
    print("\n--- Name and Score DataFrame (new_df) ---")
    print(new_df)

    # Using iloc to retrieve the first three rows
    print("\n--- First three rows of new_df using iloc ---")
    print(new_df.iloc[:3])

    # Using loc with Name as index
    print("\n--- Data for 'Charlie' using .loc with 'Name' as index ---")
    print(df_indexed.loc["Charlie"])

    # Filter rows where Score > 85
    print("\n--- Rows where Score > 85 ---")
    filt_score = df["Score"] > 85
    print(df.loc[filt_score])

    # Filter where Score > 85 and Passed is True
    print("\n--- Rows where Score > 85 AND Passed is True ---")
    filt_both = (df["Score"] > 85) & (df["Passed"])
    print(df.loc[filt_both])

    #  Sort the filtered result in descending order of Score
    print("\n--- Filtered (Score > 85 & Passed) sorted by Score descending ---")
    filtered_sorted = df.loc[filt_both].sort_values(by="Score", ascending=False)
    print(filtered_sorted)

    #  Chained filtering and sorting operation
    print("\n--- Chained: All with Category 'A', sorted by Score descending ---")
    print(df[df["Category"] == "A"].sort_values(by="Score", ascending=False))