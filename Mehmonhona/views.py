from django.shortcuts import render, get_object_or_404, redirect
from .models import Room,Deal,User
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required

def home(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,

    }
    return render(request, 'home.html', context)








def bron_qilish(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    error = None

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        end_time_str = request.POST.get('end_time')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            error = "Bunday ID ga ega foydalanuvchi topilmadi!"
            return render(request, 'bron_form.html', {'room': room, 'error': error})

        end_time = parse_datetime(end_time_str)
        if end_time is None:
            error = "Iltimos, tugash vaqtini to‘g‘ri kiriting!"
            return render(request, 'bron_form.html', {'room': room, 'error': error})


        Deal.objects.create(
            id_user=user,
            id_room=room,
            end_time=end_time
        )

        return redirect('deal_success.html')

    return render(request, 'bron_form.html', {'room': room})





def add_user(request):
    if request.method == 'POST':
        seria_id = request.POST.get('id')  # foydalanuvchining passport raqami yoki ID
        name = request.POST.get('username')
        surname = request.POST.get('surnamename')
        phone = request.POST.get('phone')

        if not seria_id:
            return render(request, 'add_user.html', {'error': 'Foydalanuvchi ID (username) kiritilishi shart!'})


        user = User.objects.create_user(
            username=seria_id,
            first_name=name,
            last_name=surname,
            password='default123',

        )




        return render(request, 'user_success.html', {'username': name})

    return render(request, 'add_user.html')



from django.shortcuts import render
from django.contrib.auth.models import User

def show_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'show_users.html', context)


