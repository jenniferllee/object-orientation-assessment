"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   ENCAPSULATION: You can combine data and functionality in a package or
   "capsule" so that similar ideas are organized together.
   ABSTRACTION: You can hide details that are not crucial in understanding
   the functionality. It is similar to the mechanics of a doorknob. You do not
   need to know how the strings/pulleys in the doorknob work to know how to
   use a doorknob.
   POLYMORPHISM: Compatible components can be interchangeable.

2. What is a class?
    A class is a "type" of thing. For example, lists, strings, and files
    are classes. If you check the type of a class, it will return "type".

3. What is an instance attribute?
    An instance attribute is a quality/characteristic/property of an instance.
    This attribute sticks directly to the instance itself.

4. What is a method?
    A method is a function defined on a class.

5. What is an instance in object orientation?
    An instance is an individual occurance of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is a quality/characteristic/property that usually pertains
   to most instances of that class. For example, if you have a Dog class,
   an example of a class attribute could be four-legged, because for the most
   part, all dogs have four legs. However, you can make an instance of the Dog
   class, Fido, who is a dog with three legs. Therefore, an instance attribute
   for Fido would be three legs. Fido is still a dog, and although most dogs
   have four legs, he is unique in that he only has three legs.

"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question + " > ")
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        question_to_add = Question(question, correct_answer)
        self.questions = self.questions + [question_to_add]
        return self.questions

    def administer(self):
        score = float(0)
        for question in self.questions:
            correct = question.ask_and_evaluate()
            if correct is True:
                score += 1
        final_score = score/(len(self.questions))
        return final_score


class Quiz(Exam):

    def administer(self):
        final_score = super(Quiz, self).administer()
        if final_score >= 0.5:
            return True
        else:
            return False


def take_test(exam, student):
    """ Takes an exam and student, administers the exam, and assigns the score
    to the student instance. Also print a message indicating the score. """

    student_score = exam.administer()
    student.score = student_score
    print "%s %s's score on %s is %s." % (student.first_name, student.last_name, exam.name, student.score)


def example(exam_name, student_first_name, student_last_name, student_address):
    """ Creates an exam and student, adds questions to the exam, and administers
    the exam for that student."""

    exam = Exam(exam_name)
    exam.add_question("What color is the sky?", "Blue")
    exam.add_question("What is 2 + 2?", "4")
    student = Student(student_first_name, student_last_name, student_address)
    take_test(exam, student)
