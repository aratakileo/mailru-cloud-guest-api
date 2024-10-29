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

### How to use
To get a list of links to send a request to form a link stream, then you will need the following code:
```py
from mailru_cloud_guest_api import MailruCloudDispatcherApiRequester

dispatcher_api_requester = MailruCloudDispatcherApiRequester()

print(dispatcher_api_requester.request_answer)
```

If there are no problems, then this code will output a dictionary containing various kinds of links to request a stream link. If something went wrong, `None` will be returned.

To send a new request, use the following method:
```py
print(dispatcher_api_requester.send_request())
```

To generate a new request link, use the following method:
```py
print(dispatcher_api_requester.generate_request_link())
```

To get a stream link to download a file, you will need the following code:
```py
from mailru_cloud_guest_api import MailruCloudFileStreamLinkGenerator

# replace `https://cloud.mail.ru/public/file_id` to your public link
file_stream_link_generator = MailruCloudFileStreamLinkGenerator('https://cloud.mail.ru/public/file_id')

print(file_stream_link_generator.file_stream_link)
```

If there are no problems, then this code will output a stream link. If something went wrong, `None` will be returned.

To generate a new stream link, use the following method:
```py
print(file_stream_link_generator.generate_link())
```

To download a file by stream link, use following method:
```py
# replace `my_file.zip` to the filename as which the downloaded file will be saved
print(file_stream_link_generator.download('my_file.zip'))
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
