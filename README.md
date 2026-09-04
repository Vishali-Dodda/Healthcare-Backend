# Healthcare Backend API

A secure Healthcare backend API built with Django REST Framework and PostgreSQL, providing JWT-based authentication and APIs for managing patients, doctors, and patient-doctor mappings.

## Project Overview

The Healthcare Backend API is a RESTful backend system developed using Django and Django REST Framework.

The system allows users to:

- Register and log in securely using JWT authentication.
- Authenticated users can be able to add and manage the patient records.
- Authenticated users can be able to add and manage the doctor records.
- Assign doctors to patients.
- View patient-doctor mappings.
- Remove patient-doctor mappings.

The project uses Django ORM for database operations and PostgreSQL as the database. Authentication and protected API access are implemented using JSON Web Tokens (JWT).

## Tech Stack

- **Backend:** Python, Django
- **API Framework:** Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JSON Web Tokens (JWT)
- **JWT Library:** djangorestframework-simplejwt
- **ORM:** Django ORM
- **API Testing:** Postman
- **Version Control:** Git & GitHub

# Features

### Authentication
- User registration with name, email, and password.
- User login with JWT authentication.
- Access and refresh token generation.
- Protected API endpoints using JWT authentication.

### Patient Management
- Create patient records using authenticated user only.
- Retrieve all patients belonging to the authenticated user.
- Retrieve a specific patient.
- Update patient information.
- Delete patient records.
- Patient ownership-based access control.

### Doctor Management
- Create doctor records using authenticated user only.
- Retrieve all doctors.
- Retrieve a specific doctor.
- Update doctor information.
- Delete doctor records.

### Patient-Doctor Mapping
- Assign a doctor to a patient.
- Retrieve all patient-doctor mappings.
- Retrieve mappings for a specific patient.
- Delete a patient-doctor mapping.
- Prevent duplicate doctor assignments to the same patient.
- Restrict mapping operations to patients owned by the authenticated user.

## Images

### User registration

<img width="933" height="311" alt="image" src="https://github.com/user-attachments/assets/e3f9a63f-b7a6-4fb7-8938-f93744041bf3" />

### User login

<img width="931" height="305" alt="image" src="https://github.com/user-attachments/assets/0796294f-709f-4695-94dd-0353584bc84e" />

### Patient data

<img width="988" height="551" alt="image" src="https://github.com/user-attachments/assets/274004f1-e84b-45b8-a0dd-0c8eb8bb214b" />

### Doctor data

<img width="986" height="547" alt="image" src="https://github.com/user-attachments/assets/68d5d9e2-21b6-4eba-ab23-a30f9e40ff05" />

### Patient-Doctor mappings

<img width="988" height="616" alt="image" src="https://github.com/user-attachments/assets/f5674df8-c6d3-4bee-994e-ab59d6c3892f" />
