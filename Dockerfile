FROM cgr.dev/chainguard/python:latest-dev as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/timeteller/venv/bin:$PATH"

WORKDIR /timeteller

RUN python -m venv /timeteller/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest

ENV TZ="America/Chicago"

WORKDIR /timeteller

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"


COPY main.py ./
COPY --from=builder /timeteller/venv /venv

ENTRYPOINT [ "python", "/timeteller/main.py" ]