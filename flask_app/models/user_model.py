from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
            SELECT *
            FROM users;
            """
        response = MySQLConnection(DATABASE).query_db(query)
        out = []
        for d in response:
            out.append(cls(d))
        return out

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT *
            FROM users
            WHERE id=%(id)s;
            """
        data = {'id': data}
        response = MySQLConnection(DATABASE).query_db(query, data)
        out = []
        for d in response:
            out.append(cls(d))
        return out

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, created_at, updated_at)
                VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );
                """
        data = {"first_name": data['first_name'],
                "last_name": data['last_name'],
                "email": data['email']}
        return MySQLConnection(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
            UPDATE users 
            SET first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id=%(id)s;
            """
        data = {"id": data['id'],
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "email": data['email']}
        return MySQLConnection(DATABASE).query_db(query, data)

    @classmethod
    def remove(cls, data):
        query = """
            DELETE
            FROM users
            WHERE id=%(id)s;
        #     """
        # data = {"id": data['id']}
        return MySQLConnection(DATABASE).query_db(query, data)
