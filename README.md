# Getting Started (for Ubuntu)

## Install Python

```cmd
sudo apt install python3
```

Verify the installation was successful:

```cmd
python3 --version
```

---

## Virtual Environment

Create a folder where we can set up a **virtual environment**. Virtualenv will isolate your Python/Django setup on a per-project basis.

```cmd
mkdir django
cd django
```

Make a virtualenv called `myvenv` (you can call this something else, but needs to be lowercase & no spaces)

```cmd
python3 -m venv myvenv
```

**NOTE:** On some versions of Debian/Ubuntu you may receive the following error:

```cmd
The virtual environment was not created successfully because ensurepip is not available. On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.
   apt install python3-venv
You may need to use sudo with that command. After installing the python3-venv package, recreate your virtual environment.
```

In this case, follow the instructions above and install the python3-venv package:

```cmd
sudo apt install python3-venv
```

**NOTE:** On some versions of Debian/Ubuntu initiating the virtual environment like this currently gives the following error:

```cmd
Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
```

To get around this, use the virtualenv command instead.

```cmd
sudo apt install python-virtualenv
virtualenv --python=python3.6 myvenv
```

**NOTE:** If you get an error like

```cmd
E: Unable to locate package python3-venv
```

then instead run:

```cmd
sudo apt install python3.6-venv
```

---

## Working with virtualenv

Start your virtual environment by running:

```cmd
source myvenv/bin/activate
```

*Remember to replace `myvenv` with your chosen `virtualenv` name!*

**NOTE:** sometimes source might not be available. In those cases try doing this instead:

```cmd
. myvenv/bin/activate
```

*You will know that you have virtualenv started when you see that the prompt in your console is prefixed with (myvenv).*

---

## Installing Django

```cmd
(myvenv) ~$ python -m pip install --upgrade pip
```

---

## Installing packages with requirements

A requirements file keeps a list of dependencies to be installed using pip install:

First create a `requirements.txt` file inside of the root of the django folder.

Add the following text:

```cmd
Django~=2.0.6
```

Now, run `pip install -r requirements.txt` to install Django.

---

## Install Git, Create a GitHub account & Initialise a Git Repo

---

## Create a PythonAnywhere account

PythonAnywhere is a service for running Python code on servers "in the cloud". We'll use it for hosting our site, live and on the Internet.

We will be hosting the blog we're building on PythonAnywhere. Sign up for a "Beginner" account on PythonAnywhere (the free tier is fine, you don't need a credit card).

[www.pythonanywhere.com](www.pythonanywhere.com)

**Note:** When choosing your username here, bear in mind that your blog's URL will take the form `yourusername.pythonanywhere.com`, so choose either your own nickname or a name for what your blog is all about.

---

## Creating a PythonAnywhere API token

This is something you only need to do once. When you've signed up for PythonAnywhere, you'll be taken to your dashboard. Find the link near the top right to your "Account" page, then select the tab named "API token", and hit the button that says "Create new API token".

---

## Django

Remember to run everything in the virtualenv. If you don't see a prefix (myvenv) in your console, you need to activate your virtualenv.

```cmd
source myvenv/bin/activate
```

**Don't forget to add the period (or dot) . at the end!**

```cmd
django-admin startproject mysite .
```

*`django-admin.py` is a script that will create the directories and files for you.*

```cmd
django
├───mysite
│     settings.py
│     urls.py
│     wsgi.py
│     _init__.py
├───manage.py
└───requirements.txt
```

**Note:** in your directory structure, you will also see your venv directory that we created before.

`manage.py` is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

The `settings.py` file contains the configuration of your website.

`urls.py` file contains a list of patterns used by urlresolver.

---

## Changing Settings

In `mysite/settings.py`:

```cmd
TIME_ZONE = 'Pacific/Auckland'
LANGUAGE_CODE = 'en-nz'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

When DEBUG is `True` and `ALLOWED_HOSTS` is empty, the host is validated against `['localhost', '127.0.0.1', '[::1]']`. This won't match our hostname on PythonAnywhere once we deploy our application so we will change the following setting:

```cmd
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
```

---

## Set up a database

We'll use the default one, `sqlite3`.

This is already set up in this part of your `mysite/settings.py` file:

```cmd
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

To create a database for our blog, let's run the following in the console: `python manage.py migrate` (we need to be in the django directory that contains the manage.py file).

---

## Starting the web server

You need to be in the directory that contains the `manage.py` file (the django directory). In the console, we can start the web server by running:

```cmd
python manage.py runserver
```

Now you need to check that your website is running. Open your browser and enter this address:

```cmd
http://127.0.0.1:8000/
```

---

## Creating an Application

To keep everything tidy, we will create a separate application inside our project. It is very nice to have everything organized from the very beginning. To create an application we need to run the following command in the console (from django directory where `manage.py` file is):

```cmd
python manage.py startapp blog
```

You will notice that a new `blog` directory is created and it contains a number of files now. The directories and files in our project should look like this:

```cmd
django
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
|   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```

After creating an application, we also need to tell Django that it should use it. We do that in the file `mysite/settings.py` (open it in your code editor). We need to find `INSTALLED_APPS` and add a line containing `'blog'`, just above `]`. So the final product should look like this:

```cmd
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

---

## Creating a blog post model

In the `blog/models.py` file we define all objects called `Models` – this is a place in which we will define our blog post.

Let's open `blog/models.py` in the code editor, remove everything from it, and write code like this:

```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

*Double-check that you use two underscore characters (_) on each side of str. This convention is used frequently in Python and sometimes we also call them "dunder" (short for "double-underscore").*

---

## Create tables for models in your database

The last step here is to add our new model to our database. First we have to make Django know that we have some changes in our model. (We have just created it!) Go to your console window and type:

```cmd
python manage.py makemigrations blog
```

Django prepared a migration file for us that we now have to apply to our database. Type:

```cmd
python manage.py migrate blog
```

---

## Django admin

To add, edit and delete the posts we've just modeled, we will use Django admin.

Let's open the `blog/admin.py` file in the code editor and replace its contents with this:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

As you can see, we import (include) the Post model defined in the previous chapter. To make our model visible on the admin page, we need to register the model with `admin.site.register(Post)`.

OK, time to look at our Post model. Remember to run `python manage.py runserver` in the console to run the web server. Go to your browser and type the address `http://127.0.0.1:8000/admin/`.

To log in, you need to create a superuser - a user account that has control over everything on the site. Go back to the command line, type `python manage.py createsuperuser`, and press enter.

```cmd
python manage.py createsuperuser
```

When prompted, type your username (lowercase, no spaces), email address, and password. Don't worry that you can't see the password you're typing in – that's how it's supposed to be. Type it in and press `enter` to continue.

Return to your browser. Log in with the superuser's credentials you chose; you should see the Django admin dashboard.

Go to Posts and experiment a little bit with it. Add five or six blog posts. Don't worry about the content –- it's only visible to you on your local computer.

Make sure that at least two or three posts (but not all) have the publish date set. It will be helpful later.

If you want to know more about Django admin, you should check Django's documentation: [https://docs.djangoproject.com/en/2.0/ref/contrib/admin/](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/)

---

## Deploy - Starting your Git repository

```cmd
$ git init
Initialized empty Git repository in ~/django/.git/
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com
```

Git will track changes to all the files and folders in this directory, but there are some files we want it to ignore. We do this by creating a file called `.gitignore` in the root directory. Open up your editor and create a new file with the following contents:

```txt
*.pyc
*~
__pycache__
myvenv
db.sqlite3
/static
.DS_Store
```

---

## Pushing your code to GitHub

---

## Deploy - Configuring our site on PythonAnywhere

Go back to the main PythonAnywhere Dashboard by clicking on the logo, and choose the option to start a "Bash" console – that's the PythonAnywhere version of a command line, just like the one on your computer.

Deploying a web app on PythonAnywhere involves pulling down your code from GitHub, and then configuring PythonAnywhere to recognise it and start serving it as a web application. There are manual ways of doing it, but PythonAnywhere provides a helper tool that will do it all for you. Let's install it first:

```cmd
pip3.6 install --user pythonanywhere
```

Now we run the helper to automatically configure our app from GitHub. Type the following into the console on PythonAnywhere (don't forget to use your GitHub username in place of `<your-github-username>`, so that the URL matches the clone URL from GitHub):

```cmd
pa_autoconfigure_django.py --python=3.6 https://github.com/JacOng17/django.git
```

The main thing to notice right now is that your database on PythonAnywhere is actually totally separate from your database on your own computer, so it can have different posts and admin accounts. As a result, just as we did on your own computer, we need to initialize the admin account with createsuperuser. PythonAnywhere has automatically activated your virtualenv for you, so all you need to do is run (**Note:** *If you do get accidentally logged out of the virtualenv, go to the PythonAnywhere **Web** tab -> **Virtualenv** section -> **Start a console in this virtualenv** ):

```cmd
(jacong17.pythonanywhere.com) $ python manage.py createsuperuser
```

Type in the details for your admin user. Best to use the same ones as you're using on your own computer to avoid any confusion, unless you want to make the password on PythonAnywhere more secure.

Now, if you like, you can also take a look at your code on PythonAnywhere using `ls`:

```cmd
(ola.pythonanywhere.com) $ ls
blog  db.sqlite3  manage.py  mysite requirements.txt static
(ola.pythonanywhere.com) $ ls blog/
__init__.py  __pycache__  admin.py  apps.py  migrations  models.py
tests.py  views.py
```

You can also go to the "Files" page and navigate around using PythonAnywhere's built-in file browser. (From the Console page, you can get to other PythonAnywhere pages from the menu button in the upper right corner. Once you're on one of the pages, there are links to the other ones near the top.)

### You are now live

Your site should now be live on the public Internet! Click through to the PythonAnywhere "Web" page to get a link to it. You can share this with anyone you want :)

You should review the [Django deployment checklist](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/) for some tips on securing your site.

### Check out your site

The default page for your site should say "It worked!", just like it does on your local computer. Try adding `/admin/` to the end of the URL, and you'll be taken to the admin site. Log in with the username and password, and you'll see you can add new Posts on the server -- remember, the posts from your local test database were not sent to your live blog.

Once you have a few posts created, you can go back to your local setup (not PythonAnywhere). From here you should work on your local setup to make changes. This is a common workflow in web development – make changes locally, push those changes to GitHub, and pull your changes down to your live Web server. This allows you to work and experiment without breaking your live Web site.

---

## Adding your Django URL

We want `http://127.0.0.1:8000/` to be the home page of our blog and to display a list of posts.

We also want to keep the mysite/urls.py file clean, so we will import URLs from our blog application to the main mysite/urls.py file.

Add a line that will import blog.urls. You will also need to change the from django.urls… line because we are using the `include` function here, so you will need to add that import to the line.

Your mysite/urls.py file should now look like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

Django will now redirect everything that comes into `http://127.0.0.1:8000/` to blog.urls and looks for further instructions there.

### blog.urls

Create a new empty file named `urls.py` in the blog directory. Add these 2 lines to import Django's function path & all of our views from the blog application.:

```python
from django.urls import path
from . import views
```

Add your 1st URL patten:

```python
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

We're now assigning a `view` called `post_list` to the root URL. This URL pattern will match an empty string and the Django URL resolver will ignore the domain name (i.e., `http://127.0.0.1:8000/`) that prefixes the full url path. This pattern will tell Django that `views.post_list` is the right place to go if someone enters your website at the `http://127.0.0.1:8000/` address.

The last part, `name='post_list'`, is the name of the URL that will be used to identify the view. This can be the same as the name of the view but it can also be something completely different. We will be using the named URLs later in the project, so it is important to name each URL in the app. We should also try to keep the names of URLs unique and easy to remember.

When you run `python manage.py runserver` to start your server, you'll get an error message because it's telling you that there is no attribute `post_list`. That's the name of the view that Django is trying to find and use, but we haven't created it yet. At this stage, your `/admin/` will also not work.

---

## Adding views

A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template. Views are placed in the `views.py` file. We will add our views to the `blog/views.py` file.

### blog/views.py

Add this line:

```python
def post_list(request):
    return render(request, 'blog/post_list.html', {})
```

We created a function (def) called `post_list` that takes `request` and will return the value it gets from calling another function `render` that will render (put together) our template `blog/post_list.html`.

Save the file, go to `http://127.0.0.1:8000/` and see what we've got. You should get another error saying *TemplateDoesNotExist*.

---

## Creating a template

Templates are saved in `blog/templates/blog` directory. So first create a directory called `templates` inside your blog directory. Then create another directory called `blog` inside your templates directory:

```cmd
blog
└───templates
    └───blog
```

Create a `post_list.html` file inside the `blog/templates/blog` directory & add:

```html
<html>
    <head>
        <title>Django blog</title>
    </head>
    <body>
        <div>
            <h1><a href="/">Django Blog</a></h1>
        </div>

        <div>
            <h2><a href="">My first post</a></h2>
            <p>The quick brown fox jumps over the wall.</p>
            <p>published: 06.09.2019, 12:14</p>
        </div>
        <hr />
        <div>
            <h2><a href="">My second post</a></h2>
            <p>The quick brown fox jumps over the wall.</p>
            <p>published: 06.09.2019, 14:14</p>
        </div>
    </body>
</html>
```

See how your website looks now: `http://127.0.0.1:8000/` (Restart your server if you still get the error).

### Deploy on live site

Commit, and push your code up to GitHub.

```cmd
git status
git add --all .
git commit -m "Changed the HTML for the site."
git push origin django
```

Pull your new code down to PythonAnywhere, and reload your web app.

On the PythonAnywhere cmd:

```cmd
cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
git pull
[...]
```

Once done, hop on over to the "Web" page and hit Reload on your web app. Your update should be live! Go ahead and refresh your website in the browser. Changes should be visible. :)

---

## Django ORM and QuerySets

### Django shell

Open up your local console (not on PythonAnywhere) and type this command:

```cmd
(myvenv) ~/django$ python manage.py shell
```

The effect should be like this:

```cmd
(InteractiveConsole)
>>>
```

It's just like the Python prompt, but with some additional Django magic. :) You can use all the Python commands here too.

### All objects

Let's display all of our posts.

```cmd
>>> Post.objects.all()
Traceback (most recent call last):
      File "<console>", line 1, in <module>
NameError: name 'Post' is not defined
```

Oops! An error showed up. It tells us that there is no Post. It's correct – we forgot to import it first!

```cmd
>>> from blog.models import Post
```

We import the model `Post` from `blog.models`. Let's try displaying all posts again:

```cmd
>>> Post.objects.all()
<QuerySet [<Post: my post title>, <Post: another post title>]>
```

This is a list of the posts we created earlier! We created these posts using the Django admin interface. But now we want to create new posts using Python, so how do we do that?

### Create object

Let's import User model first:

```cmd
>>> from django.contrib.auth.models import User
```

What users do we have in our database? Try this:

```cmd
>>> User.objects.all()
<QuerySet [<User: ola>]>
```

This is the superuser we created earlier! Let's get an instance of the user now (adjust this line to use your own username):

```cmd
>>> me = User.objects.get(username='<your-username>')
```

Create a new Post object in database:

```cmd
>>> Post.objects.create(author=me, title='Sample title', text='Test')
```

To check that it works:

```cmd
>>> Post.objects.all()
<QuerySet [<Post: my post title>, <Post: another post title>, <Post: Sample title>]>
```

Add 3 to 4 more posts then proceed to the next part.

### Filter objects

A big part of QuerySets is the ability to filter them. Let's say we want to find all posts that user ola authored. We will use `filter` instead of all in `Post.objects.all()`. In parentheses we state what condition(s) a blog post needs to meet to end up in our queryset. In our case, the condition is that `author` should be equal to `me`. The way to write it in Django is `author=me`. Now our piece of code looks like this:

```cmd
>>> Post.objects.filter(author=me)
<QuerySet [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]>
```

Or maybe we want to see all the posts that contain the word 'title' in the title field?

```cmd
>>> Post.objects.filter(title__contains='title')
<QuerySet [<Post: Sample title>, <Post: 4th title of post>]>
```

**Note:** *There are two underscore characters (_) between title and contains. Django's ORM uses this rule to separate field names ("title") and operations or filters ("contains"). If you use only one underscore, you'll get an error like "FieldError: Cannot resolve keyword title_contains".*

You can also get a list of all published posts. We do this by filtering all the posts that have published_date set in the past:

```cmd
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet []>
```

Unfortunately, the post we added from the Python console is not published yet. But we can change that! First get an instance of a post we want to publish:

```cmd
>>> post = Post.objects.get(title="Sample title")
```

And then publish it with our `publish` method:

```cmd
>>> post.publish()
```

Now try to get list of published posts again (press the up arrow key three times and hit enter):

```cmd
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: Sample title>]>
```

### Ordering objects

QuerySets also allow you to order the list of objects. Let's try to order them by created_date field:

```cmd
>>> Post.objects.order_by('created_date')
<QuerySet [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]>
```

We can also reverse the ordering by adding - at the beginning:

```cmd
>>> Post.objects.order_by('-created_date')
<QuerySet [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]>
```

### Complex queries through method-chaining

As you saw, some methods on `Post.objects` return a QuerySet. The same methods can in turn also be called on a QuerySet, and will then return a new QuerySet. Thus, you can combine their effect by **chaining** them together:

```cmd
>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
<QuerySet [<Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>, <Post: Sample title>]>
```

This is really powerful and lets you write quite complex queries. Cool! You're now ready for the next part! To close the shell, type this:

```cmd
>>> exit()
$
```

---

## Dynamic data in templates
