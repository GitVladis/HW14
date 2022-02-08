import sqlite3


def get_data(title):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_title = f"""
            SELECT MAX(date_added), title, country, release_year, listed_in, description
            FROM netflix
            WHERE title LIKE "%{title}%"                         
        """
        cur.execute(query_title)
        result_title = cur.fetchone()
        return result_title


def get_year(year1, year2):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_year = f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {year1} AND {year2}
                LIMIT 10                         
            """
        cur.execute(query_year)
        result_year = cur.fetchall()
        return result_year


def movie_children():
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_children = "SELECT title, rating, description  FROM netflix WHERE rating='G'"
        cur.execute(query_children)
        result_children = cur.fetchall()
        return result_children

def movie_family():
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_family = "SELECT title, rating, description  from netflix WHERE rating in ('PG' , 'PG-13') LIMIT 10"
        cur.execute(query_family)
        result_family = cur.fetchall()
        return result_family

def movie_adult():
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_adult = "SELECT title, rating, description  from netflix WHERE rating in ('R', 'NC-17') LIMIT 10"
        cur.execute(query_adult)
        result_adult = cur.fetchall()
        return result_adult


def movie_drama(genre):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_genre = f"""SELECT title, description from netflix WHERE listed_in LIKE "%{genre}%" AND `type`='Movie' LIMIT 10 """
        cur.execute(query_genre)
        result_genre = cur.fetchall()
        return result_genre


def actors(actor1, actor2):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_actor = f"""SELECT GROUP_CONCAT (`cast`, ",") as `cast` FROM netflix WHERE `cast` LIKE "%{actor1}%" AND `cast` LIKE "%{actor2}%" """
        cur.execute(query_actor)
        result_actor = cur.fetchone()
        list_actors = set(result_actor[0].split(", "))
        list_actors.remove(actor1)
        list_actors.remove(actor2)
        return list_actors


def movie_search(typ, year, genre):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query_genre = f"""SELECT title, description from netflix
                        WHERE  LOWER(listed_in) LIKE "%{genre.lower()}%"
                        AND LOWER(`type`)= "{typ.lower()}"
                        AND `release_year`={year} 
                        """
        cur.execute(query_genre)
        result_genre = cur.fetchall()
        return result_genre

