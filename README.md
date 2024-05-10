# kaggle-file-uploader
An application for uploading dataset files to Kaggle.com.

## Setting up API credentials without a file
The Kaggle API client looks for specific environment variables to authenticate API requests. Set the following environment variables to specify the username and API key:
`KAGGLE_USERNAME`: Your Kaggle username
`KAGGLE_KEY`: Your Kaggle API key

## Usage
How to execute the application:
```
python3 main.py <path/to/folder/with/dataset> "<Notes about the new version>"
```

Useful references for expanding this application:
- https://www.kaggle.com/code/donkeys/kaggle-python-api
- https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md