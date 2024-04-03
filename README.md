# Securely Containerize a Python Application with Chainguard Images

Example application and Dockerfile for the "Securely Containerize a Python Application with Chainguard Images" blog post on dev.to.

To run the application, first set up a Python virtual environment. Install the dependency with:

```bash
pip install -r requirements.txt 
```

Run the application:

```bash
python main.py
```

To build with Docker and run:

```bash
docker build . -t timeteller
docker run --rm timeteller
```
