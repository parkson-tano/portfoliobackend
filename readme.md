# Cameroon Portfolio Backend Repository

This repository contains the backend code for the Cameroon Portfolio project, which aims to provide a platform for coders to showcase their portfolios. The project is created with love and is open to contributions from developers worldwide.

## Features that  should be added to the frontend

1. **Portfolio Submission Form**: Users can submit their portfolios using a form, allowing them to showcase their work to the community. then the receive a key that will allow them to update their portfolio later

2. **Portfolio Update Request**: Users can request updates to their portfolios by submitting a form with their email and a unique key. The key ensures that only the portfolio owner can make updates.

## Features of the backend

1. **Admin Dashboard**: The Django admin dashboard is utilized to manage portfolio submissions, update requests, and handle lost keys.

## Getting Started

To get started with the Cameroon Portfolio project, follow these steps:

1. Clone the repository and run the backend on linux:

    ```bash
    git clone repository_url
    cd cameroon-portfolio-backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py runserver
   ```

2. Clone the repository and run the backend on windows:

    ```batch
        python -m venv venv           rem to create the virtualenvironment
        venv\Scripts\activate         rem to activate the virtualenvironment
        python manage.py runserver    rem to start the server in development mode
    ```

3. After that you can just navigate to the url

http://localhost:8000/admin to manage the website and approved or deny requests.