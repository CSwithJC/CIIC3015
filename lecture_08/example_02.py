class Student:
    """This class models a simple student.

    Attributes:
        first_name: A string of the student's first name.
        last_name: A string of the student's last name.
        grades: A list of integers, each of which represent a grade.
    """
    def __init__(self, first_name, last_name, grades):
        """Initializes the instance based on the student's attributes.

        Args:
            first_name: A string of the student's first name.
            last_name: A string of the student's last name.
            grades: A list of integers, each of which represent a grade.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def full_name(self):
        """Returns the student's full name."""
        return f"{self.first_name} {self.last_name}"

    def grade_point_average(self):
        """Returns the student's grade point average based on the grades thus far."""
        return sum(self.grades) / len(self.grades)

# Create a few students with the grades of their first three exams.
michael = Student(
    first_name='Michael',
    last_name='Fonseca',
    grades=[90, 80, 95]
)
olivia = Student(
    first_name='Olivia',
    last_name='Popeye',
    grades=[95, 80, 90]
)

# Get Michael's full name and grade point average.
print(michael.full_name())
print(michael.grade_point_average())
# Add a new grade to Michael's grades list and recalculate the grade average.
michael.grades.append(75)
print(michael.grade_point_average())

# Get Olivia's full name and grade point average.
print('\n')
print(olivia.full_name())
print(olivia.grade_point_average())
# Add a new grade to Olivia's grades list and recalculate the grade average.
olivia.grades.append(115)
print(olivia.grade_point_average())
