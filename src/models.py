from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)

    def __init__(self, fullname):
        self.fullname = fullname


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    def __init__(self, name):
        self.name = name

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')

    def __init__(self, fullname, group_id):
        self.fullname = fullname
        self.group_id = group_id

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')

    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column('date_of', Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    discipline_id = Column('discipline_id', ForeignKey('disciplines.id', ondelete='CASCADE'))
    student = relationship('Student', backref='grade')
    discipline = relationship('Discipline', backref='grade')
