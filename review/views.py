from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
import datetime
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def reviews_list(request):
    """
    Review list to disply 5 in each page
    Credit to : GoDjango
    """
    reviews = Review.objects.all().order_by('-pub_date')

    paginater = Paginator(reviews, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        reviews = paginater.page(page)
    except(EmptyPage, InvalidPage):
        reviews = paginater.page(paginater.num_pages)

    context = {'reviews': reviews}
    return render(request, 'reviews_list.html', context)


@login_required()
def add_review(request):
    """
    Allow user to add review 
    """
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        if review.save:
            review.save()
            messages.error(request, "Success! Thank you for your review!.")
            return HttpResponseRedirect(reverse("products"))
        """
        return an HttpResponseRedirect after successfully dealing
        with POST data. This prevents data from being posted twice if a
        user hits the Back button.
        """
        return HttpResponseRedirect(reverse('add_review'))

    return render(request, 'add_review.html', {'form': form})