# iShope Testing

## Python Testing:
How to run Python tests

In the terminal enter the following command:
```
python3 manage.py test
```
Results were:
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...

To test specific app:
```
python3 manage.py test <app name here>
```
## Travis:
[![Build Status](https://travis-ci.org/Tariqalrehily/iShop.svg?branch=master)](https://travis-ci.org/Tariqalrehily/iShop)

## User Stories Testing:

1. Navbar:
* Tried each link on navbar to confirm they are directed to the right page.
* Tried to visit the site without being logged in to confirm Register and login links are in the navbar.
* Tried to visit the site after being logged in to confirm Profile and logout links are in the navbar.
* Tried to scroll down at the bottom of the page to confirm navbar stick on top of the page.
* Tried on iPhone and Samsung table to confirm burger menu will replace navbar.

2. footer:
* Tried on MacBook Pro, Samsung tablet, and iPhone, to confirm footer is responsive.
* Tried to visit each link on footer to confirm they are directing to the right page.
* Tried to visit social media under follow us section, I was directed in different tab to twitter and linked pages.

3. Register form:
* Go to Register pages
* Tried and a Friend to submit an empty form, required message appear to fill fields username, password and password confirmation.
* Tried and a Friend to submit a form without email, the form was saved. Fixed this by if statement, if email is empty string, raise a Validation Error asking user to enter their email address.
* Tried and a Friend to submit a form with email already exists raise a Validation Error asking user to use a unique email address, as the email provided already used.
* Tried to submit a form with mismatching password, validation Error telling user that Passwords is not matching.
* A Friend tried to submit a form with my username, validation Error telling user that a user with that username already exists.

4. Login form:
* Tried and a Friend to login with invalid username, related validation Error message appears.
* Tried and a Friend to login with invalid password, related validation Error message appears.

5. Logout:
* After logging in, tried and a Friend to log out, both were successfully logged out.

6. Forgot password:
* Tried and a Friend to reset our passwords, by clicking on forgot password link on login page.
* Redirect us to password reset page, where we could enter our emails to start reseting our password.
* After we entered the email, we were redirected to password reset done page with the relevant message to visit your email.
* For Both, email was received, with new password reset link and username.
* Tried both to visit the provided link to reset the email, we were both redirected to iShop password reset page to enter new password.
* Tried to enter different password in password1 and password2 fields, relevant error message appears that the two password fields didn't match.
* Tired to enter the same correct password in both field, relevant message appear after redirect to password reset complete page, that password has been set, and a link to login.

7. Contact us form:
* Tried and a Friend to send an email via contact us form with an empty form, required message appear to fill fields name, email, subject, and message.
* Tried and a Friend to enter invalid email address without @, user was educated to include @, and than, user refer to enter the part following @, if submitted user will get an Email was invalid error, as it was last part (e.g .com) was not provided.
* Tried and a Friend to submit a complete form, form was success, and we were redirect to home page with user message that we received his / her message and we will contact them shortly.

8. Add to Cart:
* Tried select a product from products page, which was redirect than to that product view page.
* Tried add to cart an empty value (Qty) I was promoted to fill out the field.
* Tried to enter 0 as value (Qty), relevant error message appears that value most great than or equal to 1.
* Tried to enter -1 as value (Qty), relevant error message appears that value most great than or equal to 1.
* Tired to enter a string, relevant error message appears that value most be a number.
* Tired to enter a number 1, item was added to Cart.  

9. Amend Cart:
* Tried to enter an empty value to change (Qty) I was promoted to fill out the field.
* Tried to enter -1 as value to change (Qty), relevant error message appears that value most great than or equal to 1.
* Tired to enter a string, relevant error message appears that value most be a number.
* Tried to enter 0 as value (Qty), item was removed from Cart, and statement appears that no items are in Cart.
* Tried to increase current value of 1 more of the same item, current quantity changed to 2 item of the same product in cart.

10. Checkout:
* Tried to Checkout my current items in my cart without being logged in, I was redirected to sign in form.
* After signed in, I revisited my Cart to checkout, I was directed to checkout page.
* Tried to submit empty payment details, relevant error message about the required fields appears to fill all required filled one by one.
* Tried after filling all required filed and payment details, 500 server error appears, below stripe testing in more details:

11. Stripe:
* Tried to test strip key rendering on the page locally on my machine, by assign:
```
STRIPE_PUBLISHABLE = 'my publishable key'
STRIPE_SECRET = 'my secret key'
```
Provided payment details:
Credit card number: 4242424242424242
CVV: 111 (or any 3 numbers)
Month: current or future month.
Year: current or future month.

The result was payment was successful and I was promoted relevant message that I have paid.

* Tried to test strip key rendering on the page locally on my machine, by assign:
```
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')
```
The result was a 401 error, failed to load resource: api.stripe strip key is not rendering on page, action taken:
1.	Check jQuery scripts loaded before Stripe, as Stripe depends on jQuery.
2.	My {% block head_js %} tags are identical between my template with the checkout form and my base.html page.
3.	All of my script tags are loaded at the bottom of my base.html page.
4.	Ensure that my Stripe key is correct as tried to assign directly and that it's being rendered on the page and payment was successful.

After confirming the above, I was still with the same error message 401, Failed to load resource: the api.stripe.com/v1/tokens:1 server responded with a status of 401 (). This issue incur after user click on payment submit button, as jQuery failed to trigger stripe token to create and process payment. This bug left to be fixed.

12. Review form:
* Tried after visiting review list page, to start adding a review.
* Not logged in user will be redirect to login as log in is required to write a review.
* After logging in, I revisited reviews list page to start write a review, I was redirected to add review form.
* Tried to submit an empty review form, required message appear to fill fields user name, select rating, and comment. Each field has required message below the field.
* Tried to submit the form with just a user name, relevant message appear to select an item.
* Tried to submit the form with just a user name and select a item, relevant message appear to fill comment field.
* Tried to submit the form with a user name, select item, and a comment, success message appear and review is added.

13. Search form:
* Tried with a Fried to search for a smartphone from navbar search by entering iPhone, result was showing in search page.
* Tried to enter a new search values (on both forms located in home and search pages) by name: iPhone, brand: apple year: 2019, search results found with no issue.
* Tried to fill just the name field with iPhone, result were found with no issue.
* Tried to fill just the brand field with Samsung, result were found with no issue.
* Tried to fill just the year field with 2019, result were found with no issue.  
* The 3 search fields are in content fields, tried to enter 33 as year number, results shows no products match.

14. Pagination:
11.1 In products page:
* Tried to move to next and between pages, I was able to move to previous and next pages with no issue.
11.2 In reviews page:
* Tried for the testing to add many testing reviews to move to next and between pages, I was able to move to previous and next pages with no issue.

### Bugs:
* Strip key is not rendering in production on Heroku, both Publishable key and Secret key are provided in Config vars, but still not working.
This bug left to be fixed. Failed to load resource: the api.stripe.com/v1/tokens:1 server responded with a status of 401 (). This issue incur after 
user click on payment submit button, as jQuery failed to trigger stripe to create and process payment. The code is working when STRIPE_PUBLISHABLE and STRIPE_SECRET 
been assign direct keys values in settings.py 
