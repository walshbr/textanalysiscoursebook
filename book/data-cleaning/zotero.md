---
layout: lesson
title:  Zotero
---
You might be thinking to yourself, "I can't believe you made me read an entire section on data cleaning." Sorry you feel that way. Here is a dog in a blanket:

![dog in blanket photo](/textanalysiscoursebook/assets/data-cleaning/dog-blanket.jpeg)

Let's just pretend you said something on the order of, "metadata is all well and good, but how am I going to use this in my everyday life beyond library searches?"

We're glad you asked! In fact, metadata is something you deal with all the time. It is all around us, structuring our lives. If you go to a store and go to a particular section to grab cereal, metadata about the foods on that aisle has helped organize them and guide you to them. If you look through your phone to see that you have a missed call, you'll be presented with information about the caller, the call duration, the number, etc. All metadata. You get the idea.

For a more concrete example relevant to this book, imagine that you were asked by your instructor to write a paper on the Sherlock Holmes story "A Scandal in Bohemia." You will probably need to include a bibliography. Something like this:

Doyle, Arthur Conan. “A Scandal in Bohemia.” Sherlock Holmes: Selected Stories. Ed. Barry McCrea. Oxford: Oxford University Press, 2014. Print. Oxford World’s Classics.

Hopefully you see where we're heading: that citation is composed of nothing but metadata:

	Book Section
	Author: Doyle, Arthur Conan 
	Title: A Scandal in Bohemia
	Book: Sherlock Holmes: Selected Stories 
	Editor: Barry McCrea
	Location: Oxford
	Publisher: Oxford University Press
	Date: 2014 
	Format: Print
	Series: Oxford World’s Classics.

The citation is just metadata, organized according to a pre-arranged format: the MLA 7th Edition, in this case. Anytime you create a citation, you are just organizing the metadata for an object in an agreed-upon format. But the process is very tedious, as we're sure you've noticed over the years. Fortunately, if you've been following along, you know that computers are exceptionally good at executing tedious tasks just like these.

We know the formula for an MLA citation looks like this:

Author. Title. Book. Editor. Location: Publisher, Data. Format. Series.

The formula will vary slightly depending on the type of item you are citing, but, if we have a full metadata listing for each text, we could imagine a tool that would fill in the metadata and format it to our recipe. We could imagine software that would spit out a bibliography for us.

If you have ever used something like [easybib.com](https://www.easybib.com) to produce a bibliography, you have done exactly the process that we are describing. You fill in the metadata you want, and easybib spits out a citation.

You might have felt like you were cheating when using a tool like this as a shortcut for your citations, but we're here to let you in on a secret. Your instructors rely on similar tools. If you think putting together a bibliography for your 5 page essay is irritating, imagine doing one for a 300 page book manuscript. And at the end of the process, your publisher decides that you have to use Chicago style \(footnotes\) rather than MLA \(in-text citations\). Do you want to convert them all by hand? Neither do we. 

To deal with citation situations like this, the academic community has developed its own tool: [Zotero](https://www.zotero.org). Zotero can do everything we've described so far in a snap, but it can also do so much more. Spending a few minutes learning it will save you dozens if not hundreds of hours in your writing life. Seriously.

First visit the [Zotero download page](https://www.zotero.org/download). You can run Zotero out of Firefox, which allows you to capture and manage your citations without ever leaving the browser. But we like to separate the process of collecting citations from managing and using them. Download "Zotero Standalone" from the right window pane:

![zotero download](/textanalysiscoursebook/assets/data-cleaning/zotero-download.jpg)

This will download an application to your desktop that, if you're like us, you'll want to put in a place where you'll have quick and easy access to it. While you're at it, you will need to add at least one of the browser extensions by clicking on the button in the same pane from the downloads page. We recommend you just add the extension to every browser that you have on your computer: these little downloads are what will allow you to pull citation information down off a webpage.

Once you download all those, open up Zotero Standalone. It should look something like this:

![zotero standalone screen](/textanalysiscoursebook/assets/data-cleaning/zotero-standalone.jpg)

Your Zotero installation and library will look different from Brandon's, because his is full of materials related to things he has written. It will probably look pretty empty, since you haven't filled it with any items just yet. Let's show Brandon what's what by grabbing some metadata to store it in Zotero. We will do this three different ways.

<img src="/textanalysiscoursebook/assets/data-cleaning/zotero-add-citation.jpg" alt="adding a book citation" class="img-right medium">

First, let's enter information manually. Let's pull out our copy of Rosalind Crone's _Violent Victorians_ \(you can find the relevant metadata on [Amazon](https://www.amazon.com/dp/071908685X/?tag=mh0b-20&hvadid=4965340066&hvqmt=p&hvbmt=bp&hvdev=c&ref=pd_sl_6usflqlo9o_p) if you don't have your own copy. By clicking on the plus sign at the top, you can select the type of object you are adding to your collection. This is a book, so let's select that.

Doing so will shift your Zotero pane so that you can enter the metadata for Crone's book on the right. Go ahead and do that. Notice how you can have some categories be empty - Zotero is not picky. It has all those extra sections so that it can fit a variety of different use cases, but not every object will use every metadata category. When you're done, you should have something like this. 

![adding crone citation](/textanalysiscoursebook/assets/data-cleaning/zotero-editing-pane.jpg)

Zotero now knows about our citation, and we could use it for any number of things. But before we move on, let's cover two other ways to add citation information. Every book is given an an identifying number, an **International Standard Book Number \(ISBN\)**, and we can grab metadata using this thumbprint. This number is unique to every book. Zotero can map these numbers to their associated metadata. Clicking on the magic wand at the top of the Zotero Standalone pane will give you a place to enter an ISBN:

![magic wand ISBN input](/textanalysiscoursebook/assets/data-cleaning/zotero-magic-wand.jpg)

Try entering this one: 0520221680. Zotero should automatically go out and grab the metadata for its associated book: _Spectacular Realities_ by Vanessa Schwartz. The result might not look perfect, and you might have to tinker with it to make it look like what you want. But you should wind up with another decent looking set of metadata for a second source:

![input by isbn](/textanalysiscoursebook/assets/data-cleaning/zotero-input-by-isbn.jpg)

Magic! But wait - there's more. Visit the Amazon webpage for _[Sara Baartman and the Hottentot Venus: A Ghost Story and a Biography](https://www.amazon.com/Sara-Baartman-Hottentot-Venus-Biography/dp/0691147965)_. If you pay careful attention to your toolbars at the top of the webpage, you may have noticed a new one for Zotero \(fourth from the left in this image from Brandon's computer\).

![zotero download from chrome](/textanalysiscoursebook/assets/data-cleaning/zotero-download-from-chrome.jpg)

By default, Zotero just assumes you are trying to grab the webpage itself. When you visit a page with a citation you can download, however, the Zotero icon will change accordingly as it recognizes the metadata embedded in the page. In the image above, the Zotero icon appears as a book because it knows that it is looking at a book's metadata. Zotero will suck down the metadata on the page and store them in your Standalone App so that you can use them later. Magic!

![zotero input from web](/textanalysiscoursebook/assets/data-cleaning/zotero-input-from-web.jpg)

Well, not quite. We won't get lost in the weeds of explaining the technical details of how this works, as that is a subject for a different class. For now, just know that Zotero is interacting with hidden information on the webpage that provides information to programs like it. The average user never knows that these webpages contain information like this, but Zotero can leverage that invisible data into powerful content to make your life easier.

That being said, you need to remember the principle of garbage in, garbage out. In some cases, the webpage you are grabbing the citation from might not have complete \(or entirely accurate\) metadata. In that case, you will need to edit the citation in your Zotero library by clicking in the relevant fields, adding what's missing, and/or correcting any mistakes. Alternately, the format that libraries use to store metadata might be different from typical citation formats.  Go back up to the record for _Spectacular Realities_ and look at the title. You'll notice that the capitalization is different from what you might expect: the first word is capitalized, as are any proper nouns \("Paris," in this case\). But if you were using this in a bibliography or citation \(which we'll show you in a second\), you'd want to correct the capitalization. You would also need to change "Univ. of California Press" to "University of California Press." This is all to say that although Zotero makes things much, much _easier_, it doesn't necessarily make them _automatic_.

## Zotero for Citation Management in Microsoft Word

Now that we have our metadata, the fun begins. If you use Microsoft Word, strap in and buckle up. Go to the Zotero menu and select Preferences. From the 'Cite' menu, Install the Microsoft Word Add-in. Doing so will add a special 'Zotero' menu to every Microsoft Word document that you open. Now let's open a new Microsoft Word document and check out the new menu.

[Note: The following screenshots and narrative were written for Microsoft Word 2011, and later versions will vary slightly. Microsoft Word 2016, for example, changes the Zotero integration. In this later version you will be looking for a menu called "add-in's," and the keyboard shortcuts below will not work by default. The Zotero forums provide [a tutorial](https://www.zotero.org/support/word_processor_plugin_shortcuts) for adding keyboard shortcuts manually. There can also find a number of [screencasts](https://www.zotero.org/support/word_processor_plugin_shortcuts) to walk you through integrating with other Word versions.]

![zotero menu in word](/textanalysiscoursebook/assets/data-cleaning/zotero-menu-in-word.jpg)

There are lot of options here, but the most important for right now are 'Add Bibliography' and 'Add Citation'. First, click 'Add Citation.' You will need to select a citation style since there is none associated with this document yet. Let's suggest MLA 7th Edition because Brandon is a literary studies person. It will make him happy.

![zotero selection citation style](/textanalysiscoursebook/assets/data-cleaning/zotero-select-citation-style.jpg)

Next pops up an input field that asks you to give some information so that it can locate a citation for you. Typing in 'Crone' will allow Zotero to recognize the author for the book we inputted and bring up the metadata we want. Click it to accept.

![zotero searching for citation](/textanalysiscoursebook/assets/data-cleaning/zotero-searching-for-citation.jpg)

The input field now shows how the citation will show up. In most cases, however, we want to customize it. To do so, click on the citation to bring up some more options. Here you can add page numbers or, importantly suppress the author name depending on whether you only need the page numbers themselves. Let's give this entry the page numbers 45-7. Hit return to accept your changes.

![zotero give page numbers to citation](/textanalysiscoursebook/assets/data-cleaning/zotero-give-page-numbers-to-citation.jpg)

Et voila! Your citation appears in the text in just the same way as if you were doing it by hand, properly formatted with the correct page numbers. 

![zotero example citation](/textanalysiscoursebook/assets/data-cleaning/zotero-example-citation.jpg)

The process might appear a little slow, but once you get the hang of the workflow, this process greatly speeds up writing. Gather all your citations in one place, and then learn the handful of keyboard shortcuts for working with Zotero in Word. These are the ones we use most often:

* 'ctrl + option + a' will add a new citation.
* 'arrow keys' allow you to highlight particular objects from the Zotero search when inputting a citation
* 'return' selects a particular citation.
* 'cmd + down arrow' will bring up additional options like adding page numbers once you have a citation selected in the add citation input field.

Get the hang of these commands, and you'll save loads of time.

But adding citations is only one part of the process. You also want to add a bibliography to your document based on those citations. Zotero can do this too! From the Zotero menu in Word, select 'Add Bibliography.' Zotero will magically format the metadata you're using into bibliographical entries. Then format those into a bibliography based on the citation style you have chosen for the document. By default, the bibliography will appear wherever your cursor was. So you'll need to move it around to put it in a location that works for you. Add a couple more citations using the other things we added to Zotero and see if you can get it looking reasonable. Here is what we came up with:

![zotero text with bibliography](/textanalysiscoursebook/assets/data-cleaning/zotero-document-with-bibliography.jpg)

To make this all look reasonable, we put the bibliography at the end of the text and hit return a few times after the last sentence to give it space \(you often might insert a page break to put the bibliography on its own page\). We gave it a centered heading. And we inserted a couple other citations to flesh things out.

We hope you see how powerful Zotero can be. Zotero saves a lot of time, and it can help organize your workflow neatly and naturally. Now, when you read something new that you think could be useful, in addition to taking notes you will also add it to Zotero. Later, when you go to write, that information can be easily added to your document without much of a hassle.

Zotero is much more that just a way to produce citations and bibliographies. It also allows you to share the fruits of your labor with others. The tool is free to use because its creators believe in the open and accessible sharing of knowledge. Even its underlying code is **open source**, meaning that it is free \(and anyone can contribute to it\). This open ethos of sharing pervades the use of the tool as well. Once you get a handle for putting together your own collections of resources, you can use Zotero for examining the collections of other people as well. Zotero allows people to organize themselves into groups and share metadata among all their members. These groups are frequently open for new members and visible by all, which means that, if you are a member of the right groups, you can easily find your way towards a variety of resources relevant to your interests. We've used Zotero ourselves for similar things, to find resources as we put together courses and lesson plans on digital humanities topics. We will not cover these aspects of Zotero in this lesson, but we encourange you to explore them on your own.

Zotero isn't perfect. Sometimes, an error might occur, and you might have to wrestle with your text a bit. But the payoff is worth it. Save your work often. Back things up. And use Zotero without fear.

## Further Resources
* Jason Puckett has a more advanced breakdown of Zotero in *[Zotero: A Guide for Librarians, Researchers and Educators](https://www.amazon.com/Zotero-Guide-Librarians-Researchers-Educators/dp/0838985890/ref=sr_1_1?ie=UTF8&qid=1473948483&sr=8-1&keywords=zotero)*

