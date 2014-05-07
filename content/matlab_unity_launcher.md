Date: 2014-05-07
Title: Matlab Ubuntu Unity Launcher
Tagline: For those of us cursed with Matlab
Slug: matlab_unity_launcher
Category: Blog
Tags: matlab, unity, ubuntu
Email: patricksnape@gmail.com

I was having some trouble getting Matlab to play nicely with the Unity launcher
in Ubuntu. It seems as though Matlab requires you to pass the ``-desktop`` flag
on Linux. The default behaviour seems to be something along the lines of show
the splash screen and then close. Therefore, in order to make the launcher work 
properly, I proceeded as follows:

  1. Install Matlab as per it's instructions
  2. Add ``/usr/local/MATLAB/R2014a/bin`` to ``PATH``
  3. Launch ``matlab`` in a terminal
  4. Right click Matlab in the launcher and choose ``Lock To Launcher``
  5. Close Matlab, a launcher icon should stay (though it won't work properly)
  6. Edit the file ``~/.local/share/applications/com-mathworks-util-postvminit.desktop``
  7. Add ``-desktop`` to the end of the line ``Exec=/usr/local/MATLAB/R2014a/bin/glnxa64/MATLAB -desktop``

Note that these instructions should work for any version of Matlab (just change
the path appropriately).
