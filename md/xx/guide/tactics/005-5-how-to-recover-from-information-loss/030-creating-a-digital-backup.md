

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Creating a digital backup

---

Of the various data types discussed here, it is the 'electronic documents' that people tend to worry about most when establishing a backup policy. This term is somewhat ambiguous, but generally refers to files that you keep track of yourself and that you open manually, either by double-clicking on them or by using a particular application's File menu. Specifically, it includes text files, word processing documents, presentations, PDFs and spreadsheets, among other examples. Unlike email messages, for example, electronic documents are generally not synchronised with remote copies over the Internet.

When backing up your electronic documents, you should remember to back up your program databases, as well. If you use a calendar application or an electronic address book, for example, you will need to find the folder in which these programs store their data. Hopefully, these databases will be in the same location as your electronic documents, as they are often kept inside your **My Documents** folder on a Windows computer. If that is not the case, however, you should add the appropriate folders to your regular backup. 

Email stored by an application such as [*Thunderbird*](/en/glossary#Thunderbird) is a special example of a program database. If you use an email program, especially if you are unable or unwilling to store a copy of your messages on the server, then you must ensure that this email database is included in your regular backup. You may consider image and video files to be electronic documents or items within a program database, depending on how you interact with them. Applications like Windows Media player and iTunes, for example, work like databases. If you use programs like this, you might have to search your hard drive to learn where they store the actual media files that they help manage. 


### Storage devices ###

Before you can back up your electronic documents, you must decide what kind of storage device you will use.

**USB disk or memory sticks** - USB disk or memory sticks can be quite inexpensive, and offer large capacity. They are easy to erase or overwrite numerous times. USB disk or memory sticks have a limited lifetime, which greatly depends on ways and frequency of usage but is generally estimated to be around 10 years.

**Compact Discs (CDs)** CDs store around 700 Megabytes (MB) of data. You will need a [*CD burner*](/en/glossary#CD_burner) and blank discs in order to create a CD backup. If you want to erase a CD and update the files stored on it, you will need to have a CD-RW burner and rewritable CDs. All major operating systems, including Windows XP, now include built-in software that can write CDs and CD-RWs. Keep in mind that the information written on these discs may begin to deteriorate after five or ten years. If you need to store a backup for longer than that, you will have to recreate the CDs occasionally, buy special 'long life' discs or use a different backup method.

**Digital Video Discs (DVDs)** - DVDs store up to 4.7 Gigabytes (GB) of data. They work much like CDs but require slightly more expensive equipment. You will need a DVD or [*DVD-RW burner*](/en/glossary#CD_burner), and appropriate discs. As with a CD, the data written on a normal DVD will eventually begin to fade.

**Remote server** - A well-maintained network backup server may have almost unlimited capacity, but the speed and stability of your own Internet connection will determine whether or not this is a realistic option. Keep in mind that running a backup server in your own office, while faster than copying information over the Internet, violates the requirement that you keep a copy of your important data in two different physical locations. 
There are free storage services on the Internet, as well, but you should very carefully consider the risks of putting your information online and you should always encrypt your backups before uploading them to servers run by organisations or individuals whom you do not know and trust. See the [***Further reading***](/en/chapter_5_5) section for a few examples.

### Backup Software ###

Cobian Backup is a user-friendly tool that can be set to run automatically, at regularly scheduled times, and to include only files that have changed since your last backup. It can also compress backups to make them smaller.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Cobian Backup Guide*](/en/cobian_main)
</div>

As always, it is a good idea to encrypt your backup files using a tool such as [*TrueCrypt*](/en/glossary#TrueCrypt). More information about about data encryption can be found in [***Chapter 4: How to protect the sensitive files on your computer***](/en/chapter-4).

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*TrueCrypt - Secure File Storage Guide*](/en/truecrypt_main)
</div>
<p>
When using these backup tools, there are a few things you can do to help your backup system work smoothly:

- Organise the files on your computer. Try to move all of the folders that contain electronic documents you intend to back up into a single location, such as inside the **My Documents** folder. 
- If you use software that stores its data in an application database, you should first determine the location of that database. If it is not in a convenient location, see if the program will allow you to choose a new location for its database. If it does, you can put it in the same folder as your electronic documents.
- Create a regular schedule to perform your backup.
- Try to establish procedures for all of the staff in your office who do not already have a reliable, secure backup policy. Help your coworkers understand the importance of this issue.
- Make sure to test the process of recovering data from your backup. Remember that, in the end, it is the restore procedure, not the backup procedure, that you really care about!



<div class="background" markdown="1">
Elena: Alright, so I made an encrypted backup while I was at work, and I put it on a CD. Cobian is scheduled to update my backup in a few days. My desk at work has a drawer that locks, and I'm planning to keep these backup CDs in there so they won't get lost or broken.

<i>Nikolai: But what if your office burns down? Computer, desk, backup CDs and all? Or, what if your website forum gets used to plan some giant environmental demonstration, the authorities crack down, things get out of hand, and the organisation is raided? I doubt your little desk lock will keep the police from confiscating those CDs. What about keeping them at home, or asking a friend to store them for you?
</div>


