class Transmission():

    def __init__(self, puzzle_input="d16_input.txt"):
        self.coded_message = self._load_data(puzzle_input)
        self.decoded_message = []
        self.version_sum = 0

    def _load_data(self, puzzle_input):
        """Load day 16 puzzle input."""
        with open(puzzle_input) as f:
            hex_string = f.read().splitlines()[0]
        return self._hex2bin(hex_string)

    def decode(self, transmission=None):
        """Decode the coded message."""
        if transmission is None:
            transmission = self.coded_message
        # Continue decoding whilst not just trailing zeros
        while "1" in transmission:
            transmission = self._decode_packet_in(transmission)

    def _decode_packet_in(self, packet):
        """Decode value in packet and return remaining packet."""
        if self._is_literal(packet):
            packet = self._decode_literal(packet)
        else:
            packet = self._decode_operator(packet)
        return packet

    def _decode_literal(self, packet):
        """
        Decode literal value in packet, and return remaining
        packet.
        """
        self.version_sum += self._get_packet_version(packet)
        # Get groups in packet, and position of final character in packet
        groups, end_id = self._get_literal_groups(packet)
        # Record decoded message
        self.decoded_message.append(self._bin2int("".join(groups)))
        return packet[end_id:]

    def _get_literal_groups(self, packet):
        """
        Get groups in literal packet, and position of final
        character in packet.
        """
        # Literal packets always contain at least one group
        num_groups = 1
    
        # Count the number of groups in the packet
        while packet[5 * num_groups + 1] != "0":
            num_groups += 1
    
        # Extract groups from packet
        groups = [packet[5 * (i + 1) + 2 : 5 * (i + 2) + 1] for i in range(num_groups)]
    
        # Get position of final character in packet
        end_id = 5 * (num_groups + 1) + 1
    
        return groups, end_id

    def _decode_operator(self, packet):
        """Decode operator packet."""
        self.version_sum += self._get_packet_version(packet)

        mode = int(packet[6])
        # mode = 1
        if mode:
            # Decode the next 11 characters
            number_subpackets = self._bin2int(packet[7:18])
            subpackets = packet[18:]
            packet = ""
        # mode = 0
        else:
            # Decode the next 15 characters
            subpackets_length = self._bin2int(packet[7:22])
            subpackets = packet[22 : 22 + subpackets_length]
            # Get remaining packets
            packet = packet[22 + subpackets_length:]

        self.decode(transmission=subpackets)
        return packet

    def _get_packet_version(self, packet):
        """Get version from packet's header."""
        return self._bin2int(packet[:3])

    def _is_literal(self, packet):
        """Return True if packet is of literal type."""
        return packet[3:6] == "100"

    def _hex2bin(self, hex_str):
        """
        Convert a string representing a hexadecimal number to a
        string representing a binary number.
        """
        return format(int(hex_str, 16), f"0{len(hex_str) * 4}b")

    def _bin2int(self, bin_str):
        """
        Convert a string representing a binary number to an
        integer.
        """
        return int(bin_str, 2)

