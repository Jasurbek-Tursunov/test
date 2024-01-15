from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Question, Answer
from app.serializer import QuestionSerializer, AnswerSerializer


class QuestionViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSets(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(url_path='results', detail=False, methods=['post'])
    def get_results(self, request):
        try:
            questions = self.request.data.get('results')
            response = {}
            for question in questions:
                true_answers = []
                question_text = question.get('question').replace(' ', '')
                answers = Answer.objects.filter(question__text__icontains=question_text)
                if answers.exists():
                    for answer in answers:
                        options = question.get('options')
                        for option in options:

                            if answer.text == option.get('answer').replace(' ', ''):
                                true_answers.append(option.get('id'))

                            else:
                                continue

                    response.update({question.get('id'): true_answers})

                else:
                    continue

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
