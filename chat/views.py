from django.shortcuts import render

from django.views import View



class RoomView(View):
    def get(self, request, room_name):
        context = {
            'room_name': room_name
        }

        return render(request=request, template_name='chat/chat.html', context=context)

