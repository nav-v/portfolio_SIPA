import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("New_York_City_Population_By_Community_Districts_20251114.csv")
df.head()

number_of_crashes = df.groupby("Borough").size()
number_of_crashes 

number_of_crashes = number_of_crashes.reset_index()
number_of_crashes




number_of_crashes = (
    crashes.groupby("Borough")
           .size()
           .reset_index(name="num_crashes")
)

fig = px.bar(
    number_of_crashes,
    x="BOROUGH",
    y="num_crashes",
    title="Number of Crashes By Borough",
    labels={
        "BOROUGH": "Borough",
        "num_crashes": "Number of Crashes"
    }
)

fig.show()