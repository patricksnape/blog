Date: 2014-01-11
Title: Offscreen Rendering In Linux
Tagline: Compiling llvmpipe on Ubuntu 13.04
Slug: offscreen_rendering
Category: Blog
Tags: offscreen, llvmpipe, vtk, linux
Email: patricksnape@gmail.com

One of the techniques that I've been investigating recently, called [Morphable Models](http://www.cs.cmu.edu/~efros/courses/AP06/Papers/Blanz-siggraph-99.pdf), involves optimising the position and appearance of a 3D model in relation to a single image. In particular, the model must be rasterized in to the scene to allow for optimising over the accuracy of the fitting. This rasterisation step is reasonably easy, but something that I wanted to be able to run on a headless Linux (Ubuntu) cluster. Unfortunately, this machine does not contain a graphics card. Therefore, I thought it would be good to layout the differences between different types of 'headless' rendering, and what exactly they mean.

The term headless rendering (or offscreen rendering), seems to imply a number of differing rendering choices. ‘Headless rendering’ might involve rendering a scene:

 - Without showing a window
 - On a headless server (no active window manager)
 - Without any graphics card (software rendering)

Each of these options obviously requires a different solution. In the next few sections I'm going to give a practical example of getting each type of 'headless' rendering working using [VTK](http://www.vtk.org/), and in particlar, [Mayavi](http://code.enthought.com/projects/mayavi/).

Unfortunately, the way to do these things changes a lot between VTK versions. I have chosen VTK 5.8 because I am particularly interested in using it for offscreen rendering using Mayavi in Python and Mayavi only (at the time of writing) supports VTK 5.8. Therefore, my examples will assume that we are attempting to use VTK 5.8.

## Without showing a window
This is exactly the same as the example given in the Mayavi documentation:

```python
from mayavi import mlab
mlab.options.offscreen = True
mlab.test_contour3d()
mlab.savefig('example.png')
```

This just involves setting the offscreen option to ``True``. However, this assume that you are rendering inside an active X11 session. This obviously implies the existence of a graphics card!

## On a headless server (no X11)
This, as documented in the Mayavi documentation, involves providing a virtual X11 buffer. This requires the command ``xvfb-run``, which can be installed using ``apt-get``:

```bash
sudo apt-get install xvfb
```

Once installed, a virtual X11 frame buffer can be provided with the command:

```bash
xvfb-run --server-args="-screen 0 1024x768x24" python my_script.py
```

You will still probably want to use the offscreen flag as previously shown!

## Software rendering
This is when things start to get particularly tricky. In the case, we need to compile a custom version of VTK 5.8 that is linked against an appropriate software renderer. In the case of Linux, this is OSMesa. Now, given that we are running on Linux, we will want to use the fastest software rasterizer we can, which is llvmpipe. Therefore, we begin the complex process of building VTK 5.8 with offscreen rendering support. I was unable to generalise this process, and only able to get it working for very specific versions of the requisite libraries. Confirmation of using more recent versions is greatly appreciated.

### Building OSMesa
Download OSMesa 9.2.3 from [here](ftp://ftp.freedesktop.org/pub/mesa/9.2.3/MesaLib-9.2.3.tar.bz2). You will need to make sure you have all the dependencies as outlined [here](http://www.mesa3d.org/install.html), but most probably, for Ubuntu, you will need

```bash
sudo apt-get install scons flex bison
```

You will also need LLVM with version greater than 3.0. I managed to get it working by installing LLVM 3.2 (though I think 3.3 works as well):

```bash
sudo apt-get install llvm-3.2-dev llvm-3.2-source
```

Given that we got this from aptitude, it doesn’t seem to setup LLVM properly, so we need to set up the correct sumbolic link to ``llvm-config``:

```bash
sudo ln -s /usr/bin/llvm-config-3.2 /usr/local/bin/llvm-config
```

We can then build llvmpipe by navigating in to the extracted OSMesa folder and executing:

```bash
scons llvm=yes build=release mesa osmesa libgl-xlib
```

Which has then successfully built llvmpipe and OSMesa.

### Building Offscren VTK 5.8
Download VTK 5.8 from [here](http://www.vtk.org/files/release/5.8/vtk-5.8.0.tar.gz).

Unzip it, make a folder called ``build`` inside it and then create a new script inside ``build`` called ``configure_cmake.sh``.

Inside, paste the following script:

```bash
MESA_INSTALL_PREFIX=PATH_TO_MESA_9.2.3_FOLDER
 
cmake \
 -DBUILD_SHARED_LIBS=ON \
 -DVTK_WRAP_PYTHON=ON \
 -DVTK_USE_X=OFF \
 -DOPENGL_INCLUDE_DIR=${MESA_INSTALL_PREFIX}/include \
 -DOPENGL_gl_LIBRARY=${MESA_INSTALL_PREFIX}/build/linux-x86_64/gallium/targets/libgl-xlib/libGL.so \
 -DOPENGL_glu_LIBRARY=/usr/lib/x86_64-linux-gnu/libGLU.so \
 -DVTK_OPENGL_HAS_OSMESA=ON \
 -DOSMESA_INCLUDE_DIR=${MESA_INSTALL_PREFIX}/include \
 -DOSMESA_LIBRARY=${MESA_INSTALL_PREFIX}/build/linux-x86_64/mesa/drivers/osmesa/libosmesa.so \
 ..
```

Where ``MESA_INSTALL_PREFIX`` is the absolute path to wherever you extracted the OSMesa archive.

You can then run ``make`` to make VTK, which takes a while. You may want to use the ``-j`` switch to [decrease compile times](http://make.paulandlesley.org/jobserver.html).

Once VTK is finished, we can set up a virtualenv to use the offscreen VTK.

### Setting up Mayavi
Create a virtualenv, then ``cd`` to ``PATH_TO_VTK5.8/build/Wrapping/Python``, where ``PATH_TO_VTK5.8`` is the absolute path to wherever you built VTK 5.8.

You can then install it in to the virtualenv by running

```bash
LD_LIBRARY_PATH=PATH_TO_VTK5.8/build/bin/ python setup.py install
```

Then, to test it worked, run

```bash
LD_LIBRARY_PATH=/PATH_TO_VTK5.8/build/bin/ python
```

Then try

```python
import vtk
```

which should work without error. Then install mayavi by running

```bash
pip install numpy

LD_LIBRARY_PATH=/PATH_TO_VTK5.8/build/bin/ pip install mayavi
```

Then, we can test everything worked by running

```bash
LD_LIBRARY_PATH=/PATH_TO_VTK5.8/build/bin/ python
```

and trying

```python
from mayavi import mlab
mlab.options.offscreen = True
mlab.test_contour3d()
mlab.savefig('example.png')
```

which should successfully create the image!

In order to avoid pre-pending every command with ``LD_LIBRARY_PATH=/PATH_TO_VTK5.8/build/bin/``, you can update your ``LD_LIBRARY_PATH`` using any of the normal ways on Linux (creating a conf file in ``/etc/ld.so.conf.d/`` or updating your ``.bashrc`` file).
