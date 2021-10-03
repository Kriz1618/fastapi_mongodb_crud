# schemas helps to serialize and also convert mongodb format json to our UI needed

def studentEntity(item) -> dict:
  return {
    'id': str(item['_id']),
    'name': str(item['student_name']),
    'email': str(item['student_email']),
    'phone': str(item['student_phone']),
  }

def listOfStudentEntity(db_item_list) -> list:
  list_students = []
  for item in db_item_list:
    list_students.append(studentEntity(item))
  return list_students