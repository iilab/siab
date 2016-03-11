

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Compress and Decompress Your Files

---

List of sections on this page:

- [**3.0 How to Compress Your Backup File**](#3.0)
- [**3.1 How to Decompress Your Backup File**](#3.1)

-------

<a name="3.0"></a>
## 3.0 How to Compress Your Backup File ##

**Step 1**. **Create** a backup task as documented in section [**2.3 How to Create a Backup File**](/en/cobian_howtobackup#2.2) containing the backup files you want to archive.

**Step 2**. **Select** ![](/sbox/screen/cobian-en/22.png) from the left sidebar to activate the *New task* screen as follows:

![](/sbox/screen/cobian-en/23.png)

*Figure 1: The New task screen displaying the Compression and Strong Encryption panes*

The **Compression** pane is used to specify the method for compressing your backup.

**Note**: Compression is used to reduce the amount of space for file storage. If you have a bunch of old files that you use only occasionally, but you still want to keep, it would make sense to store them in a format where they take up as little space as possible. Compression works by removing a lot of unnecessary coding out of your documents, while leaving important information intact. Compression does not damage your original data. The files are not viewable when compressed. The process must be reversed and your files 'decompressed' when you want to view the files again.

The three sub-options in the *Compression type* drop-down list are:

*No Compression*: This option does not perform any compression, as you would expect.

*Zip Compression*: This option is the standard compression technique for **Windows** systems, and the most convenient. Archives once created can be opened with standard Windows tools (or you can download the [**ZipGenius**](http://www.zipgenius.it/) program to access them). 

Selecting a compression type listed automatically enables the *Split options* section, and its corresponding drop-down list.

The *Split options* apply to storage on removable media, for example CDs, DVDs, floppy disks and USB memory sticks. The various split options will subdivide the archive into sizes that will fit onto your storage device of choice. 

Example: 
Let's say that you are archiving a large number of files, and you want to burn them to a CD. However, your archive size turns out to be larger than 700MB (the size of a CD). The splitting function will split the archive into pieces smaller than or equal to 700MB, which you can then burn onto your CDs. If you are planning to back up onto your computer's hard disk, or the files that you want to back up are smaller than the device you plan to store them on, you can skip this section.

The following options are available to you when you click on the *Split options* drop-down list. Your choice will depend on the type of removable storage device available to you.

![](/sbox/screen/cobian-en/24.png)

*Figure 2: The Split Options drop-down list*

- 3,5" - Floppy disk. This option is big enough to perform backup of a small number of documents
- Zip - Zip Disk (check the capacity of the one you are using). You will need a special Zip Drive in your computer and the custom-made disks
- CD-R - CD disk (check the capacity of the one you are using). You will need a CD Writer in your computer and a CD writing program (see [**DeepBurner Free** ](http://www.deepburner.com/) version or other [**disk burning tools**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).
- DVD - DVD disk (check the capacity of the one you are using). You will need a DVD Writer in your computer and a DVD writing program (see [**DeepBurner Free** ](http://www.deepburner.com/) version or other [**disk burning tools**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)). 

If you are backing up onto several USB memory sticks you may want to set a custom size.

To do this, perform the following steps:

**Step 1**. **Select** the *Custom size* (bytes) option, then <b>type</b> the size of the archive in bytes into the text field as follows:

![](/sbox/screen/cobian-en/25.png)

*Figure 10: The Custom size text field*

To give you an idea of sizes

- 1KB (kilobyte) = 1024 bytes - a one-page text document made in Open Office is approximately 20kb
- 1MB (megabyte) = 1024 KB - a photo taken on a digital camera is usually between 1 - 3 MB
- 1GB (gigabyte) = 1024 MB - approximately half hour of a DVD quality movie 

**Note:** When choosing a custom size to split your backup for a CD or DVD disk, Cobian Backup will not copy the backup to your removable device automatically. Rather, it will create your archive in those files on the computer and you will need to burn them to the CD or DVD disk yourself.

*Password Protect*: This option lets you enter a password to protect the archive. Simply type, then re-type a password into the two boxes provided. When you try to decompress the archive, you will be asked for the password before the task commences.

**Note**: If you want to secure your archive, you should think about using another method than a password. **Cobian Backup** lets you encrypt your archive. This will be covered in section, [**4. How to encrypt the Backup File**](/cobian_encrypt). Alternatively, you may also refer to the [**Truecrypt Hands-on Guide**](/en/truecrypt_main) to find out how to create an encrypted storage space on your computer or removable device.

*Comment*: This option lets you write something descriptive about the archive, but it is not a requirement. 

<a name="3.1"></a>
## 3.1 How to Decompress Your Backup File ##

To decompress your backup, perform the following steps:

**Step 1**. **Select > Tools > Decompressor** as shown below;

![](/sbox/screen/cobian-en/26.png)

*Figure 3: The Tools menu displaying the Decompressor option*

The **Decompressor** window appears as follows:

![](/sbox/screen/cobian-en/27.png)

*Figure 4: The Cobian 10 Backup - Decompressor window*

**Step 2**. **Click** ![](/sbox/screen/cobian-en/28.png) to open a browse window to enable you to select the archive you want to decompress.

**Step 3**. **Select** the archive (*.zip* or *.7x* file) and then **click** ![](/sbox/screen/cobian-en/13.png).

**Step 4**. **Select** a directory into which you will unpack (output) the archived file.

**Step 5**. **Click** ![](/sbox/screen/cobian-en/29.png) to open another window that lets you choose the folder in which to unpack the archive.

**Step 6**. **Select** a folder, and then **click** ![](/sbox/screen/cobian-en/13.png).

Use **Windows Explorer** to view the files that go to that folder.


