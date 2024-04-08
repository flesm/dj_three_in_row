from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .db import SQLiteDB

Database = SQLiteDB("db.sqlite3")


class UserView(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        score = data.get('score')

        total_score = Database.get_team_score(name)
        Database.update_team_total_score(name, int(score)+int(total_score))

        return HttpResponse(status=200)


class TeamView(APIView):
    def get(self, request):
        output = []

        teams = Database.get_teams()

        for team_data in teams:
            output.append({
                'id': team_data[0],
                'name': team_data[1],
                'total_score': team_data[2]
            })

        return Response(output)
