# contact-form-processor

A fast and simple contact form processor/handler, powered by FastAPI.

## Configuration

Configuration is handled via environment variables.

| Environment variable | Description                                                         | Default                                |
| -------------------- | ------------------------------------------------------------------- | -------------------------------------- |
| `HCAPTCHA_SECRET`    | hCaptcha secret key                                                 | `None` (hCaptcha will not be verified) |
| `MAIL_FROM`          | "From" address for emails to site owner. Format: `mail@example.com` | **required**                           |
| `MAIL_TO`            | "To" address for emails to site owner. Format: `mail@example.com`   | **required**                           |
| `SMTP_HOSTNAME`      | SMTP server hostname                                                | **required**                           |
| `SMTP_STARTTLS_PORT` | STARTTLS port number for the SMTP server.                           | `587`                                  |
| `SMTP_USERNAME`      | SMTP username.                                                      | `None`                                 |
| `SMTP_PASSWORD`      | SMTP password.                                                      | `None`                                 |

## Installation

### Install with Docker

```bash
# Replace [ADDRESS]:[PORT] with whereever you want the container to listen at
# When using a reverse proxy, make sure this container is NOT EXPOSED to the
# Internet! (e.g. listen on 127.0.0.1)
docker run -d -p [ADDRESS]:[PORT] \
  --env-file=.env \
  --restart unless-stopped \
  --name contact-form-processor \
  ghcr.io/chrisx8/contact-form-processor:latest
```

### Install in a virtualenv

- This site only supports Python 3.8 or newer. Make sure Python (3.8 or newer)
  and `pip` are installed.
- Install project dependencies.

```bash
# Create virtualenv
python3 -m venv venv

# Activate virtualenv and install dependencies
source venv/bin/activate
pip install -r requirements.txt
```

- Start server

```bash
# Replace [ADDRESS]:[PORT] with whereever you want the container to listen at
# When using a reverse proxy, make sure this container is NOT EXPOSED to the
# Internet! (e.g. listen on 127.0.0.1)
uvicorn --host [ADDRESS] --port [PORT] main:app
```

## License

Copyright (C) 2022 Chris Xiao

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see
<https://www.gnu.org/licenses/>.
