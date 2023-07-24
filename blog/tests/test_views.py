from django.test import TestCase
from django.urls import reverse
from blog.models import BlogPost, BlogAuthor
from django.contrib.auth.models import User

# Create your tests here.
from datetime import datetime
class BlogPostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='teste', password='123456')
        author = BlogAuthor.objects.create(user=user, bio='Lorem Ipsum Dolor Sit Amet')
        
        for i in range(9):
            BlogPost.objects.create(name=f'Lorem {i}', description='Lorem Ipsum Dolor Sit Amet', author=author, post_date=datetime.now())
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_list.html')
    
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blogpost_list']), 5)

    def test_lists_all_blog_posts(self):
        response = self.client.get(reverse('blog-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blogpost_list']), 4)

class BlogCommentCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create(username='Teste', password='123456')
        author = BlogAuthor.objects.create(user=user, bio='Lorem Ipsum Dolor Sit Amet')
        post = BlogPost.objects.create(name='Lorem', description='Lorem Ipsum Dolor Sit Amet', author=author, post_date=datetime.now())
   
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('comment-create', args=['1']))
        self.assertRedirects(response, '/accounts/login/?next=/blog/b/1/create/')