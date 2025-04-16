def packet_to_string(packet: bytes) -> str:
  packet_str = str(packet)
  packet_str = packet_str.replace("b'", "")
  packet_str = packet_str.replace("'", "")
  return packet_str