"""Run the Leaderboard webapp"""

from datetime import datetime
import json
import altair as alt
import pandas as pd
import streamlit as st
import sort_dates
import process_json


JSON_FILENAME = "scores (1).json"
CHART_SIZE = 20
CURRENT_YEAR = int(datetime.today().strftime("%Y"))
OPTIONS = ["All-Time", "Last 5 Years",
           "Last 10 Years", "Last 15 Years",
           "Last 20 Years"] # Keep exact format consistent (LAST N YEARS)
COLUMNS = ['Candidate Name', 'Total Score', 'Highest Score', 'Date Achieved']
STYLE_MODS = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """


def draw_chart(chart_data: pd.DataFrame, limits: tuple):
    """Draw an Altair bar chart with 315 degree x-axis labels, width of 650x400px

    Input Parameters:
    -----------------
    chart_data      Type:   pd.DataFrame
                    Use:    Relevant candidate data. The number of entries shown is
                            determined by the global CHART_SIZE

    limits          Type:   tuple
                    Use:    y-axis minimum and maximum values shown on the chart, 
                            respectively
    """
    chart = alt.Chart(chart_data).mark_bar(clip=True).encode(
    x=alt.X("Candidate Name:N", sort="-y",
            axis=alt.Axis(labelAngle=315)),
    y=alt.Y("Total Score:Q",
            scale=alt.Scale(domain=(limits[0],limits[1])))).properties(
    width=650,
    height=400)

    st.write(chart)


def set_limits(output_data: list) -> tuple:
    """Grabs the name and their submissions scores from a dictionary
       in the input .json file

    Input Parameters:
    -----------------
    output_data     Type:   list
                    Use:    List of data to be converted to a DataFrame
                            [Name, Total Score, Best Score, Best Score Date]

    Output Parameters:
    -----------------

    limits          Type:   tuple
                    Use:    y-axis minimum and maximum values for charts
    """
    try:

        max_y = output_data[0][1] + 50
        min_y = output_data[CHART_SIZE][1] - 50

    except IndexError:

        max_y = 0
        min_y = 0

    min_y = max(min_y,0)

    return (min_y, max_y)


def make_chart_data(output_data: list[str,int,list,list]) -> tuple[pd.DataFrame, tuple]:
    """Converts the processed json data to a format compatible with DataFrames

    Input Parameters:
    -----------------
    json_data       Type:   list
                    Use:    List of data to be converted to a DataFrame
                            [Name, Total Score, Best Score, Best Score Date]

    Output Parameters:
    -----------------

    (data,limits)   Type:   tuple
                    Use:    Pandas DataFrame conversion of the json data and
                            the y-axis limits for the top-N chart
    """
    output_data = [[x[0],x[1],x[2][0],x[3][0]] for x in output_data if len(x[2]) > 2]

    limits = set_limits(output_data)

    chart_data = pd.DataFrame(output_data)
    chart_data.columns = COLUMNS

    return(chart_data, limits)


def visualisations(processed_data):
    """Builds the DataFrame and charts necessary for visualising
       the json data

    Input Parameters:
    -----------------
    processed_data  Type:   list
                    Use:    List of processed json data in format:
                            [[Name, Total Score, [Scores], [Dates]],
                             [ '' ],
                             [ '' ]]
    """
    chart_data, limits = make_chart_data(processed_data)
    draw_chart(chart_data[:CHART_SIZE], limits)
    st.subheader("All Candidates (3 Submissions Minimum)")
    st.table(chart_data)


if __name__ == "__main__":

    # Style and text element setups for Streamlit
    st.title("Score Leaderboard")
    st.markdown(STYLE_MODS, unsafe_allow_html=True)

    # Box for picking year range to sort by
    selected_option = st.selectbox("Time Range:", OPTIONS)

    st.subheader("Top " + str(CHART_SIZE) + " Candidates:")

    with open(JSON_FILENAME, 'r') as file:
        data = json.load(file)
    json_data = process_json.process(data)

    if selected_option == "All-Time":

        visualisations(json_data)

    else:

        year_range = int(selected_option[5:-6])
        cutoff_year = CURRENT_YEAR - year_range

        cropped_data = sort_dates.crop_dates(json_data, cutoff_year)
        visualisations(cropped_data)
