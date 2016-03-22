
---

lang: en
community: guide
type: tactics
weight: 020
title: Protect the sensitive files on your computer

---

Unauthorised access to the information on your computer or portable storage devices can be carried out remotely, if the 'intruder' is able to read or modify your data over the Internet; or physically, if he manages to get hold of your hardware. You can protect yourself against either type of threat by improving the physical and network security of your data, as discussed in [***How to protect your computer from malware and hackers***](malware) and [***How to protect your information from physical threats***](physical). It is always best to have several layers of defence, however, which is why you should also protect the files themselves. That way, your sensitive information is likely to remain safe even if your other security efforts prove inadequate.


There are two general approaches to the challenge of securing your data in this way. **You can *[encrypt](/en/glossary#Encryption)* your files**, making them unreadable to anyone but you, or **you can hide them** in the hope that an intruder will be unable to find your sensitive information. There are tools to help you with either approach, including a [*FOSS*](/en/glossary#FOSS) application called [*TrueCrypt*](/en/glossary#TrueCrypt), which can both *[encrypt](/en/glossary#Encryption)* and hide your files.

# What you can learn from this guide

- How to [*encrypt*](/en/glossary#Encryption) information on your computer
- What risks you might face by keeping your data [encrypted](/en/glossary#Encryption)
- How to protect data on USB memory sticks, in case they are lost or stolen
- What steps you can take to hide information from physical or remote intruders

## Introduction to secure file storage


:[Snippet](snippets/snippet_01)





# Encrypting your information


:[Snippet](snippets/snippet_02)

[*Encrypting*](/en/glossary#Encryption) your information is a bit like keeping it in a locked safe. Only those who have a key or know the lock's combination (an [*encryption*](/en/glossary#Encryption) key or password, in this case) can access it. The analogy is particularly appropriate for [*TrueCrypt*](/en/glossary#TrueCrypt) and tools like it, which create secure containers called 'encrypted volumes' rather than simply protecting one file at a time. You can put a large number of files into an [*encrypted*](/en/glossary#Encryption) volume, but these tools will not protect anything that is stored elsewhere on your computer or USB memory stick.

:[Hands-on: get started with TrueCrypt for Windows - secure file storage](../../tools/windows/truecrypt)

While other software can provide similar strength *[encryption](/en/glossary#Encryption)*, [*TrueCrypt*](/en/glossary#TrueCrypt) contains several important features to allow you to design your information security strategy. It offers the possibility of permanently **encrypting the whole disk of your computer** including all your files, all temporary files created during your work, all programs you have installed and all Windows operating system files. TrueCrypt supports *[encrypted](/en/glossary#Encryption)* volumes on portable storage devices. It provides 'deniability' features described in the [***Hiding your sensitive information***](secure-file-storage#469) section below. In addition TrueCrypt is a [*free and open source*](/en/glossary#FOSS) program.

:[Snippet](snippets/snippet_03)



## Tips on using file encryption safely

Storing confidential data can be a risk for you and for the people you work with. *[Encryption](/en/glossary#Encryption)* reduces this risk but does not eliminate it. The first step to protecting sensitive information is to reduce how much of it you keep around. Unless you have a good reason to store a particular file, or a particular category of information within a file, you should simply delete it (see [***How to destroy sensitive information***](destroy-sensitive-information) for more information about how to do this securely). The second step is to use a good file [*encryption*](/en/glossary#Encryption) tool, such as [*TrueCrypt*](/en/glossary#TrueCrypt).


:[Snippet](snippets/snippet_04)

Returning to the analogy of a locked safe, there are a few things you should bear in mind when using [*TrueCrypt*](/en/glossary#TrueCrypt) and tools like it. No matter how sturdy your safe is, it won't do you a whole lot of good if you leave the door open. When your [*TrueCrypt*](/en/glossary#TrueCrypt) volume is 'mounted' (whenever you can access the contents yourself), your data may be vulnerable, so you should keep it closed except when you are actually reading or modifying the files inside it. 


There are a few situations when it is especially important that you remember not to leave your [*encrypted*](/en/glossary#Encryption) volumes mounted:

* Disconnect them when you walk away from your computer for any length of time. Even if you typically leave your computer running overnight, you need to ensure that you do not leave your sensitive files accessible to physical or remote intruders while you are gone.
* Disconnect them before putting your computer to sleep. This applies to both 'suspend' and 'hibernation' features, which are typically used with laptops but may be present on desktop computers as well.
* Disconnect them before allowing someone else to handle your computer. When taking a laptop through a security checkpoint or border crossing, it is important that you disconnect all [*encrypted*](/en/glossary#Encryption) volumes and shut your computer down completely.
* Disconnect them before inserting an untrusted USB memory stick or other external storage device, including those belonging to friends and colleagues.
* If you keep an [*encrypted*](/en/glossary#Encryption) volume on a USB memory stick, remember that just removing the device may not immediately disconnect the volume. Even if you need to secure your files in a hurry, you have to dismount the volume properly, then disconnect the external drive or memory stick, then remove the device. You might want to practice until you find the quickest way to do all of these things.
	
If you decide to keep your [*TrueCrypt*](/en/glossary#TrueCrypt) volume on a USB memory stick, you can also keep a copy of the [*TrueCrypt*](/en/glossary#TrueCrypt) program with it. This will allow you to access your data on other people's computers. The usual rules still apply, however: if you don't trust the machine to be free of [*malware*](/en/glossary#Malware), you probably shouldn't be typing in your passwords or accessing your sensitive data.


# Hiding your sensitive information

One issue with keeping a safe in your home or office, to say nothing of carrying one in your pocket, is that it tends to be quite obvious. Many people have reasonable concerns about incriminating themselves by using [*encryption*](/en/glossary#Encryption). Just because the legitimate reasons to [*encrypt*](/en/glossary#Encryption) data outnumber the illegitimate ones does not make this threat any less real. Essentially, there are two reasons why you might shy away from using a tool like [*TrueCrypt*](/en/glossary#TrueCrypt): the risk of self-incrimination and the risk of clearly identifying the location of your most sensitive information.




## Considering the risk of self-incrimination

[*Encryption*](/en/glossary#Encryption) is illegal in some countries, which means that downloading, installing or using software of this sort might be a crime in its own right. And, if the police, military or intelligence services are among those groups from whom you are seeking to protect your information, then violating these laws can provide a pretext under which your activities might be investigated or your organisation might be persecuted. In fact, however, threats like this may have nothing to do with the legality of the tools in question. Any time that merely being associated with [*encryption*](/en/glossary#Encryption) software would be enough to expose you to accusations of criminal activity or espionage (regardless of what is actually inside your [*encrypted*](/en/glossary#Encryption) volumes), then you will have to think carefully about whether or not such tools are appropriate for your situation.

If that is the case, you have a few options:

- You can avoid using data security software entirely, which would require that you store only non-confidential information or invent a system of code words to protect key elements of your sensitive files.
- You can rely on a technique called [*steganography*](/en/glossary#Steganography) to hide your sensitive information, rather than encrypting it. There are tools that can help with this, but using them properly requires very careful preparation, and you still risk incriminating yourself in the eyes of anyone who learns what tool you have used.
- You can try to store all of your sensitive information in a secure webmail account, but this demands a reliable network connection and a relatively sophisticated understanding of computers and Internet services. This technique also assumes that network [*encryption*](/en/glossary#Encryption) is less incriminating than file [*encryption*](/en/glossary#Encryption) and that you can avoid accidentally copying sensitive data onto your hard drive and leaving it there.
- You can keep sensitive information off of your computer by storing it on a USB memory stick or portable hard drive. However, such devices are typically even more vulnerable than computers to loss and confiscation, so carrying around sensitive, unencrypted information on them is usually a very bad idea.
	
If necessary, you can employ a range of such tactics. However, even in circumstances where you are concerned about self-incrimination, it may be safest to use [*TrueCrypt*](/en/glossary#TrueCrypt) anyway, while attempting to disguise your [*encrypted*](/en/glossary#Encryption) volume as best you can.

If want to make your encrypted volume less conspicuous, you can rename it to look like a different type of file. Using the '.iso' file extension, to disguise it as a CD image, is one option that works well for large volumes of around 700 MB. Other extensions would be more realistic for smaller volumes. This is a bit like hiding your safe behind a painting on the wall of your office. It might not hold up under close inspection, but it will offer some protection. You can also rename the [*TrueCrypt*](/en/glossary#TrueCrypt) program itself, assuming you have stored it as you would a regular file on your hard drive or USB memory stick, rather than installing it as a program. The [***TrueCrypt Guide***](truecrypt/windows) explains how to do this.




## Considering the risk of identifying your sensitive information

Often, you may be less concerned about the consequences of 'getting caught' with [*encryption*](/en/glossary#Encryption) software on your computer or USB memory stick and more concerned that your encrypted volume will indicate precisely where you store the information that you most wish to protect. While it may be true that no one else can read it, an intruder will know that it is there, and that you have taken steps to protect it. This exposes you to various non-technical methods through which that intruder might attempt to gain access, such as intimidation, blackmail, interrogation and torture. It is in this context that [*TrueCrypt's*](/en/glossary#TrueCrypt) deniability feature, which is discussed in more detail below, comes into play.

[*TrueCrypt's*](/en/glossary#TrueCrypt) deniability feature is one of the ways in which it goes beyond what is typically offered by file [*encryption*](/en/glossary#Encryption) tools. This feature can be thought of as a peculiar form of [*steganography*](/en/glossary#Steganography) that disguises your most sensitive information as other, less sensitive, hidden data. It is analogous to installing a subtle 'false bottom' inside that not-so-subtle office safe. If an intruder steals your key, or intimidates you into giving her the safe's combination, she will find some convincing 'decoy' material, but not the information that you truly care about protecting.

Only you know that your safe contains a hidden compartment in the back. This allows you to 'deny' that you are keeping any secrets beyond what you have already given to the intruder, and might help protect you in situations where you must reveal a password for some reason. Such reasons might include legal or physical threats to your own safety, or that of your colleagues, associates, friends and family members. The purpose of deniability is to give you a chance of escaping from a potentially dangerous situation even if you choose to continue protecting your data. As discussed in the Considering the risk of self-incrimination section above, however, this feature is much less useful if merely being caught with a safe in your office is enough to bring about unacceptable consequences.

[*TrueCrypt's*](/en/glossary#TrueCrypt) deniability feature works by storing a 'hidden volume' inside your regular [*encrypted*](/en/glossary#Encryption) volume. You open this hidden volume by providing an alternate password that is different from the one you would normally use. Even if a technically sophisticated intruder gains access to the standard volume, he will be unable to prove that a hidden one exists. Of course, he may very well know that [*TrueCrypt*](/en/glossary#TrueCrypt) is capable of hiding information in this way, so there is no guarantee that the threat will disappear as soon as you reveal your decoy password. Plenty of people use [*TrueCrypt*](/en/glossary#TrueCrypt) without enabling its deniability feature, however, and it is generally considered impossible to determine, through analysis, whether or not a given [*encrypted*](/en/glossary#Encryption) volume contains this kind of 'false bottom'. That said, it is your job to make sure that you do not reveal your hidden volume through less technical means, such as leaving it open or allowing other applications to create shortcuts to the files that it contains. The ***Further reading*** section, below, can point you to more information about this.


:[Snippet](snippets/snippet_05)



# Further reading

- For additional information on securing your files, see the *2.4 Cryptology* chapter, the *2.8 Steganography* Chapter and *4.2 Case Study 3* from the [Digital Security and Privacy for Human Rights Defenders](http://www.frontlinedefenders.org/esecman) book.
- The [TrueCrypt Documentation](http://andryou.com/truecrypt/docs/index.php) discusses in details many aspects of information encryption and [TrueCrypt FAQ](http://andryou.com/truecrypt/faq.php) provides answers to some common questions about TrueCrypt.
