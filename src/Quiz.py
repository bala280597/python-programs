class Test :
    question_data = [
        {"text": "A slug's blood is green.", "answer": "True"},
        {"text": "The loudest animal is the African Elephant.", "answer": "False"},
        {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
        {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
        {
            "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
            "answer": "True"},
        {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
         "answer": "False"},
        {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
        {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
        {"text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
        {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
        {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
    ]
import random
class Quiz(Test):
    def __init__(self):
        self.question_data = super().question_data
        self.count=0
    def get_question(self):
        random_option = random.choice(self.question_data)
        question = random_option['text']
        answer = random_option['answer']
        return question,answer

    def delete_from_list(self,question):
        k = 0
        for i in self.question_data:
            if i['text'] == question:
                break
            k += 1
        del self.question_data[k]

    def check_list(self):
        if not self.question_data:
            return True
    def validate_response(self,answer,response):
        if answer == response:
            self.count += 1
            return self.count,1
        else:
            print('Answer is Wrong')
            return self.count,0

quiz = Quiz()
while True:
    q,a = quiz.get_question()
    quiz.delete_from_list(q)
    if quiz.check_list():
        print('You won!!!!')
        break
    print(q)
    get_response = input("Answer the following : True/False")
    count,response = quiz.validate_response(a,get_response)
    if response == 1:
        continue
    else:
        print('You Lost')
        break
print('score is',count)
