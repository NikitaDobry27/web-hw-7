from sqlalchemy import select

from src.db import session
from src.models import Teacher, Student, Discipline, Grade, Group


"""Teacher"""


def create_teacher(fullname):
    new_teacher = Teacher(fullname)
    session.add(new_teacher)
    session.commit()
    print(f"Teacher {fullname} created with ID {new_teacher.id}")


def update_teacher(id, fullname):
    teacher = session.query(Teacher).filter_by(id=id).first()
    teacher.fullname = fullname
    session.commit()
    print(f"Teach name with ID {teacher.id} has been updated to {teacher.fullname}")


def remove_teacher(id):
    teacher = session.execute(select(Teacher).filter_by(id=id)).scalar_one_or_none()
    session.delete(teacher)
    session.commit()
    print(f"Teacher with ID {teacher.id} has been removed")


def list_teachers(id=None):
    if id:
        result = session.query(Teacher).where(Teacher.id == id).all()
    else:
        result = session.query(Teacher).all()
    for teacher in result:
        print(f"ID: {teacher.id}, Full Name: {teacher.fullname}")


"""Disciplines"""


def create_discipline(name, teacher_id):
    new_discipline = Discipline(name, teacher_id)
    session.add(new_discipline)
    session.commit()
    print(
        f"Discipline {name} created with ID {new_discipline.id} and assigned to teacher with ID {new_discipline.teacher_id}"
    )


def update_discipline(id, name, teacher_id):
    discipline = session.query(Discipline).filter_by(id=id).first()
    discipline.name = name
    discipline.teacher_id = teacher_id
    session.commit()
    print(
        f"Discipline name with ID {discipline.id} has been updated to {name} and assigned to teacher with ID {discipline.teacher_id}"
    )


def remove_discipline(id):
    discipline = session.execute(
        select(Discipline).filter_by(id=id)
    ).scalar_one_or_none()
    session.delete(discipline)
    session.commit()
    print(f"Discipline with ID {discipline.id} has been removed")


def list_disciplines(id=None):
    if id:
        result = session.query(Discipline).where(Discipline.id == id).all()
    else:
        result = session.query(Discipline).all()
    for discipline in result:
        print(f"ID: {discipline.id}, Full Name: {discipline.name}")


"""Groups"""


def create_group(name):
    new_group = Group(name)
    session.add(new_group)
    session.commit()
    print(f"Group {name} created with ID {new_group.id}")


def update_group(id, name):
    group = session.query(Group).filter_by(id=id).first()
    group.name = name
    session.commit()
    print(f"Group name with ID {group.id} has been updated to {name}")


def remove_group(id):
    group = session.execute(select(Group).filter_by(id=id)).scalar_one_or_none()
    session.delete(group)
    session.commit()
    print(f"Group {group.name} has been removed")


def list_groups(id=None):
    if id:
        result = session.query(Group).where(Group.id == id).all()
    else:
        result = session.query(Group).all()
    for group in result:
        print(f"ID: {group.id}, Full Name: {group.name}")


"""Students"""


def create_student(name, group_id):
    new_student = Student(name, group_id)
    session.add(new_student)
    session.commit()
    print(
        f"Student {name} created with ID {new_student.id} and assigned to group with ID {new_student.group_id}"
    )


def update_student(id, name, group_id):
    student = session.query(Student).filter_by(id=id).first()
    student.fullname = name
    student.group_id = group_id
    session.commit()
    print(
        f"Student name with ID {student.id} has been updated to {name} and assigned to group with ID {student.group_id}"
    )


def remove_student(id):
    student = session.execute(select(Student).filter_by(id=id)).scalar_one_or_none()
    session.delete(student)
    session.commit()
    print(f"Student with ID {student.id} has been removed")


def list_students(id=None):
    if id:
        result = session.query(Student).where(Student.id == id).all()
    else:
        result = session.query(Student).all()
    for student in result:
        print(
            f"ID: {student.id}, Full Name: {student.fullname}, GroupID: {student.group_id}"
        )


if __name__ == "__main__":
    pass
    # create_teacher('Nikita Bazhenov')
    # update_teacher(6, 'Sasha Petrov')
    # remove_teacher(6)
    # create_discipline("Management", 2)
    # update_discipline(9, "Business")
    # remove_discipline(9)
    # create_group('TT-1')
    # update_group(4, 'TT-2')
    # remove_group(4)
    # create_student('Nikita Bazhenov', 5)
    # update_student(52, 'Stas Petrenko', 1)
    # remove_student(52)
    # list_teachers(2)
    # list_disciplines(2)
    list_students(50)
