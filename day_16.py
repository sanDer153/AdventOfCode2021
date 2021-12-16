from math import prod

hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',
              'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
transmission = ''
with open('day_16_input.txt') as f:
    for char in f.readline().strip():
    # for char in "9C0141080250320F1802104A08":
        transmission += hex_to_bin[char]


class Packet:

    def __init__(self, binary):
        self.version = int(binary[0:3], base=2)
        self.type_id = int(binary[3:6], base=2)
        self.unprocessed_body = binary[6:]
        self.length = len(binary)

    def get_length(self):
        return self.length


class LiteralValuePacket(Packet):

    def __init__(self, binary):
        super().__init__(binary)

        self.binary_literal_value = ''
        self.literal_value = 0

        self.unpack_body()

    def unpack_body(self):
        last_bit = False
        while len(self.unprocessed_body) > 0 and '1' in self.unprocessed_body and not last_bit:
            if self.unprocessed_body[0] == '0':
                last_bit = True
            self.binary_literal_value += self.unprocessed_body[1:5]
            self.unprocessed_body = self.unprocessed_body[5:]

        self.length = 6 + (len(self.binary_literal_value) // 4) * 5
        self.literal_value = int(self.binary_literal_value, base=2)

    def get_version(self):
        return self.version

    def get_value(self):
        return self.literal_value


class OperatorPacket(Packet):

    def __init__(self, binary):
        super().__init__(binary)

        self.length_type_id = 0
        self.length_id = 0
        self.inner_packets = []

        self.length_type_id = int(self.unprocessed_body[0], base=2)
        self.unprocessed_body = self.unprocessed_body[1:]
        if self.length_type_id == 0:
            self.length_id = int(self.unprocessed_body[:15], base=2)
            self.unprocessed_body = self.unprocessed_body[15:]
        else:
            self.length_id = int(self.unprocessed_body[:11], base=2)
            self.unprocessed_body = self.unprocessed_body[11:]

        self.unpack_body()

    def unpack_body(self):
        while len(self.unprocessed_body) > 0 and \
            '1' in self.unprocessed_body and \
            ((self.length_type_id == 0 and sum([x.get_length() for x in self.inner_packets]) < self.length_id) or (self.length_type_id == 1 and len(self.inner_packets) < self.length_id)):

            if self.unprocessed_body[3:6] == '100':
                new_packet = LiteralValuePacket(self.unprocessed_body)
                self.inner_packets.append(new_packet)
                self.unprocessed_body = self.unprocessed_body[new_packet.get_length():]
            else:
                new_packet = OperatorPacket(self.unprocessed_body)
                self.inner_packets.append(new_packet)
                self.unprocessed_body = self.unprocessed_body[new_packet.get_length():]

        self.length = 6 + 16 - 4 * self.length_type_id + sum([x.get_length() for x in self.inner_packets])

    def get_version(self):
        return self.version + sum([x.get_version() for x in self.inner_packets])

    def get_value(self):

        if self.type_id == 0:
            return sum([x.get_value() for x in self.inner_packets])
        elif self.type_id == 1:
            return prod([x.get_value() for x in self.inner_packets])
        elif self.type_id == 2:
            return min([x.get_value() for x in self.inner_packets])
        elif self.type_id == 3:
            return max([x.get_value() for x in self.inner_packets])
        elif self.type_id == 5:
            if self.inner_packets[0].get_value() > self.inner_packets[1].get_value():
                return 1
            else:
                return 0
        elif self.type_id == 6:
            if self.inner_packets[0].get_value() < self.inner_packets[1].get_value():
                return 1
            else:
                return 0
        elif self.type_id == 7:
            if self.inner_packets[0].get_value() == self.inner_packets[1].get_value():
                return 1
            else:
                return 0


def first_star():
    # test_packet = LiteralValuePacket('110100101111111000101000')
    master_packet = OperatorPacket(transmission)
    print(master_packet.get_version())


def second_star():
    master_packet = OperatorPacket(transmission)
    print(master_packet.get_value())


first_star()
second_star()