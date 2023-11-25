# Spontan App
Spontan microservices consist of 3 end-points
- Main - /main
- get similar product - /getSimilarProduct
- get list similar - /getListSimilar
- insert similar - /insertSimilar

<!-- GETTING STARTED -->
## Getting Started

These are steps to install Spontan App locally

### Prerequisites

1. Create  Python environment
  ```sh
  # Create a virtual environment
  python -m venv my_microservice_env
  ```
2. Activate Environment
  ```sh 
  # Activate the virtual environment (on Windows)
  my_microservice_env\Scripts\activate

  # Activate the virtual environment (on macOS/Linux)
  source my_microservice_env/bin/activate
  ```

### Installation
_please make sure the env is in active, or activate the environment_

1. Clone the repo
   ```sh
   git clone https://github.com/ilhamrizk/spontan_app_env.git
   ```
2. Set up Environment
   ```sh
   # Move to folder repo
   cd spontan_app_env

   # install requirements
   pip install -r requirements.txt

   # Install NLTK
   python download_nltk.py
   ```
   
### Start Services
_please make sure the env is in active, or activate the environment_

1. Start the app
  ```sh
  python app.py
  ```
