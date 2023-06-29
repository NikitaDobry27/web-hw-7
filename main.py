import argparse
import crud


parser = argparse.ArgumentParser(description="CLI for CRUD operations")

parser.add_argument(
    "-a",
    "--action",
    choices=["create", "list", "update", "remove"],
    required=True,
    help="CRUD action to perform",
)
parser.add_argument(
    "-m",
    "--model",
    choices=["Teacher", "Student", "Discipline", "Grade", "Group"],
    required=True,
    help="Model to perform action on",
)
parser.add_argument("-n", "--name", type=str, help="Name for create action")
parser.add_argument("-id", "--id", type=int, help="ID for update or remove action")
parser.add_argument("-tid", "--teacher", type=int, help="Teacher id of the student")
parser.add_argument("-gid", "--group", type=int, help="Group id of the student")

args = parser.parse_args()

OPERATIONS = {
    "Teacher": {
        "create": crud.create_teacher,
        "remove": crud.remove_teacher,
        "update": crud.update_teacher,
        "list": crud.list_teachers,
    },
    "Student": {
        "create": crud.create_student,
        "remove": crud.remove_student,
        "update": crud.update_student,
        "list": crud.list_students,
    },
    "Group": {
        "create": crud.create_group,
        "remove": crud.remove_group,
        "update": crud.update_group,
        "list": crud.list_groups,
    },
    "Discipline": {
        "create": crud.create_discipline,
        "remove": crud.remove_discipline,
        "update": crud.update_discipline,
        "list": crud.list_disciplines,
    },
}


def crud_operations(action, model, name=None, id=None, tid=None, gid=None):
    model_functions = OPERATIONS.get(model)
    action_function = model_functions.get(action)

    match (action, model):
        case ("create", "Teacher" | "Group"):
            action_function(name)
        case ("create", "Discipline"):
            action_function(name, tid)
        case ("create", "Student"):
            action_function(name, gid)
        case ("list", _):
            action_function(id)
        case ("update", "Teacher" | "Group"):
            action_function(id, name)
        case ("update", "Discipline"):
            action_function(id, name, tid)
        case ("update", "Student"):
            action_function(id, name, gid)
        case ("remove", _):
            action_function(id)
        case _:
            print("Invalid action or model")


if __name__ == "__main__":
    crud_operations(
        args.action, args.model, args.name, args.id, args.teacher, args.group
    )
