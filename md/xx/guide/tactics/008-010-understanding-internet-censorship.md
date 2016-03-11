

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

Research carried out by organisations like the [OpenNet Initiative (ONI)](http://opennet.net/) and [Reporters Without Borders (RSF)](http://www.rsf.org/)
indicates that many countries filter a wide variety of social,
political and 'national security' content, while rarely publishing
precise lists of what has been blocked. Naturally, those who wish to
control their citizens' access to the Internet also make a special
effort to block known proxies and websites that offer tools and
instruction to help people circumvent these filters.

Despite the guarantee of free access to information enshrined in
Article 19 of the Universal Declaration of Human Rights, the number of
countries engaged in Internet censorship has continued to increase
dramatically over the past few years. As the practice of Internet
filtering spreads throughout the world, however, so does access to the
circumvention tools that have been created, deployed and publicised by
activists, programmers and volunteers. 

Before exploring the various ways to bypass Internet censorship, you
should first develop a basic understanding of how these filters
work. In doing so, it may be helpful to consider a greatly-simplified model of your connection to the Internet.

### Your Internet connection ###

![](/sites/securitybkp.ngoinabox.org/security/files/img/1-en.png)

The first step of your connection to the Internet is typically made
through an <i>Internet Service Provider[*ISP*](/en/glossary#ISP)  at your home, office,
school, library or Internet cafe. The [*ISP*](/en/glossary#ISP) assigns your computer an [*IPaddress*](/en/glossary#IP_address), which various Internet services can use to identify you and send you information, such as the emails and webpages you request.
Anyone who learns your [*IP address*](/en/glossary#IP_address) can figure out what city
you are in. Certain well-connected organisations in your country,
however, can use this information to determine your precise location.


- **Your ISP** will know which building you are in or which phone line you are using if you access the Internet through a modem.	
- **Your Internet cafe, library or business** will know which computer you were using at a given time, as well as which port or wireless access point you were connected to.	
- **Government agencies** may know all of these details, as a result of their influence over the organisations above.
	
At this stage, your [*ISP*](/en/glossary#ISP) relies on the network
infrastructure in your country to connect its users, including you,
with the rest of the world. On the other end of your connection, the
website or Internet service you are accessing has gone through a
similar process, having received its own IP addresses from an [*ISP*](/en/glossary#ISP)  in
its own country. Even without all of the technical details, a basic
model like this can be helpful when considering the various tools
that allow you get around filters and remain anonymous on the Internet.

### How websites are blocked ###

Essentially, when you go to view a webpage, you are showing the
site's [*IP address*](/en/glossary#IP_address) to your [*ISP*](/en/glossary#ISP) and asking it to connect you with the webserver's [*ISP*](/en/glossary#ISP). And, if you have an unfiltered Internet connection, it will do precisely that. If you are in a country that censors the
Internet, however, it will first consult a [*blacklist*](/en/glossary#Blacklist)  of forbidden websites and then decide whether or not to comply with your request.

In some cases, there may be a central organisation that handles
filtering in place of the [*ISPs*](/en/glossary#ISP) themselves. Often, a [*blacklist*](/en/glossary#Blacklist) will
contain [*domain names*](/en/glossary#Domain_names), such as www.blogger.com, rather than [*IPaddresses*](/en/glossary#IP_addresses). And, in some countries, filtering software monitors your connection, rather than trying to block specific Internet addresses.
This type of software scans through the requests that you make and the
pages that are returned to you, looking for sensitive key words and
then deciding whether or not to let you see the results.

And, to make matters worse, when a webpage is blocked you may not
even know it. While some filters provide a 'block page' that explains
why a particular page has been censored, others display misleading
error messages. These messages may imply that the page cannot be
found, for example, or that the address was misspelled.

In general, it is easiest to adopt a worst-case perspective toward
Internet censorship, rather than trying to research all of the
particular strengths and weaknesses of the filtering technologies used
in your country. In other words, you might as well assume that: 

- Your Internet traffic is monitored for keywords
- Filtering is implemented directly at the [*ISP*](/en/glossary#ISP) level
- Blocked sites are [*blacklisted*](/en/glossary#Blacklist) by both their  [*IP addresses*](/en/glossary#IP_address) and their [*domain names*](/en/glossary#Domain_name)
- You may be given an unclear or misleading reason to explain why a blocked site fails to load. 
	
Because the most effective circumvention tools can be used regardless
of which filtering methods are in place, it does not generally do any harm to
make these pessimistic assumptions

<div class="background" markdown="1">
Mansour: So, if I find one day that I can't access the blog, but a friend in another country can still see it just fine, does that mean the government has blocked it?

Magda: Not necessarily. There could be some problem that only affects people who are trying to reach the website from here. Or, it could be some issue with your computer that only shows up on certain types of webpages. You're on the right track, though. You could also try visiting it yourself while using a circumvention tool. After all, most of these tools rely on external proxy servers, which is a bit like asking a friend in another country to test a website for you, except you get to do it yourself.
</div>


