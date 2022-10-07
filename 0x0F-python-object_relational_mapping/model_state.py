#!/usr/bin/python3
"""class defination of a state"""


if __name__ == '__main__':
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class state(Base):
        """maps the tables

        Args:
            Base (obj): Inherited class
        """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement=True,
                    Nullable=False)
        name = Column(String(128), Nullable=False)
