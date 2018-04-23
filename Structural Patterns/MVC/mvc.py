# We are going to use MVC pattern to implement a Student information query system.

class Student_Model(object):
    def __init__(self, name=None, enroll_status=None, gpa=None):
        self.name = name
        self.enroll_status = enroll_status
        self.gpa = gpa

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_enroll_status(self, enroll_status):
        self.enroll_status = enroll_status

    def get_enroll_status(self):
        return self.enroll_status

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

class Student_View(object):
    def show_student_information(self, student_name, student_enroll_status, student_gpa):
        print("Name:", student_name, " Enroll Status:", student_enroll_status, "GPA:", student_gpa)

class Student_Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_student_information(self):
        self.view.show_student_information(self.model.get_name(), self.model.get_enroll_status(), self.model.get_gpa())

    def add_new_student(self, name, enroll_status, gpa):
        self.model.set_name(name)
        self.model.set_enroll_status(enroll_status)
        self.model.set_gpa(gpa)

    def update_student_info(self, name=None, enroll_status=None, gpa=None):
        if name is not None:
            self.model.set_name(name)

        if enroll_status is not None:
            self.model.set_enroll_status(enroll_status)

        if gpa is not None:
            self.model.set_gpa(gpa)

if __name__ == '__main__':
    model = Student_Model()
    view = Student_View()
    controller = Student_Controller(model, view)

    controller.add_new_student("Jason", "part-time", "3.70")
    controller.show_student_information()

    controller.update_student_info(enroll_status="full-time", gpa="4.00")
    controller.show_student_information()
