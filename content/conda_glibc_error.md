Date: 2015-02-13
Title: Conda GLIBC_2.15 Error
Tagline: A simple solution
Slug: conda_glibc
Category: Blog
Tags: conda, python, glibc
Email: patricksnape@gmail.com

If, when using conda (Anaconda or Miniconda), you experience an error that is something like the following:

```
ImportError: /home/pts08/miniconda/envs/_test/bin/../lib/libm.so.6: version `GLIBC_2.15' not found (required by /home/pts08/miniconda/envs/_test/lib/python2.7/site-packages/cyffld2/../../../libfftw3f.so.3)
```

You can quickly solve this by removing/moving the ``libm.so.6`` library so that your packages don't accidentally link against it.

For example:

```
mv /home/pts08/miniconda/envs/_test/bin/../lib/libm.so.6 /home/pts08/miniconda/envs/_test/bin/../lib/libm.so.6.bak
```

This problem is caused because conda ships with a package called ``system`` that contains ``libm`` (library for fast math calculations). However, the ``libm.so`` version that it ships with is linked against an older version of GLIBC than was used to build the library that is failing to link. This causes a conflict which cannot be resolved and results in the not found error.
