# **CRUD Operations CLI**

This command-line interface (CLI) performs CRUD (Create, Read, Update, Delete) operations on different models. It uses argparse for command-line argument parsing and Python's **`match-case`** structure for routing actions.

## **Usage**

You can perform CRUD operations on the following models:

- Teacher
- Student
- Group
- Discipline

The CLI accepts the following command-line arguments:

- **`a`**, **`-action`**: The action to perform. It can be one of **`create`**, **`list`**, **`update`**, or **`remove`**.
- **`m`**, **`-model`**: The model to perform the action on. It can be one of **`Teacher`**, **`Student`**, **`Group`**, or **`Discipline`**.
- **`n`**, **`-name`**: The name to use when creating or updating a record.
- **`id`**: The ID of the record to update or remove.
- **`tid`**, **`-teacher`**: The teacher ID to use when creating or updating a discipline.
- **`gid`**, **`-group`**: The group ID to use when creating or updating a student.

Here are some example usages:

```

# Create a new Teacher
python3 main.py -a create -m Teacher -n "John Doe"

# List all Teachers
python3 main.py -a list -m Teacher

# Update a Teacher with ID 1
python3 main.py -a update -m Teacher -n "Jane Doe" -id 1

# Remove a Teacher with ID 1
python3 main.py -a remove -m Teacher -id 1

# And similarly for other models

```

To list a specific record, you can pass its ID as an argument:

```

# List a Teacher with ID 1
python3 main.py -a list -m Teacher -id 1

```

## **Note**

Please make sure that the database configuration in **`src/db.py`** is correct before running the program.
