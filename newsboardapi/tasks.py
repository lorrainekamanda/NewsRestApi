from newsboardproject.celery import app
from .models import Post

@app.task
def restart_votes():
    post_counts= Post.objects.all().iterator()
    for post in post_counts:
        post.upvotes.clear()


