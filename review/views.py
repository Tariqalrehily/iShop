from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
import datetime


def reviews_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews_list.html', context)


@login_required()
def add_review(request):
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
            return HttpResponseRedirect(reverse('products'))
        """
        return an HttpResponseRedirect after successfully dealing
        with POST data. This prevents data from being posted twice if a
        user hits the Back button.
        """
        return HttpResponseRedirect(reverse('add_review'))

    return render(request, 'add_review.html', {'form': form})