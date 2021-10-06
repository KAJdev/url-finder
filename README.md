# url-finder
A small python module to detect all real links in a given string.


## Example

```py
import url_finder

text = """
Picking out google.com is trivial. As well as youtube.com,
and even knows what is a real tld, and what is not.a.real.top-level-domain!
"""

assert url_finder.get_urls(text) == ["https://google.com", "https://youtube.com"]
```

## Install
```
pip install url-finder
```
