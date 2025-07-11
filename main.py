import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "Chinook_Sqlite.sqlite"  # Adjust path if needed

def get_top_artists():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = """
        SELECT
            ar.Name as name,
            SUM(ii.UnitPrice * ii.Quantity) as sales
        FROM
            InvoiceLine ii
            JOIN Track t ON ii.TrackId = t.TrackId
            JOIN Album al ON t.AlbumId = al.AlbumId
            JOIN Artist ar ON al.ArtistId = ar.ArtistId
        GROUP BY
            ar.ArtistId
        ORDER BY
            sales DESC
        LIMIT 10
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "sales": row[1]} for row in results]
