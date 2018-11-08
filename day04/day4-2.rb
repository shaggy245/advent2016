input = File.readlines(ARGV.first, chomp: true)

def find_legit(ename)
  characters = Hash.new(0)
  ename.each_char do |char|
    characters[char] += 1
  end
  characters.sort_by {|k, v| [-v, k]}.flatten.keep_if {|x| x.is_a? String}[0,5].join()
end

def decode(room, sector_id)
  abc = [*('a'..'z')]
  roomname = ""
  room.chars.each do |character|
    if character == '-'
      roomname += ' '
    else
      roomname += abc[(abc.index(character) + sector_id) % 26]
    end
  end
  return roomname
end

input.each do |line|
  code = line.split(/[-\[\]]/)
  ename = code[0..-3].join()
  sector_id = code[-2].to_i
  checksum = code[-1]
  if find_legit(ename) == checksum
    if decode(code[0..-3].join('-'), sector_id).include? "north"
      puts sector_id
    end
  end
end

