# AfagR_Docker_week12

[![Build and Push Docker Image](https://github.com/nogibjj/AfagR_Docker_mini12/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/AfagR_Docker_mini12/actions/workflows/CI.yml)

I developed a containerized Flask application that generates workout plan based on a database of pre-defined workout plans. 

## Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment (optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```


5. Access & use the App

- 5.1 Click the link `http://localhost:5001` to visit the application
![Image2](images/request.png)

- 5.2 Welcome Page
![Image2](images/welcome.png)

- 5.3 Enter the target area and see the workout plan
![Image](images/result.png)


## Dockerhub Image

The application image is available on Docker Hub: 
![Image](images/docker_image.png)




## Testing

Run the tests using:
```bash
python -m pytest test_app.py
```
![Image](images/test.png)



## Continuous Integration

The project uses GitHub Actions for CI/CD. The workflow includes:
- Running tests
- Building Docker image
- Publishing to Docker Hub
