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
