set infile [open [lindex $argv 0] r]
set file [read -nonewline $infile]
close $infile

# Transpose lines matrix
foreach line [split $file "\n"] {
  lappend lines2 [split $line ""]
}

for {set index 0} {$index < [llength [lindex $lines2 0]]} {incr index} {
    lappend res [lsearch -all -inline -subindices -index $index $lines2 *]
}

# Find most-occurring character in each column
foreach col $res {
  foreach uchar [lsort -unique $col] {
    lappend char_count "$uchar [llength [lsearch -all $col $uchar]]"
  }
  append code "" [lindex [lindex [lsort -integer -decreasing -index 1 $char_count] 0] 0]
  set char_count ""
}

puts $code
