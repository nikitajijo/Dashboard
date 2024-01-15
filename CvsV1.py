
import streamlit as st
import pandas as pd
import plotly.express as px

# Extract the sheet ID from the provided URL
url = "https://docs.google.com/spreadsheets/d/1-x9J-LtPP4AKURdpOhF7ON8YR-zxbr_ydcc__i4VGLI/edit#gid=0"
sheet_id = url.split("/d/")[1].split("/")[0]

# Specify the sheet name
sheet_name = "exp_1(Nikita)"

# Construct the URL for downloading the CSV
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Read the CSV into a DataFrame
df = pd.read_csv(csv_url)
df['experiment'] = 'exp_1'

# Extract the sheet ID from the provided URL
url = "https://docs.google.com/spreadsheets/d/1dZuYzMEetKlRXp-02ZhtQVOc_vfutKTTsk5xLoI8MqE/edit#gid=0"
sheet_id = url.split("/d/")[1].split("/")[0]

# Specify the sheet name
sheet_name = "exp_2(Nikita)"

# Construct the URL for downloading the CSV
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Read the CSV into a DataFrame
df2 = pd.read_csv(csv_url)
df2['experiment'] = 'exp_2'

combined_df = pd.concat([df, df2], ignore_index=True)

# Group by the specified columns and sum the numeric columns
summed_df = combined_df.groupby(['variation', 'ad_type', 'var_1', 'var_2', 'var_3', 'device_type', 'date','experiment']).agg({
    'impressions': 'sum',
    'clicks': 'sum',
    'revenue': lambda x: pd.to_numeric(x, errors='coerce').sum(),  # Convert to float and sum
    'views': 'sum'
}).reset_index()

# Pivot the DataFrame
result_df = summed_df.melt(id_vars=['variation', 'ad_type', 'var_1', 'var_2', 'var_3', 'device_type', 'date', 'experiment'],
                    value_vars=['impressions', 'clicks', 'revenue', 'views'],
                    var_name='metric',
                    value_name='value')

# Pivot table to have 'C' and 'V1' as columns
result_df = result_df.pivot_table(index=['ad_type', 'var_1', 'var_2', 'var_3', 'device_type','metric', 'date', 'experiment'], columns=['variation'], values='value', aggfunc='sum').reset_index()
result_df = result_df.sort_values(by=['experiment','ad_type','var_2','device_type','metric'])

# Group by the specified columns
grouped_df = result_df.groupby(['ad_type', 'var_1', 'var_2', 'var_3', 'device_type', 'metric', 'experiment'])

# Define a function to fill NaN values with the average of each group
def fillna_with_group_mean(column):
    return column.fillna(column.mean())

# Apply the fillna function to each group
result_df[':C'] = grouped_df[':C'].transform(fillna_with_group_mean)
result_df[':V1'] = grouped_df[':V1'].transform(fillna_with_group_mean)

# Calculate % change and add a new column
result_df['%change'] = (result_df[':V1'] / result_df[':C']) - 1

st.title("Dashboard for C vs V1 Over Time")

# Dropdown for variable selection
selected_metric = st.selectbox("Select Metric", result_df['metric'].unique())

# Dropdown for experiment selection
selected_experiment = st.selectbox("Select Experiment", result_df['experiment'].unique())

# Dropdown for ad_type selection
selected_ad_type = st.selectbox("Select Ad Type", result_df['ad_type'].unique())

# Dropdown for var_2 selection
selected_var_2 = st.selectbox("Select var_2", result_df['var_2'].unique())

# Dropdown for device type selection
selected_device_type = st.selectbox("Select Device Type", result_df['device_type'].unique())

# Filter DataFrame based on selected experiment, ad_type, var_2, and device type
filtered_df = result_df[
    (result_df['metric'] == selected_metric) &
    (result_df['experiment'] == selected_experiment) &
    (result_df['ad_type'] == selected_ad_type) &
    (result_df['var_2'] == selected_var_2) &
    (result_df['device_type'] == selected_device_type)
]

# Sort DataFrame by 'date'
filtered_df = filtered_df.sort_values('date')

# Line chart with secondary y-axis
fig = px.line(
    filtered_df,
    x='date',
    y=[':C', ':V1'],
    title=f"{selected_metric.capitalize()} Over Time",
    labels={'value': selected_metric},
    line_shape="linear"
)
fig.update_yaxes(title_text=':C', secondary_y=False)
fig.update_yaxes(title_text=':V1', secondary_y=True)

# Show the chart
st.plotly_chart(fig)
