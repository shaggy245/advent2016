input = File.readlines(ARGV.first, chomp: true)

def find_legit(ename)
  characters = Hash.new(0)
  ename.chars.each do |char|
    characters[char] += 1
  end
  characters.sort_by {|k, v| [-v, k]}.flatten.keep_if {|x| x.is_a? String}[0,5].join()
end

total = 0

input.each do |line|
  code = line.split(/[-\[\]]/)
  ename = code[0..-3].join()
  sector_id = code[-2].to_i
  checksum = code[-1]
  if find_legit(ename) == checksum
    total += sector_id
  end
end

puts total
