import requests
import time

BASE_URL = 'http://127.0.0.1:8000/api/'

timestamp = int(time.time())

TEST_APPLICANT = {
    "first_name": "rahul4",
    "last_name": "sow44",
    "email": "rahu4l.snow@example.com",
    "phone": "+12125690",
    "gender": "male",
    "available": "full_time",
    "disability": "No",
    "disability_detail":"MAy be",
    "linkedin": "https://linkedin.com/in/johndoe",
    'resume': 'file.pdf',
    'cover_letter': 'file.pdf',
}

def create_categories_and_jobs():
    print("Creating categories and jobs...")
    if True:
        response = requests.get(BASE_URL + 'categories/')
        category_id = response.json()
        print(category_id)

        response = requests.get(BASE_URL + 'jobs/')
        print('\n\n\n\n')
        job_id = response.json()
        print(f'Jobs : {job_id}')

        print("\nJob Category Counts (from /categories/with_counts/):")
    response = requests.get(BASE_URL + 'categories/with_counts/')
    categories = response.json()
    print(categories)
    print('\n\n')

    response = requests.get(BASE_URL + f'categories/2/')
    print(f'category by id : {response.json()}')
    print('\n\n')

    response = requests.get(BASE_URL + 'jobs/2/')
    job_one = response.json()
    print(f'jod by id : {job_one}')

    job_id = 2
    print(f"Applying for job ID: {job_id}")
    files = {
        'resume': ('resume.pdf', b'Test resume content', 'application/pdf'),
        'cover_letter': ('cover.pdf', b'Test cover letter content', 'application/pdf')
    }
    data = TEST_APPLICANT.copy()
    data['job'] = job_id
    response = requests.post(BASE_URL + 'applicants/', data=data, files=files)
    print(f"Successfully applied for job ID: {job_id} --- {response.json()}")

if __name__ == "__main__":
    print("Starting minimal API tests...")
    try:
        create_categories_and_jobs()
        
    except AssertionError as e:
        print(f"Test failed: {e}")


# add api and call http://127.0.0.1:8000/api/applicants/
#   and count the total objects and instead '17' write that number and dont disturb other file