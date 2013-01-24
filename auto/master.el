(TeX-add-style-hook "master"
 (lambda ()
    (LaTeX-add-bibliographies
     "thesis")
    (LaTeX-add-environments
     "constraint")
    (TeX-add-symbols
     '("wraptbl" ["argument"] 1)
     '("hypcell" ["argument"] 1)
     '("join" ["argument"] 2)
     '("posscite" ["argument"] 1)
     '("orth" 1)
     '("BuildChpNum" 2)
     '("consdef" 2)
     '("pprop" 1)
     '("prop" 1)
     '("mapping" 3)
     '("xm" 1)
     '("fstr" 2)
     '("troof" 2)
     '("fd" 2)
     '("dtei" 1)
     '("us" 1)
     '("dom" 2)
     '("smoi" 1)
     '("triang" 2)
     '("alternation" 2)
     '("midwayarrow" 2)
     '("mfeaturebox" 2)
     '("featurebox" 2)
     '("featurestring" 1)
     '("phonint" 1)
     '("fea" 2)
     '("preff" 1)
     '("suff" 1)
     '("fwe" 4)
     '("twp" 3)
     '("twe" 3)
     '("mbp" 1)
     '("mbi" 1)
     '("mb" 1)
     '("ipa" 1)
     "hand"
     "gc"
     "ie"
     "cf"
     "iem"
     "cfm"
     "egm"
     "checkmark"
     "delmark"
     "underscore"
     "ldbr"
     "rdbr"
     "textlbracket"
     "textrbracket"
     "rt"
     "mo"
     "smo"
     "owd"
     "sy"
     "ssy"
     "hd"
     "dte"
     "wdm"
     "vs"
     "scm"
     "thickhrulefill"
     "dash"
     "endash"
     "delink"
     "fake")
    (TeX-run-style-hooks
     "url"
     "flafter"
     "ntheorem"
     "cleveref"
     "tabulary"
     "threeparttable"
     "eqparbox"
     "fixme"
     "varwidth"
     "ulem"
     "normalem"
     "stmaryrd"
     "wasysym"
     "rotating"
     "mdwlist"
     "pifont"
     "array"
     "colortbl"
     "footmisc"
     "multiple"
     "todonotes"
     "enumitem"
     "hyphenat"
     "multirow"
     "microtype"
     "amssymb"
     "linguex"
     "eulervm"
     "csquotes"
     "autostyle"
     "xltxtra"
     "xspace"
     "hyperref"
     "polyglossia"
     "OTtablx-extras"
     "open"
     "round"
     "adjustbox"
     "latex2e"
     "memoir12"
     "memoir"
     "openany"
     "12pt"
     "a4paper"
     "oldfontcommands"
     "frontmatter/title"
     "frontmatter/frontmatterstart"
     "frontmatter/acknowledgements"
     "frontmatter/intro"
     "frontmatter/mainmatterstart"
     "part1/chap01"
     "part1/chap02"
     "part1/chap03"
     "part1/chap04"
     "part2/start"
     "part2/intro"
     "part2/sir-benfro"
     "part2/bothoa"
     "part2/discussion"
     "part2/conclusion")))

