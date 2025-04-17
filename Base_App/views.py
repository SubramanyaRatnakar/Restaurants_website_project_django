from django.shortcuts import render,HttpResponse,redirect
from Base_App.models import ItemList,Items,AboutUs,Feedback,BookTable
from django.shortcuts import render
from .models import Items, Feedback
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
# Create your views here.
def Home_view(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()  # Renamed variable
    review = Feedback.objects.all()
    return render(request, "home.html" , {'items': items, 'categories': categories,'review':review})


def About_view(request):
    data = AboutUs.objects.all()
    return render(request, "about.html",{'data':data})


def Menu_view(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()  # Renamed variable
    return render(request, "menu.html", {'items': items, 'categories': categories})


def Book_table_view(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        total_person = request.POST.get("total_person")
        booking_date = request.POST.get("booking_date")
        
        if user_name and phone_number and email and total_person and booking_date:
            BookTable.objects.create(
                user_name=user_name,
                phone_number=phone_number,
                email=email,
                total_person=total_person,
                booking_date=booking_date
            )
            return redirect("book_table")  # 👈 Redirect after success
    return render(request, "book_table.html")

def feedback(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name", "").strip()
        description = request.POST.get("description", "").strip()
        rating = request.POST.get("rating", "").strip()
        image = request.FILES.get("image")  # ✅ Capture image from request.FILES

        if user_name and description and rating:
            feedback_entry = Feedback(user_name=user_name, description=description, rating=rating, image=image)
            feedback_entry.save()
            return redirect("feedback")  # ✅ Redirect after saving

    return render(request, "feedback.html")


def dashboard(request):
    total_users = User.objects.count()
    new_users_week = User.objects.filter(date_joined__gte=now() - timedelta(days=7)).count()
    total_items = Items.objects.count()
    total_feedbacks = Feedback.objects.count()

    # Example: Top 5 most recent feedbacks
    recent_feedbacks = Feedback.objects.order_by('-id')[:5]

    # Item popularity (dummy count - assuming each Item has a field 'orders')
    item_names = [item.name for item in Items.objects.all()]
    item_counts = [item.orders if hasattr(item, 'orders') else 0 for item in Items.objects.all()]

    context = {
        'total_users': total_users,
        'new_users_week': new_users_week,
        'total_items': total_items,
        'total_feedbacks': total_feedbacks,
        'recent_feedbacks': recent_feedbacks,
        'item_names': item_names,
        'item_counts': item_counts,
    }
    return render(request, 'dashboard.html', context)
