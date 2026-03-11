import pandas 


def load_csv(file_name: str) -> pandas.DataFrame:
    column_names = ["age", "score", "label"]
    try:
        df = pandas.read_csv(file_name)
        
        return df[column_names]
    except Exception as e:
        print(f"Error loading file: {e}")
        return pandas.DataFrame(columns=column_names)

def print_output(df: pandas.DataFrame) -> None:
    print(f"First 5 rows:\n{df.head()}\n")
    print(f"Last 5 rows:\n{df.tail()}\n")
    print("Structural info:")
    df.info() 
    print(f"\nSummary statistics:\n{df.describe()}\n")

def process_data(df: pandas.DataFrame) -> None:
    if df.empty:
        print("No data to process.")
        return
        
    age_column = df["age"]
    print(f"Age series:\n{age_column}\n")

    selected_columns_df = df[["age", "score"]]
    print(f"Selected columns dataframe:\n{selected_columns_df}\n")

    filtered_rows = df[df["score"] > 80]
    print(f"Rows with score > 80:\n{filtered_rows}\n")

if __name__ == "__main__":
    
    df = load_csv("employee.csv")
    print_output(df)
    process_data(df)