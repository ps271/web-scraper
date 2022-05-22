import os

from pymongo import MongoClient
# from app import logger


class MongoDb:
    def __init__(self) -> None:
        self._connection_parameter = None
        self._connection = None

    def set_connection_parameter(self, **kwargs):
        self._connection_parameter = {
            "user": os.environ.get('MONGODB_USER') if not kwargs.get('user') else kwargs.get('user'),
            "password": os.environ.get('MONGODB_PASSWORD') if not kwargs.get('password') else kwargs.get('password'),
            "host": os.environ.get('MONGODB_HOST') if not kwargs.get('host') else kwargs.get('host'),
            "port": int(os.environ.get('MONGODB_PORT')) if not kwargs.get('port') else kwargs.get('port'),
            "database": os.environ.get('MONGODB_DATABASE') if not kwargs.get('database') else kwargs.get('database')
        }

    def get_connection_parameter(self):
        return self._connection_parameter

    def set_connection(self):
        if self._connection_parameter is None:
            self.set_connection_parameter()

        try:
            conn = MongoClient(
                username=self._connection_parameter['user'],
                password=self._connection_parameter['password'],
                host=self._connection_parameter['host'],
                port=self._connection_parameter['port'],
                                )

            self._connection = conn
        except Exception as ce:
            """logger.error(f'''[MONGODB] Error in making mongodb connection with
                host {self._connection_parameter['host']} ,
                port {self._connection_parameter['port']} ,
                user {self._connection_parameter['user']} ,
                database {self._connection_parameter['database']} ,
                error={ce}''')"""
            raise Exception(f"[MONGODB] Connection Error with MongoDb connection {str(self._connection)}")
        else:
            try:
                self._connection.server_info()
            except Exception as e:
                # logger.error("[MONGODB] Connection Broken With Server...........")
                # logger.error(f'[MONGODB] Error: {e}')
                # logger.error("[MONGODB] ...........Trying To Reconnect...........")
                self.set_connection()
            else:
                return self._connection

    @property
    def connection(self):
        if self._connection is None:
            self.set_connection()
        return self._connection

    def close_connection(self):
        if self._connection is not None:
            try:
                self._connection.close()
            except Exception as e:
                """
                logger.error(
                    f'''[MONGODB] Unable to close mongodb connection.
                    Connection might be already closed. Error : {e}'''
                    )
                logger.error(f'[MONGODB] connection {str(self._connection)}')
                """
            finally:
                self._connection = None
                self._connection_parameter = None
                return self._connection, self._connection_parameter, 'Connection closed successfully.'
        return self._connection, self._connection_parameter, 'Connection is already closed!'
