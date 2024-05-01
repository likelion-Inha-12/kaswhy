from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20) # 20자 이하로만 작성할 수 있는 이름 필드를 가집니다.
    email = models.EmailField(unique=True) # unique 속성을 가진 email필드를 가집니다.


class Post(models.Model):
    member_id = models.ForeignKey(Member, verbose_name = "member", on_delete= models.CASCADE) # 글 작성자를 표시하기 위해 Member의 id를 fk로 가집니다.
    title = models.CharField(max_length=50) # 50글자가 최대인 문자열
    content = models.TextField(null=True, blank=True) # 글자 수 제한이 없는 긴 문자열, null, blank 허용
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성시, 현재시간 저장

    def __str__ (self): # admin에서 post 객체의 이름 설정 (해당 객체의 title로 post 객체가 보임)
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length= 200, null=True, blank = True) # 댓글 작성, 글은 200자로 제한 
    user_id = models.ForeignKey(Member, verbose_name = "member", on_delete= models.CASCADE) # member id를 fk로 가짐
    post_id = models.ForeignKey(Post,verbose_name = "post", on_delete= models.CASCADE, related_name="comments") # post id를 fk로 가짐

    def __str__(self):
        return self.content
    
class UserPost(models.Model):
    user_id = models.ForeignKey(Member, verbose_name = "member", on_delete= models.CASCADE) # member id를 fk로 가짐
    post_id = models.ForeignKey(Post,verbose_name = "post", on_delete= models.CASCADE) # post id를 fk로 가짐
