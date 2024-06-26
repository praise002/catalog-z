# Catalog
Catalog-Z is a free stock image and video website built with Django, Bootstrap, and JavaScript. It allows users to browse, search, and download high-quality images and videos for personal and commercial use.

## Features
- **Browse Categories**: Explore a wide range of categories to find the perfect image or video.
- **Search**: Use the search feature to quickly find specific images or videos based on keywords.
- **Download**: Download images and videos for free, for both personal and commercial use.
- **Responsive Design**: The website is built with Bootstrap, ensuring it looks great on all devices.
- **Horizontal Scroll**: The website implements horizontal scroll to load more content as the user scrolls horizontally.

## Technologies Used
- **Django**: Backend framework for building the website and handling data.
- **Bootstrap**: Frontend framework for designing responsive and mobile-first websites.
- **JavaScript**: Used for implementing dynamic features such as horizontal scroll and search.
- **Cloudinary**: Integration for storing and serving images and videos.
- **PostgreSQL**: Database management system used by Django for storing data.

![Admin Login](media/admin-login.png)

![Admin Dashboard](media/admin-dashboard-1.png)

![Admin Dashboard](media/admin-dashboard-2.png)

## Getting Started
To run this project locally, follow these steps:
1. Clone the repository:
```
git clone https://github.com/praise002/catalog-z.git
```
2. Navigate to the project directory:
```
cd catalog-z
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Apply database migrations:
```
python manage.py migrate
```
5. Run the development server:
```
python manage.py runserver
```
6. Open your web browser and navigate to http://localhost:8000 to view the website.

## References and Resources
- [Templatemo](https://templatemo.com)
- [Registration form template](https://mdbootstrap.com/docs/standard/extended/registration/)
- [Login template incomplete](https://mdbootstrap.com/docs/standard/extended/login/)
- [remove download solution 1](https://www.quora.com/How-do-I-disable-the-download-button-from-the-controls-in-HTML5-video-for-Google-Chrome)
- [remove download solution 2](https://stackoverflow.com/questions/60469776/how-to-remove-the-download-button-from-video-element#:~:text=Just%20use%20the%20setAttribute%20method,the%20download%20option%20for%20you.&text=That%20button%20is%20not%20provided,browser%20that's%20viewing%20the%20content.)