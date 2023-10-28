from attr import dataclass
import mysql.connector
from db.db import db
from datetime import datetime

@dataclass
class Player():
    player_id: str
    family_name: str
    given_name: str
    birth_date: datetime.date
    female: bool
    goal_keeper: bool
    defender: bool
    midfielder: bool
    forward: bool
    count_tournaments: int
    list_tournaments: str
    player_wikipedia_link: str

class PlayerDAO():
    @staticmethod
    def create_player(db: db, player: Player) -> None:
        try:
            query = """
                INSERT INTO players (
                    player_id,
                    family_name,
                    given_name,
                    birth_date,
                    female,
                    goal_keeper,
                    defender,
                    midfielder,
                    forward,
                    count_tournaments,
                    list_tournaments,
                    player_wikipedia_link
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor = db.conn.cursor()
            cursor.execute(query, (
                player.player_id,
                player.family_name,
                player.given_name,
                player.birth_date,
                player.female,
                player.goal_keeper,
                player.defender,
                player.midfielder,
                player.forward,
                player.count_tournaments,
                player.list_tournaments,
                player.player_wikipedia_link
            ))
            cursor.close()
            db.conn.commit()
            print("Player created successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    @staticmethod
    def get_player(db: db, player_id: str) -> Player:
        try:
            query = """
                SELECT * FROM players WHERE player_id = %s
            """
            cursor = db.conn.cursor()
            cursor.execute(query, (player_id,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    @staticmethod
    def get_all_players(db: db) -> list:
        try:
            query = """
                SELECT * FROM players
            """
            cursor = db.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    @staticmethod
    def update_player(db: db, player: Player) -> None:
        try:
            query = """
                UPDATE players SET
                    family_name = %s,
                    given_name = %s,
                    birth_date = %s,
                    female = %s,
                    goal_keeper = %s,
                    defender = %s,
                    midfielder = %s,
                    forward = %s,
                    count_tournaments = %s,
                    list_tournaments = %s,
                    player_wikipedia_link = %s
                WHERE player_id = %s
            """
            cursor = db.conn.cursor()
            cursor.execute(query, (
                player.family_name,
                player.given_name,
                player.birth_date,
                player.female,
                player.goal_keeper,
                player.defender,
                player.midfielder,
                player.forward,
                player.count_tournaments,
                player.list_tournaments,
                player.player_wikipedia_link,
                player.player_id
            ))
            cursor.close()
            db.conn.commit()
            print("Player updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    @staticmethod
    def delete_player(db: db, player_id: str) -> None:
        try:
            query = """
                DELETE FROM players WHERE player_id = %s
            """
            cursor = db.conn.cursor()
            cursor.execute(query, (player_id,))
            cursor.close()
            db.conn.commit()
            print("Player deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")