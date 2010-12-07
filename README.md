Djabbler 0.0.3/0.1.RC:101206
============================


Djabbler is a blogging engine built in my spare time on the Django framework. Yes, it's one among many redundant apps of this kind, but my goal is not for it to be adopted into use by by everyone using Django. Although I intend to make Djabbler and its development accessible to anyone, I'm building it solely to learn Django.

By Phillip Marshall


Change log
----------

Releases are named [version]:[date]. For example, 0.0.1:101129 means version 0.0.1, released on Nov 29th, 2010. The extra date bits are used just in case there are bug fixes distributed between versions.

* 0.0.3/0.1.RC:101206 (Current)
    * [DOC] Note that once I move up to version 0.1, I'll be removing bloat from the documentation regarding versions 0.0.x (see: the entire changelog, subsection 0.0.0 of the roadmap). A lot of those changes had nothing to do with the any actual code, so there's no point in keeping them, I think. 
    * [DOC] Removed Dilla from roadmap. I still think it's cool, I just don't see myself using it that much. I'll fill in the database with my own blog!
    * [DOC] Added a lot to the readme, most notably redoing the roadmap and adding links and disclaimers in the footer.
* 0.0.2:101129
    * [DOC] Oh, github supports markdown READMEs? Let's see if that works.
    * [ADD] All requests to djabbler.urls return djabbler.views.hello().
* 0.0.1:101129
    * [DOC] Made this README
    * [DOC] Started with a Creative Commons A-NC-SA 3.0 license. We'll see how that works.


Version Roadmap
---------------

* 0.0 Pre-release
    * 0.0.0 Personal setup and configuration.
        * 0.0.1 Made this README in markdown, converted to html for distrib.
        * 0.0.2 Pointed URLs properly, made hello world view for not /admin/.
        * 0.0.3/0.1.RC Host site configured, south, /admin/, Gity.app.
    * 0.1 "Hello, World!" is fully-functional.
        * 0.1.1 Define the djabbler.models.Entry.
        * 0.1.2 Plug djabbler into contrib.admin.
        * 0.1.3 Make a view and template to show all Entries, descending.
        * 0.1.4/0.2.RC Make a view and template to show one Entry.
    * 0.2 Basic blog front-end ready.
        * 0.2.1 Make a method to post without contrib.admin, form at /post/.
        * 0.2.2 Document how templates hook into the site's main base.html.
        * 0.2.3 Find a better URL scheme than /1/ meaning post 1. Slugs?
        * 0.2.4/0.3.RC Admin version of index, to edit and delete posts.
    * 0.3 Basic blog back-end ready.
        * 0.3.1 Base CSS for all Djabbler views.
        * 0.3.2 CSS and JS for front-end views.
        * 0.3.3/1.0.RC CSS and JS for back-end views.
* 1.0 Fully working release, but very basic.
* 2.0 Pretty release, with shinier templates and features.
* To Do Eventually:
    * Markdown and Smartypants support.
    * Commenting with html sanitization.
    * Fully remove contrib.admin dependance.
    * Multiple author accounts.
    * Split up this documentation.
    * Possibly get better licensing terms

---

The Djabbler source code lives at [Github](https://github.com/wizpig64/djabbler). Feel free to contribute!

Read the Djabbler development blog at [wizpig64.com](http://wizpig64.com/), and email me at <djabbler@wizpig64.com> with feedback, questions, or bugs.

Djabbler is coded with [TextMate](http://macromates.com/), synchronized with [Gity](http://macendeavor.com/), and made sane using [South](http://south.aeracode.org/docs/about.html) for data and schema migrations.

While I recommend South for moving between versions, I will not be providing South's migration scripts. I may share the migrations that South makes me write myself in the change log. If you are familiar with South, you should be able to figure out how to make --auto migrations yourself. Disclaimer: Nothing is my fault ever.

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/) Unported License.