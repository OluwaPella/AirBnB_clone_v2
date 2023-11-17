from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:

    __engine = None
    __session = None

    def __int__(self):
        """ creating table in envr"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database  = getenv("HBNB_MYSQL_DB")
        env  = getenv("HBNB_ENV")

        db_url = f'mysql+mysqldb://{user}:{passwd}@{host}/{database}'
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for lis in query:
                key = "{}.{}".format(type(lis).__name__, lis.id)
                dic[key] = lis

        else:
            list_all = [User, State, City, Amenity, Place, Review]
                for classe in list_all:
                    query = self.__session.query(classe)
                for element in query:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    dic[key] = element
        return dic

    def new(self, obj):
        """ adding  new element in database
        """
        self.__session.add(obj)

    def save(self):
        """this commit all chnages 
        of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ this delete from the database session
         obj if not None"""
         
         if obj:
             self.__session.delete(obj)

    def reload(self):

