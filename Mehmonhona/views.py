from django.shortcuts import render, get_object_or_404, redirect
from .models import Room,Deal,User
from django.utils import timezone
def home(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,

    }
    return render(request, 'home.html', context)

def deal(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        end_time = request.POST.get('end_time')

        Deal.objects.create(
            id_user=request.user,
            id_room=room.id_room_type,
            start_time=timezone.now(),
            end_time=end_time
        )

        room.is_active = False
        room.save()

        return render(request, 'deal_success.html', {'room': room.id_room_type})

    return render(request, 'deal.html', {'room': room.id_room_type})
from django.shortcuts import render
from .models import User  # <-- o‘zingiz yozgan User model

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        surname = request.POST.get('surnamename')
        seria_id = request.POST.get('seria')
        phone = request.POST.get('phone')


        User.objects.create(
            name=name,
            surname=surname,
            seria_id=seria_id,
            phone=phone
        )

        return render(request, 'user_success.html', {'username': name})

    return render(request, 'add_user.html')





