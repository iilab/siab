
---

lang: en
community: guide
type: tactics
weight: 030
title: Destroy sensitive information

---

The previous chapters have discussed a number of tools and habits that can help you protect your sensitive data, but what happens when you decide that you no longer need to keep a piece of information? If you determine, for example, that your encrypted backup copies of a particular file are sufficient, and you want to delete the master, what is the best way to do so? Unfortunately, the answer is more complicated than you might think. When you delete a file, even after you empty the **Recycle bin**, the contents of that file remain on your hard drive and can be recovered by anyone who has the right tools and a little luck. 

In order to ensure that deleted information does not end up in the wrong hands, you will have to rely on special software that removes data securely and permanently. [*Eraser*](/en/glossary#Eraser) is one such tool, and is discussed below. Using [*Eraser*](/en/glossary#Eraser) is a bit like shredding a paper document rather than simply tossing it into a bin and hoping that nobody finds it. And, of course, deleting files is only one example of a situation in which you might need to destroy sensitive data. If you consider the details that someone, particularly a powerful, politically-motivated adversary, could learn about you or your organisation by reading certain files that you thought you had deleted, you will probably think of a few more examples of data that you'd like to permanently erase, by destroying outdated backups, [*wiping*](/en/glossary#Wiping) old hard drives before giving them away, deleting old user accounts, and clearing your web browsing history, for example. [*CCleaner*](/en/glossary#CCleaner), the other tool described in this chapter, can help you face the challenge of deleting the many temporary files that your operating system and applications create every time you use them.


# What you can learn from this guide

- How to remove sensitive information from your computer permanently
- How to remove information stored on removable storage devices like CDs and USB memory sticks
- How to prevent someone from learning what documents you have previously been viewing on your computer
- How to maintain your computer so that deleted files cannot be recovered in the future

## Introduction to secure file deletion


:[](snippets/snippet_01)





# Deleting information

From a purely technical perspective, there is no such thing as a delete function on your computer. Of course, you can drag a file to the Recycle Bin and empty the bin, but all this really does is clear the icon, remove the file's name from a hidden index of everything on your computer, and tell Windows that it can use the space for something else. Until it actually does use that space, however, the space will be occupied by the contents of the deleted information, much like a filing cabinet that has had all of its labels removed but still contains the original files. This is why, if you have the right software and act quickly enough, you can restore information that you've deleted by accident, as discussed in our guide [**How to recover from information loss**](backup).

You should also keep in mind that files are created and insecurely deleted, without your knowledge, every time you use your computer. Suppose, for example, that you are writing a large report. It may take you a week, working several hours each day, and every time the document is saved, Windows will create a new copy of the document and store it on your hard drive. After a few days of editing, you may have unknowingly saved several versions of the document, all at different stages of completion. 

Windows generally deletes the old versions of a file, of course, but it does not look for the exact location of the original in order to overwrite it securely when a new copy is made. Instead, it simply puts the latest version into a new section of the metaphorical filing cabinet mentioned above, moves the label from the old section to the new one, and leaves the previous draft where it was until some other program needs to use that space. Clearly, if you have a good reason to destroy all traces of that document from your filing cabinet, removing the latest copy is not going to be enough, and simply throwing away the label would be even worse.

Remember, too, that computer hard drives are not the only devices that store digital information. CDs, DVDs, USB memory sticks, floppy disks, flash memory cards from mobile phones and removable hard drives all have the same issues, and you should not trust a simple delete or rewrite operation to clear sensitive information from any of them.



# Wiping information with secure deletion tools

When you use a secure deletion tool, such as those recommended in this chapter, it would be more accurate to say that you are replacing, or 'overwriting,' your sensitive information, rather than simply deleting it. If you imagine that the documents stored in those hypothetical filing cabinet discussed above are written in pencil, then secure deletion software not only erases the content, but scribbles over the top of every word. And, much like pencil lead, digital information can still be read, albeit poorly, even after it has been erased and something has been written over the top of it. Because of this, the tools recommended here overwrite files with random data several times. This process is called [*wiping*](/en/glossary#Wiping), and the more times information is overwritten, the more difficult it becomes for someone to recover the original content. Experts generally agree that three or more overwriting passes should be made; some standards recommend seven or more. [*Wiping*](/en/glossary#Wiping) software automatically makes a reasonable number of passes, but you can change that number if you like.




## Wiping files

There are two common ways to [*wipe*](/en/glossary#Wiping) sensitive data from your hard drive or storage device. You can [*wipe*](/en/glossary#Wiping) a single file or you can [*wipe*](/en/glossary#Wiping) all of the 'unallocated' space on the drive. When making this decision, it may be helpful to think about the other hypothetical example proposed earlier--the long report that may have left incomplete copies scattered throughout your hard drive even though only one file is visible. If you [*wipe*](/en/glossary#Wiping) the file itself, you guarantee that the current version is completely removed, but you leave the other copies where they are. In fact, there is no way to target those copies directly, because they are not visible without special software. By [*wiping*](/en/glossary#Wiping) all of the blank space on your storage device, however, you ensure that all previously-deleted information is destroyed. Returning to the metaphor of the poorly-labeled file cabinet, this procedure is comparable to searching through the cabinet, then erasing and scribbling repeated over any documents that have already had their labels removed.
passwords
[*Eraser*](/en/glossary#Eraser) is a free and open-source secure deletion tool that is extremely easy to use. You can [*wipe*](/en/glossary#Wiping) files with [*Eraser*](/en/glossary#Eraser) in three different ways: by selecting a single file, by selcting the contents of the **Recycle Bin**, or by [*wiping*](/en/glossary#Wiping) all unallocated space on the drive. [*Eraser*](/en/glossary#Eraser) can also [*wipe*](/en/glossary#Wiping) the contents of the Windows [*swap file*](/en/glossary#Swap_file), which is discussed further below.


:[](../../tools/windows/eraser)

While secure deletion tools will not damage any visible files unless you explicitly [*wipe*](/en/glossary#Wiping) them, it is still important to be careful with software like this. After all, accidents happen, which is why people find **Recycle Bins** and data recovery tools so useful. If you get accustomed to [*wiping*](/en/glossary#Wiping) your data every time you delete something, you may find yourself with no way to recover from a simple mistake. Always make sure you have a secure backup before [*wiping*](/en/glossary#Wiping) large amounts of data from your computer.


:[](snippets/snippet_02)



## Wiping temporary data

The feature that allows [*Eraser*](/en/glossary#Eraser) to [*wipe*](/en/glossary#Wiping) all unallocated space on a drive is not as risky as it might sound, because it only [*wipes*](/en/glossary#Wiping) previously-deleted content. Normal, visible files will be unaffected. On the other hand, this very fact serves to highlight a separate issue: [*Eraser*](/en/glossary#Eraser) can not help you clean up sensitive information that has not been deleted, but that may be extremely well-hidden. Files containing such data may be tucked away in obscure folders, for example, or stored with meaningless filenames. This is not a major issue for electronic documents, but can be very important for information that is collected automatically whenever you use your computer. Examples include:

- Temporary data recorded by your browser while displaying webpages, including text, images, [*cookies*](/en/glossary#Cookie), account information, personal data used to complete online forms and the history of which websites you have visited.
- Temporary files saved by various applications in order to help you recover should your computer crash before you can save your work. These files might contain text, images, spreadsheet data and the names of other files, along with other potentially sensitive information.
- Files and links stored by Windows for the sake of convenience, such as shortcuts to applications you have used recently, obvious links to folders that you might prefer to keep hidden and, of course, the contents of your <b>Recycle Bin</b> should you forget to empty it.
- The Windows [*swap file*](/en/glossary#Swap_file). When your computer's memory is full, for example when you have been running several programs at the same time on an older computer, Windows will sometimes copy the data you are using into a single large file called the [*swap file*](/en/glossary#Swap_file). As a result, this file might contain almost anything, including webpages, document content, passwords or encryption keys. Even when you shut down your computer, the [*swap file*](/en/glossary#Swap_file) is not removed, so you must wipe it manually.

In order to remove common temporary files from your computer, you can use a freeware tool called [*CCleaner*](/en/glossary#CCleaner), which was designed to clean up after software like Internet Explorer, Mozilla [*Firefox*](/en/glossary#Firefox) and Microsoft Office applications (all of which are known to expose potentially sensitive information), as well as cleaning Windows itself. [*CCleaner*](/en/glossary#CCleaner) has the ability to delete files securely, which saves you from having to [*wipe*](/en/glossary#Wiping) unallocated drive space, using [*Eraser*](/en/glossary#Eraser), after each time you run it.

:[](../../tools/windows/ccleaner)




# Tips on using secure deletion tools effectively

You are now familiar with a few of the ways in which information might be exposed on your computer or storage device, even if you are dilligent about erasing sensitive files. You also know what tools you can use to [*wipe*](/en/glossary#Wiping) that information permanently. There are a few simple steps that you should follow, especially if it is your first time using these tools, in order to ensure that your drive is cleaned safely and effectively:

- Create an encrypted backup of your important files, as discussed in our guide [**How to recover from information loss**](backup).
- Close down all unnecessary programs and disconnect from the Internet.
- Delete all unnecessary files, from all storage devices, and empty the **Recycle Bin**
- [*Wipe*](/en/glossary#Wiping) temporary files using [*CCleaner*](/en/glossary#CCleaner).
- [*Wipe*](/en/glossary#Wiping) the Windows [*swap file*](/en/glossary#Swap_file) using [*Eraser*](/en/glossary#Eraser).
- [*Wipe*](/en/glossary#Wiping) all of the free space on your computer and other storage devices using [*Eraser*](/en/glossary#Eraser). You might need to let this procedure run overnight, as it can be quite slow.

You should then get into the habit of:

- Periodically using [*CCleaner*](/en/glossary#CCleaner) to [*wipe*](/en/glossary#Wiping) temporary files
- [*Wiping*](/en/glossary#Wiping) sensitive electronic documents using [*Eraser*](/en/glossary#Eraser), instead of using the **Recycle Bin** or the Windows delete function
- Periodically using [*Eraser*](/en/glossary#Eraser) to [*wipe*](/en/glossary#Wiping) the Windows [*swap file*](/en/glossary#Swap_file)
- Periodically using [*Eraser*](/en/glossary#Eraser) to [*wipe*](/en/glossary#Wiping) all unallocated space on your hard drives, USB memory sticks, and any other storage devices that may have had sensitive information deleted from them recently. This might include floppy disks, rewritable CDs, rewritable DVDs and removable flash memory cards from cameras, mobile phones or portable music players.



# Tips on wiping the entire contents of a storage device

You might occasionally need to [*wipe*](/en/glossary#Wiping) a storage device completely. When you sell or give away an old computer, it is best to remove the hard drive and let the computer's new owner acquire one for herself. If this is not an option, however, you should at least [*wipe*](/en/glossary#Wiping) the drive thoroughly with [*Eraser*](/en/glossary#Eraser) before handing it over. And, even if you do keep the drive, you will probably want to [*wipe*](/en/glossary#Wiping) it anyway, regardless of whether you intend to reuse or discard it. Similarly, if you purchase a new hard drive, you should [*wipe*](/en/glossary#Wiping) your old one after copying your data and making a secure backup. If you are intending to throw away or recycle an old drive, you should also consider destroying it physically. (Many computer support professionals recommend a few strong blows with a hammer before discarding any data-storage device that once contained sensitive information.)

In any of the situations described above, you will need to use [*Eraser*](/en/glossary#Eraser) to [*wipe*](/en/glossary#Wiping) an entire hard drive, which is impossible as long as the operating system is running on that particular drive. The easiest way to get around this issue is to remove the drive and put it into an external USB 'drive enclosure,' which you can then plug into any computer with [*Eraser*](/en/glossary#Eraser) installed on it. At that point, you can delete the full contents of the external drive and then use [*Eraser*](/en/glossary#Eraser) to [*wipe*](/en/glossary#Wiping) all of its unallocated space. Fortunately, this is not something you will have to do often, as it may take quite some time.

Rather than trying to [*wipe*](/en/glossary#Wiping) data that have been stored on a rewritable CD or DVD, it is often better to destroy the disc itself. If necessary, you can create a new one containing any information you wish to keep. And, of course, this is the only way to 'erase' content from a non-rewritable disc. It is surprisingly difficult to destroy the contents of a CD or DVD completely. You may have heard stories about information being recovered from such discs even after they were cut into small pieces. While these stories are true, reconstructing information in this way takes a great deal of time and expertise. You will have to judge for yourself whether or not someone is likely to expend that level of resources in order to access your data. Typically, a sturdy pair of scissors (or a very sturdy paper shredder) will do the job nicely. If you want to take extra precautions, you can mix up the resulting pieces and dispose of them in various locations far from your home or office. 


:[](snippets/snippet_03)



# Further reading

- While it does not use secure deletion techniques to wipe them permanently, Firefox does provide a built-in way to clear many of its own temporary files. This feature is described in the [***Firefox Guide***](firefox/windows).
- The [CCleaner FAQ](http://www.piriform.com/ccleaner/faq) provides additional information about installing and using the tool.
- Although much of the paper is quite technical, the introduction of Peter Guttmann's [Secure Deletion of Data from Magnetic and Solid-State Memory](http://www.usenix.org/publications/library/proceedings/sec96/full_papers/gutmann/) is worth reading, as the [method](http://en.wikipedia.org/wiki/Gutmann_method) he describes has had a major influence on the developers of *Eraser* and other secure file removal tools. 
