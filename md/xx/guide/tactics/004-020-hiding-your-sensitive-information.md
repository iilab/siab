

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

One issue with keeping a safe in your home or office, to say nothing of carrying one in your pocket, is that it tends to be quite obvious. Many people have reasonable concerns about incriminating themselves by using [*encryption*](/en/glossary#Encryption). Just because the legitimate reasons to [*encrypt*](/en/glossary#Encryption) data outnumber the illegitimate ones does not make this threat any less real. Essentially, there are two reasons why you might shy away from using a tool like [*TrueCrypt*](/en/glossary#TrueCrypt): the risk of self-incrimination and the risk of clearly identifying the location of your most sensitive information.

### Considering the risk of self-incrimination ###

[*Encryption*](/en/glossary#Encryption) is illegal in some countries, which means that downloading, installing or using software of this sort might be a crime in its own right. And, if the police, military or intelligence services are among those groups from whom you are seeking to protect your information, then violating these laws can provide a pretext under which your activities might be investigated or your organisation might be persecuted. In fact, however, threats like this may have nothing to do with the legality of the tools in question. Any time that merely being associated with [*encryption*](/en/glossary#Encryption) software would be enough to expose you to accusations of criminal activity or espionage (regardless of what is actually inside your [*encrypted*](/en/glossary#Encryption) volumes), then you will have to think carefully about whether or not such tools are appropriate for your situation.

If that is the case, you have a few options:

- You can avoid using data security software entirely, which would require that you store only non-confidential information or invent a system of code words to protect key elements of your sensitive files.
- You can rely on a technique called [*steganography*](/en/glossary#Steganography) to hide your sensitive information, rather than encrypting it. There are tools that can help with this, but using them properly requires very careful preparation, and you still risk incriminating yourself in the eyes of anyone who learns what tool you have used.
- You can try to store all of your sensitive information in a secure webmail account, but this demands a reliable network connection and a relatively sophisticated understanding of computers and Internet services. This technique also assumes that network [*encryption*](/en/glossary#Encryption) is less incriminating than file [*encryption*](/en/glossary#Encryption) and that you can avoid accidentally copying sensitive data onto your hard drive and leaving it there.
- You can keep sensitive information off of your computer by storing it on a USB memory stick or portable hard drive. However, such devices are typically even more vulnerable than computers to loss and confiscation, so carrying around sensitive, unencrypted information on them is usually a very bad idea.
	
If necessary, you can employ a range of such tactics. However, even in circumstances where you are concerned about self-incrimination, it may be safest to use [*TrueCrypt*](/en/glossary#TrueCrypt) anyway, while attempting to disguise your [*encrypted*](/en/glossary#Encryption) volume as best you can.

If want to make your encrypted volume less conspicuous, you can rename it to look like a different type of file. Using the '.iso' file extension, to disguise it as a CD image, is one option that works well for large volumes of around 700 MB. Other extensions would be more realistic for smaller volumes. This is a bit like hiding your safe behind a painting on the wall of your office. It might not hold up under close inspection, but it will offer some protection. You can also rename the [*TrueCrypt*](/en/glossary#TrueCrypt) program itself, assuming you have stored it as you would a regular file on your hard drive or USB memory stick, rather than installing it as a program. The [***TrueCrypt Guide***](/en/truecrypt_main) explains how to do this.

### Considering the risk of identifying your sensitive information ###

Often, you may be less concerned about the consequences of 'getting caught' with [*encryption*](/en/glossary#Encryption) software on your computer or USB memory stick and more concerned that your encrypted volume will indicate precisely where you store the information that you most wish to protect. While it may be true that no one else can read it, an intruder will know that it is there, and that you have taken steps to protect it. This exposes you to various non-technical methods through which that intruder might attempt to gain access, such as intimidation, blackmail, interrogation and torture. It is in this context that [*TrueCrypt's*](/en/glossary#TrueCrypt) deniability feature, which is discussed in more detail below, comes into play.

[*TrueCrypt's*](/en/glossary#TrueCrypt) deniability feature is one of the ways in which it goes beyond what is typically offered by file [*encryption*](/en/glossary#Encryption) tools. This feature can be thought of as a peculiar form of [*steganography*](/en/glossary#Steganography) that disguises your most sensitive information as other, less sensitive, hidden data. It is analogous to installing a subtle 'false bottom' inside that not-so-subtle office safe. If an intruder steals your key, or intimidates you into giving her the safe's combination, she will find some convincing 'decoy' material, but not the information that you truly care about protecting.

Only you know that your safe contains a hidden compartment in the back. This allows you to 'deny' that you are keeping any secrets beyond what you have already given to the intruder, and might help protect you in situations where you must reveal a password for some reason. Such reasons might include legal or physical threats to your own safety, or that of your colleagues, associates, friends and family members. The purpose of deniability is to give you a chance of escaping from a potentially dangerous situation even if you choose to continue protecting your data. As discussed in the [***Considering the risk of self-incrimination***](#Considering_the_risk_of_self-incrimination) section, however, this feature is much less useful if merely being caught with a safe in your office is enough to bring about unacceptable consequences.

[*TrueCrypt's*](/en/glossary#TrueCrypt) deniability feature works by storing a 'hidden volume' inside your regular [*encrypted*](/en/glossary#Encryption) volume. You open this hidden volume by providing an alternate password that is different from the one you would normally use. Even if a technically sophisticated intruder gains access to the standard volume, he will be unable to prove that a hidden one exists. Of course, he may very well know that [*TrueCrypt*](/en/glossary#TrueCrypt) is capable of hiding information in this way, so there is no guarantee that the threat will disappear as soon as you reveal your decoy password. Plenty of people use [*TrueCrypt*](/en/glossary#TrueCrypt) without enabling its deniability feature, however, and it is generally considered impossible to determine, through analysis, whether or not a given [*encrypted*](/en/glossary#Encryption) volume contains this kind of 'false bottom'. That said, it is your job to make sure that you do not reveal your hidden volume through less technical means, such as leaving it open or allowing other applications to create shortcuts to the files that it contains. The [***Further reading***](/en/chapter_4_3) section, below, can point you to more information about this.

<div class="background" markdown="1">
Claudia: Alright, so let's toss some junk into the standard volume, and then we can move all our testimonies into the hidden one. Do you have some old PDFs or something we can use?

Pablo: Well, I was thinking about that. I mean, the idea is for us to give up the decoy password if we have no other choice, right? But, for that to be convincing, we need to make sure those files look kind of important, don't you think? Otherwise, why would we bother to encrypt them? Maybe we should use some unrelated financial documents or a list of website passwords or something.

</div>


