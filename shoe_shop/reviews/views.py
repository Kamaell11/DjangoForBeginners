from django.shortcuts import render, get_object_or_404, redirect

from .models import Review
from .forms import ReviewForm
from shop.models import Shoe

def product_reviews(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    reviews = Review.objects.filter(shoe=shoe).order_by("-created_at")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shoe = shoe
            review.user = request.user
            review.save()
            return redirect("product_details", shoe_id=shoe.id)
    else:
        form = ReviewForm()

    return render(request, "reviews/review_section.html", {
        "shoe": shoe,
        "reviews": reviews,
        "form": form,
    })
