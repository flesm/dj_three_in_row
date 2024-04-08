import sqlite3


class SQLiteDB:
    def __init__(self, db_file):
        self.db_file = db_file

    def get_teams(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `teams`")
        teams = result.fetchall()
        conn.close()
        return teams

    def get_team_score(self, name):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        result = cursor.execute("SELECT `total_score` FROM `teams` WHERE `name` = (?)", (name,))
        score = result.fetchone()
        conn.close()
        return score[0]

    def update_team_total_score(self, name, total_score):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("UPDATE `teams` SET `total_score` = (?) WHERE `name` = (?)", (total_score, name))
        conn.commit()
        conn.close()
