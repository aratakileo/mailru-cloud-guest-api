# mailru-cloud-guest-api
Non-official wrapper API for mail.ru cloud designed to generate a link or links to a file stream via a public link, for example to download file as a guest

### Requirements
- `python >= 3.10`

### Install
```
pip install git+https://github.com/aratakileo/mailru-cloud-guest-api.git
```

<details>
  <summary>for <code>windows</code></summary>
  

```
py -m pip install git+https://github.com/aratakileo/mailru-cloud-guest-api.git
```
</details>

<details>
  <summary>for <code>unix</code>/<code>macos</code></summary>
  

```
python3 -m pip install git+https://github.com/aratakileo/mailru-cloud-guest-api.git
```
</details>


### Quick how to use
You can easily get a link to stream a file download by writing the following code, which will output the streaming link to the console:

```py
from mailru_cloud_guest_api import FileStreamGenerator

# replace `https://cloud.mail.ru/public/file_id` with your public link
print(FileStreamGenerator.of('https://cloud.mail.ru/public/file_id').generate().stream_link)
```

### How to use
This library offers a special object for generating a file stream link. You can create it as follows:

```py
from mailru_cloud_guest_api import FileStreamGenerator

# replace `https://cloud.mail.ru/public/file_id` with your public link
streamGenerator = FileStreamGenerator.of('https://cloud.mail.ru/public/file_id')
```

Before generating the file stream link, you can configure the generator using the following methods:
```py
# set request email
streamGenerator.setMail('your_mail@mail.ru')

# set file stream link in seconds
streamGenerator.set_lifetime_in_seconds(10)

# set file stream link in minutes
streamGenerator.set_lifetime_in_minutes(5)

# set file stream link in hours
streamGenerator.set_lifetime_in_hours(1)
```

After configuring the generator, you can get a special object that stores the file stream link:

```py
container = streamGenerator.generate()

# print file stream link
print(container.stream_link)

# download file (replace `my_file.zip` with the filename as which the downloaded file will be saved)
container.download('my_file.zip')
```

### License
```
Copyright (c) 2024 Arataki Leo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
