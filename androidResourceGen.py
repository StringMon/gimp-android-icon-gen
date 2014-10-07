#!/usr/bin/env python

from gimpfu import *
import io
import os
from collections import defaultdict

def python_android_icon_generator(img, layer, folder_structure, wrap, outDirectory, outname, websz, xhdpisz, hdpisz, mdpisz):
	if wrap: 
		filename = os.path.basename(img.filename).split(".")[0] #gets file name for use as directory
		outDirectory = os.path.join(outDirectory, filename)	
		
	'''
	The wrap option allows the user to generate output inside a directory 
	(e.g. if they want to generate icons and email them to a someone else).
	By disabling the wrap option and selecting the root folder of an 
	Android source project, the user can directly overwrite the drawables
	of the project, allowing effortless updating of icons.
	''' 
	
	
	
	sizes = { #map sizes to icon dimensions (icons are square, we only
				"web": websz,
				"xhdpi": xhdpisz,
				"hdpi": hdpisz,
				"mdpi": mdpisz
				}
	if folder_structure:
		outpaths = {#map sizes to output folder structures
					"web":   outDirectory,
					"xhdpi": os.path.join(outDirectory, "res", "drawable-xhdpi"),
					"hdpi":  os.path.join(outDirectory, "res", "drawable-hdpi"),
					"mdpi":  os.path.join(outDirectory, "res", "drawable-mdpi")
					}
	else:
		outpaths = defaultdict(lambda: outDirectory)
	
	for size, res in sizes.items():
		fileNameAugment = "-web" if size == "web" else ("" if folder_structure else "-{}".format(size))

		saveScaledImage(img, outpaths[size], outname + fileNameAugment, res)
	return;
# end


	
def saveScaledImage(image, filepath, filename, res):
	
	
	if not os.path.exists(filepath):
		os.makedirs(filepath)
		
	fullpath = os.path.join(filepath, filename + ".png")
	
	scaledImage = gimp.Image(image.width, image.height, RGB)#new image to copy original to
	
	layer = pdb.gimp_layer_new_from_visible(image, scaledImage, 'final')#merge visible to new, unassociated layer
	scaledImage.add_layer(layer)
	layer.scale(res, res, 0) 
	scaledImage.resize(res, res, 0, 0)
	
	pdb.file_png_save_defaults(scaledImage, layer, fullpath, fullpath)
		# save to file

# end 




###################### setup ##########################################

defaultPath = os.path.join(os.path.expanduser("~"), "Desktop");
defaultPath = defaultPath if os.path.exists(defaultPath) else os.path.expanduser("~")


register(
        "python_fu_icon_gen",
        "Android icon output generator",
        "Generates android target files for mdpi, hdpi, xhdpi and web in proper Android file structures (res/drawable-hdpi, res/drwable-mdpi etc...)",
        "Anton Lodder",
        "Anton Lodder",
        "2013",
        "<Image>/Android/Generate Icon Set...",
        "RGB*, GRAY*",
        [
        (PF_TOGGLE, "folder_structure", "Use Android resource directory structure?", True),
		(PF_TOGGLE, "wrap", "Wrap output in a folder?", True),
		(PF_DIRNAME, "filepath", "Output Filepath", defaultPath),
        (PF_STRING, "filename", "Android Resource Name", "ic_launcher"),
        (PF_INT16, "websz", "Dimension - web:", 512),
        (PF_INT16, "xhdpisz", "Dimension - xhdpi:", 96),
        (PF_INT16, "hdpisz", "Dimension - hdpi:", 72),
        (PF_INT16, "mdpisz", "Dimension - mdpi:", 48),
		],
		[],
        python_android_icon_generator)

main()
'''

		

'''