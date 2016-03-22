

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: Jitsi - Add contacts and communicate text & voice

---

List of sections on this page:

- [**3.1 Add contacts (buddies) to Jitsi**](#3.1)
- [**3.2 Text chat (Instant Messaging) with OTR encryption**](#3.2)
- [**3.3 Voice and video chat with ZRTP encryption**](#3.3)


<a name="3.1"></a>
## 3.1 Add contacts (buddies) to Jitsi ##

After adding at least one account to Jitsi and logging in, you are ready to add your contacts and communicate with them.

To add a contact to Jitsi follow steps below:

**Step 0**. Open the Jitsi main window by **selecting Start > Jitsi** or **double-clicking** the **Jitsi** desktop icon.

**Step 1**. **select *File* > *Add contact...*** which will open the following window:

![](/sbox/screen/jitsi-en/30.png)

*Figure 1: Add contact window*

**Step 2**. **Select** which of your accounts you would like to add this contact to (for example *terance.the.tester@jit.si*). 

**Optional**: You may also add the contact to a *group* among your other contacts. However, first you must create the group. You can do this by selecting ***File* > *Create group...*** from the menu). 

**Type in** your contact's user name or address into the ***ID or Number*** field (for example, *sally.the.doer@jit.si*). 

You can choose the name or nickname for the contact, which will be visible in your contacts list in the **Jitsi** main window; **type it into the *Display name*** field. 

**Step 3**. **Click** on *Add* to close the *Add contact* window and come back to Jitsi main window. In your contact list you will now see your new contact added with the note "Waiting for authorisation" as indicated below:

![](/sbox/screen/jitsi-en/31.png)

*Figure 2: Jitsi main window with added contact waiting for authorisation*
 
**Step 4**. When your contact (sally.the.doer@jit.si) logs in to her account, a pop-up window will inform her that you have requested to add her to your list of contacts:

![](/sbox/screen/jitsi-en/32.png)

*Figure 3: Window requesting authorisation of a new contact*

Your contact has a choice of selecting the *Ignore* option, in which case your request will continue awaiting authorisation; *Deny*, in which case you will receive information that your request was rejected; and *Authorise*, in which case you will receive information that your contact has accepted your authorisation request, and the entry for your contact in your contact list will become active:

![](/sbox/screen/jitsi-en/33.png)

*Figure 4: Jitsi main window with the new contact authorised*

<a name="3.2"></a>
## 3.2 Text chat (Instant Messaging) with OTR encryption

Now that you added and authorised your contact, you can click on their name in the contact list and initiate text conversation, voice or video calls, and desktop sharing, by choosing the relevant icon under their name:

![](/sbox/screen/jitsi-en/34.png)

*Figure 5: Selected contact in the Jitsi main window with icons for IM, voice or video call and desktop sharing*

**Step 1**. We will now explore one of Jitsi's most important features: the ability to text chat securely, encrypting your messages with [*OTR*](/en/glossary#OTR). OTR functions in a similar manner to [*GPG/PGP*](/en/glossary#PGP) described in other chapters in this toolkit. Just as with PGP, before you and your contact can encrypt your communications, you both need to configure **Jitsi** to generate your encryption keys. You can do this by **selecting *Tools* > *Options*** menu and **selecting the *Security*** tab and ***Chat*** sub-tab. You will then see a window similar to one shown in the image below:

![](/sbox/screen/jitsi-en/35.png)

*Figure 6: Part of the chat options window where you can generate encryption keys for your text chats*

**Step 2**. Next, **click** the ***Generate*** button. As a result you will see the fingerprint of the key that has been generated:

![](/sbox/screen/jitsi-en/36.png)

*Figure 7: Part of the chat options window showing fingerprint for your generated OTR encrypted text chat*

One key is generated per account. You only need to do this again if you add a new account or install Jitsi on another device and do not move the existing keys to it.

Now you are ready to communicate:

**Step 3**. **Select a contact** from Jitsi main window and **click** on the *send message* icon (first from the left under the contact's name) to open a text chat window:

![](/sbox/screen/jitsi-en/37.png)

*Figure 8: Text chat window with the OTR encryption indicated but **not** engaged*

Note the *Encrypt chat with OTR* icon, the open padlock on the right-top side of the window. This inconspicuous symbol informs you whether the chat is encrypted or not. Now the lock is open (there is a tiny space between handle and the body of the lock!). 

**Step 4**. **click on the *Encrypt chat with OTR* icon**. Note the changes in the window:

![](/sbox/screen/jitsi-en/38.png)

*Figure 9: Text chat window after clicking on the Encrypt chat with OTR icon*

Observe that the padlock is now locked. This means that whatever messages you and your contact send to each other are encrypted. Note the message that this is an *unverified private conversation* and that you should *authenticate* sally.the.doer@jit.si.

**Step 5**. **click on the link *authenticate sally.the.doer@jit.si*** to open the *Authenticate Buddy* window:

![](/sbox/screen/jitsi-en/39.png)

*Figure 10: Authenticate Buddy window with fingerprints for you and your contact*

Note the message that encourages you to compare the fingerprints of your keys with your contact over another channel (not this text chat). In doing this, you can be more certain that you are communicating with your contact and not somebody else. A good choice for key comparisons is to do it face to face, or via video or voice communication as these provide easier means to authenticate the identity of the other person. After you compare fingerprints, **select** the option ***I have* verified** the fingerprint from the pull-down menu and **click on *Authenticate Buddy***:

![](/sbox/screen/jitsi-en/40.png)

*Figure 11: Part of the Authenticate Buddy window after selecting "I have" verified the fingerprint of your contact*

Closing the *Authenticate Buddy* window returns you to the chat window:

![](/sbox/screen/jitsi-en/41.png)

*Figure 12: Text chat window with authenticated OTR encryption*

Note that padlock no longer includes the orange triangle with the white exclamation mark. This means that you have authenticated your contact. **The authentication should be done only once per contact.** If the triangle with exclamation mark returns, it means that you are chatting to somebody who you have not yet authenticated. This can happen when your contact moves to another device with another encryption key (another installation of Jitsi, or another OTR enabled program, etc.). In this case you will need to re-authenticate each other again to be sure of the identity of person with whom you communicate.

**Jitsi** allows you to text chat with more than one person in the same time. OTR encryption will only work when chatting to one person.


<a name="3.3"></a>
## 3.3 Voice and video chat with ZRTP encryption ##

**Jitsi** offers voice and video chats which can be independently encrypted with open standard called ZRTP. In order to initiate the chat you need to 

**Step 1**. **Click** on the contact in **Jitsi** contact list and **click** on the voice (second icon from the left under the contact's name) or video (third) icon - see figure 5 above. A new window will appear indicating that **Jitsi** is establishing the connection:

![](/sbox/screen/jitsi-en/42.png)

*Figure 13: Call window indicating Ringing status*

Your contact will see incoming call notification:

![](/sbox/screen/jitsi-en/43.png)

*Figure 14: Incoming call notification*

**Step 2.** If your contact **accepts the call** you will receive information that you are connected:

![](/sbox/screen/jitsi-en/44.png)

*Figure 15: Received call window without ZRTP encryption*

**Note** the red open padlock. This means that your call is not yet encrypted with ZRTP.

**Step 3.** **Wait...** Your and your contact's programs are establishing an encrypted connection, which may take a moment. If they succeed you will see the letters *zrtp* appear against an orange backgrond with a closed padlock like below. If they don't succeed in establishing a connection, you still can chat but without encryption. You can disconnect, restart **Jitsi** and try again to see if this time the programs will connect with encryption. ZRTP may not work in calls between accounts from different providers (such as between Google and Jit.si).

![](/sbox/screen/jitsi-en/45.png)

*Figure 16: Part of the Call window with ZRTP encryption engaged but not yet confirmed*

**Step 4**. **Observe** the section under the letters *zrtp* and padlock with the message "Compare with partner" followed by 4 characters. **Read** these letters to your contact and ask if she sees the same characters. If she does, it means that your communication is encrypted and nobody is interfering with it. You can **click *Confirm***. The orange *zrtp* field will turn green:

![](/sbox/screen/jitsi-en/46.png)

*Figure 17: Part of the Call window with confirmed ZRTP encryption engaged*

**Step 5**. You may close the black confirmation section of the window by clicking on the white x sign on upper-right part of the black section:

![](/sbox/screen/jitsi-en/47.png)

*Figure 18: Part of the call window with confirmed ZRTP encryption engaged*

**Jitsi** lets you voice and video chat with more than one person. **Note** that with this communication, ZRTP encryption can be engaged between initiator of the call and other parties, but not between parties themselves.


