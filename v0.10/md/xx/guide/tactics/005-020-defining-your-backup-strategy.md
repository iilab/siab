

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Defining your backup strategy

---

To back up all of the data types listed above, you will need a combination of software and process solutions. Essentially, you need to make sure that each data type is stored in at least two separate locations.

**Electronic documents** - Create a full backup of the documents on your computer using a program like [*Cobian Backup*](/en/glossary#Cobian_Backup), which is described in more detail below. Store the backup on something portable so that you can take it home or to some other safe location. External hard drives, CD/DVDs or USB memory sticks are possible choices. Some people use CDs or DVDs for this, since the risk of overwriting and losing your backup is lower. Blank CDs may be cheap enough to allow you to use a new one every time you make a backup.

Because this category of data often contains the most sensitive information, it is particularly important that you protect your electronic document backups using encryption. You can learn how to do this in [***Chapter 4: How to protect the sensitive files on your computer***](/en/chapter-4) and in the [***TrueCrypt Guide***](/en/truecrypt_main).

**Program databases** - Once you have determined the location of your program databases, you can back them up in the same way as electronic documents.

**Email** - Rather than accessing your email only through a web browser, install an email client like [*Thunderbird*](/en/glossary#Thunderbird) and configure it to work with your account. The [***Thunderbird Guide***](/en/thunderbird_main) explains in detail how to do this. Also most webmail services will provide instructions on how to use such programs and, often, how to import your email addresses into them. You can learn more about this in the Further Reading section, below. If you choose to move your old email messages to your computer so they are not stored on the server (e.g. for security reasons), make sure that you include them in the backup of electronic documents described above.

**Mobile phone contents** - To back up the phone numbers and text messages on your mobile phone, you can connect it to your computer using the appropriate software, which is generally available from the website of the company that manufactured your phone. You may need to buy a special USB cable to do this.

**Printed documents** - Where possible, you should scan all of your important papers, then back them up along with your other electronic documents, as discussed above.

In the end, you should have rearranged your storage devices, data types and backups in a way that makes your information much more resistant to disaster:

<table width="100%" border="1">
<tbody>
<tr>
<th>Data Type</th>
<th>Master/Duplicate</th>
<th>Storage Device</th>
<th>Location</th>
</td>
</tr>
<tr>
<td>Electronic documents</td>
<td>Master</td>
<td>Computer hard drive</td>
<td>Office
</td>
</tr>
<tr>
<td>Electronic documents</td>
<td>Duplicate</td>
<td>CDs</td>
<td>Home
</td>
</tr>
<tr>
<td>A few important electronic documents</td>
<td>Duplicate</td>
<td>USB memory stick</td>
<td>With me
</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Data Type</th>
<th>Master/Duplicate</th>
<th>Storage Device</th>
<th>Location</th>
</td>
</tr>
<tr>
<td>Program databases</td>
<td>Master</td>
<td>Computer hard drive</td>
<td>Office
</td>
</tr>
<tr>
<td>Program databases</td>
<td>Duplicate</td>
<td>CDs</td>
<td>Home
</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Data Type</th>
<th>Master/Duplicate</th>
<th>Storage Device</th>
<th>Location</th>
</td>
</tr>
<tr>
<td>Email &amp; email contacts</td>
<td>Duplicate</td>
<td>Gmail account</td>
<td>Internet
</td>
</tr>
<tr>
<td>Email &amp; email contacts</td>
<td>Master</td>
<td>Thunderbird on office computer</td>
<td>Office
</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Data Type</th>
<th>Master/Duplicate</th>
<th>Storage Device</th>
<th>Location</th>
</td>
</tr>
<tr>
<td>Text messages &amp; mobile phone contacts</td>
<td>Master</td>
<td>Mobile phone</td>
<td>With me
</td>
</tr>
<tr>
<td>Text messages &amp; mobile phone contacts</td>
<td>Duplicate</td>
<td>Computer hard drive</td>
<td>Office
</td>
</tr>
<tr>
<td>Text messages &amp; mobile phone contacts</td>
<td>Duplicate</td>
<td>Backup SIM</td>
<td>Home
</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Data Type</th>
<th>Master/Duplicate</th>
<th>Storage Device</th>
<th>Location</th>
</td>
</tr>
<tr>
<td>Printed documents</td>
<td>Master</td>
<td>Desk drawer</td>
<td>Office
</td>
</tr>
<tr>
<td>Scanned documents</td>
<td>Duplicate</td>
<td>CDs</td>
<td>At home
</td>
</tr>
</tbody>
</table>




<div class="background" markdown="1">

Elena: I know some people who keep all of their important documents on Gmail, by attaching them to 'draft' messages or emails to themselves. Would that count as a 'second physical location' for my files?

Nikolai: It might help you recover if you lose one or two very important documents, but it's pretty awkward. Honestly, how many documents per week would you be willing to back up like that? Plus, you need to consider whether or not those attachments are safe, especially if you're at all worried about your email being monitored. Unless you're connecting to Gmail securely, this is a bit like handing over your sensitive information on a silver platter. Using an HTTPS connection to Gmail in order to back up small Truecrypt volumes or KeePass database files would be pretty safe, because they're encrypted, but I really wouldn't recommend this as a general-purpose backup strategy.
</div>


