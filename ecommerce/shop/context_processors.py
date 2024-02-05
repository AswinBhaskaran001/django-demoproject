from shop.models import Category
def nav_link(request):
    c=Category.objects.all()
    return {'links':c}