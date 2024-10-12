# MD Clone - Blog and Content Management System

This repository contains the implementation of an MD Clone with blog management, category and tag organization, and user profile functionalities.

---

## Table of Contents

- [Introduction](#introduction)
- [Blog: Managing Posts, Images, and Content](#blog-managing-posts-images-and-content)
- [Categories and Tags](#categories-and-tags)
- [User Profile: Managing User Information and Profiles](#user-profile-managing-user-information-and-profiles)
- [Technologies](#technologies)
- [Usage](#usage)
- [Contact](#contact)
- [License](#license)

---

## Introduction

MD Clone is a Django-based blog management system where users can create posts, manage categories and tags, and update their profiles. The project uses Django’s powerful ORM and TinyMCE for rich text content management.

---

## Blog: Managing Posts, Images, and Content

The blog module allows users to create and manage content, including text, images, and HTML. Key features include:

- **Post Title**: Each post has a title, automatically generating a URL-friendly slug using `AutoSlugField`.
- **Content**: Rich content of the post is managed with TinyMCE, allowing for text formatting, image embedding, and HTML.
- **Cover Image**: Blog posts can include a cover image to represent the content visually.
- **Is Active**: Indicates whether the post is published.
- **Timestamps**: Automatically records post creation and update times.

This module provides an easy way for users to share updates, thoughts, and news through engaging content.

---

## Categories and Tags

The category and tag system helps organize blog content effectively:

- **Category Management**: Categories such as “Technology,” “Lifestyle,” and “News” can be created to group similar posts.
- **Tag Management**: Users can add tags to their posts, helping readers discover related content. Each tag is auto-populated from the post title and can be managed individually.

Categories and tags provide a structured way to organize and filter blog content.

---

## User Profile: Managing User Information and Profiles

The user profile system is linked to Django’s built-in `User` model and allows for managing personal information.

- **Profile Information**: Users can update their personal information, including an avatar image and Instagram handle.
- **Slug**: Each user has a unique slug for easy URL management.
- **Profile Content**: The `TinyMCE` editor allows users to write detailed descriptions about themselves.

This module offers users a personalized experience by allowing them to manage their profile data.

---

## Technologies

- **Django Framework**: The core of the web application backend.
- **PostgreSQL**: Database for structured data management.
- **TinyMCE**: Rich text editor for creating and managing blog content.
- **AutoSlugField**: Automatically generates slugs for posts and categories based on titles.

---

## Usage

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/md-clone.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

---

## Contact

For any inquiries or issues, please contact [your-email@example.com](mailto:your-email@example.com).

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
