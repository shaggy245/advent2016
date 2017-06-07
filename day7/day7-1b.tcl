# Finite state machine reading whole file at once and iterating through chars

set infile [open "input" r]
set chars [read -nonewline $infile]
close $infile

#STATES
#outside_init - outside blank state
#outside_a - matched char 'a'
#outside_ab - matched char 'a' and subsequent char 'b' that != 'a'
#outside_abb - matched char 'a', 'b', and 3rd char 'b'
#outside_abba - matched 'abba' outside brackets
##
#inside_init - inside blank state
#inside_a - matched char 'a'
#inside_ab - matched char 'a' and subsequent char 'b' that != 'a'
#inside_abb - matched char 'a', 'b', and 3rd char 'b'
#inside_abba - matched 'abba' inside brackets
##
## Already matched outside
#tls_inside_init - inside blank state
#tls_inside_a - matched char 'a'
#tls_inside_ab - matched char 'a' and subsequent char 'b' that != 'a'
#tls_inside_abb - matched char 'a', 'b', and 3rd char 'b'
#tls_inside_abba - matched 'abba' inside brackets

set char_a ""
set char_b ""
set state "outside_init"
set tls_count 0

while { [eof $infile] < 1 } {
  set char [read $infile 1]

  # Check if char is \n, [, or ]
  switch $char {
    "\[" {
      set char_a ""
      set char_b ""
      if { $state == "outside_abba"} {
        set state "tls_inside_init"
      } elseif { $state == "inside_abba" } {
        set state "inside_abba"
      } elseif { $state == "tls_inside_abba" } {
        set state "tls_inside_abba"
      } else {
        set state "inside_init"
      }
      continue
    }
    "\]" {
      set char_a ""
      set char_b ""
      if { $state == "inside_abba" } {
        set state "inside_abba"
      } elseif {$state == "tls_inside_abba"} {
        set state "tls_inside_abba"
      } elseif { [string range $state 0 2] == "tls"} {
        set state "outside_abba"
      } else {
        set state "outside_init"
      }
      continue
    }
    "\n" {
      if { $state == "outside_abba" } {
        incr tls_count
      }
      set char_a ""
      set char_b ""
      set state "outside_init"
      continue
    }
  }

  #puts $state
  switch $state {
    "outside_init" {
      set char_a $char
      set state "outside_a"
    }
    "outside_a" {
      if { $char_a != $char } {
        set char_b $char
        set state "outside_ab"
      } else {
        set char_a $char
        set state "outside_a"
      }
    }
    "outside_ab" {
      if { $char == $char_b } {
        set state "outside_abb"
      } else {
        set char_a $char_b
        set char_b $char
        set state "outside_ab"
      }
    }
    "outside_abb" {
      if { $char == $char_a } {
        set state "outside_abba"
      } elseif { $char == $char_b } {
        set char_a $char
        set state "outside_a"
      } else {
        set char_a $char_b
        set char_b $char
        set state "outside_ab"
      }
    }
    "outside_abba" { }
    "inside_init" {
      set char_a $char
      set state "inside_a"
    }
    "inside_a" {
      if { $char_a != $char } {
        set char_b $char
        set state "inside_ab"
      } else {
        set char_a $char
        set state "inside_a"
      }
    }
    "inside_ab" {
      if { $char == $char_b } {
        set state "inside_abb"
      } else {
        set char_a $char_b
        set char_b $char
        set state "inside_ab"
      }
    }
    "inside_abb" {
      if { $char == $char_a } {
        set state "inside_abba"
      } elseif { $char == $char_b } {
        set char_a $char_b
        set state "inside_a"
      } else {
        set char_a $char_b
        set char_b $char
        set state "inside_ab"
      }
    }
    "inside_abba" { }
    "tls_inside_init" {
      set char_a $char
      set state "tls_inside_a"
    }
    "tls_inside_a" {
      if { $char_a != $char } {
        set char_b $char
        set state "tls_inside_ab"
      } else {
        set char_a $char
        set state "tls_inside_a"
      }
    }
    "tls_inside_ab" {
      if { $char == $char_b } {
        set state "tls_inside_abb"
      } else {
        set char_a $char_b
        set char_b $char
        set state "tls_inside_ab"
      }
    }
    "tls_inside_abb" {
      if { $char == $char_a } {
        set state "tls_inside_abba"
      } elseif { $char == $char_b } {
        set char_a $char_b
        set state "tls_inside_a"
      } else {
        set char_a $char_b
        set char_b $char
        set state "tls_inside_ab"
      }
    }
    "tls_inside_abba" { }
    default {
      puts "SOMETHINGS MESSED UP"
      break
    }
  }

}
puts $tls_count
