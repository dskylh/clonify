class User:
    """
    Holds any info about users
    """
    def __init__(self, user_name, password, logged_in=False):
        self.user_name = user_name
        self.password = password
        self.logged_in = logged_in

    def check_password(self, password: str) -> bool:
        """
        Check if a given password is the same with user's password
        :param password:
        :return:
        """
        return password == self.password
