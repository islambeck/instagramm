from instagramm.models import *

posts = Post.objects.all()

posts_postman = Post.objects.filter(title='Postman')

posts_filter = posts_postman.filter(body='body')

posts_2023 = Post.objects.filter(date_posted__year=2023)

post_windows = Post.objects.filter(body__startswith='Windows',date_posted__year=2022)

posts = Post.objects.filter(date_posted__year=2021)

posts = Post.objects.get(id=1)

posts= Post.objects.get(date_updated__year=2023)


posts = Post.objects.filter(date_updated__year=2024).first()

posts = Post.objects.exclude(date_posted__year=2023).filter(title_startswith='Linux')

posts = Post.objects.all().order_by('id')
posts = Post.objects.all().order_by('title')

posts = Post.objects.all().order_by('-title')

posts = Post.objects.all().values('value')
posts = Post.objects.all().values('title', 'body')

posts = Post.objects.all().values_list('title', 'body')

posts = Post.objects.all().values_list('title', flat=True)

posts = Post.objects.all().none()

comments = Comment.objects.all()

comments = Comment.objects.all().select_related('post','user','post__user')
# select_related получает bnner join

###prefetch related =

posts = Post.objects.all()

posts = Post.objects.all()[0:2]

post = Post.objects.all().order_by('-id'[0])

post  = Post.objects.filter(id=250)[0]

posts = Post.objects.all().only('title', 'body')

###filter lookup type

posts = Post.objects.filter(date_posted__lte='2022-12-31')

post = Post.objects.filter(date_posted__gte='2022-12-31')

post = Post.objects.filter(date_posted__gt='2022-12-31')

post = Post.objects.filter(tile__iexact='post about program')

posts = Post.objects.filter(title__contains='program')

posts = Post.objects.filter(title__icontains='program')


posts = Post.objects.filter(id__in=[3, 4])


comments = Comment.objects.filter(post__title__incontains='program')

comments = Comment.objects.filter(post__user__username__startswith='adm')

posts = Post.objects.filter(date__posted__year=2022, title__icontains='program')

from django.db.models import Q


posts = Post.objects.filter(Q(date__posted__year=2022) | Q(title__icontains='postman'))


posts = Post.objects.filter(
    (Q(date__posted__year=2022) | Q(title__icontains='postman'))&
    (Q(body__icontains='gamin'))
)