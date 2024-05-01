import json
from django.http import JsonResponse, HttpResponse
from .models import *
from django.shortcuts import get_object_or_404, get_list_or_404

def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()

        return JsonResponse({'message':'success!!!!!'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id' : post.pk,
        '제목' : post.title,
        '내용' : post.content,
        '메시지' : '조회 성공'
    }
    return JsonResponse(data, status=200)

def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all()
        return HttpResponse(comment_list, status=200)

def like(request):
    if request.method == 'POST':
        if UserPost.objects.filter(user_id=user_id, post_id=post_id).exists():
            return HttpResponse("이미 좋아요를 눌렀습니다.", status=409)
        
        data = json.loads(request.body)

        user_id = data.get('user_id')
        post_id = data.get('post_id')

        like = UserPost(
            user_id = user_id,
            post_id = post_id
        )
        like.save()

    return HttpResponse(status=204)
    
def get_like(request, post_id):
    if request.method == 'GET':
        post = get_list_or_404(UserPost, pk=post_id)
        return HttpResponse(len(post), status=200)
    return HttpResponse(status=204)

# def allUser(request):
#     if request.method == 'GET':
#         post = UserPost.objects.all()

#         post_comment_counts = []

#         for tmp in post:


#         return JsonResponse(data, status = 200)
#     return JsonResponse({'message':'GET 요청만 허용됩니다.'})

