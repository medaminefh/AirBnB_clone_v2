#!/usr/bin/python3
"""
db storage class
"""

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.city import City
from models.state import State
from models.review import Review


class DBStorage:
    """Mysql db storage class"""
    __engine = None
    __session = None

    classes = {"Amenity": Amenity, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}

    def __init__(self):
        """Instantiate a DBStorage object"""
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER,
                                             PWD,
                                             HOST,
                                             DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in DBStorage.classes:
            if cls is None or cls is DBStorage.classes[clss] or cls is clss:
                objs = self.__session.query(DBStorage.classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)


    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
