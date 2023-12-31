from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from first.models import Sport, Hall, Event, Comment, Like, Dislike


# Create your views here.
class IndexView(View):
    def get(self, request):
        recent_events = Event.objects.order_by('-id')[:3]
        halls = Hall.objects.all()

        return render(request, 'base.html', {'recent_events': recent_events, 'halls': halls})


class LoginView(View):
    def get(self, request):
        return render(request, 'login_page.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login_page.html', {'error': 'Błędne dane logowania. Spróbuj ponownie.'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class CreateUserView(View):
    def get(self, request):
        return render(request, 'create_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'create_user.html', {'error': 'Hasła się nie zgadzają. Spróbuj ponownie.'})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return render(request, 'base.html')


class AddSportView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'add_sport.html')

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')

        nowy_sport = Sport(name=name, description=description)
        nowy_sport.save()

        return redirect('index')


class AddHallView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        sports = Sport.objects.all()
        return render(request, 'add_hall.html', {'sports': sports})

    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')

        nowa_hala = Hall(name=name, address=address)
        nowa_hala.save()

        return redirect('index')


class AddEventView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        halls = Hall.objects.all()
        sports = Sport.objects.all()
        return render(request, 'add_event.html', {'halls': halls, 'sports': sports})

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        hall_id = request.POST.get('hall')
        sport_id = request.POST.get('sport')
        price = request.POST.get('price')
        date = request.POST.get('date')

        hall = Hall.objects.get(id=hall_id)
        sport = Sport.objects.get(id=sport_id)

        nowe_wydarzenie = Event(name=name, description=description, hall=hall, sport=sport, price=price, date=date)
        nowe_wydarzenie.save()

        return redirect('show_event')


class JoinEventView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        events = Event.objects.all()
        return render(request, 'join_event.html', {'events': events})

    def post(self, request):
        event_id = request.POST.get('event')
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user  # User.objects.get(pk=user_id)
        if user_id:

            try:
                event = Event.objects.get(pk=event_id)
                if event.users.filter(id=user_id).exists():
                    events = Event.objects.all()
                    return render(request, 'join_event.html', {'events': events})
                else:
                    event.users.add(user)
                    event.save()
                    events = Event.objects.all()
                    return render(request, 'join_event.html', {'events': events})
            except Event.DoesNotExist:
                events = Event.objects.all()
                return render(request, 'join_event.html', {'events': events})


class EditEventView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        halls = Hall.objects.all()
        sports = Sport.objects.all()
        return render(request, 'edit_event.html', {'event': event, 'halls': halls, 'sports': sports})

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        hall_id = request.POST.get('hall')
        sport_id = request.POST.get('sport')
        event.price = request.POST.get('price')
        event.date = request.POST.get('date')

        hall = Hall.objects.get(id=hall_id)
        sport = Sport.objects.get(id=sport_id)

        event.hall = hall
        event.sport = sport

        event.save()

        events = Event.objects.order_by('-id')[:5]
        return render(request, 'show_event.html', {'events': events})


class DeleteEventView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
            event.delete()
        except Event.DoesNotExist:
            pass
        return redirect('show_event')


class AddCommentView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        text = request.POST.get('comment_text')
        if text:
            Comment.objects.create(event=event, user=request.user, text=text)
        return redirect('event_detail', event_id=event_id)


class LikeEventView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        like, created = Like.objects.get_or_create(event=event, user=request.user)
        if not created:
            like.delete()
        return redirect(reverse('show_event'))


class DislikeEventView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        dislike, created = Dislike.objects.get_or_create(event=event, user=request.user)
        if not created:
            dislike.delete()
        return redirect(reverse('show_event'))


class ShowEventView(View):
    def get(self, request):
        events = Event.objects.order_by('-id')[:5]
        likes = {}
        dislikes = {}
        for event in events:
            likes[event.id] = event.likes.count()
            dislikes[event.id] = event.dislikes.count()
        return render(request, 'show_event.html', {'events': events, 'likes': likes, 'dislikes': dislikes})


class AddCommentView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # 'login' to nazwa twojego adresu URL dla strony logowania
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(event=event, user=request.user, text=text)
        return redirect('show_event')
