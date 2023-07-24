from django.test import TestCase
from blog.models import BlogAuthor, BlogPost, BlogComment
from django.contrib.auth.models import User

# Create your tests here.

class BlogAuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='teste', password='123456')
        BlogAuthor.objects.create(user=user, bio='Lorem Ipsum Dolor Sit Amet')
    
    def test_author_user_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('user').verbose_name
        
        self.assertEqual(field_label, 'user')
        
    def test_author_bio_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        
        self.assertEqual(field_label, 'bio')
    
    def test_author_bio_max_length(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        
        self.assertEqual(max_length, 1000)
    
    def test_object_name_is_user_username(self):
        author = BlogAuthor.objects.get(id=1)
        expected_name = author.user.username
        
        self.assertEqual(str(author), expected_name)
    
    def test_author_get_absolute_url(self):
        author = BlogAuthor.objects.get(id=1)
        
        self.assertEqual(author.get_absolute_url(), '/blog/blogger/1/')
    
from datetime import datetime
class BlogPostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='teste', password='123456')
        author = BlogAuthor.objects.create(user=user, bio='Lorem Ipsum Dolor Sit Amet')
        now = datetime.now()
        BlogPost.objects.create(name='Lorem', description='Lorem Ipsum Dolor Sit Amet', author=author, post_date=now)
    
    def test_post_name_label(self):
        post = BlogPost.objects.get(id=1)
        label = post._meta.get_field('name').verbose_name
        
        self.assertEqual(label, 'name')
    
    def test_post_description_label(self):
        post = BlogPost.objects.get(id=1)
        label = post._meta.get_field('description').verbose_name
        
        self.assertEqual(label, 'description')
    
    def test_post_author_label(self):
        post = BlogPost.objects.get(id=1)
        label = post._meta.get_field('author').verbose_name
        
        self.assertEqual(label, 'author')
    
    def test_post_post_date_label(self):
        post = BlogPost.objects.get(id=1)
        label = post._meta.get_field('post_date').verbose_name
        
        self.assertEqual(label, 'post date')
    
    def test_post_name_max_length(self):
        post = BlogPost.objects.get(id=1)
        max_length = post._meta.get_field('name').max_length
        
        self.assertEqual(max_length, 200)
    
    def test_post_description_max_length(self):
        post = BlogPost.objects.get(id=1)
        max_length = post._meta.get_field('description').max_length
        
        self.assertEqual(max_length, 1000)
    
    def test_post_object_name_is_name(self):
        post = BlogPost.objects.get(id=1)
        expected_name = post.name
        
        self.assertEqual(expected_name, str(post))
    
    def test_post_get_absolute_url(self):
        post = BlogPost.objects.get(id=1)
        
        self.assertEqual(post.get_absolute_url(), '/blog/b/1/')
    
class BlogCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='teste', password='123456')
        author = BlogAuthor.objects.create(user=user, bio='Lorem Ipsum Dolor Sit Amet')
        now = datetime.now()
        post = BlogPost.objects.create(name='Lorem', description='Lorem Ipsum Dolor Sit Amet', author=author, post_date=now)
        BlogComment.objects.create(description='Lorem Ipsum Dolor Sit Amet', post_date=now, author=user, blog=post)
    
    def test_comment_description_label(self):
        comment = BlogComment.objects.get(id=1)
        label = comment._meta.get_field('description').verbose_name
        
        self.assertEqual(label, 'description')
    
    def test_comment_post_date_label(self):
        comment = BlogComment.objects.get(id=1)
        label = comment._meta.get_field('post_date').verbose_name
        
        self.assertEqual(label, 'post date')
    
    def test_comment_author_label(self):
        comment = BlogComment.objects.get(id=1)
        label = comment._meta.get_field('author').verbose_name
        
        self.assertEqual(label, 'author')
    
    def test_comment_blog_label(self):
        comment = BlogComment.objects.get(id=1)
        label = comment._meta.get_field('blog').verbose_name
        
        self.assertEqual(label, 'blog')
    
    def test_comment_description_max_length(self):
        comment = BlogComment.objects.get(id=1)
        max_length = comment._meta.get_field('description').max_length
        
        self.assertEqual(max_length, 500)
    
    def test_comment_name_is_description(self):
        comment = BlogComment.objects.get(id=1)
        expected_name = comment.description
        
        self.assertEqual(expected_name, str(comment))
    
    def test_comment_truncate_str(self):
        comment = BlogComment.objects.get(id=1)
        
        comment.description = 'a' * 75
        expected_description = comment.description
        self.assertEqual(comment.truncate_str(), expected_description)
        
        comment.description = 'a' * 76
        expected_description = 'a' * 75 + ' ...'
        self.assertEqual(comment.truncate_str(), expected_description)