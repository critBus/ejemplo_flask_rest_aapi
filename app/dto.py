from flask_restx import fields
from .extencions import api
from .models import Student

course_input_dto= api.model('CourseInput', {
    'name': fields.String,
})

course_dto= api.model('Course',{
    'id': fields.Integer,
    'name': fields.String,
    # 'students': fields.List(fields.Nested(Student))
})
student_dto= api.model('Student',{
    'id': fields.Integer,
    'name': fields.String,
    'course': fields.Nested(course_dto)
})


student_input_dto= api.model('StudentInput',{
    'name': fields.String,
    'course_id': fields.Integer
})