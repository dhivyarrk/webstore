from backend.database import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, , unique=True)
    user_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date, nullable=False)
    membership = db.Column(db.String(), nullable=False, default='regular')
    contact_number = db.Column(db.Integer)
    email_id = db.Column(db.String(), nullable=False)
    user_type = db.Column(db.String(), nullable=False, default='customer')

    __table_args__ = (
        db.CheckConstraint(membership.in_(['regular', 'premium']), name='member_types'),
    )

    __table_args__ = (
        db.CheckConstraint(user_type.in_(['customer', 'employee', 'admin']), name='user_types'),
    )


class WomensProducts(db.Model):
    __tablename__ = 'womensproducts'

    product_id = db.Column(db.Integer, primary_key=True, unique=True)
    product_name = db.Column(db.String(), nullable=False)
    product_description = db.Column(db.String(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    availability = db.Column(db.Integer)   

class KidsProducts(db.Model):
    __tablename__ = 'kidsproducts'

    product_id = db.Column(db.Integer, primary_key=True, unique=True)
    product_name = db.Column(db.String(), nullable=False)
    product_description = db.Column(db.String(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    availability = db.Column(db.Integer)

class Categories(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True, unique=True)
    category_name = db.Column(db.String(), default='regular', nullable=False)
    category_description = db.Column(db.String(), nullable=False)

    __table_args__ = (
        db.CheckConstraint(category_name.in_(['womensclothes', 'womensaccessories','kidsclothes','kidsshoes',]), name='category_name'),
    )    

class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    payment_status = db.Column(db.String(), nullable=False, default='pending')

    __table_args__ = (
        db.CheckConstraint(payment_status.in_(['pending', 'paid','cancelled']), name='payment_status'),
    ) 

class Shipments(db.Model):
    __tablename__ = 'shipments'

    shipment_id = db.Column(db.Integer, primary_key=True, unique=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    shipment_status = db.Column(db.String(), default='not_initiated')
    shipped_from_warehouse_date = db.Column(db.Date)
    reached_destination_date = db.Column(db.Date)
    out_for_delivery_date = db.Column(db.Date)
    delivered_date = db.Column(db.Date)

    __table_args__ = (
        db.CheckConstraint(shipment_status.in_(['not_initiated', 'shipped_from_warehouse','reached_destination', 'out_for_delivery','delivered']), name='payment_status'),
    )
