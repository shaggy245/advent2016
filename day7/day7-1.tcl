set infile [open [lindex $argv 0] r]
set file [read -nonewline $infile]
close $infile

set lines [split $file "\n"]

set tls_count 0
foreach line $lines {
  set in_hypernet 0
  set found_tls 0
  for {set idx 0} {$idx < ([string length $line] - 3)} {incr idx} {
    if {[string index $line [expr ($idx + 3)]] == "\["} {
      set in_hypernet 1
      incr idx 3
      continue
    } elseif {[string index $line [expr ($idx + 3)]] == "\]"} {
      set in_hypernet 0
      incr idx 3
      continue
    }
    if {[string index $line $idx] != [string index $line [expr ($idx + 1)]] && ([string index $line $idx] == [string index $line [expr ($idx + 3)]] && [string index $line [expr ($idx + 1)]] == [string index $line [expr ($idx + 2)]])} {
      if {$in_hypernet == 0} {
        set found_tls 1
      } else {
        set found_tls 0
        break
      }
    }
  }
  if {$found_tls == 1} {
    incr tls_count
  }
}
puts $tls_count
