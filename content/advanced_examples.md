Title: Example code etc
Date: 2012-12-01 10:02
Status: draft

This article contains some example of advanced syntex, including
intra-site links, math and including a notebook.

[a link relative to content root]({filename}/article1.md)

Include a notebook:

{% notebook test.ipynb %}

Some inline code:

```python
def factorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n - 1)
```
