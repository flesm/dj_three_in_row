from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team


class UserView(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        score = data.get('score')
        # name = request.POST.get('name')
        # score = request.POST.get('score')

        team = get_object_or_404(Team, name=name)
        team.total_score += int(score)
        team.save()

        return HttpResponse(status=200)

        # def get(self, request):
        #     output = [
        #         {
        #             'session_key': output.session_key,
        #             'score': output.score,
        #             'team_id': output.score
        #         } for output in User.objects.all()
        #     ]
        #     return Response(output)

        # def post(self, request):
        #     serializer = UserSerializer(data=request.data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #         return Response(serializer.data)


class TeamView(APIView):
    def get(self, request):
        output = [
            {
                'id': output.id,
                'name': output.name,
                'total_score': output.total_score
            } for output in Team.objects.all()
        ]
        return Response(output)


# def get_or_create_user(request):
#     session_key = request.session.session_key
#     # team = Team.objects.get(id_team=1)  # зрабіць функцыянал выбару каманды
#     if not session_key:
#         request.session.save()
#         session_key = request.session.session_key
#         user = User.objects.create(session_key=session_key, score=300, team_id=3)
#     else:
#         user = User.objects.get(session_key=session_key)
#
#     return user
#
#
# def login(request):  # дзе будзе запускацца функцыя get_or_create_user калі мы выдалім login
#     # user = get_or_create_user(request)
#     user = User.objects.get(session_key='wayv5mujwo2egyyot748euxo7hads519')
#     user.score = 440
#     user.save()
#     return render(request, 'game/login.html', {'user': user})