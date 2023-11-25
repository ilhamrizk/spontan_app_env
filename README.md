# Spontan App
Spontan microservices consist of 3 end-points
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

## End-points
### getSimilarProduct - GET
to get a similar product from input free text. return the best similar product and store to data
http://localhost:5000/getSimilarProduct
  ```json
  {
      "pos": "roundup 500ml"
  }
  ```

Request example
  ```py
  import requests
  
  url = "http://localhost:5000/getSimilarProduct"
  
  payload = "{\r\n    \"pos\": \"petro za plus\"\r\n}"
  headers = {}
  
  response = requests.request("GET", url, headers=headers, data=payload)
  
  print(response.text)
  ```

Response example
  ```json
  {
    "result": {
      "best_match": {
        "Brand": "Tanpa Merek ",
        "Formula": NaN,
        "Product SKU": "Tanpa Merek TRICHOTEC WP",
        "Type": "Pestisida Biologi",
        "description": "Tanpa Merek TRICHOTEC WP Tanpa Merek  Pestisida Biologi",
        "description_clean": [
          "wp",
          "trichotec",
          "pestisida",
          "biologi"
        ],
        "description_nonumber": [
          "wp",
          "trichotec",
          "pestisida",
          "biologi"
        ],
        "index": 4118,
        "new_sku": 1.0
      },
      "classification": "match",
      "product": "marshal wp",
      "similarity": 0.2,
      "time": "Wed, 22 Nov 2023 22:57:05 GMT"
    }
  }
  ```

### getListSimilar - GET
return list of similar product
http://localhost:5000/getListSimilar

Request example
  ```py
  import requests
  
  url = "http://localhost:5000/getListSimilar"
  
  payload = "{\r\n    \"pos\": \"petro za plus\"\r\n}"
  headers = {}
  
  response = requests.request("GET", url, headers=headers, data=payload)
  
  print(response.text)
  ```
Response example
  ```json
  {
      "result": [
          {
              "Brand": "PIHC",
              "Category": "pupuk",
              "Formula": NaN,
              "Product SKU": "ZA Plus Petro",
              "Type": "ZA",
              "description": "ZA Plus Petro PIHC ZA",
              "index": 7,
              "is_fertilizer": 1,
              "is_fertilizer_n_friend": 1,
              "new_sku": 0.0,
              "similarity": 0.75
          },
          {
              "Brand": "Tanpa Merek ",
              "Category": "pupuk",
              "Formula": NaN,
              "Product SKU": "Tanpa Merek ZA PLUS PETRO",
              "Type": "Urea",
              "description": "Tanpa Merek ZA PLUS PETRO Tanpa Merek  Urea",
              "index": 4203,
              "is_fertilizer": 1,
              "is_fertilizer_n_friend": 1,
              "new_sku": 1.0,
              "similarity": 0.75
          },
          {
              "Brand": "PETRO",
              "Category": "pupuk",
              "Formula": NaN,
              "Product SKU": "PETRO ZA (Butiran)",
              "Type": "ZA (Butiran)",
              "description": "PETRO ZA (Butiran) PETRO ZA (Butiran)",
              "index": 297,
              "is_fertilizer": 1,
              "is_fertilizer_n_friend": 1,
              "new_sku": 1.0,
              "similarity": 0.6666666666666666
          },
          {
              "Brand": "PIHC",
              "Category": "pupuk",
              "Formula": NaN,
              "Product SKU": "ZA Petro",
              "Type": "ZA",
              "description": "ZA Petro PIHC ZA",
              "index": 6,
              "is_fertilizer": 1,
              "is_fertilizer_n_friend": 1,
              "new_sku": 0.0,
              "similarity": 0.5
          },
          {
              "Brand": "Tanpa Merek ",
              "Category": "pupuk",
              "Formula": NaN,
              "Product SKU": "Tanpa Merek PUPUK PETRO NPK PHONSKA PLUS",
              "Type": "Pupuk NPK",
              "description": "Tanpa Merek PUPUK PETRO NPK PHONSKA PLUS Tanpa Merek  Pupuk NPK",
              "index": 4624,
              "is_fertilizer": 1,
              "is_fertilizer_n_friend": 1,
              "new_sku": 1.0,
              "similarity": 0.4
          }
      ]
  }
  ```
### insertSimilar - POST
insert by index a simlilar product to data, return success if success
http://localhost:5000/insertSimilar

Request example
  ```py
  import requests
  
  url = "http://localhost:5000/insertSimilar"
  
  payload = "{'index': 7}"
  headers = {}
  
  response = requests.request("GET", url, headers=headers, data=payload)
  
  print(response.text)
  ```
Response example
  ```json
  {
      "result": "success"
  }
  ```
