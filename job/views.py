from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.urls import reverse
# Create your views here.


def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj
    }
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):
    job_detail = get_object_or_404(Job, pk=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
            print('done ')

    form = ApplyForm()
    context = {
        'job': job_detail,
        'form': form
    }
    return render(request, 'job/job_details.html', context)


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))

    form = JobForm()

    context = {
        'form': form
    }
    return render(request, 'job/add_job.html', context)
