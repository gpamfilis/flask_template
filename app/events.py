# example event


#@db.event.listens_for(Order, "after_insert")
#def insert_order_to_printer(mapper, connection, target):
#    po = PrinterOrder.__table__
#    connection.execute(po.insert().values(store_id=target.store_id, order_id=target.id, scenario=target.order_type))
