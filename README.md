
# Cloudflare Checker
This project includes a Python tool that detects whether given websites are utilizing Cloudflare. Cloudflare is a content delivery network and security service employed by numerous websites to enhance security and performance. This tool examines specific URLs and determines the usage of Cloudflare services based on server headers.

## Project Features
Single URL Check: Using the project, you can determine whether a specific URL is using Cloudflare services or not. If the URL is not in a valid format or experiences a timeout during the connection, information about its status will be provided.

File-Based Check: The project examines whether URLs listed in a file are using Cloudflare services. This feature allows you to automatically analyze large lists of URLs.

### Requirements

The following Python libraries are necessary for this project to function:

argparse: Used for handling command-line arguments.

requests: Used for sending and receiving HTTP requests.

### Command Line Arguments

```
-d, --domain: Used to check the Cloudflare status of a single URL.

-i, --input: Used to check the Cloudflare status of URLs from a file.

-h, --help: Used to view help messages. 
```

### Usage Example
> #### Single URL Check:

```python cloudflare_check.pt --domain https://example.com```

![](https://github.com/ahmetnuysal/cloudflare_check/blob/main/Pics/Cloudflare_Check_%C3%87%C4%B1kt%C4%B1.png)

> #### File-Based Check:

```python cloudflare_check.pt --input https://example.com```

![](https://github.com/ahmetnuysal/cloudflare_check/blob/main/Pics/Cloudflare_Check_%C3%87%C4%B1kt%C4%B1_Toplu.png)

### How to Containerize Project with Docker?

> #### 1. Creating a Dockerfile:
  The first step is to create a Dockerfile, which will enable you to move our project into a Docker container. The Dockerfile contains the steps for building a container.

> #### 2. Building the Docker Image:
  To create the Docker image, open your command prompt and navigate to the directory where your project is located. Then, run the following command:
  
  ```docker build -t python-docker .```
  
  Here, the "-t" flag assigns a tag to the image. "python-docker" is the name you want to give to your image. The dot "." represents the current directory.

> #### 3.Running the Container:
  After successfully building the Docker image, you can start a container using the following command:

  ```docker run python-docker python cloudflare_check.py -i file.txt or docker run python-docker python cloudflare_check.py -d website-URL```




