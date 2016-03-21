
---

lang: en
community: lgbti-mena
type: tactics
weight: 020
title: How to remove hidden information from files

---

Metadata is information about a file (such as a word document, a PDF, a picture, music file etc.) that is stored within the file itself. This information can include the time and date a file was created, the username of the people who created or edited it, information about the device that created it, and other kinds of information. As a result of this, the metadata in a file could tell someone who created a file, on what computer or device, when, and in what location.

While this information is generated automatically by many devices (like cameras, computers, and phones) it can be edited and manipulated by those who know where to look. This can also be a good thing, as it means you can take control over the metadata you choose to share when you share files. 

Let's take pictures as an example. When you take a picture with your digital camera, what happens? If your camera or phone knows where you are, then that information (in the form of GPS coordinates) can be saved in the metadata of the file. If your camera knows what time it is, it records the date and time the picture was taken. If your camera or phone has a serial number that may be recorded in metadata as well. Digital image file formats such as TIFF (Tagged Image File Format) and JPEG (Joint Photographic Experts Group) created by digital cameras or smartphones, contain metadata in a format called EXIF (Exchangeable image file format) which could include all of the above information and even a thumbnail of the original image. 

Other files such as text documents include metadata too. A text document's metadata, for example, may contain information about how long the document is, who the author is, when the document was written, and a short summary of the document.

Metadata can be very useful in helping to organise non-sensitive information. For those who share sensitive or media widely, however, unknowingly attaching information to files can be very dangerous. If you take a picture of a police officer doing something illegal, and share it on the internet without taking care to scrub metadata from the file first, the data may be used to identify who took the picture (in this case, you). 

In order to ensure that this won't happen, it's important to learn how to "scrub" or remove metadata from files when necessary. In part, we have to rely on a special software that removes metadata securely from files. [*Metanull*](../metanull/windows) removes metadata from images, is one such tool, and is discussed below. Furthermore, there are many non-technical, but rather behavioural, ways that we can stop meta-data getting into files in the first place.

# What you can learn from this guide

- How to remove or edit the metadata from files such as image files
- How to upload photos on the internet without revealing the hidden data in it
- How to prevent adding metadata to your files

# Removing metadata from image files
You can check the metadata of a photo by right-clicking on it and selecting *Properties*, or by using a metadata viewer software such as [Photome](http://www.photome.de/download_en.html).

You will see the following:

- **GPS information**

<table border="1">
<tbody>
<tr>
<th>Field</th>
<th>Content</th>
</tr>
<tr>
<td>GPS Tag Version</td>
<td>Version 2.2</td>
</tr>
<tr>
<td>North or South Latitude</td>
<td>North Latitude</td>
</tr>
<tr>
<td>Latitude</td>
<td>50 28 07, 775</td>
</tr>
<tr>
<td>East or west longitude</td>
<td>East Longitude</td>
</tr>
<tr>
<td>Longitude</td>
<td>7 37 32, 75</td>
</td>
</tr>
<tr>
<td>Atitude Reference</td>
<td>Sea Level</td>
</tr>
<tr>
<td>Altitude</td>
<td>262 m</td>
</td>
</tr>
</tbody>
</table>

The above information can specify your exact location, which is in our example: **1 km northwest of Nauort, Nauort, Westerwaldkreis, Germany, Europe.**

- **Image information**

<table border="1">
<tbody>
<tr>
<th>Field</th>
<th>Content</th>
</tr>
<tr>
<td>Manufacturer</td>
<td>Nikon Corporation</td>
</tr>
<tr>
<td>Image input euipment model</td>
<td>Nikon D80</td>
</tr>
<tr>
<td>File change date and time</td>
<td>2007-05-20 11:19:41</td>
</tr>
<tr>
<td>Image resolution in width and heigh direction</td>
<td>300 dpi</td>
</tr>
</tbody>
</table>

In the example above, the metadata shows the exact location where the photo was taken, which device was used to take the photo, the time when the photo was taken, and other image specifications.

These are just a sample of the data inlcuded in the image; it also includes further camera details, JPEG details and much more.

You can prevent a specific kind of metadata like **GPS** location from being captured. For example:

1. Switching off wireless and gps location (under location services) and mobile data (this can be found under data manager -> data delivery). 

2. When taking a photo, make sure that the settings of the tag-location from the photo app is off too. 

Using tools like [**Metanull**](metanull/windows), you can ensure that all metadata is removed before you share it. This tool is discussed in details below.

**Note:** Some files like DOCs and PDFs can hold image files within them. If you aren't careful, you can scrub the metadata on the document that is holding the image, but the metadata for the embedded image is still there! Using metanull before adding the image to the DOC would remove all metadata from it beforehand.

<div class=getstarted markdown=1>
Hands-on: Get started with the [*Metanull Guide*](metanull/windows)
</div>

:[](../../tools/windows/metanull)





# Removing metadata from documents and other files
As noted above, other commonly used file types such as Portable Document Files (PDFs) or word processing documents created by applications such as Microsoft Office or LibreOffice contain metadata which may include:

- The username of the person who created a document
- The name of the person who most recently edited saved a document
- The date when a document was created and modified

In some cases, your document might also contain additional kinds of personally identifiable information such as such as the addresses, e-mail addresses, government ID, IP addresses, or any unique identifier associated with personally identifiable information in another program on your computer.

Some of this information is easily accessible by viewing the file properties (which can be accessed by right clicking on the file icon and selecting *properties*). Other information or hidden data need specific softwares to be viewed. In any case, depending on your context, this information might put you at risk if you are working and exchanging sensitive information. 





# Removing metadata from PDF files
**Windows** or **MAC OS** users can use programs such as **Adobe Acrobat XI Pro** (for which a trial version is available) to remove or edit the hidden data from **PDF** files.

Opening any PDF file with Acrobat will allow you to edit the metadata by going to *File* menu and then selecting *properties*. Here, you can modify the document author’s name, title, subject, keywords and any additional metadata. Regarding the creation time, modification time, type of device used for creation the file, and other hidden data you don't see, you can remove it by going to *Tools* menu, then *Protection*, and selecting *Remove hidden information*. 

**Note:** For GNU/Linux users, [*PDF MOD*](https://live.gnome.org/PdfMod) is a free and open source tool to edit and remove metadata from PDF files. However, it doesn't remove the creation or modification time, it also doesn't remove the type of device used for creating the PDF.





# Removing metadata from LibreOffice documents
In LibreOffice documents the metadata can be viewed by selecting the *File* menu, then *Properties*. Under the *General* tab you can click *Reset* to reset the general user data, such as total editing time and revision number. Also make sure the *Apply user data* checkbox on this screen is unchecked, so the name of the creator will be removed. When you are done, the next step is to go to the *Description* and the *Custom Properties* tabs to clear any data there that you don't want to appear. Lastly, click on the *Securit** tab and uncheck the *Record change* box if it's not unchecked by default. 


**Note:** 

- If you use the *Versions* feature, you can delete older versions of the document which may be stored there through going to the *File* menu and *Versions*.

- If you use the *Changes* feature, go to the *Edit* menu then *Changes* to *Accept or reject* in order to clear the data relating to changes made to the document over time, if you no longer need this information.

## Other Strategies for scrubbing metadata ##

1. Some file types contain more metadata than others, so if you don't want to play around with software, and the formatting of a file doesn't matter, you can change files from ones that contain a lot of metadata (such as .DOCs and .JPEGs for example) to ones that don't (.TXTs and .PNGs for example)

2. Avoid using your real name, address, company or organisation name when registering copies of software such as Microsoft Office, Open Office, Libre Office, Adobe Acrobat and others. If you must give a name or address, use a fake one. 




# Further reading

- For more information on metadata removal tools, have a look at the following:

[*Comparison of metadata editors*](https://en.wikipedia.org/wiki/Comparison_of_metadata_editors)
