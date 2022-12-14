from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import SignUpForm
from .models import Room , Message

def homepage(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})

@login_required
def joinRoom(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    members = User.objects.all()
    newContext = { }
    context = { }
    i = 0
    for member in members:
        for message in messages:
            if member.username == message.user.username:
                context = {
                    'member': message.user.username,
                    'message': message.content,
                    'dttime': message.data_added
                }
        newContext[i] = context
        i +=1
        if len(newContext) == len(members):
            break
    print(newContext)


    return render(request, 'singleRoom.html', {'room': room , 'messages': messages, 'context': newContext})


