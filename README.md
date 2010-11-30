Djabbler
========


Djabbler is a blogging engine built in my spare time on the Django framework. Yes, I know, it's only one among many.

By Phillip Marshall


Change log
----------

Releases are named as version:date (e.g. 0.0.1:101129, meaning version 0.0.1, released on Nov 29th, 2010). The extra date bits for bug fixes between versions.

* 0.0.2:101129 (Current)
    * [DOC] Oh, github supports markdown READMEs? Let's see if that works.
    * [ADD] All requests to djabbler.urls return djabbler.views.hello().
* 0.0.1:101129
    * [DOC] Made this README
    * [DOC] Started with a Creative Commons A-NC-SA 3.0 license. We'll see how that works.


Version Roadmap
---------------

This is a "loose" roadmap: room has been left for jumping around between features. In this way, for example, if commenting comes out before Markdown support does, it can be called 1.1. Note that the 0.0.0 section is for my own personal use, and should not concern others.

* 0.0 Pre-release
    * 0.0.0 Personal setup and configuration.
        * 0.0.1 Made this README in markdown, converted to html for distrib.
        * 0.0.2 Pointed URLs properly, made hello world view for not /admin/.
        * 0.0.3-0.1 The following in any order:
            * Set up Amazon EC2 server.
            * Make git scripts, or become more comfortable with Gity.app.
            * Configure the surrounding Django project.
            * Install plugins like South (migrations), Dilla (lipsum filler).
            * Basic contrib.admin support.
            * Find more thorough licensing terms, split Documentation.
    * 0.1 "Hello, World!" works.
        * 0.1.1-0.2.0 The following in any order:
            * Define the djabbler.Entry model
            * Basic template to work with Entry's generic view
            * Hook into the admin interface for adding and editing posts
    * 0.2 Basic blog ready, with entry and display methods.
        * 0.2.1 Flesh out templates: base, index, and individual.
        * 0.2.2 Make a better URL syntax than /1/ meaning post 1.
    * 0.3-0.99 TBD.
* 1.0 Fully working release, but very basic.
    * 1.1-1.99 Ideas for the future:
        * Markdown, Smartypants support.
        * Commenting, with html sanitization.
        * Admin interface dependance removed.
        * Multiple authors.
* 2.0 Pretty release, with shinier templates and features.
    * 2.1-2.99 Etcetera.

---

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/) Unported License.

Code available at [Github](https://github.com/wizpig64/djabbler), feel free to contribute!

Email me at <djabbler@wizpig64.com> with questions, comments, or bugs. Thanks!