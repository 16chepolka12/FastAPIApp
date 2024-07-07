from sqlalchemy.orm import DeclarativeBase #базовая модель от которой будут наследоваться новые таблицы


class Base(DeclarativeBase):
    pass
