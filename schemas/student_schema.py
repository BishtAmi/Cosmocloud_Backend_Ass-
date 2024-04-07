def student_serializer(student):
    address = student.get('address', {})
    return {
        'id': str(student["_id"]),  # Assuming 'id' should be the same as 'name' for this example
        'name': str(student["name"]),
        'age': int(student["age"]),
        'address': {
            'city': address.get('city',''),
            'country': address.get('country','')
        }
    }
def students_serializer(students) -> list:
    return [student_serializer(student) for student in students]
