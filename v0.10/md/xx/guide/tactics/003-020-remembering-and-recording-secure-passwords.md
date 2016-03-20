

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Remembering and recording secure passwords

---

Looking over the list of suggestions above, you might wonder how anyone without a photographic memory could possibly keep track of passwords that are this long, complex and meaningless without writing them down. The importance of using a different password for each account makes this even more difficult. There are a few tricks, however, that might help you create passwords that are easy to remember but extremely difficult to guess, even for a clever person using advanced 'password cracking' software. You also have the option of recording your passwords using a tool like [*KeePass*](/en/glossary#KeePass) that was created specifically for this purpose. 


### Remembering secure passwords ###

It is important to use different types of characters when choosing a password. This can be done in various ways:

- Varying capitalisation, such as: 'My naME is Not MR. MarSter' 
- Alternating numbers and letters, such as: 'a11 w0Rk 4nD N0 p14Y' 
- Incorporating certain symbols, such as: 'c@t(heR1nthery3' 
- Using multiple languages, such as: 'Let Them Eat 1e gateaU au ch()colaT' 

Any of these methods can help you increase the complexity of an otherwise simple password, which may allow you to choose one that is secure without having to give up entirely on the idea of memorizing it. Some of the more common substitutions (such as the use of a zero instead of an 'o' or the '@' symbol in place of an 'a') were long-ago incorporated into password-cracking tools, but they are still a good idea. They increase the amount of time that such tools would require to learn a password and, in the more common situations where tools of this sort cannot be used, they help prevent lucky guesses.


Passwords can also take advantage of more traditional [*mnemonic devices*](/en/glossary#Mnemonic_device), such as the use of acronyms. This allows long phrases to be turned into complex, seemingly-random words: 

- 'To be or not to be? That is the question' becomes '2Bon2B?TitQ' 
- 'We hold these truths to be self-evident: that all men are created equal' becomes 'WhtT2bs-e:taMac=' 
- 'Are you happy today?' becomes 'rU:-)2d@y?' 

These are just a few examples to help you come up with your own method of encoding words and phrases to make them simultaneously complex and memorable.

A little effort to make the password more complex goes a very long way. Increasing the length of a password even just by a few characters, or by adding numbers or special characters, makes it much more difficult to crack. For demonstrative purposes, the table below shows how much longer it may take a hacker to break a list of progressively more complex passwords by trying different combinations of the password one after another.

<table border="1">
<tbody>
<tr>
<th>Sample Password </th>
<th>Time to crack with an everyday computer</th>
<th>Time to crack with a very fast computer</th>
</tr>
<tr>
<td>bananas</td>
<td>Less than 1 day</td>
<td>Less than 1 day</td>
</tr>
<tr>
<td>bananalemonade</td>
<td>2 days</td>
<td>Less than 1 day</td>
</tr>
<tr>
<td>BananaLemonade</td>
<td>3 months, 14 days</td>
<td>Less than 1 day</td>
</tr>
<tr>
<td>B4n4n4L3m0n4d3</td>
<td>3 centuries, 4 decades</td>
<td>1 month, 26 days</td>
</tr>
<tr>
<td>We Have No Bananas</td>
<td>19151466 centuries</td>
<td>3990 centuries
</td>
</tr>
<tr>
<td>W3 H4v3 N0 B4n4n45</td>
<td>20210213722742 centuries</td>
<td>4210461192 centuries</td>
</tr>
</tbody>
</table>

Of course, the time it would take to crack any of the above passwords would vary widely depending on the nature of the attack, and the resources available to the attacker. Moreover, new methods to crack passwords are constantly being devised. All the same, the table does demonstrate that passwords become vastly more difficult to break by simply varying characters and using two words or, even better, a short phrase.

The table above is based on [Passfault](https://passfault.appspot.com/password_strength.html)'s calculations. Passfault is one of a number of websites which allow you to test the strength of your passwords. However, while such resources are good for demonstrating the relative efficiency of different types of passwords, you should avoid introducing your actual passwords into these sites.






### Recording passwords securely ###

While a little creativity may allow you to remember all of your passwords, the need to change those passwords periodically means that you might quickly run out of creativity. As an alternative, you can generate random, secure passwords for most of your accounts and simply give up on the idea of remembering them all. Instead, you can record them in a portable, encrypted [*secure password database*](/en/glossary#Secure_password_database), such as [*KeePass*](/en/glossary#KeePass).

<div class="getstarted" markdown="1">
***Hands-on: Get started with the*** [***KeePass - Secure Password Storage Guide***](/en/keepass_main)
</div>

Of course, if you use this method, it becomes especially important that you create and remember a very secure password for [*KeePass*](/en/glossary#KeePass), or whatever tool you choose. Whenever you need to enter a password for a specific account, you can look it up using only your master password, which makes it much easier to follow all of the suggestions above. <i>*[KeePass](/en/glossary#KeePass)* is portable, as well, which means that you can put the database on a USB memory stick in case you need to look up a password while you are away from your primary computer.

Although it is probably the best option for anybody who has to maintain a large number of accounts, there are a few drawbacks to this method. First, if you lose or accidentally delete your only copy of a password database, you will no longer have access to any of the accounts for which it contained passwords. This makes it extremely important that you back up your [*KeePass*](/en/glossary#KeePass) database. Look over [***Chapter 5: How to recover from information loss***](/en/chapter-5) for more information on backup strategies. Fortunately, the fact that your database is encrypted means that you don't have to panic if you lose a USB memory stick or a backup drive containing a copy of it. 

The second major drawback could be even more important. If you forget your [*KeePass*](/en/glossary#KeePass) master password, there is no way to recover it or the contents of the database. So, be sure to choose a master password that is both secure and memorable!

The strength of this method may, in certain situations, become its weakness. If somebody forces you to give away your Keepass database master password, they will gain access to all of the passwords stored in  the Keepass database. If this is a situation you may face, you could treat your Keepass database as a sensitive file, and protect it as we describe in [***Chapter 4: How to protect the sensitive files on your computer***](/en/chapter-4).  You can also create a separate Keepass database to contain passwords  protecting more sensitive information and take extra
precautions with  that database.

<div class="background" markdown="1">
Mansour: Wait a minute. If KeePass uses a single master password to protect all of your other passwords, how is it more secure than just using that same password for all of your accounts? I mean, if a bad guy learns the master password, he gets access to everything, right?

Magda: It's a good thought, and you're right that protecting your master password is really important, but there are a couple of key differences. First of all, this 'bad guy' would not only need your password, he'd need your KeePass database file, too. If you just share the same password between all of your accounts, then he'd only need the password itself. Plus, we know that KeePass is extremely secure, right? Well, other programs and websites can go either way. Some of them are much less secure than others, and you don't want someone breaking into a weak website, and then using what he learns to access a more secure account. And there's another thing, too. KeePass makes it really easy to change your master password if you think it's necessary. I should be so lucky! I spent all day today updating my passwords.
</div>


