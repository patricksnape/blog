Title: Example code etc
Date: 2012-12-01 10:02

See below intra-site link examples in Markdown format.

[a link relative to content root]({filename}/article1.md)

{% notebook test.ipynb %}

```python
def factorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n - 1)
```