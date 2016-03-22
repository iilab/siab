
---

lang: en
community: guide
type: tactics
weight: 025
title: Recover from information loss

---

Each new method of storing or transferring digital information tends to introduce several new ways in which the information in question can be lost, taken or destroyed. Years of work can disappear in an instant, as a result of theft, momentary carelessness, the confiscation of computer hardware, or simply because digital storage technology is inherently fragile. There is a common saying among computer support professionals: &quot;it's not a question of *if* you will lose your data; it's a question of *when*.&quot; So, *when* this happens to you, it is extremely important that you already have an up-to-date backup and a well-tested means of restoring it. The day you are reminded about the importance of a backup system is generally the day after you needed to have one in place.

Although it is one of the most basic elements of secure computing, formulating an effective backup policy is not as simple as it sounds. It can be a significant planning hurdle for a number of reasons: the need to store original data and backups in different physical locations, the importance of keeping backups confidential the challenge of coordinating among different people who share information with one another using their own portable storage devices. In addition to backup and file-recovery tactics, this guide addresses two specific tools, [*Cobian Backup*](/en/glossary#Cobian_Backup) and [*Recuva*](/en/glossary#Recuva). 

# What you can learn from this guide

- How to organise and back up your information
- Where you should store your backups
- How you can manage your backups securely
- How to recover files that have been deleted accidentally

## Introduction to file recovery


:[Snippet](snippets/snippet_01)





# Identifying and organising your information

While it is clearly important that you take steps to prevent disaster, by making sure that your information is physically safe, free of [*malware*](/en/glossary#Malware) and protected by a good [*firewall*](/en/glossary#Firewall) and strong passwords, on their own these steps are not enough. There are simply too many things that can go wrong, including virus attacks, [*hackers*](/en/glossary#Hacker), electrical short circuits, power spikes, water spills, theft, confiscation, demagnetisation, operating system crashes and hardware failure, to name just a few. Preparing for disaster is just as important as defending against it.


:[Snippet](snippets/snippet_02)

The first step to formulating a *backup policy* is to picture where your personal and work information is currently located. Your email, for example, may be stored on the provider's mail server, on your own computer, or in both places at once. And, of course, you might have several email accounts. Then, there are important documents on the computers you use, which may be in the office or at home. There are address books, chat histories and personal program settings. It is also possible that some information is stored on removable media as well, including USB memory sticks, portable hard drives, CDs, DVDs, and old floppy disks. Your mobile phone contains a list of contacts and may have important text messages stored in it. If you have a website, it may contain a large collection of articles built up over years of work. And, finally, don't forget your non-digital information, such as paper notebooks, diaries and letters.

Next, you need to define which of these files are 'master copies,' and which are duplicates. The master copy is generally the most up-to-date version of a particular file or collection of files, and corresponds to copy that you would actually edit if you needed to update the content. Obviously, this distinction does not apply to files of which you have only one copy, but it is extremely important for certain types of information. One common disaster scenario occurs when only duplicates of an important document are backed up, and the master copy itself gets lost or destroyed before those duplicates can be updated. Imagine, for example, that you have been travelling for a week while updating the copy of a particular spreadsheet that you keep on your USB memory stick. At this point, you should begin thinking of that copy as your master copy, because the periodic, automated backups of the outdated version on your office computer are no longer useful.

Try to write down the physical location of all master and duplicate copies of the information identified above. This will help you clarify your needs and begin to define an appropriate backup policy. The table below is a very basic example. Of course, you will probably find that your list is much longer, and contains some 'storage devices' with more than one 'data type' and some data types that are present on multiple devices.

| Data type                                                                        | Master / Duplicate | Storage device           | Location |
| ------------------------------------------------------------------------------------- | --------------------------- | ------------------------------- | -------------|
| Electronic documents                                                       | Master                  | Computer hard drive   | Office     |
| A few important electronic documents                                | Duplicate              |  USB memory stick    | With me |
| Program databases (photos, address book, calendar, etc.)   | Master                 | Computer hard drive    | Office     |
| A few electronic documents                                               | Duplicate              | CDs                          | Home     |
| Email & email contacts                                                      | Master                 | Gmail account           | Internet   |
| Text messages & phone contacts                                       | Master                 | Mobile phone             | With me |
| Printed documents (contracts, invoices, etc.)                       | Master                 | Desk drawer              | Office     |

In the table above, you can see that:

- The only documents that will survive if your office computer's hard drive crashes are the duplicates on your USB memory stick and the CD copies at home.
- You have no offline copy of your email messages or your address book, so if you forget your password (or if someone manages to change it maliciously), you will lose access to them.
- You have no copies of any data from your mobile phone.
- You have no duplicate copies, digital or physical, of printed documents such as contracts and invoices.



# Defining your backup strategy

To back up all of the data types listed above, you will need a combination of software and process solutions. Essentially, you need to make sure that each data type is stored in at least two separate locations.

**Electronic documents** - Create a full backup of the documents on your computer using a program like [*Cobian Backup*](/en/glossary#Cobian_Backup), which is described in more detail below. Store the backup on something portable so that you can take it home or to some other safe location. External hard drives, CD/DVDs or USB memory sticks are possible choices. Some people use CDs or DVDs for this, since the risk of overwriting and losing your backup is lower. Blank CDs may be cheap enough to allow you to use a new one every time you make a backup.

Because this category of data often contains the most sensitive information, it is particularly important that you protect your electronic document backups using encryption. You can learn how to do this in [***How to protect the sensitive files on your computer***](secure-file-storage) and in the [***TrueCrypt Guide***](truecrypt/windows).

**Program databases** - Once you have determined the location of your program databases, you can back them up in the same way as electronic documents.

**Email** - Rather than accessing your email only through a web browser, install an email client like [*Thunderbird*](/en/glossary#Thunderbird) and configure it to work with your account. The [***Thunderbird Guide***](thunderbird/windows) explains in detail how to do this. Also most webmail services will provide instructions on how to use such programs and, often, how to import your email addresses into them. You can learn more about this in the Further Reading section, below. If you choose to move your old email messages to your computer so they are not stored on the server (e.g. for security reasons), make sure that you include them in the backup of electronic documents described above.

**Mobile phone contents** - To back up the phone numbers and text messages on your mobile phone, you can connect it to your computer using the appropriate software, which is generally available from the website of the company that manufactured your phone. You may need to buy a special USB cable to do this.

**Printed documents** - Where possible, you should scan all of your important papers, then back them up along with your other electronic documents, as discussed above.

In the end, you should have rearranged your storage devices, data types and backups in a way that makes your information much more resistant to disaster:


| Data Type                                             | Master/Duplicate | Storage Device                     | Location |
| ----------------------------------------------------------- | ------------------------ | ------------------------------------------ | ------------ |
| Electronic documents                             | Master               | Computer hard drive              | Office     |
| Electronic documents                             | Duplicate           | CDs                                     | Home     |
| A few important electronic documents      | Duplicate           | USB memory stick                | With me |
| Program databases                                | Master               | Computer hard drive               | Office     |
| Program databases                                | Duplicate           | CDs                                      | Home     |
| Email & email contacts                          | Master               | Gmail account                       | Internet   |
| Email & email contacts                          | Duplicate           | Thunderbird on office computer | Office     |
| Text messages & mobile phone contacts | Master               | Mobile phone                         | With me |
| Text messages & mobile phone contacts | Duplicate           | Computer hard drive                | Office     |
| Text messages & mobile phone contacts | Duplicate           | Backup SIM card                    | Home     |
| Printed documents                                 | Master               | Desk drawer                          | Office     |
| Scanned documents                               | Duplicate           | CDs                                      | Home     |


:[Snippet](snippets/snippet_03)




# Creating a digital backup

Of the various data types discussed here, it is the 'electronic documents' that people tend to worry about most when establishing a backup policy. This term is somewhat ambiguous, but generally refers to files that you keep track of yourself and that you open manually, either by double-clicking on them or by using a particular application's File menu. Specifically, it includes text files, word processing documents, presentations, PDFs and spreadsheets, among other examples. Unlike email messages, for example, electronic documents are generally not synchronised with remote copies over the Internet.

When backing up your electronic documents, you should remember to back up your program databases, as well. If you use a calendar application or an electronic address book, for example, you will need to find the folder in which these programs store their data. Hopefully, these databases will be in the same location as your electronic documents, as they are often kept inside your **My Documents** folder on a Windows computer. If that is not the case, however, you should add the appropriate folders to your regular backup. 

Email stored by an application such as [*Thunderbird*](/en/glossary#Thunderbird) is a special example of a program database. If you use an email program, especially if you are unable or unwilling to store a copy of your messages on the server, then you must ensure that this email database is included in your regular backup. You may consider image and video files to be electronic documents or items within a program database, depending on how you interact with them. Applications like Windows Media player and iTunes, for example, work like databases. If you use programs like this, you might have to search your hard drive to learn where they store the actual media files that they help manage. 



## Storage devices

Before you can back up your electronic documents, you must decide what kind of storage device you will use.

**USB disk or memory sticks** - USB disk or memory sticks can be quite inexpensive, and offer large capacity. They are easy to erase or overwrite numerous times. USB disk or memory sticks have a limited lifetime, which greatly depends on ways and frequency of usage but is generally estimated to be around 10 years.

**Compact Discs (CDs)** CDs store around 700 Megabytes (MB) of data. You will need a [*CD burner*](/en/glossary#CD_burner) and blank discs in order to create a CD backup. If you want to erase a CD and update the files stored on it, you will need to have a CD-RW burner and rewritable CDs. All major operating systems, including Windows XP, now include built-in software that can write CDs and CD-RWs. Keep in mind that the information written on these discs may begin to deteriorate after five or ten years. If you need to store a backup for longer than that, you will have to recreate the CDs occasionally, buy special 'long life' discs or use a different backup method.

**Digital Video Discs (DVDs)** - DVDs store up to 4.7 Gigabytes (GB) of data. They work much like CDs but require slightly more expensive equipment. You will need a DVD or [*DVD-RW burner*](/en/glossary#CD_burner), and appropriate discs. As with a CD, the data written on a normal DVD will eventually begin to fade.

**Remote server** - A well-maintained network backup server may have almost unlimited capacity, but the speed and stability of your own Internet connection will determine whether or not this is a realistic option. Keep in mind that running a backup server in your own office, while faster than copying information over the Internet, violates the requirement that you keep a copy of your important data in two different physical locations. 
There are free storage services on the Internet, as well, but you should very carefully consider the risks of putting your information online and you should always encrypt your backups before uploading them to servers run by organisations or individuals whom you do not know and trust. See the ***Further reading*** section for a few examples.



## Backup software
Cobian Backup is a user-friendly tool that can be set to run automatically, at regularly scheduled times, and to include only files that have changed since your last backup. It can also compress backups to make them smaller.

:[Hands-on: get started with Cobian Backup for Windows](../../tools/windows/cobian)

As always, it is a good idea to encrypt your backup files using a tool such as [*TrueCrypt*](/en/glossary#TrueCrypt). More information about about data encryption can be found in [***How to protect the sensitive files on your computer***](secure-file-storage).


:[Hands-on: get started with TrueCrypt for Windows - secure file storage](../../tools/windows/truecrypt)

When using these backup tools, there are a few things you can do to help your backup system work smoothly:

- Organise the files on your computer. Try to move all of the folders that contain electronic documents you intend to back up into a single location, such as inside the **My Documents** folder. 
- If you use software that stores its data in an application database, you should first determine the location of that database. If it is not in a convenient location, see if the program will allow you to choose a new location for its database. If it does, you can put it in the same folder as your electronic documents.
- Create a regular schedule to perform your backup.
- Try to establish procedures for all of the staff in your office who do not already have a reliable, secure backup policy. Help your coworkers understand the importance of this issue.
- Make sure to test the process of recovering data from your backup. Remember that, in the end, it is the restore procedure, not the backup procedure, that you really care about!


:[Snippet](snippets/snippet_04)



# Recovering from accidental file deletion

When you delete a file in Windows, it disappears from view, but its contents remain on the computer. Even after you empty the **Recycle Bin**, information from the files you deleted can usually still be found on the hard drive. See [***How to destroy sensitive information***](destroy-sensitive-information) to learn more about this. Occasionally, if you accidentally delete an important file or folder, this security vulnerability can work to your advantage. There are several programs that can restore access to recently-deleted files, including a tool called [*Recuva*](recuva/windows).


:[Hands-on: get started with Recuva for Windows - file recovery](../../tools/windows/recuva)

These tools do not always work, because Windows may have written new data over your deleted information. Therefore, it is important that you do as little as possible with your computer between deleting a file and attempting to restore it with a tool like [*Recuva*](recuva/windows). The longer you use your computer before attempting to restore the file, the less likely it is that you will succeed. This also means that you should use the portable version of *Recuva* instead of installing it after deleting an important file. Installing the software requires writing new information to the file system, which may coincidentally overwrite the critical data that you are trying to recover.

While it might sound like a lot of work to implement the policies and learn the tools described in this guide, maintaining your backup strategy, once you have a system in place, is much easier than setting it up for the first time. And, given that backup may be the single most important aspect of data security, you can rest assured that going through this process is well worth the effort. 


# Further reading

- More information on backup and data recovery can be found in the *2.3 Information Backup, Destruction and Recovery* chapter of the [Digital Security and Privacy for Human Rights Defenders](http://www.frontlinedefenders.org/esecman) book.
- Note that online backup brings new risks. At minimum, **remember to encrypt your sensitive information separately yourself** before you upload it to
the server. Assuming you do the step above, there are free online data storage services as a convenient way to back up your information. Some
options include: [SpiderOak](https://spideroak.com/), [Google
Drive](https://drive.google.com/start), [tahoe-lafs](https://tahoe-lafs.org/trac/tahoe-lafs). 
- There is an excellent article on data recovery in [Wikipedia](http://en.wikipedia.org/wiki/Data_recovery).
