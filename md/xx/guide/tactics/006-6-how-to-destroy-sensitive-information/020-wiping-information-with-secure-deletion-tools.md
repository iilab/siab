

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

When you use a secure deletion tool, such as those recommended in this chapter, it would be more accurate to say that you are replacing, or 'overwriting,' your sensitive information, rather than simply deleting it. If you imagine that the documents stored in those hypothetical filing cabinet discussed above are written in pencil, then secure deletion software not only erases the content, but scribbles over the top of every word. And, much like pencil lead, digital information can still be read, albeit poorly, even after it has been erased and something has been written over the top of it. Because of this, the tools recommended here overwrite files with random data several times. This process is called [*wiping*](/en/glossary#Wiping), and the more times information is overwritten, the more difficult it becomes for someone to recover the original content. Experts generally agree that three or more overwriting passes should be made; some standards recommend seven or more. [*Wiping*](/en/glossary#Wiping) software automatically makes a reasonable number of passes, but you can change that number if you like.

### Wiping files ### 

There are two common ways to [*wipe*](/en/glossary#Wiping) sensitive data from your hard drive or storage device. You can [*wipe*](/en/glossary#Wiping) a single file or you can [*wipe*](/en/glossary#Wiping) all of the 'unallocated' space on the drive. When making this decision, it may be helpful to think about the other hypothetical example proposed earlier--the long report that may have left incomplete copies scattered throughout your hard drive even though only one file is visible. If you [*wipe*](/en/glossary#Wiping) the file itself, you guarantee that the current version is completely removed, but you leave the other copies where they are. In fact, there is no way to target those copies directly, because they are not visible without special software. By [*wiping*](/en/glossary#Wiping) all of the blank space on your storage device, however, you ensure that all previously-deleted information is destroyed. Returning to the metaphor of the poorly-labeled file cabinet, this procedure is comparable to searching through the cabinet, then erasing and scribbling repeated over any documents that have already had their labels removed.

[*Eraser*](/en/glossary#Eraser) is a free and open-source secure deletion tool that is extremely easy to use. You can [*wipe*](/en/glossary#Wiping) files with [*Eraser*](/en/glossary#Eraser) in three different ways: by selecting a single file, by selcting the contents of the **Recycle Bin**, or by [*wiping*](/en/glossary#Wiping) all unallocated space on the drive. [*Eraser*](/en/glossary#Eraser) can also [*wipe*](/en/glossary#Wiping) the contents of the Windows [*swap file*](/en/glossary#Swap_file), which is discussed further below.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Eraser - Secure File Removal Guide*](/en/eraser_main)
</div>

While secure deletion tools will not damage any visible files unless you explicitly [*wipe*](/en/glossary#Wiping) them, it is still important to be careful with software like this. After all, accidents happen, which is why people find **Recycle Bins** and data recovery tools so useful. If you get accustomed to [*wiping*](/en/glossary#Wiping) your data every time you delete something, you may find yourself with no way to recover from a simple mistake. Always make sure you have a secure backup before [*wiping*](/en/glossary#Wiping) large amounts of data from your computer.

<div class="background" markdown="1">
Elena: I know word processing programs like Microsoft Word and Open Office sometimes make temporary copies of a file while you're working on it. Do other programs do that too, or should I mostly just worry about files that I create and delete myself?

Nikolai: Actually, there are lots of places on your computer where programs leave traces of your personal information and online activities. I'm talking about websites you've visited, draft emails you've worked on recently and other things like that. All of this stuff could be sensitive, depending on how often you use that
computer.
</div>

### Wiping temporary data ###

The feature that allows [*Eraser*](/en/glossary#Eraser) to [*wipe*](/en/glossary#Wiping) all unallocated space on a drive is not as risky as it might sound, because it only [*wipes*](/en/glossary#Wiping) previously-deleted content. Normal, visible files will be unaffected. On the other hand, this very fact serves to highlight a separate issue: [*Eraser*](/en/glossary#Eraser) can not help you clean up sensitive information that has not been deleted, but that may be extremely well-hidden. Files containing such data may be tucked away in obscure folders, for example, or stored with meaningless filenames. This is not a major issue for electronic documents, but can be very important for information that is collected automatically whenever you use your computer. Examples include:

- Temporary data recorded by your browser while displaying webpages, including text, images, [*cookies*](/en/glossary#Cookie), account information, personal data used to complete online forms and the history of which websites you have visited.
- Temporary files saved by various applications in order to help you recover should your computer crash before you can save your work. These files might contain text, images, spreadsheet data and the names of other files, along with other potentially sensitive information.
- Files and links stored by Windows for the sake of convenience, such as shortcuts to applications you have used recently, obvious links to folders that you might prefer to keep hidden and, of course, the contents of your <b>Recycle Bin</b> should you forget to empty it.
- The Windows [*swap file*](/en/glossary#Swap_file). When your computer's memory is full, for example when you have been running several programs at the same time on an older computer, Windows will sometimes copy the data you are using into a single large file called the [*swap file*](/en/glossary#Swap_file). As a result, this file might contain almost anything, including webpages, document content, passwords or encryption keys. Even when you shut down your computer, the [*swap file*](/en/glossary#Swap_file) is not removed, so you must wipe it manually.

In order to remove common temporary files from your computer, you can use a freeware tool called [*CCleaner*](/en/glossary#CCleaner), which was designed to clean up after software like Internet Explorer, Mozilla [*Firefox*](/en/glossary#Firefox) and Microsoft Office applications (all of which are known to expose potentially sensitive information), as well as cleaning Windows itself. [*CCleaner*](/en/glossary#CCleaner) has the ability to delete files securely, which saves you from having to [*wipe*](/en/glossary#Wiping) unallocated drive space, using [*Eraser*](/en/glossary#Eraser), after each time you run it.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*CCleaner  - Secure File Deletion and Work Session Wiping Guide*](/en/ccleaner_main)
</div>

