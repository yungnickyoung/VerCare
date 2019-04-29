# VerCare
Aggregates and compares medical procedure prices for nearby hospitals in order to help you find the perfect price.

SwampHacks 2019 3rd place winner!

## Inspiration
A law was enacted on January 1, 2019 requiring all hospitals to be transparent with pricing for all goods provided by each hospital. In an attempt to circumvent this law, hospitals made their pricing data as convoluted as possible, using extremely technical terms to describe items in their sets of data. Our goal was to make our healthcare truly transparent, and stop predatory pricing. All too often we hear stories of students who are forced to go to a hospital that refuses to provide quotes for their ailments and then bill absurd amounts of money that only pile onto debts. Our system was meant for the masses in mind. You don’t need to know medical terms, you don’t need to know how to scour the internet to find a CSV file with 5000 items (yes, 5000 items was the **average** length CSV file with data we found) then figure out the translation of your illness. All you have to do is go to VerCare, type in your possible diagnosis, and click search. We search all the hospitals around you, and we give you the true price in a format you can understand.
## What it does
VerCare collects medical procedure prices from nearby hospitals and provides a centralized platform for viewing and comparing them, allowing you to find the procedure you need at the cheapest price.
## How we built it
VerCare uses data publicly released by hospitals as required by law. This data is stored in our sqlite database. VerCare uses Flask to manage the website's various pages and Bootstrap to present information to the user in an appealing yet simple manner. 
## Challenges we ran into
We faced various unknowns and challenges along the way. In particular, we had significant problems getting the database to cooperate with Flask. We also experienced issues understanding and fully utilizing the power of templates.
## Accomplishments that we're proud of
This project was a first for us on many levels. It was our first time using Bootstrap to create a website's front end. It was our first time getting hands-on experience with databases. We had never before used Flask's templates to such an extensive degree.
## What we learned
Working on VerCare, we learned about a variety of technologies as mentioned above. Some of us also were able to learn much more about git than we had previously known. Most importantly, we realized just how complicated things can get when trying to tie multiple components made by different people together.
## What's next for VerCare
We plan to include many more hospitals in our database (and upgrade from sqlite as a result). The front end will be improved, with some more aesthetic appeal as well as some quality of life improvements, such as the ability to order tables by their different columns.
