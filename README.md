# Slimmed-Down-Shopping-Site

## Introduction
I've created a web-based application for an online store using Flask, which includes a product catalog where users can view, search, and see detailed information about each product. This project is responsive and designed to provide a seamless experience across various devices.

## Data Model
In this project, I used SQLite for the database. The primary model is the `Product` model, representing the items in the store.

### Product Model
- `product_no`: String - This is a unique identifier for each product.
- `description`: String - Here, I store description of the product.
- `price`: Float - Represents the selling price.
- `image`: String - Refers to the filename of the product's image in the static directory.
- `category`: String - Used for classifying products.

## Assumptions
- **Image Storage**: I assumed that all product images are stored in `static/images/` and referenced accordingly in the `Product` model.
- **Unique Product Numbers**: Ensured each product has a unique `product_no`.
- **Category Classification**: Used `category` for organizing and potentially filtering products.

## Challenges and Solutions
- **Database Initialization**: Initially setting up and populating the SQLite database was a critical step.
- **Image Path Handling**: I had to ensure that the image paths in the HTML templates correctly linked to the product images.
- **Responsive Design**: Adjusting CSS for a responsive design was challenging but essential.
- **Search Functionality**: Implementing a robust search functionality required careful consideration, especially for filtering by different attributes.
- **Routing and URL Parameters**: Managing Flask routes, especially for individual product details, was a key focus.
- **Deployment on Azure**: Deploying the Flask app on Azure involved configuring environment variables.
- **Undefined Variables in Templates**: I had to ensure all variables passed to Jinja templates were defined to avoid runtime errors.

## Deployment
- I successfully deployed the web app on Azure Web Services, focusing on setting up the required configurations and environment variables to ensure smooth operation and compatibility with the Azure hosting environment.
- Code deployed at: [https://shoppingsitekonege.azurewebsites.net](https://shoppingsitekonege.azurewebsites.net)  (The site takes some time to open. I do not know why.)
