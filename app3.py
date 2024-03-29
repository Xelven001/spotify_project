from flask import Blueprint, request, jsonify
import sqlite3

app3 = Blueprint('app3', __name__)



@app3.route('/get_data')

def get_data():
    connection = sqlite3.connect('spotify_data.db')
    cursor = connection.cursor()

    selected_genre = request.args.get('genre3')

    if selected_genre:
        query = f"SELECT year,\
                    genre,\
                    avg(duration_ms)/1000 as duration   \
                    FROM song_metrics\
                    WHERE genre = ? \
                    AND genre IN ('Hip-Hop','Electronic','Rock','Pop')\
                    AND year BETWEEN '2000' and '2019'\
                    GROUP BY year,genre\
                    "       
        cursor.execute(query, (selected_genre,))
    else:
        query = "SELECT year,\
                    genre,\
                    avg(duration_ms)/1000 as duration     \
                    FROM song_metrics\
                    WHERE genre IN ('Hip-Hop','Electronic','Rock','Pop')\
                    AND year BETWEEN '2000' and '2019'\
                    GROUP BY year,genre\
                    "        
        cursor.execute(query)



    data = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    connection.close()

    result = [dict(zip(columns, row)) for row in data]

    return jsonify(result)