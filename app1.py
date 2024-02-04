from flask import Blueprint, request, jsonify
import sqlite3

app1 = Blueprint('app1', __name__)


@app1.route('/get_data')

def get_data():
    connection = sqlite3.connect('spotify_data.db')
    cursor = connection.cursor()

    selected_genre = request.args.get('genre')

    if selected_genre:
        query = f"SELECT genre, year, count(song) as 'Total Songs', avg(popularity) as 'Average Popularity', avg(danceability) as 'Average Danceability', avg(duration_ms)/1000 as 'Average Duration(Seconds)', avg(energy) as 'Average Energy', avg(key) as 'Average Key', avg(loudness) as 'Average Loudness', avg(mode) as 'Average Mode', avg(speechiness) as 'Average Speechiness', avg(acousticness) as 'Average Acousticness', avg(instrumentalness) as 'Average Instrumentalness', avg(liveness) as 'Average Liveness', avg(valence) as 'Average Valence', avg(tempo) as 'Average Tempo' FROM song_metrics WHERE genre = ? and year BETWEEN '1999' and '2019' AND genre IN ('Hip-Hop','Electronic','Rock','Pop')  GROUP BY genre,year"
        cursor.execute(query, (selected_genre,))
    else:
        query = "SELECT genre, year, count(song) as 'Total Songs', avg(popularity) as 'Average Popularity', avg(danceability) as 'Average Danceability' , avg(duration_ms)/1000 as 'Average Duration(Seconds)', avg(energy) as 'Average Energy', avg(key) as 'Average Key', avg(loudness) as 'Average Loudness', avg(mode) as 'Average Mode', avg(speechiness) as 'Average Speechiness', avg(acousticness) as 'Average Acousticness', avg(instrumentalness) as 'Average Instrumentalness', avg(liveness) as 'Average Liveness', avg(valence) as 'Average Valence', avg(tempo) as 'Average Tempo' FROM song_metrics WHERE year BETWEEN '1999' and '2019' AND genre IN ('Hip-Hop','Electronic','Rock','Pop') GROUP BY genre,year "
        cursor.execute(query)

   
    data = cursor.fetchall()

    # Get column names from the cursor description
    columns = [column[0] for column in cursor.description]

    # Close the database connection
    connection.close()

    # Convert data to a list of dictionaries
    result = [dict(zip(columns, row)) for row in data]

    # Return data as JSON
    return jsonify(result)