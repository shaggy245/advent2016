set infile [open [lindex $argv 0] r]
set file [read -nonewline $infile]
close $infile

# Create a matrix of each row and chars in the row
foreach line [split $file "\n"] {
  lappend lines2 [split $line ""]
}
# Transpose lines matrix
for {set index 0} {$index < [llength [lindex $lines2 0]]} {incr index} {
    lappend res [lsearch -all -inline -subindices -index $index $lines2 *]
}

# Find most-occurring character in each column
foreach col $res {
  # Iterate through unique characters in each column and count
  foreach uchar [lsort -unique $col] {
    # Append the character and character count {a 3} to a char_count array
    # Use lsearch -all to create an array containing indexes of occurrences
    # and count the length of the lsearch results to get the count of character
    # occurrences.
    lappend char_count "$uchar [llength [lsearch -all $col $uchar]]"
  }
  # Sort the char_count list of lists by # of occurrences (-index 1) and return
  # the character with the highest occurrence number. Append that char to code.
  append code "" [lindex [lindex [lsort -integer -decreasing -index 1 $char_count] 0] 0]
  set char_count ""
}

puts $code
