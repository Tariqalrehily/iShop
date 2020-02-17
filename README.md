# iShop

[![Build Status](https://travis-ci.org/Tariqalrehily/iShop.svg?branch=master)](https://travis-ci.org/Tariqalrehily/iShop)

iShop is an online smartphones shop, was designed and build to give an effective online shopping experience. Aimed to help
customer to search and find their potential smartphones. iShop provide users an ease why to navigate through the website, by providing
clear way to search, find and pay for a smartphone(s).

Each smartphone presented with photo, initial infromation, and price. By clicking on smartphone card, user will be redirected to view more information
about that product. More infromation including (Name, photo, price, Brand, year, and description). User can add the smartphone to cart by entering quantity and
hit add to Cart button. 

iShop was designed, built, and deployed by Tariq Alrehily as part of Code Institute final project for Full Stack Web Development Diploma.

# UX:

## Goals:
### Visitor Goals:
* People who would like to purchase a new smartphones.
* People who would like to see more information about a smartphone.

### User goals:
* Search and find a new smartphone.
* Enjoy reading about smartphones in the market
* Read information about smartphone.
* Buy a smartphone.

iShop meets this requirements, by carefully designed the best way for site's users to search, find, and pay for a smartphones.
The home page was designed to include the site features to ease for users to use iShop. The navigation fits users needs by navigate to
products page, search for a product and see what is in their cart.

### Business Goals:
* Provide user with the safety felling as they are using / buying from iShop by using trusted third party payment provider such as stripe.
* Provide clear way on how to use the site.  
* Build Contact us form for user / customer support.
* Provide a review form, to build trust by existed registered users.

[Wireframe mockups](https://github.com/Tariqalrehily/iShop/blob/master/iShop-Wireframe-mockups.pdf)

## User Stories:
1. As a (first time) visitor of the website, I want to see directly what kind of website I'm looking at; presented photos and statements provide the
visitor with clear idea of the propose of the site.
2. As a prospect, I want to see clearly what kind of services iShop delivers. I'm expecting to see relevant information without searching through the website; this was provided by set slider show for some of the products. Also, by giving the user a clear statement of what is the website about and three steps to buy a smartphone.
3. As a IT recruiter, searching projects for clients, I want to see relevant information about services and people behind the company. Two social media sits are provided at bottom (footer). Also, Contact us form.
4. As a (co-)owner of the company, I want to use the website as an digital business card. I need the website to be in line of the corporate identity, and also be available for good use of mobile devices (responsive design);
5. As a prospect/customer/visitor, I want to find some contact information about the company, i.e. social media / contact us form, phone number, and location of the office.

## Features:
### Existing Features:
##### Navbar:
* Navbar features on all pages, with fixed in top.
* Desktop view: On the left of the navbar, five links on pages are provided. iShop logo(Home page), Products to view all smartphones, Register and login if user is is not registered / or logged in, or Profile and logout if your is already logged in. Reviews linked to list of review page. On the right side in the navbar, search bar and cart are provided.
* Tablet and Mobile view: iShop logo remains in the left, with burger menu on the right, dropdown display: Products, (Register and Login / or Profile and Logout), Reviews, search bar, and cart).

##### Footer:
* The footer features on all pages.
* The footer include three parts:
Part one: Popular Links: All Products and Reviews.
Part two: contact us, location and phone number.
Part three: for user to follow us on Social media (Twitter and LinkedIn).
* Copyright information for iShop.

##### Home page (iShop):
* Slider, include three slider as promotion images of smartphones.
* Introduction and brief statement of iShop in one line.
* Steps to start shopping with iShop.
* Three search bar are provided as on the home page, for user to be able to start a new search to find their wish smartphone, which are search by: name, brand, year.
* Six exited smartphones and a link to view more / all products.
* A thanks note for site visitor.

##### Products:
* Products list up to nine products as card featured. Each Product has some basic information about the product, such as image, name include brand size and color. Also, at the bottom of the card a product price.
* Pagination buttons are provided depending on results returned from the database. option are current page and number of pages, previous and next.

##### View Product:
* Each product has slug set to generate a valid url to view that product information.
* Each product information include: Name, image, price, add to cart after selecting quantity (option 1 up to 50) user has to input a number that was done by set required field. 0 and less than 1 values won't be accepted, brand, year, and description.
* At the bottom, link to browse more products provided to redirect user to all products page.

##### Search page:
* Page to include smartphones results from the search input.
* At the top of the page: three search bar are provided as on the home page, for user to be able to start a new search.
* Three virous search bars are provided to help user to find their wish smartphone, which are: by name, brand, year.
* The three bars were placeholder by type of search and an example of search input.

##### Reviews:
* At the top, add review link added to redirect user to add a review form.
* list of existed reviews, each review include: user name, rating, date and time, and review content.
* Pagination buttons are provided depending on results returned from the database. option are current page and number of pages, previous and next.

##### Add Review:
* To add a review user needs to be registered. Not logged in users will be redirect to login page.
* After logging in: user will be informed to enter user name (text), rating(select menu 1 to 5), and comment. By hit add button, review will be Added successfully.
* A note for user attention that he / she will not be able to edit or delete review once added.  

##### Cart:
* User's shopping list display all items in cart as a table rows.
* Each item has information as: photo, name, price, quantity and ability to amend current quantity.
* Link to all products page if user wish to continue shopping.
* Total price of items.
* Checkout button to redirect to checkout page.
* If no item in user's cart, user will be informed by (No items are in your Cart!)

##### Checkout:
* User's order summary list display as a table rows. each item include: photo, name, price, and quantity.
* Total price of items.
* Payment details form, for user to complete their parches.
* Button to submit payment.
* message will be informing user if payment was successful or there an issue with payment at the top of the page.
* User will be redirect to home page after successfully payment.

##### User account pages:
* Register page: Include registration form, educate user to provide Email, username, password, password confirmation. Instructions on how to select the password provided the password field. Submit button.
* Login page: Include login form, educate user to provide username, password. Instructions on why they need to login as provided on the sign in form. Forgot password link and Submit button. On the login form, user is educated that they will need to be logged in to view cart or add a review.
* Profile page: Layout as User's Profile at the top of the page, below, Hi username, and user email. To ease the use for the user five links were provided: Cart, products, contact us, home page, and logout. Also, A thanks statement fro user being with iShop.
* logout link at the in navbar or user's profile will logout user and informing them by a message at the top of the page.

##### Password reset pages:
* Password reset form: inform user to enter their email address and hit reset, password button to start resetting password.
* Password reset done page: inform user with a message that we have sent them an email with instructions for setting new password to the e-mail address that we have.
* password reset email: send an email with password reset link and username in case user forgot.
* Password reset confirm page: inform user to enter new password. New password and confirm password. Once user entered a valid password1 and password2(confirm), user can hit change password button to reset the password.
* Password reset complete page: inform message that password has been set, and login link.

##### Contact us page:
* Contact us provided in the footer in all pages and as a link in user's profile page.
* iShop users can contact us by filling contact us form, by providing name, email, subject, and message. Send button at the bottom of the page.

## Features Left To Implement:
1. Sending an email to customer with their shopping sumary and recipet, once order is placed. 
2. Sending an acknowledgement email to user once they submitted a contact us form. 
3. Onces the site has an acutl and availbe products, include Terms & Conditions page. 

## Data Models:
1. User model: iShop uses the standard User model provided by django.contrib.auth.models
2. Products app model: 
 ```
name = models.CharField(max_length=254, default='')
description = models.TextField(default='')
price = models.DecimalField(max_digits=6, decimal_places=2)
image = models.ImageField(upload_to='images')
brand = models.CharField(max_length=200, default='')
year = models.IntegerField(default='')
slug = models.SlugField(unique=True)
 ```
 3. Review app model:
```
pub_date = models.DateTimeField('date published')
user_name = models.CharField(max_length=100)
rating = models.IntegerField(choices=RATING_CHOICES)
comment = models.CharField(max_length=1000)
```
4. Order model within checkout app:
```
full_name = models.CharField(max_length=50, blank=False)
phone_number = models.CharField(max_length=20, blank=False)
country = models.CharField(max_length=40, blank=False)
postcode = models.CharField(max_length=20, blank=True)
street_address1 = models.CharField(max_length=40, blank=False)
street_address2 = models.CharField(max_length=40, blank=False)
town_or_city = models.CharField(max_length=40, blank=False)
state = models.CharField(max_length=40, blank=False)
date = models.DateField()
```
5. Order model within checkout app:
```
order = models.ForeignKey(Order, null=False)
product = models.ForeignKey(Product, null=False)
quantity = models.IntegerField(blank=False)
```

## Languages Used:
* HTML5, CSS3, , Javascript, Python3

## Libraries Used:
* Bootstrap, FontAwesome, jQuery.

## Technologies Used:
* [Django](https://www.djangoproject.com/) as python web framework fro development and coding.
* [AWS S3 bucket](https://aws.amazon.com/) to store static files and images.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable configuration of AWS S3.
* [Django Storages](https://django-storages.readthedocs.io/en/latest/) is a collection of custom storage backends for Django.
* [Gunicorn](https://gunicorn.org/) pre-fork worker model to aid in project deployment to Heroku.
* [Pillow](https://pillow.readthedocs.io/en/stable/) an imaging library to process storing images in database.
* [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
* [Whitenoise](http://whitenoise.evans.io/en/stable/) to allows the web app to serve its own static files.
* [Stripe](https://stripe.com/ie) as payment method to validate credit card payment.
* [Travis](https://travis-ci.org/) for continues integration.
* [Git](https://git-scm.com/) to handle version control.
* [GitHub](https://github.com/) to store and share all project code remotely.
* [Pencil](https://pencil.evolus.vn/) to create iShop Wireframe mockups.
* [SQlite3](https://www.sqlite.org/index.html) for development database on django.
* [PostgreSQL](https://www.postgresql.org/) for production database, provided by Heroku.

## Testing
Testing is in separate file and can be found [TESTING.md](https://github.com/Tariqalrehily/iShop/blob/master/TESTING.md)

### Devices Tested:
* Desktop: MacBook Pro 13 inch, also wider screens
* Tablet: Samsung
* Phones: iPhone 6 and xiaomi

## Deployment
### To Github using Gitpod:
1. Created a new repository on GitHub. To avoid errors, I did not initialize the new repository with README, license, or gitignore files. I added these files after my project has been pushed to GitHub.
2. Create a gitpod account.
3. Install gitpod extension on chrome browser.
3. Navigate to gitpod button top right on github repository page.
4. Gitpod check the current brach automatically and run compiler to start gitpod IDE.
5. Give the right permissions to gitpod to commit to changes to github.
6. Two ways to commit and push changes to github:
6.1 From gitpod bulid tools:
* Naviagte to Git soucrce control
* Stage ll changes
* Write a commit message in the input box on top left on gitpod IDE.
* From the right menu push to github.

6.2 From gitpod terminal:
* Run:
  ```
  git status
  ```
* Added the files and stage them for the commit, by:
```
$ git add fileName
```
* Commit the files that have staged, by:
```
$ git commit -m "commit message"
```
* Push the changes to GitHub Master branch, by:
```
$ git push -u origin master
```

* After, do this to commit and push my projects changes and keep my GitHub repository up to date.

### From Github:
* To run the project locally:
1. Install Pip, python3, and git on your local machine.
2. Project required the following services, Create free accounts on: [AWS to set S3 bucket](https://aws.amazon.com/) and [Stripe](https://stripe.com/ie) as payment method to validate credit card payment.
3. On GitHub, navigate to the main page of the repository.


1. On GitHub, navigate to the main page of the [repository](https://github.com/Tariqalrehily/iShop).
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click  to copy the clone URL for the repository.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type:
```
git clone https://github.com/Tariqalrehily/iShop
```
7. Press Enter. Your local clone will be created.
8. Install all required modules with the following CLI:
```
pip3 -r requirements.txt.
```
9. Set environment variables in your Project / Application as follow:
```
os.environ.setdefault("DATABASE_URL", "YOUR PostgreSQL URL")
os.environ.setdefault("SECRET_KEY", " YOUR SECRET KEY")

os.environ.setdefault("STRIPE_PUBLISHABLE", "YOUR STRIPE PUBLISHABLE")
os.environ.setdefault("STRIPE_SECRET", "YOUR STRIPE SECRET")

os.environ.setdefault("AWS_SECRET_KEY_ID", "YOUR AWS SECRET KEY ID")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "YOUR AWS SECRET ACCESS KEY")

os.environ.setdefault("EMAIL_ADDRESS", "YOUR EMAIL ADDRESS")
os.environ.setdefault("EMAIL_PASSWORD", "YOUR EMAIL PASSWORD")

```
If you are using .bashrc file please see [instruction](https://serverfault.com/questions/606/what-is-the-best-way-to-set-an-environment-variable-in-bashrc) on how to do so.

### To Heroku:
1. Create requirements.txt file using:
```
 pip3 freeze > requirements.txt.
```
2. Create a Procfile using:
```
 echo web: python app.py > Procfile.
```
3. Push the changes to github by ```git add```, ```git commit```, and ```git push```.
4. Create a new app on Heroku (You most have an account).
5. On the Heroku app dashboard navigate to deploy.
6. On deploy page navigate to deployment method and select gitHub.
7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars", and set the following config vars:

| Key  | Value |
| ------------- | ------------- |
| AWS_SECRET_ACCESS_KEY  | YOUR AWS SECRET ACCESS KEY  |
| AWS_SECRET_KEY_ID | YOUR AWS SECRET KEY ID |
| DATABASE_URL | YOUR PostgreSQL URL  |
| DISABLE_COLLECTSTATIC | 1  |
| EMAIL_ADDRESS | YOUR EMAIL ADDRESS |
| EMAIL_PASSWORD | YOUR EMAIL PASSWORD |
| SECRET_KEY| YOUR STRIPE SECRET  |
| STRIPE_PUBLISHABLE | YOUR STRIPE PUBLISHABLE |
| STRIPE_SECRET| YOUR STRIPE SECRET |

## Credit:
### Content:
* Product (smartphones) information was taking from [Amazon](https://www.amazon.co.uk/s)

## Media:
* The main three photo on slider:
First photo: by [Tyler Lastovich](https://www.pexels.com/photo/black-iphone-7-on-brown-table-699122/)
Second photo: by [Torsten Dettlaff](https://www.pexels.com/photo/space-gray-iphone-6-193004/)
Third photo: by [Plush Design Studio](https://www.pexels.com/photo/silver-iphone-x-with-airpods-788946/)
* Products photos was taking from [Amazon](https://www.amazon.co.uk/s)

## Code:
* Reviews app code was inspired by [Jose A Dianes](https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a)
* Contact Us code was inspired by [Will Vincent](https://wsvincent.com/django-contact-form/)
* Footer code was inspired by [Namiq Namaz](https://codepen.io/NamiqNamaz/pen/QZYyEq?editors=1010)
* Pagination code was inspired by an online youtube video by [GoDjango](https://www.youtube.com/watch?v=lOcLr6CXg2s)

## Acknowledgement:
* To my mentor Anthony Ngene provided me guides and the Tutor team for their help and advises.
* This project to aimed to be real life smartphones shop, once all products are actually available. For the propose of this
project smartphones content was taking as referred to above from [Amazon](https://www.amazon.co.uk/s)

## Disclaimer:
* The materials on this application is currently for educational and entertainment purposes only.  
