from flet import app, DataTable, DataColumn, DataRow, DataCell, Text
import chinook.db as db

def main(page):
    page.title = "Top 10 Best-Selling Artists"
    page.vertical_alignment = "start"

    artists = db.get_top_artists()  # Returns list of dicts: [{'name': ..., 'sales': ...}, ...]

    table = DataTable(
        columns=[
            DataColumn(Text("Artist")),
            DataColumn(Text("Total Sales")),
        ],
        rows=[
            DataRow(
                cells=[
                    DataCell(Text(artist["name"])),
                    DataCell(Text(f"{artist['sales']:.2f}")),
                ]
            )
            for artist in artists
        ],
    )

    page.add(table)

if __name__ == "__main__":
    app(target=main)
