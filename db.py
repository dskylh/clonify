import sqlite3 as sq

from music import Music
from user import User


# from user import User


class DbConnection:
    def __init__(self):
        try:
            self.sqliteConnection = sq.connect("clonify.db")
            curs = self.sqliteConnection.cursor()
            userTable = """
            CREATE TABLE IF NOT EXISTS USERS(
                UserId INTEGER PRIMARY KEY,
                UserName VARCHAR(100) NOT NULL UNIQUE,
                Password VARCHAR(100) NOT NULL
                );
            """
            curs.execute(userTable)

            musicTable = """
            CREATE TABLE IF NOT EXISTS MUSIC(
                    MusicId INTEGER PRIMARY KEY,
                    MusicName VARCHAR(200) NOT NULL,
                    Artist VARCHAR(200),
                    Album varchar(200),
                    Genre varchar(200),
                    PathToMusic varchar(255) NOT NULL
                    )
            """
            curs.execute(musicTable)

            print("database created")

        except sq.Error as error:
            print("Error occurred while initializing database: ", error)

    # deneme icin todo make it right

    def addUser(self, username: str, password: str):
        try:
            usrCursor = self.sqliteConnection.cursor()
            insertQuery = f"INSERT INTO USERS(UserName, Password) VALUES('{username}', '{password}')"
            usrCursor.execute(insertQuery)
            # usrCursor.execute("select * from USERS")
            # print(type(usrCursor))
            # for row in usrCursor:
            #     print(row)
            self.sqliteConnection.commit()
            usrCursor.close()
        except sq.Error as error:
            # 2067 is the error given when an unique constraint is failed
            # only works in python 3.11!!
            if error.sqlite_errorcode == 2067:
                print("Please select a different username.")
            else:
                print("Something went wrong while adding the user to the database: ", error)

    def addMusic(self, musicName: str, pathToMusic: str, artist="", album="", genre=""):
        try:
            musicCursor = self.sqliteConnection.cursor()
            insertQuery = f"INSERT INTO MUSIC (MusicName, Artist, Album, Genre, PathToMusic) VALUES ('{musicName}', " \
                          f"'{artist}', '{album}', '{genre}', '{pathToMusic}') "
            musicCursor.execute(insertQuery)
            musicCursor.execute("Select * from MUSIC")
            # for row in musicCursor:
            #     print(row)
            musicCursor.close()
            self.sqliteConnection.commit()

        except sq.Error as error:
            print("Error occured while inserting into Music table: ", error)

    def getUser(self, username=""):
        try:
            selectQuery = f"SELECT * FROM USERS WHERE UserName like '%{username}%'"
            userCursor = self.sqliteConnection.cursor()
            userCursor.execute(selectQuery)
            # for row in userCursor:
            #     print(row)
            return userCursor.fetchone()
        except sq.Error as error:
            print("Error occurred while selecting user from database: ", error)

    def getMusic(self, musicName):
        try:
            selectQuery = f"SELECT * FROM MUSIC where MusicName like '%{musicName}%'"
            musicCursor = self.sqliteConnection.cursor()
            musicCursor.execute(selectQuery)
            music = musicCursor.fetchone()
            return music
            # musicname = music[1]
            # artist = music[2]
            # album = music[3]
            # genre = music[4]
            # pathToMusic = music[5]
        except sq.Error as error:
            print("Error occurred while selecting music from database: ", error)


if __name__ == "__main__":
    sqlcon = DbConnection()
    # sqlcon.addUser("bruh1", "123")
    # print(sqlcon.sqliteConnection.cursor().execute("Select * from USERS").fetchall())
    user1 = sqlcon.getUser("bruh1")
    print(user1)
    # sqlcon.addMusic("music1", "artist1", "album1", "genre1", "path1")
    music = sqlcon.getMusic("music1")
    print(music)
    # print(user1.userName)
    

    # sqlcon.addUser(User("bruh", "123"))
    # print(user.userName)
    # sqlcon.addMusic("Silvera", "music/Gojira - Silvera [OFFICIAL VIDEO].wav",
    #                 artist="Gojira", album="Magma", genre="Metal")

    # sqlcon.addMusic("MusicName", "abc", artist="artistdeneme", album="albumdeneme")
