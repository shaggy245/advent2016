# Count the number of lines in a text file
#
package require md5

set infile [open "input" r]
set lines [split [read -nonewline $infile] "\n"]
close $infile

set password ""
set extra_char 0
set cnt 0

while {$cnt < 8} {
    set door_id_md5 [md5::md5 -hex $lines$extra_char]
    #puts $door_id_md5
    if { [string equal -length 5 $door_id_md5 "00000"] } {
        append password [string index $door_id_md5 5]
        incr cnt
        puts $password
    }
    incr extra_char
    #set $extra_char [expr {$extra_char + 1}]
}
puts $password


###################################
#def calc_password(door_id):
#    password = ""
#    extra_char = 0
#    cnt = 0
#    while cnt < 8:
#        md5 = hashlib.new("md5")
#        md5.update((door_id + str(extra_char)).encode("utf-8"))
#        door_id_md5 = md5.hexdigest()
#        if door_id_md5[:5] == "00000":
#            password += door_id_md5[5]
#            cnt += 1
#        extra_char += 1
#    return password
