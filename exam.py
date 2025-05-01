class Exam:
    subject = "Math"

    def __init__(self, mark):
        self.mark = mark

    def attend_to_exam(self, name):
        self.name = name
        return f'Congratulation {name} for attending the exam, good luck'
    
    def get_marks(self):
        return f'You got {self.mark} marks'
    

mukto = Exam(80)
print(mukto.attend_to_exam("Mukto"))
print(mukto.get_marks())