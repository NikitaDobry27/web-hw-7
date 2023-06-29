from pprint import pprint
from sqlalchemy import func, desc, and_, distinct, select

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_1():
    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


def select_2():
    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .where(Grade.discipline_id == 3)
        .group_by(Student.fullname)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return result


def select_3():
    result = (
        session.query(
            Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .where(Grade.discipline_id == 4)
        .group_by(Group.name)
        .order_by(desc("avg_grade"))
        .all()
    )
    return result


def select_4():
    result = (
        session.query(
            Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .group_by(Group.name)
        .order_by(desc("avg_grade"))
        .all()
    )
    return result


def select_5():
    result = session.query(Discipline.name).where(Discipline.teacher_id == 1).all()
    return result


def select_6():
    result = session.query(Student.fullname).where(Student.group_id == 2).all()
    return result


def select_7():
    result = (
        session.query(Student.fullname, Grade.grade)
        .select_from(Grade)
        .join(Student)
        .where(and_(Student.group_id == 2, Grade.discipline_id == 2))
        .all()
    )
    return result


def select_8():
    result = (
        session.query(
            Teacher.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Discipline, Discipline.teacher_id == Teacher.id)
        .join(Grade, Grade.discipline_id == Discipline.id)
        .filter(Teacher.id == 4)
        .group_by(Teacher.fullname)
        .all()
    )
    return result


def select_9():
    result = (
        session.query(distinct(Discipline.name))
        .join(Grade)
        .join(Student)
        .where(Student.id == 2)
        .all()
    )
    return result


def select_10():
    result = (
        session.query(distinct(Discipline.name))
        .join(Grade)
        .join(Student)
        .where(and_(Student.id == 2, Discipline.teacher_id == 1))
        .all()
    )
    return result


def select_11():
    result = (
        session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Student)
        .join(Discipline)
        .where(and_(Student.id == 4, Discipline.teacher_id == 1))
        .all()
    )
    return result


def select_12():
    group_id = 2
    dis_id = 2
    subq = (
        select(Grade.date_of)
        .join(Student)
        .join(Group)
        .where(and_(Grade.discipline_id == dis_id, Group.id == group_id))
        .order_by(desc(Grade.date_of))
        .limit(1)
    ).scalar_subquery()

    result = (
        session.query(
            Student.fullname, Discipline.name, Group.name, Grade.grade, Grade.date_of
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(
            and_(
                Grade.discipline_id == dis_id,
                Group.id == group_id,
                Grade.date_of == subq,
            )
        )
        .order_by(desc(Grade.date_of))
        .all()
    )
    return result


if __name__ == "__main__":
    # print(select_1())
    # print(select_2())
    # print(select_3())
    # print(select_4())
    # print(select_5())
    # pprint(select_6())
    # pprint(select_7())
    # pprint(select_8())
    # pprint(select_9())
    # pprint(select_10())
    # pprint(select_11())
    pprint(select_12())
