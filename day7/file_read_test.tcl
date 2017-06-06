set infile [open [lindex $argv 0] r]
#set file [read -nonewline $infile]

while {[eof $infile] == 0} {
  puts [read $infile 1]
}


close $infile
