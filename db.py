import sqlite3 as sq

from music import Music
from user import User


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


    def addUser(self, user: User):
        usrCursor = self.sqliteConnection.cursor()
        try:
            insertQuery = f"INSERT INTO USERS(UserName, Password) VALUES('{user.userName}', '{user.password}')"
            usrCursor.execute(insertQuery)
            self.sqliteConnection.commit()
        except sq.Error as error:
            # 2067 is the error given when an unique constraint is failed
            # only works in python 3.11!!
            if error.sqlite_errorcode == 2067:
                print("Please select a different username.")
            else:
                print("Something went wrong while adding the user to the database: ", error)
        finally:
            usrCursor.close()

    def addMusic(self, music: Music):
        musicCursor = self.sqliteConnection.cursor()
        try:
            insertQuery = f"INSERT INTO MUSIC (MusicName, Artist, Album, Genre, PathToMusic) VALUES ('{music.musicName}', " \
                          f"'{music.artist}', '{music.album}', '{music.genre}', '{music.pathToMusic}') "
            musicCursor.execute(insertQuery)
            musicCursor.execute("Select * from MUSIC")
            # for row in musicCursor:
            #     print(row)
            self.sqliteConnection.commit()

        except sq.Error as error:
            print("Error occured while inserting into Music table: ", error)
        finally:
            musicCursor.close()

    def getUser(self, username: str) -> User:
        userCursor = self.sqliteConnection.cursor()
        try:
            selectQuery = f"SELECT UserName, Password FROM USERS WHERE UserName = '{username}'"
            userCursor.execute(selectQuery)
            fetching = userCursor.fetchone()
            assert fetching is not None
            uName = fetching[0]
            pswd = fetching[1]
            return User(uName, pswd)
        except sq.Error as error:
            print("Error occurred while selecting user from database: ", error)
            return User(None, None) 
        except AssertionError:
            print("Aradiginiz kullanici bulunamamistir.")
            return User(None, None) 
        finally:
            userCursor.close()

    def getMusics(self, musicName: str) -> list[Music]:
        musicCursor = self.sqliteConnection.cursor()
        try:
            selectQuery = f"SELECT * FROM MUSIC where MusicName like '%{musicName}%'"
            musicCursor.execute(selectQuery)
            selectQueryResult = musicCursor.fetchall()
            assert selectQueryResult is not None 
            musicList = [Music(None, None)] 
            for music in selectQueryResult:
                print(music)
                musicList.append(Music(musicName=music[1], 
                                       pathToMusic=music[5], 
                                       artist=music[2], 
                                       album=music[3], 
                                       genre=music[4]))
            musicList.pop(0)
            return musicList
        except sq.Error as error:
            print("Error occurred while selecting music from database: ", error)
            return [Music(None, None)] 
        except AssertionError:
            print("Boyle bir sarki bulunamamistir")
            return [Music(None, None)]
        finally:
            musicCursor.close()


if __name__ == "__main__":
    sqlcon = DbConnection()
    user1 = sqlcon.getUser("userclas")
    # print(user1.userName)
    musicList = sqlcon.getMusics("banger")
    for music in musicList:
        print(music.musicName)

    
