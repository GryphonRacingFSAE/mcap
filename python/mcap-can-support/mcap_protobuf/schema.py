from mcap.writer import Writer as McapWriter
from cantools.database.can import Message as CANMessage

def register_schema(writer: McapWriter, message_class: CANMessage, dbc_file: str):
    return writer.register_schema(
        name=message_class.name,
        encoding="can",
        data=dbc_file,
    )
