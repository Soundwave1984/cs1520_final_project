from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.order_model import Base, Order

# Create Flask app with explicit template and static folders
app = Flask(__name__, 
           template_folder="templates",
           static_folder="static")

# Database setup
engine = create_engine('sqlite:///orders.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/<int:table_number>')
def main_menu(table_number):
    """Main menu route that accepts table number"""
    return render_template('main_menu.html', table_number=table_number)

@app.route('/order/<int:table_number>', methods=['POST'])
def order(table_number):
    """Process order submission"""
    try:
        # Get form data
        customer_name = request.form.get('customer_name')
        order_summary = request.form.get('order_summary')
        
        # Create order dictionary for template
        order_data = {
            'customer_name': customer_name,
            'table_number': table_number,
            'orders': order_summary
        }
        
        # Save to database
        new_order = Order(
            customer_name=customer_name,
            orders=order_summary,
            table_number=table_number
        )
        
        session.add(new_order)
        session.commit()
        
        return render_template('order_summary.html', order=order_data)
    
    except Exception as e:
        session.rollback()
        return f"Error processing order: {str(e)}", 500

@app.route('/kitchen/')
def kitchen():
    """Kitchen view showing all pending orders"""
    try:
        # Query all orders from database
        orders = session.query(Order).all()
        
        # Convert Order objects to dictionaries for template
        orders_list = []
        for order in orders:
            order_dict = {
                'id': order.id,
                'customer_name': order.customer_name,
                'table_number': order.table_number,
                'orders': order.orders
            }
            orders_list.append(order_dict)
        
        return render_template('kitchen.html', orders=orders_list)
    
    except Exception as e:
        return f"Error loading kitchen orders: {str(e)}", 500

@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    """Delete an order by ID"""
    try:
        order = session.query(Order).filter_by(id=order_id).first()
        if order:
            session.delete(order)
            session.commit()
        return redirect(url_for('kitchen'))
    
    except Exception as e:
        session.rollback()
        return f"Error deleting order: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)