This is the LaTeX source for my University of Tromsø PhD thesis
'Representation and variation in substance-free phonology: a case
study in Celtic'. You are welcome to look at it and take bits and
pieces if you like them. I am by far not the most advanced LaTeX user
out there, but hopefully this might be useful.

# Things you will need

* A Unicode-friendly environment. Thanks to the ridiculous ease of
  entering IPA characters in Emacs, I am not using the tipa package
  here. I believe most modern LaTeX implementations are Unicode-aware
  (at least on Unix systems), but I'm not sure how well Unicode is
  supported in the Windows ecosystem, especially in the text editors.

* A fairly recent system (preferably the latest TeX Live). Two
  packages that have been known to trip up older systems are `linguex`
  (which changed from `\refdash` to `\firstrefdash`) and `cleveref`
  (where `\cpageref` is unavailable in older versions).

* The fonts. The `eulervm` package should be available on most TeX
  systems. For the body text, you will need
  [Gentium Basic and Gentium Plus](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=Gentium_download),
  [Junicode](http://junicode.sourceforge.net/), and
  [Inconsolata](http://www.levien.com/type/myfonts/inconsolata.html).

* The `.bib` file. It's a bit of a mess, especially with respect to
  the keys. There is no consistent naming structure, and some are less
  obvious. Sorry about that. (Again, RefTeX makes finding stuff in
  your bibliography so ridiculously easy that you stop worrying about
  the keys.)

* The `bothoa-corpus` package referred to in Chapter 7 is available
  [separately](http://github.com/anghyflawn/bothoa-corpus)

* The `OTtablx-extras` package is available
  [separately](http://github.com/anghyflawn/OTtablx-extras)
