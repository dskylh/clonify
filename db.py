import sqlite3 as sq
from music import Music
from user import User


class DbConnection:
    """
    Database connection and handling class
    """

    def __init__(self):
        """
        Creates the table for the database if they already don't exist
        """
        try:
            self.sqlite_connection = sq.connect("clonify.db")
            curs = self.sqlite_connection.cursor()
            user_table = """
            CREATE TABLE IF NOT EXISTS USERS(
                UserId INTEGER PRIMARY KEY,
                UserName VARCHAR(100) NOT NULL UNIQUE,
                Password VARCHAR(100) NOT NULL,
                Logged_in BOOLEAN NOT NULL
                );
            """
            curs.execute(user_table)

            music_table = """
            CREATE TABLE IF NOT EXISTS MUSIC(
                    MusicId INTEGER PRIMARY KEY,
                    MusicName VARCHAR(200) NOT NULL,
                    Artist VARCHAR(200),
                    Album varchar(200),
                    Genre varchar(200),
                    PathToMusic varchar(255) NOT NULL UNIQUE
                    )
            """
            curs.execute(music_table)

            print("Connected to the database")

        except sq.Error as error:
            print("Error occurred while initializing database: ", error)

    def adduser(self, user: User):
        """
        add a user to the USERS table
        :param user:
        :return:
        """
        user_cursor = self.sqlite_connection.cursor()
        try:
            insert_query = (
                f"INSERT INTO USERS(UserName, Password, Logged_in) VALUES(?, ?, ?)"
            )
            user_cursor.execute(
                insert_query, (user.user_name, user.password, user.logged_in)
            )
            self.sqlite_connection.commit()
        except sq.Error as error:
            # 2067 is the error given when an unique constraint is failed
            if error.sqlite_errorcode == 2067:
                print("Please select a different username.")
                print(
                    "Something went wrong while adding the user to the database: ",
                    error,
                )
        finally:
            user_cursor.close()

    def change_user_logged_in(self, user: User):
        """
        Changes the currently logged-in user from the USERS table.
        Will also log out any other logged-in users.
        :param user: User that will be logged in
        """
        update_cursor = self.sqlite_connection.cursor()
        user.logged_in = True
        update_logged_in_user = "UPDATE USERS SET Logged_in = ? WHERE UserName = ?"
        cleanup = "UPDATE USERS SET Logged_in = 0 WHERE Logged_in = 1"
        try:
            update_cursor.execute(cleanup)
            update_cursor.execute(
                update_logged_in_user, (user.logged_in, user.user_name)
            )
            self.sqlite_connection.commit()
        except sq.Error as error:
            print("Error occurred while updating Users table: ", error)
        finally:
            update_cursor.close()

    def log_out_user(self):
        """
        Logs out any logged-in user
        """
        log_out_cursor = self.sqlite_connection.cursor()
        try:
            log_out_query = "UPDATE USERS SET Logged_in = 0 WHERE Logged_in = 1"
            log_out_cursor.execute(log_out_query)
            self.sqlite_connection.commit()
        except sq.Error as error:
            print("Error occured while updating Users table: ", error)
        finally:
            log_out_cursor.close()

    def get_logged_in_user(self) -> User:
        """
        Returns the currently logged-in user in a User type
        :return User:
        """
        login_cursor = self.sqlite_connection.cursor()
        try:
            login_cursor.execute(
                "SELECT UserName, Password, Logged_in FROM USERS WHERE Logged_in = 1"
            )
            login_user = login_cursor.fetchone()
            assert login_user is not None
            user_name = login_user[0]
            password = login_user[1]
            logged_in = login_user[2]
            if logged_in == 1:
                logged_in = True
            else:
                logged_in = False
            return User(user_name, password, logged_in)
        except sq.Error as error:
            print("Error occurred while selecting from USERS: ", error)
            return User(None, None, False)
        except AssertionError:
            return User(None, None, False)

        finally:
            login_cursor.close()

    def add_music(self, music: Music):
        """
        Adds a music to the MUSIC table
        :param music:
        """
        music_cursor = self.sqlite_connection.cursor()
        try:
            insert_query = f"INSERT INTO MUSIC (MusicName, Artist, Album, Genre, PathToMusic) VALUES (?, ?, ?, ?, ?)"
            music_cursor.execute(
                insert_query,
                (
                    music.music_name,
                    music.artist,
                    music.album,
                    music.genre,
                    music.path_to_music,
                ),
            )
            music_cursor.execute("Select * from MUSIC")
            self.sqlite_connection.commit()

        except sq.Error as error:
            if error.sqlite_errorcode == 2067:
                print("Please use a different path for the music: ", error)
                raise error
            else:
                print("Error occured while inserting into Music table: ", error)
        finally:
            music_cursor.close()

    def get_user(self, username: str) -> User:
        """
        Searches the database for any user matching the given username
        :param username: username for the user that will be returned
        :return: If no user is found matching than it returns a User(None, None, False)
        """
        user_cursor = self.sqlite_connection.cursor()
        try:
            select_query = (
                f"SELECT UserName, Password FROM USERS WHERE UserName = '{username}'"
            )
            user_cursor.execute(select_query)
            fetching = user_cursor.fetchone()
            assert fetching is not None
            u_name = fetching[0]
            pswd = fetching[1]
            return User(u_name, pswd)
        except sq.Error as error:
            print("Error occurred while selecting user from database: ", error)
            return User(None, None)
        except AssertionError:
            print("Aradiginiz kullanici bulunamamistir.")
            return User(None, None)
        finally:
            user_cursor.close()

    def get_musics(self, search_query: str, search_type="") -> list[Music]:
        music_cursor = self.sqlite_connection.cursor()
        try:
            select_query = (
                f"SELECT * FROM MUSIC where MusicName like '%{search_query}%'"
            )
            if search_type == "Albüm":
                select_query = (
                    f"SELECT * FROM MUSIC where Album like '%{search_query}%'"
                )
            elif search_type == "Sanatçı":
                select_query = (
                    f"SELECT * FROM MUSIC where Artist like '%{search_query}%'"
                )
            music_cursor.execute(select_query)
            select_query_result = music_cursor.fetchall()
            assert select_query_result is not None
            music_list = [Music(None, None)]
            for music in select_query_result:
                music_list.append(
                    Music(
                        music_name=music[1],
                        artist=music[2],
                        album=music[3],
                        genre=music[4],
                        path_to_music=music[5],
                    )
                )
            if len(music_list) != 1:
                music_list.pop(0)
            return music_list
        except sq.Error as error:
            print("Error occurred while selecting music from database: ", error)
            return [Music(None, None)]
        except AssertionError:
            print("Boyle bir sarki bulunamamistir")
            return [Music(None, None)]
        finally:
            music_cursor.close()


if __name__ == "__main__":
    sqlcon = DbConnection()
    sqlcon.add_music(
        Music(
            "Stranded",
            "music/Gojira - Stranded [OFFICIAL VIDEO].ogg",
            artist="Gojira",
            genre="Metal",
            album="Magma",
        )
    )
