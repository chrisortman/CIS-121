# 1
# digit.each { |row| row[1, 1] = row[1, 1] * scale }
# digit.each do |row|
#     if row =~ /\|/
#         scale.times { puts row }
#     else
#         puts row
#     end
# end

# 2
# class LCD
#     attr_accessor( :size, :spacing )

# #
# # This hash is used to define the segment display for the
# # given digit. Each entry in the array is associated with
# # the following states:
# #
# #    HORIZONTAL
# #    VERTICAL
# #    HORIZONTAL
# #    VERTICAL
# #    HORIZONTAL
# #    DONE
# #
# # The HORIZONTAL state produces a single horizontal line. There
# # are two types:
# #
# #    0 - skip, no line necessary, just space fill
# #    1 - line required of given size
# #
# # The VERTICAL state produces a either a single right side line,
# # a single left side line or a both lines.
# #
# #    0 - skip, no line necessary, just space fill
# #    1 - single right side line
# #    2 - single left side line
# #    3 - both lines
# #
# # The DONE state terminates the state machine. This is not needed
# # as part of the data array.
# #
# @@lcdDisplayData = {
#     "0" => [ 1, 3, 0, 3, 1 ],
#     "1" => [ 0, 1, 0, 1, 0 ],
#     "2" => [ 1, 1, 1, 2, 1 ],
#     "3" => [ 1, 1, 1, 1, 1 ],
#     "4" => [ 0, 3, 1, 1, 0 ],
#     "5" => [ 1, 2, 1, 1, 1 ],
#     "6" => [ 1, 2, 1, 3, 1 ],
#     "7" => [ 1, 1, 0, 1, 0 ],
#     "8" => [ 1, 3, 1, 3, 1 ],
#     "9" => [ 1, 3, 1, 1, 1 ]
#     }

#     @@lcdStates = [
#     "HORIZONTAL",
#     "VERTICAL",
#     "HORIZONTAL",
#     "VERTICAL",
#     "HORIZONTAL",
#     "DONE"
#     ]

#     def initialize( size=1, spacing=1 )
#         @size = size
#         @spacing = spacing
#     end

#       def display( digits )
#           states = @@lcdStates.reverse
#           0.upto(@@lcdStates.length) do |i|
#               case states.pop
#               when "HORIZONTAL"
#                   line = ""
#                   digits.each_byte do |b|
#                       line += horizontal_segment(
#                           @@lcdDisplayData[b.chr][i]
#                       )
#                   end
#                   print line + "\n"
#               when "VERTICAL"
#                   1.upto(@size) do |j|
#                       line = ""
#                       digits.each_byte do |b|
#                           line += vertical_segment(
#                               @@lcdDisplayData[b.chr][i]
#                           )
#                       end
#                       print line + "\n"
#                   end
#               when "DONE"
#                   break
#               end
#           end
#       end

#       def horizontal_segment( type )
#           case type
#           when 1
#               return " " + ("-" * @size) + " " + (" " * @spacing)
#           else
#               return " " + (" " * @size) + " " + (" " * @spacing)
#           end
#       end

#       def vertical_segment( type )
#           case type
#           when 1
#               return " " + (" " * @size) + "|" + (" " * @spacing)
#           when 2
#               return "|" + (" " * @size) + " " + (" " * @spacing)
#           when 3
#               return "|" + (" " * @size) + "|" + (" " * @spacing)
#           else
#               return " " + (" " * @size) + " " + (" " * @spacing)
#           end
#       end
#     end

# from sys import argv

# script, vert_line, hori_line = argv
# vert = "-"
# hori = "|"
# space = ""

# def ascii(vert, hori, space):
#     new = space.replace(""," ")
#     return ascii

# ascii(vert, hori, space)
# var1 = ascii("-", "|", "")

# print "%s%s%s%s%s%s%s%s%s" % (space, (vert*2), (space*8), (vert*2), (space*3), (vert*2), (space*8), (vert*2), space)
# from sys import argv

# script, zero, ascii_one, ascii_two, ascii_three, ascii_four, ascii_five = argv
# zero = {"""

def line1():
    print " --        --   --        --"
    return line1
def line2():
    print "|  |    |    |    | |  | |"
    return line2
def line3():
    print "|  |    |    |    | |  | |"
    return line3
def line4():
    print "           --   --   --   --"
    return line4
def line5():
    print "|  |    | |       |    |    | "
    return line5
def line6():
    print "|  |    | |       |    |    |"
    return line6
def line7():
    print " --        --   --        --"
    return line7
    
print "%s%s%s%s%s%s%s" % (line1(), line2(), line3(), line4(), line5(), line6(), line7())
# print line1(), line2(), line3(), line4(), line5(), line6(), line7()
# S H O U L D  P R I N T
# print """
#  --        --   --        -- 
# |  |    |    |    | |  | |   
# |  |    |    |    | |  | |   
#           --   --   --   -- 
# |  |    | |       |    |    |
# |  |    | |       |    |    |
#  --        --   --        -- 
# """


