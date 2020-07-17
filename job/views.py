from django.shortcuts import render, get_object_or_404
from .models import Job
from django.core.paginator import Paginator
# Create your views here.


def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj
    }
    return render(request, 'job/job_list.html', context)


def job_details(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    context = {
        'job': job_detail
    }
    return render(request, 'job/job_details.html', context)
