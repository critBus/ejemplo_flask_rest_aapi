from flask_restx import Resource,Namespace
from .dto import course_dto,student_dto,course_input_dto,student_input_dto
from .extencions import db
from .models import Course, Student

ns=Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"message":"Hello World"}

@ns.route("/courses")
class CoursesListAPI(Resource):

    @ns.marshal_list_with(course_dto)
    def get(self):
        return Course.query.all()

    @ns.expect(course_input_dto)
    @ns.marshal_with(course_dto)
    def post(self):
        payload=ns.payload
        name=payload["name"]
        course=Course(name=name)
        db.session.add(course)
        db.session.commit()
        return course,201

@ns.route("/courses/<int:id>")
class CoursesDetailAPI(Resource):
    @ns.marshal_with(course_dto)
    def get(self,id):
        course=Course.query.get(id)
        return course,200
    @ns.expect(course_input_dto)
    @ns.marshal_with(course_dto)
    def put(self,id):
        payload=ns.payload
        name=payload["name"]
        course=Course.query.get(id)
        course.name=name
        db.session.commit()
        return course

    def delete(self,id):
        course=Course.query.get(id)
        db.session.remove(course)
        db.session.commit()
        return {},204



@ns.route("/students")
class StudentsListAPI(Resource):
    @ns.marshal_list_with(student_dto)
    def get(self):
        return Student.query.all()

    @ns.expect(student_input_dto)
    @ns.marshal_with(student_dto)
    def post(self):
        payload=ns.payload
        name=payload["name"]
        course_id=payload["course_id"]
        student=Student(name=name,course_id=course_id)
        db.session.add(student)
        db.session.commit()
        return student,201


@ns.route("/students/<int:id>")
class StudentDetailAPI(Resource):
    @ns.marshal_with(student_dto)
    def get(self, id):
        student=Student.query.get(id)
        return student
    @ns.expect(student_input_dto)
    @ns.marshal_with(student_dto)
    def put(self,id):
        payload=ns.payload
        name=payload["name"]
        student=Student.query.get(id)
        student.name=name
        db.session.commit()
        return student

    def delete(self,id):
        student=Student.query.get(id)
        db.session.remove(student)
        db.session.commit()
        return {},204
