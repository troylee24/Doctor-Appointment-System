# Doctor Appointment System
A REST API built with Python, Django, Django Rest Framework (DRF).<br />

This project provides an appointment service where registered doctors and patients can schedule appointments. It provides endpoints for basic CRUD operations on each entity (i.e. Doctor, Patient, Appointment) and some filtering options based on query parameters.

---

## Project Files Description
`/myproj/myapi/`
* **models.py** - Defines the models.
* **validators.py** - Defines custom validators for models.
* **serializers.py** - Serializes the models.
* **views.py** - Defines the HTTP methods and behaviors for a request.
* **urls.py** - Maps endpoint URLs to approriate views.

`/myproj/myproj/`
* **urls.py** - Includes all endpoints defined in `/myproj/myapi/urls.py`.
* **settings.py** - Defines the settings for the project (i.e. enables `myapi` and `rest_framework`).

---

## Install Dependencies
```
$ pip install django
$ pip install djangorestframework
```

## Getting Started
```
$ cd myproj
$ python3 manage.py runserver
```

## Model Migration
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

---

## Models

### Doctor
* `id`: int *(primary key)*
* `first_name`: string
* `last_name`: string

### Patient
* `id`: int *(primary key)*
* `first_name`: string
* `last_name`: string

### Appointment
* `id`: int *(primary key)*
* `doctor`: Doctor *(foreign key)*
* `patient`: Patient *(foreign key)*
* `date`: datetime.date
* `time`: datetime.time
* `kind`: string *('NP' - "New Patient", 'FU' - "Follow-up")*

---

## API Endpoints

### API Root
* Displays hyperlinks to main endpoints: `GET ''`

### Doctors
Interacts with the Doctor model
* Show all doctors: `GET /doctors/`
* Add new doctor: `POST /doctors/`
* Show a doctor: `GET /doctors/<doctor.id>/`
* Update a doctor: `PUT /doctors/<doctor.id>/`
* Delete a doctor: `DELETE /doctors/<doctor.id>/`

### Patients
Interacts with the Patient model
* Show all patients: `GET /patients/`
* Add new patient: `POST /patients/`
* Show a patient: `GET /<patient.id>/`
* Update a patient: `PUT /patients/<patient.id>/`
* Delete a patient: `DELETE /patients/<patient.id>/`

### Appointments
Interacts with the Appointment model
* Show all appointments: `GET /appointments/`
* Schedule a new appointment: `POST /appointments/`
* Cancel an appointment: `DELETE /appointments/`
* Show an appointment: `GET /appointments/<appointment.id>/`
* Update an appointment: `PUT /appointments/<appointment.id>/`
* Delete an appointment: `DELETE /appointments/<appointment.id>/`

### Filtering
* Doctor's appointment schedule for a given day: `/appointments/?doctor=<doctor.id>&date=<appointment.date>/`
  
### Filtering [To-Do]
* Doctor's appointment schedule: `/appointments/?doctor=<doctor.id>/`
* Patient's appointment schedule: `/appointments/?patient=<patient.id>/`
* All appointments at a given time: `/appointments/?time=<appointment.time>/`
* All appointments for a given day: `/appointments/?date=<appointment.date>/`
* Doctor's appointment schedule with a given patient: `/appointments/?doctor=<doctor.id>&patient=<patient.id>/`
