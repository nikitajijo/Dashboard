{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPHeRZXi9aoZfN20YzPoU+c",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nikitajijo/Dashboard/blob/main/Untitled7_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install streamlit -q"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ahAQg6esqwrp",
        "outputId": "c15389e2-c0e7-4098-b0e4-8a97a6a99634"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.4/8.4 MB\u001b[0m \u001b[31m22.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m196.4/196.4 kB\u001b[0m \u001b[31m16.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m39.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m7.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m4.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget -q -O - ipv4.icanhazip.com"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bt4c6rZKqyXG",
        "outputId": "7ba5a2dc-cd82-4ceb-aed1-5eab51222d6c"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "35.239.191.28\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "97dtXEd77qsG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "87ab351a-5f5e-48aa-c9b0-b60478f3fe9b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "\n",
        "# Extract the sheet ID from the provided URL\n",
        "url = \"https://docs.google.com/spreadsheets/d/1-x9J-LtPP4AKURdpOhF7ON8YR-zxbr_ydcc__i4VGLI/edit#gid=0\"\n",
        "sheet_id = url.split(\"/d/\")[1].split(\"/\")[0]\n",
        "\n",
        "# Specify the sheet name\n",
        "sheet_name = \"exp_1(Nikita)\"\n",
        "\n",
        "# Construct the URL for downloading the CSV\n",
        "csv_url = f\"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}\"\n",
        "\n",
        "# Read the CSV into a DataFrame\n",
        "df = pd.read_csv(csv_url)\n",
        "df['experiment'] = 'exp_1'\n",
        "\n",
        "# Extract the sheet ID from the provided URL\n",
        "url = \"https://docs.google.com/spreadsheets/d/1dZuYzMEetKlRXp-02ZhtQVOc_vfutKTTsk5xLoI8MqE/edit#gid=0\"\n",
        "sheet_id = url.split(\"/d/\")[1].split(\"/\")[0]\n",
        "\n",
        "# Specify the sheet name\n",
        "sheet_name = \"exp_2(Nikita)\"\n",
        "\n",
        "# Construct the URL for downloading the CSV\n",
        "csv_url = f\"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}\"\n",
        "\n",
        "# Read the CSV into a DataFrame\n",
        "df2 = pd.read_csv(csv_url)\n",
        "df2['experiment'] = 'exp_2'\n",
        "\n",
        "combined_df = pd.concat([df, df2], ignore_index=True)\n",
        "\n",
        "# Group by the specified columns and sum the numeric columns\n",
        "summed_df = combined_df.groupby(['variation', 'ad_type', 'var_1', 'var_2', 'var_3', 'device_type', 'date','experiment']).agg({\n",
        "    'impressions': 'sum',\n",
        "    'clicks': 'sum',\n",
        "    'revenue': lambda x: pd.to_numeric(x, errors='coerce').sum(),  # Convert to float and sum\n",
        "    'views': 'sum'\n",
        "}).reset_index()\n",
        "\n",
        "# Pivot the DataFrame\n",
        "result_df = summed_df.melt(id_vars=['variation', 'ad_type', 'var_1', 'var_2', 'var_3', 'device_type', 'date', 'experiment'],\n",
        "                    value_vars=['impressions', 'clicks', 'revenue', 'views'],\n",
        "                    var_name='metric',\n",
        "                    value_name='value')\n",
        "\n",
        "# Pivot table to have 'C' and 'V1' as columns\n",
        "result_df = result_df.pivot_table(index=['ad_type', 'var_1', 'var_2', 'var_3', 'device_type','metric', 'date', 'experiment'], columns=['variation'], values='value', aggfunc='sum').reset_index()\n",
        "result_df = result_df.sort_values(by=['experiment','ad_type','var_2','device_type','metric'])\n",
        "\n",
        "# Group by the specified columns\n",
        "grouped_df = result_df.groupby(['ad_type', 'var_1', 'var_2', 'var_3', 'device_type', 'metric', 'experiment'])\n",
        "\n",
        "# Define a function to fill NaN values with the average of each group\n",
        "def fillna_with_group_mean(column):\n",
        "    return column.fillna(column.mean())\n",
        "\n",
        "# Apply the fillna function to each group\n",
        "result_df[':C'] = grouped_df[':C'].transform(fillna_with_group_mean)\n",
        "result_df[':V1'] = grouped_df[':V1'].transform(fillna_with_group_mean)\n",
        "\n",
        "# Calculate % change and add a new column\n",
        "result_df['%change'] = (result_df[':V1'] / result_df[':C']) - 1\n",
        "\n",
        "st.title(\"Dashboard for C vs V1 Over Time\")\n",
        "\n",
        "# Dropdown for variable selection\n",
        "selected_metric = st.selectbox(\"Select Metric\", result_df['metric'].unique())\n",
        "\n",
        "# Dropdown for experiment selection\n",
        "selected_experiment = st.selectbox(\"Select Experiment\", result_df['experiment'].unique())\n",
        "\n",
        "# Dropdown for ad_type selection\n",
        "selected_ad_type = st.selectbox(\"Select Ad Type\", result_df['ad_type'].unique())\n",
        "\n",
        "# Dropdown for var_2 selection\n",
        "selected_var_2 = st.selectbox(\"Select var_2\", result_df['var_2'].unique())\n",
        "\n",
        "# Dropdown for device type selection\n",
        "selected_device_type = st.selectbox(\"Select Device Type\", result_df['device_type'].unique())\n",
        "\n",
        "# Filter DataFrame based on selected experiment, ad_type, var_2, and device type\n",
        "filtered_df = result_df[\n",
        "    (result_df['metric'] == selected_metric) &\n",
        "    (result_df['experiment'] == selected_experiment) &\n",
        "    (result_df['ad_type'] == selected_ad_type) &\n",
        "    (result_df['var_2'] == selected_var_2) &\n",
        "    (result_df['device_type'] == selected_device_type)\n",
        "]\n",
        "\n",
        "# Sort DataFrame by 'date'\n",
        "filtered_df = filtered_df.sort_values('date')\n",
        "\n",
        "# Line chart with secondary y-axis\n",
        "fig = px.line(\n",
        "    filtered_df,\n",
        "    x='date',\n",
        "    y=[':C', ':V1'],\n",
        "    title=f\"{selected_metric.capitalize()} Over Time\",\n",
        "    labels={'value': selected_metric},\n",
        "    line_shape=\"linear\"\n",
        ")\n",
        "fig.update_yaxes(title_text=':C', secondary_y=False)\n",
        "fig.update_yaxes(title_text=':V1', secondary_y=True)\n",
        "\n",
        "# Show the chart\n",
        "st.plotly_chart(fig)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wr6rr-60qwuz",
        "outputId": "3ac1a616-c312-4bd1-9847-601b3b417e04"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.239.191.28:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[K\u001b[?25hnpx: installed 22 in 6.088s\n",
            "your url is: https://grumpy-knives-look.loca.lt\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "A9-wACHvqwyS"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
