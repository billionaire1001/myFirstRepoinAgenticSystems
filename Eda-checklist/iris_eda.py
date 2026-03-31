
import pandas 
import plotly.express

# 1. Load the Iris dataset from the provided link
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pandas.read_csv(url)

# 2. Inspect the dataset structure after loading
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset shape (rows, columns):", df.shape)

# 3. Check column information and missing values
print("\nColumn data types and non-null counts:")
print(df.info())

print("\nCount of missing values in each column:")
print(df.isnull().sum())

# 4. Summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

print("Dataset Structure: \n")
print("- The dataset contains 150 samples and 5 columns. No missing values are present. \n")

# 5. Analyze the distribution of one feature (petal_length)
fig = plotly.express.histogram(df, x='petal_length', nbins=30, color='species',
                   title='Distribution of Petal Length by Species')
fig.show()
print("Petal Length Distribution by Species: \n")
print("- Petal length shows clear separation between 'setosa' and other species. \n")

# 6. Identify possible outliers using box plots
fig2 = plotly.express .box(df, x='species', y='sepal_width', points='all',
              title='Sepal Width Distribution and Outliers by Species')
fig2.show()
print("Sepal Width Distribution and Outliers by Species: \n")
print("- 'setosa' species appears to have a wider range and higher median sepal width. \n")
print("- A few outliers are present in all species, especially for 'setosa'. \n")

# 7. Analyze relationships between variables (petal_length vs petal_width)
fig3 = plotly.express. scatter(df, x='petal_length', y='petal_width', color='species',
                  title='Petal Length vs Petal Width by Species',
                  labels={'petal_length': 'Petal Length (cm)', 'petal_width': 'Petal Width (cm)'})
fig3.show()
