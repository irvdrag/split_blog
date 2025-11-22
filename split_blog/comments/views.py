from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from post.models import Post
from .models import Comment
from .forms import CommentForm
from django.http import HttpResponseForbidden
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_id = request.POST.get('parent_id')  # para respuestas
            parent_obj = Comment.objects.get(id=parent_id) if parent_id else None

            Comment.objects.create(
                post=post,
                user=request.user,
                content=form.cleaned_data['content'],
                parent=parent_obj
            )
    return redirect(post.get_absolute_url())

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Solo el autor puede borrar
    if comment.user != request.user:
        return HttpResponseForbidden("No tienes permiso para borrar este comentario.")

    post_url = comment.post.get_absolute_url()  # Guardamos la URL del post antes de borrar

    comment.delete()  # Se borra el comentario (y sus respuestas)

    return redirect(post_url)