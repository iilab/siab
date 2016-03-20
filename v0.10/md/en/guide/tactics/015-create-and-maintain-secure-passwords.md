
---

lang: en
community: guide
type: tactics
weight: 015
title: Create and maintain secure passwords

---

Many of the secure services that allow us to feel comfortable using digital technology to conduct important business, from signing in to our computers and sending email to encrypting and hiding sensitive data, require that we remember a password. These secret words, phrases or strings of gibberish often provide the first, and sometimes the only, barrier between your information and anyone who might want to read, copy, modify or destroy it without your permission. There are many ways in which someone could learn your passwords, but you can defend against most of them by applying a few specific tactics and by using a secure password database tool, such as KeePass.

# What you can learn from this guide

- The elements of a secure password
- A few tricks for remembering long, complicated passwords
- How to use the KeePass secure password database to store passwords instead of remembering them

## Introduction to passwords



{{ snippet: ./015-snippet_01.md }}




# Selecting and maintaining secure passwords

In general, when you want to protect something, you lock it up with a key. Houses, cars and bicycle locks all have physical keys; protected files have encryption keys; bank cards have PIN numbers; and email accounts have passwords. All of these keys, physical and electronic, have one thing in common: they open their respective locks just as effectively in the hands of somebody else. You can install advanced firewalls, secure email accounts, and encrypted disks, but if your password is weak, or if you allow it to fall into the wrong hands, they will not do you much good.



## Elements of a strong password

A password should be difficult for a computer program to guess. 

- **Make it long:** The longer a password is, the less likely it is that a computer program would be able to guess it in a reasonable amount of time. You should try to create passwords that include ten or more characters. Some people use passwords that contain more than one word, with or without spaces between them, which are often called passphrases. This is a great idea, as long as the program or service you are using allows you to choose long enough passwords.
- **Make it complex:** In addition to length, the complexity of a password also helps prevent automatic 'password cracking' software from guessing the right combination of characters. Where possible, you should always include upper case letters, lower case letters, numbers and symbols, such as punctuation marks, in your password. 

A password should be difficult for others to figure out. 

- **Make it practical:** If you have to write your password down because you can't remember it, you may end up facing a whole new category of threats that could leave you vulnerable to anybody with a clear view of your desk or temporary access to your home, your wallet, or even the trash bin outside your office. If you are unable to think of a password that is long and complex but still memorable, the [Remembering secure passwords](#155) section, below, might be of some help. If not, you should still choose something secure, but you may need to record it using a secure password database such as [KeePass](keepass/windows). Other types of password-protected files, including Microsoft Word documents, should not be trusted for this purpose, as many of them can be broken in seconds using tools that are freely available on the Internet.
- **Don't make it personal:** Your password should not be related to you personally. Don't choose a word or phrase based on information such as your name, social security number, telephone number, child's name, pet's name, birth date, or anything else that a person could learn by doing a little research about you. 
- **Keep it secret:** Do not share your password with anyone unless it is absolutely necessary. And, if you must share a password with a friend, family member or colleague, you should change it to a temporary password first, share that one, then change it back when they are done using it. Often, there are alternatives to sharing a password, such as creating a separate account for each individual who needs access. Keeping your password secret also means paying attention to who might be reading over your shoulder while you type it or look it up in a secure password database.

A password should be chosen so as to minimise damage if someone does learn it. 

- **Make it unique:** Avoid using the same password for more than one account. Otherwise, anyone who learns that password will gain access to even more of your sensitive information. This is particularly true because some services make it relatively easy to crack a password. If you use the same password for your Windows user account and your Gmail account, for example, someone with physical access to your computer can crack the former and use what they learn to access the latter. For similar reasons, it is a bad idea to rotate passwords by swapping them around between different accounts. 

- **Keep it fresh:** Change your password on a regular basis, preferably at least once every three months. Some people get quite attached to a particular password and never change it. This is a bad idea. The longer you keep one password, the more opportunity others have to figure it out. Also, if someone is able to use your stolen password to access your information and services without you knowing about it, they will continue to do so until you change the password. 

{{ snippet: ./015-snippet_02.md }}




# Remembering and recording secure passwords

Looking over the list of suggestions above, you might wonder how anyone without a photographic memory could possibly keep track of passwords that are this long, complex and meaningless without writing them down. The importance of using a different password for each account makes this even more difficult. There are a few tricks, however, that might help you create passwords that are easy to remember but extremely difficult to guess, even for a clever person using advanced 'password cracking' software. You also have the option of recording your passwords using a tool like [KeePass](keepass/windows) that was created specifically for this purpose.



## Remembering secure passwords

It is important to use different types of characters when choosing a password. This can be done in various ways:

- Varying capitalisation, such as: '**My naME is Not MR. MarSter**' 
- Alternating numbers and letters, such as: '**a11 w0Rk 4nD N0 p14Y**' 
- Incorporating certain symbols, such as: '**c@t(heR1nthery3**' 
- Using multiple languages, such as: '**Let Them Eat 1e gateaU au ch()colaT**' 

Any of these methods can help you increase the complexity of an otherwise simple password, which may allow you to choose one that is secure without having to give up entirely on the idea of memorizing it. Some of the more common substitutions (such as the use of a zero instead of an 'o' or the '@' symbol in place of an 'a') were long-ago incorporated into password-cracking tools, but they are still a good idea. They increase the amount of time that such tools would require to learn a password and, in the more common situations where tools of this sort cannot be used, they help prevent lucky guesses.

Passwords can also take advantage of more traditional mnemonic devices, such as the use of acronyms. This allows long phrases to be turned into complex, seemingly-random words: 

- 'To be or not to be? That is the question' becomes '**2Bon2B?TitQ**' 
- 'We hold these truths to be self-evident: that all men are created equal' becomes '**WhtT2bs-e:taMac=**' 
- 'Are you happy today?' becomes '**rU:-)2d@y?**' 

These are just a few examples to help you come up with your own method of encoding words and phrases to make them simultaneously complex and memorable.

A little effort to make the password more complex goes a very long way. Increasing the length of a password even just by a few characters, or by adding numbers or special characters, makes it much more difficult to crack. For demonstrative purposes, the table below shows how much longer it may take a hacker to break a list of progressively more complex passwords by trying different combinations of the password one after another.

| Sample password       | Time to crack with an everyday computer | Time to crack with a very fast computer |
| -------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------- |
| bananas                     | Less than 1 day                                     | Less than 1 day                                  |
| bananalemonade         | 2 days                                                  | Less than 1 day                                  |
| BananaLemonade       | 3 months, 14 days                                 | Less than 1 day                                   |
| B4n4n4L3m0n4d3       | 3 centuries, 4 decades                           | 1 month, 26 days                                 |
| We Have No Bananas | 19151466 centuries                                | 3990 centuries                                     |
| W3 H4v3 N0 B4n4n45 | 20210213722742 centuries                      | 4210461192 centuries     [Passfault](https://passfault.appspot.com/password_strength.html)                     |


Of course, the time it would take to crack any of the above passwords would vary widely depending on the nature of the attack, and the resources available to the attacker. Moreover, new methods to crack passwords are constantly being devised. All the same, the table does demonstrate that passwords become vastly more difficult to break by simply varying characters and using two words or, even better, a short phrase.

The table above is based on [Passfault](https://passfault.appspot.com/password_strength.html)'s calculations. Passfault is one of a number of websites which allow you to test the strength of your passwords. However, while such resources are good for demonstrating the relative efficiency of different types of passwords, you should avoid introducing your actual passwords into these sites.



## Recording passwords securely

While a little creativity may allow you to remember all of your passwords, the need to change those passwords periodically means that you might quickly run out of creativity. As an alternative, you can generate random, secure passwords for most of your accounts and simply give up on the idea of remembering them all. Instead, you can record them in a portable, encrypted secure password database, such as [KeePass](keepass/windows).

{{ tool: ../tools/windows/keepass }}

Of course, if you use this method, it becomes especially important that you create and remember a very secure password for [**KeePass**](keepass/windows), or whatever tool you choose. Whenever you need to enter a password for a specific account, you can look it up using only your master password, which makes it much easier to follow all of the suggestions above. [**KeePass**](keepass/windows) is portable, as well, which means that you can put the database on a USB memory stick in case you need to look up a password while you are away from your primary computer.

Although it is probably the best option for anybody who has to maintain a large number of accounts, there are a few drawbacks to this method. First, if you lose or accidentally delete your only copy of a password database, you will no longer have access to any of the accounts for which it contained passwords. This makes it extremely important that you back up your KeePass database. Look over our guide [**How to recover from information loss**](backup) for more information on backup strategies. Fortunately, the fact that your database is encrypted means that you don't have to panic if you lose a USB memory stick or a backup drive containing a copy of it. 

The second major drawback could be even more important. If you forget your [KeePass](keepass/windows) master password, there is no way to recover it or the contents of the database. So, be sure to choose a master password that is both secure and memorable!

The strength of this method may, in certain situations, become its weakness. If somebody forces you to give away your KeePass database master password, they will gain access to all of the passwords stored in  the KeePass database. If this is a situation you may face, you could treat your KeePass database as a sensitive file, and protect it as we describe in our guide [**How to protect the sensitive files on your computer**](secure-file-storage).  You can also create a separate KeePass database to contain passwords protecting more sensitive information and take extra precautions with that database.

{{ snippet: ./015-snippet_03.md }}


# Further reading

- To learn more about secure passwords, see the *2.2 Password Protection* chapter and the Appendix D. How long should my password be? in the [Digital Security and Privacy for Human rights Defenders](https://www.frontlinedefenders.org/esecman) book
- Wikipedia has informative articles on [Passwords](https://en.wikipedia.org/wiki/Password), [Guidelines for password strength](https://en.wikipedia.org/wiki/Password_strength), and [password cracking](https://en.wikipedia.org/wiki/Password_cracking).
