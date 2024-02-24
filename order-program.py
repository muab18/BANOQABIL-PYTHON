import streamlit as st
import sqlite3

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        st.error(e)
    return conn

# Function to create a table in the database if it does not exist
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Orders
                     (id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER)''')
    except sqlite3.Error as e:
        st.error(e)

# Function to insert order data into the database
def insert_order(conn, item, quantity):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO Orders (item, quantity) VALUES (?, ?)", (item, quantity))
        conn.commit()
        st.success("Order placed successfully!")
    except sqlite3.Error as e:
        st.error(e)

# Function to retrieve all orders from the database
def get_orders(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Orders")
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        st.error(e)

# Main function
def main():
    st.title("Food Order App")

    # Create a connection to the SQLite database
    conn = create_connection("orders.db")
    if conn is not None:
        # Create the Orders table if it does not exist
        create_table(conn)

        st.sidebar.title("Menu")
        menu_options = ["Pizza", "Burger", "Pasta"]
        selected_option = st.sidebar.selectbox("Select an item", menu_options)

        if selected_option == "Pizza":
            pizza_order(conn)
        elif selected_option == "Burger":
            burger_order(conn)
        elif selected_option == "Pasta":
            pasta_order(conn)

        # Display all orders
        st.subheader("All Orders")
        orders = get_orders(conn)
        if orders:
            for order in orders:
                st.write(f"Item: {order[1]}, Quantity: {order[2]}")

        conn.close()

# Function for pizza order
def pizza_order(conn):
    st.subheader("Pizza Order")
    toppings = st.multiselect("Select toppings", ["Pepperoni", "Mushrooms", "Onions", "Peppers"])
    size = st.radio("Select size", ["Small", "Medium", "Large"])
    quantity = st.number_input("Quantity", min_value=1, value=1)
    if st.button("Place Order"):
        insert_order(conn, f"{size} Pizza with {', '.join(toppings)}", quantity)

# Function for burger order
def burger_order(conn):
    st.subheader("Burger Order")
    beef_options = ["Single Beef Burger", "Double Beef Burger"]
    selected_beef = st.radio("Select beef patty", beef_options)
    cheese = st.checkbox("Add cheese?")
    bacon = st.checkbox("Add bacon?")
    fries = st.checkbox("Add fries?")
    if st.button("Place Order"):
        extras = []
        if cheese:
            extras.append("Cheese")
        if bacon:
            extras.append("Bacon")
        if fries:
            extras.append("Fries")
        insert_order(conn, f"{selected_beef} with {', '.join(extras)}", 1)

# Function for pasta order
def pasta_order(conn):
    st.subheader("Pasta Order")
    pasta_type = st.selectbox("Select pasta type", ["Spaghetti", "Fettuccine", "Penne"])
    sauce = st.radio("Select sauce", ["Marinara", "Alfredo", "Pesto"])
    if st.button("Place Order"):
        insert_order(conn, f"{pasta_type} with {sauce} sauce", 1)

if __name__ == "__main__":
    main()
