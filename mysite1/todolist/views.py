from django.shortcuts import render, get_object_or_404, redirect
from .models import Diary, Comment
from django.utils import timezone
from .forms import DiaryForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.


def index(request):

   page=request.GET.get('page','1')

   diary_list = Diary.objects.order_by('-create_date')

   paginator=Paginator(diary_list, 10)
   page_obj=paginator.get_page(page)

   context = {'diary_list': page_obj}
   return render(request, 'todolist/diary_list.html', context)


def detail(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    context = {'diary': diary}
    return render(request, 'todolist/diary_detail.html', context)


def comment_create(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.diary = diary
            comment.save()
            return redirect('todolist:detail', diary_id=diary.id)
    else:
        form = CommentForm()

    context = {'diary': diary, 'form': form}
    return render(request, 'todolist/diary_detail.html', context)

    diary.comment_set.create(content=request.POST.get(
        'content'), create_date=timezone.now())
    return redirect('todolist:detail', diary_id=diary.id)


def diary_create(request):

    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.create_date = timezone.now()
            diary.save()
            return redirect('todolist:index')
    else:
        form = DiaryForm()

    context = {'form': form}
    return render(request, 'todolist/diary_form.html', context)
