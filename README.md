
# Zarcode - A Tech Interview Prep App

This is a tech interview preparation app and a forum for current and aspiring software engineers. Here Engineers can post about their interview experiences, have tech discussions, and get an idea to prepare for their technical interviews.

## Problem Definition

There is no all-in-one platform in Bangladesh where aspiring software engineers can get to know about the interview process of different tech companies of Bangladesh. 
So, we are trying to solve this problem by making an app where candidates of Bangladesh can share their interview experiences and ask about any interview related queries so that they can get prepared to get into tech companies in Bangladesh. We are trying to reduce the gap between candidates and interview procedures and experiences of tech companies. 



## Features

### Security Features

* User Registration with Email activation and strong password requirement.
* Login system with JWT authentication.
* A user cannot access any URL of the website without logging in.
* A user cannot post anything without logging in.
* A user cannot edit or delete another person’s post or comment.

### Product Features

#### User Profile

The product has a user profile feature. The profile page contains - the user's username, profile picture, cover photo, where the user works and where the user lives. 

It also contains contain the user’s previous posts and a option to create new post from the profile page.

A user can also edit his/her profile from this page.

#### Posting & Commenting

In our app, a user can post about their interview experiences, queries about interviews, memes, and general discussions. We divide the postings into three categories. The categories are -
* Interview Experiences - Users can post about their interview experiences with the name of the company that they interviewed at. Here they will describe their interview experience, the procedure of interview at that company, the interview timeline, the types of questions asked in the interview.
* Queries about Interviews - Users can post in our app if they have any questions or queries about the interview procedure of a specific company. They might want suggestions about their preparation or ask any specific questions.
* Memes and General Discussion - In this category users can have general discussions and fun about software engineering and interview processes in general.
Users can comment under any of the posts and interact with each other.
Users can also edit their posts and comments. They can also attach images with their posts or comments if they want.

We have also implemented a like/upvote/bump system for every post and comments in our app. The bump is a representation of the popularity of the post.

#### Searching & Filtering

* The product has a category-based search option so that users can search by post title, text, or author to find their relevant posts and/or questions.
* The product should has a post filtering so that users can easily see the type of posts they want to see and avoid distractions.

#### Custom UI

* The UI is built from scratch using custom CSS
## Tech Stack

**Programming Languages:** Python, Javascript

**Database:** SQLite3

**Framework/Library:** Django, ReactJS

**Web Design:** HTML, CSS, Bootstrap

**API:** Django REST Framework

## Screenshots

### Our home page -

![Screenshot_20221229_101231](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/ed675c7b-2a13-438c-af84-3e51218a47f5)

![Screenshot_20221229_101612](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/fb9c3f61-7574-4504-9817-8db1f98f8495)

### Sign Up Page - 

![Screenshot_20221229_102942](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/e3415a08-2c54-409d-b0c8-1774837b0d86)

### Login Page -

![Screenshot_20221229_105830](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/a520ed37-b862-439f-9c15-813c34aab7db)

### Create Profile Page -

![Screenshot_20221229_112630](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/954e2312-3cab-4f01-b888-1f81d01b7683)

### Profile Page -

![Screenshot_20221229_112753](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/9899289e-841c-4ff3-b268-8702626d5466)

### Search Bar & New Post Box

![Screenshot_20221229_113031](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/0b2c9611-f476-4fba-897a-cf610108819a)

### Post Details Page (See More)

![Screenshot_20221229_113602](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/1342cc63-fa22-455e-afd4-b2bbcd207b68)

### Post Comment Page

![Screenshot_20221229_113621](https://github.com/kasif-zisan/InterviewPrepApp-Backend-/assets/75033362/1fc53f98-d1f4-4f5c-b53b-f0b00fa094d3)

There are many more amazing features in our app such as - post reporting, pagination etc.

## Install & Run Locally

To run the app, at first you will first need to clone the project

```bash
git clone https://github.com/kasif-zisan/InterviewPrepApp-Backend-.git
```

Our backend runs on python django. To run the backend of our app, we first need Python.
To download python, visit -

[https://www.python.org/downloads/]

After that, install and create a virtual environment.

To install a virtual environment -
```code
pip install virtualenv
```
To create virtual environment -
```code
virtualenv virtual_environment_name
```
To activate your virtual environment -
```code
virtual_environment_name\scripts\activate
```
Now that we have activated our virtual envionment, we have to install our necessary packages to run this app. 

For this first go to the project directory.

All of our packages are listed in the requirements.txt file.
To install the packages -
```code
pip install -r requirements.txt
```
After this we have installed all of our dependencies.

Now to run our app, first lets migrate the database.
```code
py manage.py makemigrations
py manage.py migrate
```
Start the server

```bash
py manage.py runserver
```

Now hopefully the backend part of the app is running fine.



