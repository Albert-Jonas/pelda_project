class IIOHandler:
    def read_input(self ) -> str:
        pass

    def write_output(self, output: str) -> None:
        pass


class IDatabaseHandler:
    def get_user_credentials(self, userName: str) -> str:
        pass


class IAuthenticator:
    def authenticate(self, userName: str, passWord: str) -> bool:
        pass