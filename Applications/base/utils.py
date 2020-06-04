from .models import Post, Category, SocialNetworks, Web
from django.core.paginator import Paginator
def Consult(id):
    try:
        return Post.objects.get(id=id)
    except:
        return None

def GetSocial():
    return SocialNetworks.objects.filter(state=True).latest('creationDate')

def GetWeb():
    return Web.objects.filter(state=True).latest('creationDate')


def GenCategory(CategoryName, request):
    MainPosts = Post.objects.filter(
                state = True,
                published = True,
                category= Category.objects.get(name = CategoryName)
                )

    try:
        category = Category.objects.get(name = CategoryName)
    except:
        category = None
    
    paginator = Paginator(MainPosts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    Context ={
        'MainPosts':posts,
        'Socials':GetSocial,
        'Web':GetWeb,
        'Category':category
    }
    return Context
