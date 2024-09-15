from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #save new user
            login(request, user) #then log the user in after registration
            return redirect('/') #redirect to home or success page
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
            return redirect('home')
            
    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect back to profile after saving

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'blog/profile.html', context)


    # crud operation to handle post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date'] #this orders by date posted
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comment.all()
        context['comment'] = comments
        context['form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
       # Save the form without committing to get a Post instance
        post = form.save(commit=False)
        post.author = self.request.user  # Set the post author to the current user
        post.save()  # Save the Post instance

        # Now that the post has a primary key, save the many-to-many tags
        form.save_m2m()  # Save the tags

        return super().form_valid(form)
    
    
    
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        # Associate the comment with the post and user
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user #set the post author to the current user
        form.instance.tags.set(*form.cleaned_data['tags'])
        return super().form_valid(form)
    
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author #only allow the author to edit post
    


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to delete the post
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'


    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        #ensure only the author of the comment can delete it
        comment = self.get_object()
        return self.request.user == comment.author

def search(request):
    query = request.GET.get('q') #get the search query from the request
    results = []

    if query:
        #search for posts based on title, content, or tags
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)  # 'tags__name' if using django-taggit
        ).distinct()   # Use distinct to avoid duplicates if a post matches multiple criteria

    return render(request, 'blog/search_results.html', {'query': query, 'results': results})

# view that filters post based on selected tags

class TagFilteredPostListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        return Post.objects.filter(tags__name=tag_name)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context