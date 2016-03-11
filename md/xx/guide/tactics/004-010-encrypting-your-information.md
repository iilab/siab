

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<div class="background" markdown="1">
Pablo: But my computer is already protected by the Windows login password! Isn't that good enough?

Claudia: Actually, Windows login passwords are usually quite easy to break. Plus, anybody who gets his hands on your computer for long enough to restart it with a LiveCD in the drive can copy your data without even having to worry about the password. If they manage to take it away for a while, then you're in even worse trouble. It's not just Windows passwords you need to worry about, either. You shouldn't trust Microsoft Word or Adobe Acrobat passwords either.
</div>

[*Encrypting*](/en/glossary#Encryption) your information is a bit like keeping it in a locked safe. Only those who have a key or know the lock's combination (an [*encryption*](/en/glossary#Encryption) key or password, in this case) can access it. The analogy is particularly appropriate for [*TrueCrypt*](/en/glossary#TrueCrypt) and tools like it, which create secure containers called 'encrypted volumes' rather than simply protecting one file at a time. You can put a large number of files into an [*encrypted*](/en/glossary#Encryption) volume, but these tools will not protect anything that is stored elsewhere on your computer or USB memory stick.

<div class="getstarted" markdown="1">
**Hands-on: Get started with the** [***TrueCrypt  - Secure File Storage Guide***](/en/truecrypt_main)
</div>

While other software can provide similar strength *[encryption](/en/glossary#Encryption)*, [*TrueCrypt*](/en/glossary#TrueCrypt) contains several important features to allow you to design your information security strategy. It offers the possibility of permanently **encrypting the whole disk of your computer** including all your files, all temporary files created during your work, all programs you have installed and all Windows operating system files. TrueCrypt supports *[encrypted](/en/glossary#Encryption)* volumes on portable storage devices. It provides 'deniability' features described in the [***Hiding your sensitive information***](/en/chapter_4_2) section below. In addition TrueCrypt is a [*free and open source*](/en/glossary#FOSS) program.

<div class="background" markdown="1">
Pablo: Alright, now you have me worried. What about other users on the same computer? Does this mean they can read files in the 'My Documents' folder?

Claudia: I like the way you're thinking! If your Windows password doesn't protect you from intruders, how can it protect you from other people with accounts on the same computer? In fact, your My Documents folder is normally visible to anybody, so other users wouldn't even have to do anything clever to read your unencrypted files. You're right, though, even if the folder is made 'private,' you're still not safe unless you use some kind of encryption.</i>
</div>

### Tips on using file encryption safely ###

Storing confidential data can be a risk for you and for the people you work with. *[Encryption](/en/glossary#Encryption)* reduces this risk but does not eliminate it. The first step to protecting sensitive information is to reduce how much of it you keep around. Unless you have a good reason to store a particular file, or a particular category of information within a file, you should simply delete it (see [***Chapter 6: How to destroy sensitive information***](/en/chapter-6) for more information about how to do this securely). The second step is to use a good file [*encryption*](/en/glossary#Encryption) tool, such as [*TrueCrypt*](/en/glossary#TrueCrypt).

<div class="background" markdown="1">
Claudia: Well, maybe we don't actually need to store information that could identify the people who gave us these testimonies. What do you think?

Pablo: Agreed. We should probably write down as little of that as possible. Plus, we should think up a simple code we can use to protect names and locations that we absolutely have to record.			
</div>

Returning to the analogy of a locked safe, there are a few things you should bear in mind when using [*TrueCrypt*](/en/glossary#TrueCrypt) and tools like it. No matter how sturdy your safe is, it won't do you a whole lot of good if you leave the door open. When your [*TrueCrypt*](/en/glossary#TrueCrypt) volume is 'mounted' (whenever you can access the contents yourself), your data may be vulnerable, so you should keep it closed except when you are actually reading or modifying the files inside it. 


There are a few situations when it is especially important that you remember not to leave your [*encrypted*](/en/glossary#Encryption) volumes mounted:

- Disconnect them when you walk away from your computer for any length of time. Even if you typically leave your computer running overnight, you need to ensure that you do not leave your sensitive files accessible to physical or remote intruders while you are gone.
- Disconnect them before putting your computer to sleep. This applies to both 'suspend' and 'hibernation' features, which are typically used with laptops but may be present on desktop computers as well.
- Disconnect them before allowing someone else to handle your computer. When taking a laptop through a security checkpoint or border crossing, it is important that you disconnect all [*encrypted*](/en/glossary#Encryption) volumes and shut your computer down completely.
- Disconnect them before inserting an untrusted USB memory stick or other external storage device, including those belonging to friends and colleagues.
- If you keep an [*encrypted*](/en/glossary#Encryption) volume on a USB memory stick, remember that just removing the device may not immediately disconnect the volume. Even if you need to secure your files in a hurry, you have to dismount the volume properly, then disconnect the external drive or memory stick, then remove the device. You might want to practice until you find the quickest way to do all of these things.
	
If you decide to keep your [*TrueCrypt*](/en/glossary#TrueCrypt) volume on a USB memory stick, you can also keep a copy of the [*TrueCrypt*](/en/glossary#TrueCrypt) program with it. This will allow you to access your data on other people's computers. The usual rules still apply, however: if you don't trust the machine to be free of [*malware*](/en/glossary#Malware), you probably shouldn't be typing in your passwords or accessing your sensitive data.


