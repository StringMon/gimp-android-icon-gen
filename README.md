gimp-android-icon-gen

This is a Python-Fu Gimp plugin designed to make it easy to generate output icon resources for your android project. The plugin takes your current visible image in Gimp and generates web-, xhdpi-, hdpi- and mdpi- png assets in the proper android folder structure. With this plugin, you can iteratively tweak and test the icon for your android app without having to export multiple files or drag and drop or rename anything.

To install, just put `androidResourceGen.py` in your `.gimp-X.X/plug-ins` folder and restart Gimp. Make sure you have Gimp Python support enabled.

On Windows, it's `5USERPROFILE%\AppData\Roaming\GIMP\X.X\plug-ins`.
