import mysql.connector
import pandas as pd
import plotly.express as px


def fetch_city_data():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="112145",
        port=3306,
        database="cities"
    )
    cursor = conn.cursor(dictionary=True)

    # Fetch city data
    cursor.execute("SELECT City, `Location`, `Development Ranking (HDI)`, Religion, Language FROM cities LIMIT 51")
    cities = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Check if we have data
    if not cities:
        print("No city data found.")
        return None

    # Convert to a DataFrame for easy manipulation
    cities_df = pd.DataFrame(cities)

    # Split 'Location' column into 'Latitude' and 'Longitude'
    cities_df[['Latitude', 'Longitude']] = cities_df['Location'].str.split(',', expand=True).astype(float)
    cities_df.drop(columns=['Location'], inplace=True)

    return cities_df


def create_minimalistic_map(cities_df):
    # Create an interactive scatter plot map with Plotly
    fig = px.scatter_geo(
        cities_df,
        lat='Latitude',
        lon='Longitude',
        hover_name='City',
        hover_data={
            "Development Ranking (HDI)": True,
            "Religion": True,
            "Language": True,
            "Latitude": False,  # Hide in hover data
            "Longitude": False  # Hide in hover data
        },
        title="Minimalistic World Map of Cities"
    )

    # Customize marker size, color, and opacity
    fig.update_traces(marker=dict(size=5, color="blue", opacity=0.7))  # Smaller and more subtle markers

    # Use a minimalistic map style
    fig.update_geos(
        projection_type="natural earth",
        showland=True,
        landcolor="whitesmoke",
        oceancolor="lightblue",
        showocean=True,
        showlakes=False,
        showcountries=True,
        countrycolor="lightgray",
        coastlinecolor="lightgray"
    )

    # Update layout for a minimalistic look
    fig.update_layout(
        title="Minimalistic World Map of Cities",
        font=dict(size=12),
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        showlegend=False
    )

    # Display the map
    fig.show()


def main():
    # Fetch the city data from the database
    cities_df = fetch_city_data()

    if cities_df is not None:
        # Create and display the minimalistic map
        create_minimalistic_map(cities_df)


if __name__ == "__main__":
    main()
